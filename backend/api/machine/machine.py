from typing import List

from fastapi import APIRouter, Query
from app.machine.models import Machine

from app.machine.services import MachineService
from app.machine.schemas import (
    ExceptionResponseSchema,
    GetMachineListResponseSchema,
)
from .request.machine import (
    AddMachineRequest,
    UpdateMachineRequest,
)

import math
from datetime import datetime

machine_router = APIRouter()

############### Schema ###############
@machine_router.post(
    "/schema/{category}",
    response_model=None,
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def get_schema(
    category: str,
):
    print ("get schema request")
    try:
        machine_schema = eval(category)(
            id = 0,
            name = "",
            location = "",
            email = "",
            number = "",
            enum = True
        )
        response = {k: str(type(v)) for k, v in machine_schema.__dict__.items() if not k.startswith('_')}
    except Exception as e:
        return { "success": False, "message": e.args[0] }
    print ("get schema success")
    return { "success": True, "message": f"Get {category} schema successfully", "info": response }

############### Getting name, location, email, number, enum (active/not active), createat_at and edited_at ###############
@machine_router.post(
    "",
    response_model=None,
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def add_machine(
    request: AddMachineRequest,
):
    response = await MachineService().add_machine(**request.dict())
    return response

############### update machine ###############
@machine_router.put(
    "/{id}",
    response_model=None,
    responses={"404": {"model": ExceptionResponseSchema}},
)
async def update_machine(
    id: int,
    request: UpdateMachineRequest,
):
    response = await MachineService().update_machine(id=id, **request.dict())
    return response

@machine_router.delete(
    "/{id}",
    response_model=None,
    responses={"404": {"model": ExceptionResponseSchema}},
)
async def delete_machine(
    id: int,
):
    response = await MachineService().delete_machine(id=id)
    return response

@machine_router.get(
    "",
    response_model=List[GetMachineListResponseSchema],
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def get_machine_list(
    id: int = Query(None, description="Machine Id"),
    email: str = Query(None, description="Email"),
    page: int = Query(0, description="Page Number"),
    size: int = Query(10, description="Size"),
    order_by: str = Query("id", description="Sort by spec field"),
    desc: bool = Query(False, description="Descending order"),
):
    ts = datetime.utcnow()
    response = await MachineService().get_machine_list(id=id, email=email, page=page, size=size, order_by=order_by, desc=desc)
    consumed = math.ceil((datetime.utcnow().timestamp()-ts.timestamp())*1000)
    print (f"Finished in {consumed}ms")
    return response
