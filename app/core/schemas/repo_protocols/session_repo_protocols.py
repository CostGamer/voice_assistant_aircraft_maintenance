from typing import Protocol

from pydantic import UUID4

from app.core.models.pydantic_models import GetSession, PostSession
from app.core.models.sqlalchemy_models import Session


class SessionRepoProtocol(Protocol):
    async def create_session(
        self, session_data: PostSession, users_aircrafts_id: UUID4
    ) -> UUID4:
        """Generate new session"""
        pass

    async def get_current_user_session(self, user_id: UUID4) -> Session | None:
        """Fetch current user session"""
        pass

    async def check_user_active_session(self, user_id: UUID4) -> Session | None:
        """Check if there any active session"""
        pass

    async def get_all_completed_session(self, user_id: UUID4) -> list[GetSession]:
        """Fetch all users's completed sessions"""
        pass
