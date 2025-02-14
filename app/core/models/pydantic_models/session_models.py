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
    dialog_history: dict | None = Field(
        ..., description="Dialogue history as a list of messages"
    )
