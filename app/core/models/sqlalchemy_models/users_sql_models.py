import uuid
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_sql_models import Base

if TYPE_CHECKING:
    from .aircrafts_sql_models import Aircrafts
    from .airlines_sql_models import Airlines
    from .report_sql_models import Report


class Users(Base):
    __tablename__ = "users"

    login: Mapped[str] = mapped_column(nullable=False, unique=True)
    password: Mapped[bytes] = mapped_column(nullable=False)

    users_airlines: Mapped[list["UsersAirlines"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    users_aircrafts: Mapped[list["UsersAircrafts"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    reports: Mapped[list["Report"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )


class UsersAirlines(Base):
    __tablename__ = "users_airlines"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    airline_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("airlines.id"), nullable=False
    )

    user: Mapped["Users"] = relationship(back_populates="users_airlines")
    airline: Mapped["Airlines"] = relationship(back_populates="users_airlines")


class UsersAircrafts(Base):
    __tablename__ = "users_aircrafts"

    user_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("users.id"), nullable=False)
    aircraft_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("aircrafts.id"), nullable=False
    )

    user: Mapped["Users"] = relationship(back_populates="users_aircrafts")
    aircraft: Mapped["Aircrafts"] = relationship(back_populates="users_aircrafts")
