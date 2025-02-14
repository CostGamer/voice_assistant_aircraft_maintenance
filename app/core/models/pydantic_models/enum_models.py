from enum import Enum


class StatusEnum(str, Enum):
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ERROR = "error"
