from datetime import datetime

from pydantic import UUID4, BaseModel, ConfigDict, Field

from .enum_models import ReportTypeEnum


class ReportBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    session_id: UUID4 = Field(
        ..., description="Unique identifier of the session associated with the report"
    )
    report_type: ReportTypeEnum = Field(
        default=ReportTypeEnum.DIALOG_HISTORY,
        description="Type of the report (e.g., error report, dialog_history report, etc.)",
    )
    content: dict = Field(
        ..., description="Detailed content of the report in JSON format"
    )
    created_at: datetime = Field(
        ..., description="Timestamp of when the report was created (UTC)"
    )
