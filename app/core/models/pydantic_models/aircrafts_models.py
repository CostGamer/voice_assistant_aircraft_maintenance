from pydantic import BaseModel, ConfigDict, Field


class Aircrafts(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    aircraft_type: str = Field(..., description="Type of the aircraft")
    registration_number: str = Field(
        ..., description="Registration number of the aircraft"
    )
    serial_number: str = Field(..., description="Serial number of the aircraft")
