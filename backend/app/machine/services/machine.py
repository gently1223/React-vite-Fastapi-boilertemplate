import json
import random
import string
import secrets

from typing import List, Optional
from fastapi import BackgroundTasks

# Migrate to other file

from sqlalchemy import and_, or_, select

from core.exceptions import DuplicateValueException

from ..models import Machine
# from core.exceptions import CustomException, ForbiddenException, NotFoundException
from core.db import Transactional, session
from utils.validator import validation


class MachineService:
    def __init__(self):
        ...

    async def get_machine_list(
        self,
        id: int,
        email: str,
        page: int,
        size: int,
        order_by: str,
        desc: bool,
        accept_language: Optional[str],
    ) -> List[Machine]:
        email = validation(email=email, is_essential=False)
        try:
            if size > 100:
                size = 100
            query = select(Machine)
            if id:
                query = query.where(Machine.id==id)
            elif email:
                query = query.where(Machine.email==email)
            offset = page*size
            if desc:
                query = query.order_by(getattr(Machine, order_by).desc())
            else:
                query = query.order_by(getattr(Machine, order_by))
            query = query.offset(offset=offset).limit(size)
            result = await session.execute(query)
            machines = result.scalars().all()
        except Exception as e:
            print (e.args[0])
            machines = []
        return machines

    async def add_machine(
        self,
        name: str,
        location: str,
        email: str,
        number: str,
        enum: bool,
        background_tasks: BackgroundTasks,
        accept_language: Optional[str],
    ) -> dict:
        email = validation(email=email)
        number += ('-' + ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(40)))
        query = select(Machine).where(or_(Machine.email==email, Machine.number==number))
        result = await session.execute(query)
        machine = result.first()
        if machine:
            raise DuplicateValueException(message="This email or machine number exists")
        # background_tasks.add_task(self.task_add_machine, name, location, email, number, enum)
        try:
            machine = Machine(
                name=name,
                location=location,
                email=email,
                number=number,
                enum=enum,
            )
            session.add(machine)
            await session.flush()
            print ("Machine has been added successfully")
        except Exception as e:
            print (e.args[0])
        response = {
            "success": True,
            "message": "Machine has been added successfully",
            "machine_info": {
                "id": machine.id,
                "name": machine.name,
                "location": machine.location,
                "email": machine.email,
                "number": machine.number,
                "enum": machine.enum,
        } }
        return response
    
    async def update_machine(
        self,
        id: int,
        name: str,
        location: str,
        background_tasks: BackgroundTasks,
        accept_language: Optional[str],
    ) -> dict:
        background_tasks.add_task(self.task_update_machine, id, name, location)
        response = { "success": True, "message": "Machine has been updated successfully" }
        return response
    
    async def delete_machine(
        self,
        id: int,
        background_tasks: BackgroundTasks,
        accept_language: Optional[str],
    ) -> dict:
        background_tasks.add_task(self.task_delete_machine, id)
        response = { "success": True, "message": "Machine has been deleted successfully" }
        return response
    
    @Transactional()
    async def task_add_machine(
        self,
        name: str,
        location: str,
        email: str,
        number: str,
        enum: bool,
    ):
        try:
            machine = Machine(
                name=name,
                location=location,
                email=email,
                number=number,
                enum=enum,
            )
            session.add(machine)
            print ("Machine has been added successfully")
        except Exception as e:
            print (e.args[0])

    @Transactional()
    async def task_update_machine(
        self,
        id: int,
        name: str,
        location: str,
    ):
        try:
            query = select(Machine).where(Machine.id==id)
            result = await session.execute(query)
            machine = result.scalars().first()
            if not machine:
                print ("Machine not found")
            else:
                machine.name = name if name else machine.name
                machine.location = location if location else machine.location
                print ("Machine has been updated successfully")
        except Exception as e:
            print (e.args[0])
    
    @Transactional()
    async def task_delete_machine(
        self,
        id: int,
    ):
        try:
            query = select(Machine).where(Machine.id==id)
            result = await session.execute(query)
            machine = result.scalars().first()
            if not machine:
                print ("Machine not found")
            else:
                await session.delete(machine)
                print ("Machine has been deleted successfully")
        except Exception as e:
            print (e.args[0])