from pydantic import BaseModel, Field


class AddMachineRequest(BaseModel):
    name: str = Field("Machine", description="Machine name")
    location: str = Field(None, description="Machine location")
    email: str = Field(..., description="Machine email")
    number: str = Field(..., description="Machine number")
    enum: bool = Field(False, description="Machine enum")

class UpdateMachineRequest(BaseModel):
    name: str = Field("Machine", description="Machine Name")
    location: str = Field(None, description="Machine location")
