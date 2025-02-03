from pydantic import BaseModel, ConfigDict, Field


class Airlines(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    name: str = Field(..., description="Name of the airline")
    registration_number: str = Field(
        ..., description="Registration number of the airline"
    )
