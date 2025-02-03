from pydantic import BaseModel, ConfigDict, Field

from .aircrafts_models import Aircrafts
from .airlines_models import Airlines


class User(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    login: str = Field(..., description="Login of the user")
    name: str = Field(..., description="Full name of the user")


class GetUser(User):
    airlines: list[Airlines] = Field(
        ..., description="List of airlines associated with the user"
    )
    aircrafts: list[Aircrafts] = Field(
        ..., description="List of aircrafts permit to the user"
    )
