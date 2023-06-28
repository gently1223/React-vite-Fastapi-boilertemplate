from pydantic import BaseModel
from .machine import GetMachineListResponseSchema


class ExceptionResponseSchema(BaseModel):
    error: str
