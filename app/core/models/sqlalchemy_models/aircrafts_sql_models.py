import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_sql_models import Base

if TYPE_CHECKING:
    from .maintenance_sql_model import MaintenanceStep
    from .users_sql_models import UsersAircrafts


class Aircrafts(Base):
    __tablename__ = "aircrafts"

    aircraft_type: Mapped[str] = mapped_column(nullable=False)
    registration_number: Mapped[str] = mapped_column(nullable=False, unique=True)
    serial_number: Mapped[str] = mapped_column(nullable=False, unique=True)

    users_aircrafts: Mapped[list["UsersAircrafts"]] = relationship(
        back_populates="aircraft"
    )
    aircraft_parts: Mapped[list["AircraftPart"]] = relationship(
        "AircraftPart", back_populates="aircraft"
    )

    def __repr__(self) -> str:
        return f"<Aircraft(type={self.aircraft_type}, reg_number={self.registration_number}, serial_number={self.serial_number})>"


class AircraftPart(Base):
    __tablename__ = "aircraft_parts"

    name: Mapped[str] = mapped_column(nullable=False)
    description: Mapped[str] = mapped_column(nullable=True)
    serial_number: Mapped[str] = mapped_column(nullable=False, unique=True)
    aircraft_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("aircrafts.id"), nullable=False
    )

    aircraft: Mapped["Aircrafts"] = relationship(
        "Aircrafts", back_populates="aircraft_parts"
    )
    maintenance_steps: Mapped[list["MaintenanceStep"]] = relationship(
        "MaintenanceStep", back_populates="part"
    )

    def __repr__(self) -> str:
        return f"<AircraftPart(name={self.name}, description={self.description}, aircraft_id={self.aircraft_id})>"
