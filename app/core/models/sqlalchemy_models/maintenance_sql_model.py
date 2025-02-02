import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_sql_models import Base

if TYPE_CHECKING:
    from .aircrafts_sql_models import AircraftPart
    from .session_sql_models import Session


class MaintenanceStep(Base):
    __tablename__ = "maintenance_steps"

    step_name: Mapped[str] = mapped_column(nullable=False)
    step_count: Mapped[int] = mapped_column(nullable=True)
    description: Mapped[str] = mapped_column(nullable=True)
    part_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("aircraft_parts.id"), nullable=False
    )
    status: Mapped[int] = mapped_column(nullable=True)

    part: Mapped["AircraftPart"] = relationship(
        "AircraftPart", back_populates="maintenance_steps"
    )
    session: Mapped["Session"] = relationship(
        "Session", back_populates="maintenance_steps"
    )

    def __repr__(self) -> str:
        return f"<MaintenanceStep(step_name={self.step_name}, order={self.step_count}"
