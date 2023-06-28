import string
import secrets

from typing import List

# Migrate to other file

from sqlalchemy import or_, select

from core.exceptions import DuplicateValueException, NotFoundException, UnprocessableEntity

from ..models import Machine
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

    @Transactional()
    async def add_machine(
        self,
        name: str,
        location: str,
        email: str,
        number: str,
        enum: bool,
    ) -> dict:
        email = validation(email=email)
        number += ('-' + ''.join(secrets.choice(string.ascii_letters + string.digits) for i in range(40)))
        query = select(Machine).where(or_(Machine.email==email, Machine.number==number))
        result = await session.execute(query)
        machine = result.first()
        if machine:
            raise DuplicateValueException(message="This email or machine number exists")
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
            raise e
            # raise UnprocessableEntity(message=e)
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
    
    @Transactional()
    async def update_machine(
        self,
        id: int,
        name: str,
        location: str,
    ) -> dict:
        query = select(Machine).where(Machine.id==id)
        result = await session.execute(query)
        machine = result.scalars().first()
        if not machine:
            raise NotFoundException(message="Machine not found")
        machine.name = name if name else machine.name
        machine.location = location if location else machine.location
        print ("Machine has been updated successfully")
        return { "success": True, "message": "Machine has been updated successfully" }
    
    @Transactional()
    async def delete_machine(
        self,
        id: int,
    ) -> dict:
        query = select(Machine).where(Machine.id==id)
        result = await session.execute(query)
        machine = result.scalars().first()
        if not machine:
            raise NotFoundException(message="Machine not found")
        await session.delete(machine)
        print ("Machine has been deleted successfully")
        return { "success": True, "message": "Machine has been deleted successfully" }