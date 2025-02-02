import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_sql_models import Base

if TYPE_CHECKING:
    from .maintenance_sql_model import MaintenanceStep
    from .report_sql_models import Report
    from .users_sql_models import UsersAircrafts


class Session(Base):
    __tablename__ = "session"

    users_aircrafts_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("users_aircrafts.id"), nullable=False
    )
    name: Mapped[str] = mapped_column(nullable=False)
    current_step_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("maintenance_steps.id"), nullable=False
    )
    status: Mapped[str] = mapped_column(nullable=False)

    users_aircrafts: Mapped["UsersAircrafts"] = relationship(
        "UsersAircrafts", back_populates="session"
    )

    maintenance_steps: Mapped[list["MaintenanceStep"]] = relationship(
        "MaintenanceStep", back_populates="session"
    )

    reports: Mapped[list["Report"]] = relationship("Report", back_populates="session")

    def __repr__(self) -> str:
        return f"<Session(id={self.id}, name={self.name}, status={self.status}, current_step_id={self.current_step_id})>"
