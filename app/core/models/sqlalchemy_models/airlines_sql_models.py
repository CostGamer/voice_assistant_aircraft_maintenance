from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_sql_models import Base

if TYPE_CHECKING:
    from .users_sql_models import UsersAirlines


class Airlines(Base):
    __tablename__ = "airlines"

    name: Mapped[str] = mapped_column(nullable=False)
    registration_number: Mapped[str] = mapped_column(unique=True, nullable=False)

    users_airlines: Mapped[list["UsersAirlines"]] = relationship(
        back_populates="airline"
    )

    def __repr__(self) -> str:
        return f"<Airlines(name={self.name}, registration_number={self.registration_number})>"
