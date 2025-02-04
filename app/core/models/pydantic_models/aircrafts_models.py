from pydantic import UUID4, BaseModel, ConfigDict, Field

from .maintenance_models import Maintance


class Aircrafts(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    aircraft_type: str = Field(..., description="Type of the aircraft")
    registration_number: str = Field(
        ..., description="Registration number of the aircraft"
    )
    serial_number: str = Field(..., description="Serial number of the aircraft")


class AircraftPart(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID4 = Field(..., description="Aircraft part ID", alias="id")
    name: str = Field(..., description="Aircraft part name", alias="name")
    description: str = Field(
        ..., description="Aircraft part description", alias="description"
    )
    serial_number: str = Field(
        ..., description="Aircraft part serial number", alias="serial_number"
    )


class GetAircraftParts(AircraftPart):
    maintaince_steps: list[Maintance]
