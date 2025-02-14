from logging import getLogger

from fastapi import Request
from pydantic import UUID4

from app.core.custom_exceptions import (
    HaveOpenSessionError,
    UserHasNoSessionError,
    UserHasNotPermissionToAircraftError,
)
from app.core.models.pydantic_models import GetSession, PostSession
from app.core.schemas.repo_protocols import CommonRepoProtocol, SessionRepoProtocol
from app.core.schemas.service_protocols import CommonServiceProtocol

logger = getLogger(__name__)


class PostSessionService:
    def __init__(
        self,
        session_repo: SessionRepoProtocol,
        common_service: CommonServiceProtocol,
        common_repo: CommonRepoProtocol,
    ) -> None:
        self._session_repo = session_repo
        self._common_service = common_service
        self._common_repo = common_repo

    async def __call__(self, request: Request, session_data: PostSession) -> UUID4:
        user_id = await self._common_service._get_user_id(request)

        active_session = await self._session_repo.check_user_active_session(user_id)
        if active_session:
            raise HaveOpenSessionError

        get_user_aircraft_id = await self._common_repo.get_user_aircraft(
            aircraft_registration_number=session_data.aircraft_registration_number,
            user_id=user_id,
        )
        if not get_user_aircraft_id:
            raise UserHasNotPermissionToAircraftError

        res = await self._session_repo.create_session(
            session_data=session_data, users_aircrafts_id=get_user_aircraft_id[0]
        )
        return res


class GetCurrentSessionService:
    def __init__(
        self, session_repo: SessionRepoProtocol, common_service: CommonServiceProtocol
    ) -> None:
        self._session_repo = session_repo
        self._common_service = common_service

    async def __call__(
        self,
        request: Request,
    ) -> GetSession:
        user_id = await self._common_service._get_user_id(request)

        session = await self._session_repo.get_current_user_session(user_id)
        if not session:
            raise UserHasNoSessionError

        return GetSession.model_validate(session)


class GetCompletedUserSessionService:
    def __init__(
        self, session_repo: SessionRepoProtocol, common_service: CommonServiceProtocol
    ) -> None:
        self._session_repo = session_repo
        self._common_service = common_service

    async def __call__(
        self,
        request: Request,
    ) -> list[GetSession]:
        user_id = await self._common_service._get_user_id(request)

        sessions = await self._session_repo.get_all_completed_session(user_id)
        return sessions
