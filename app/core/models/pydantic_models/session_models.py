from pydantic import UUID4, BaseModel, ConfigDict, Field

from .enum_models import StatusEnum


class SessionBase(BaseModel):
    name: str = Field(..., description="Session's name")
    status: StatusEnum = Field(
        default=StatusEnum.IN_PROGRESS,
        description="Session status (e.g., 'in_progress', 'completed')",
    )


class PostSession(SessionBase):
    aircraft_registration_number: str = Field(
        ..., description="Aircraft that will be maintaince"
    )


class GetSession(SessionBase):
    model_config = ConfigDict(from_attributes=True)

    users_aircrafts_id: UUID4 = Field(
        ..., description="Aircraft related to specific user ID"
    )
    current_step_id: UUID4 | None = Field(
        ..., description="Current maintenance step ID"
    )
    dialog_history: dict = Field(
        ..., description="Dialogue history as a list of messages"
    )


class PutStepSession(BaseModel):
    current_step_id: UUID4 = Field(..., description="Current maintenance step ID")
    aircraft_part: str = Field(..., description="The name of the aircraft part")
    command_for_maintainer: str = Field(
        ..., description="The command that voice assistant give"
    )
    maintainer_reply: str = Field(
        ..., description="The text represantation of the worker reply"
    )


class GetComplitedSession(GetSession):
    model_config = ConfigDict(from_attributes=True)

    id: UUID4 = Field(..., description="ID of updated session")
