import uuid
from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, func
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base_sql_models import Base

if TYPE_CHECKING:
    from .session_sql_models import Session


class Report(Base):
    __tablename__ = "reports"

    session_id: Mapped[uuid.UUID] = mapped_column(
        ForeignKey("session.id"), nullable=False
    )
    report_type: Mapped[str] = mapped_column(nullable=False)
    content: Mapped[dict] = mapped_column(JSONB, nullable=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now())

    session: Mapped["Session"] = relationship("Session", back_populates="reports")

    def __repr__(self) -> str:
        return f"<Report(id={self.id}, session_id={self.session_id}, report_type={self.report_type}, created_at={self.created_at})>"
