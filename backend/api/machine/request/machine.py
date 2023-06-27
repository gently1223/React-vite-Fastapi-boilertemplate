from pydantic import BaseModel, Field


class AddMachineRequest(BaseModel):
    name: str | None = Field("Machine", description="Machine name")
    location: str | None = Field(None, description="Machine location")
    email: str = Field(..., description="Machine email")
    number: str = Field(..., description="Machine number")
    enum: bool | None = Field(False, description="Machine enum")

class UpdateMachineRequest(BaseModel):
    name: str | None = Field("Machine", description="Machine Name")
    location: str | None = Field(None, description="Machine location")
