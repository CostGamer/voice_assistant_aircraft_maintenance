from enum import Enum


class StatusEnum(str, Enum):
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ERROR = "error"


class ReportTypeEnum(str, Enum):
    ERROR_REPORT = "error_report"
    DIALOG_HISTORY = "dialog_history"
