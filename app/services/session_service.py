from datetime import datetime, timezone
from typing import Any

from fastapi import Request
from pydantic import UUID4

from app.core.custom_exceptions import (
    AircraftPartNotExistsError,
    HaveOpenSessionError,
    StepNotExistsError,
    UserHasNoSessionError,
    UserHasNotPermissionToAircraftError,
)
from app.core.models.pydantic_models import (
    GetComplitedSession,
    GetSession,
    PostSession,
    PutStepSession,
)
from app.core.schemas.repo_protocols import CommonRepoProtocol, SessionRepoProtocol
from app.core.schemas.service_protocols import CommonServiceProtocol


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

        content: dict[str, Any] = {
            "messages": [],
        }

        res = await self._session_repo.create_session(
            session_data=session_data,
            users_aircrafts_id=get_user_aircraft_id[0],
            content=content,
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


class PatchStepSessionService:
    def __init__(
        self, session_repo: SessionRepoProtocol, common_service: CommonServiceProtocol
    ) -> None:
        self._session_repo = session_repo
        self._common_service = common_service

    async def __call__(
        self,
        request: Request,
        step_data: PutStepSession,
    ) -> GetSession:
        check_step_exists = await self._session_repo.check_step_exists(
            step_data.current_step_id
        )
        if not check_step_exists:
            raise StepNotExistsError

        check_aircraft_part_exists = (
            await self._session_repo.check_aircraft_part_exists(step_data.aircraft_part)
        )
        if not check_aircraft_part_exists:
            raise AircraftPartNotExistsError

        user_id = await self._common_service._get_user_id(request)

        session = await self._session_repo.get_current_user_session(user_id)
        assert session is not None
        current_session = GetSession.model_validate(session)

        updated_dialog_history = await self._update_content_json(
            current_session.dialog_history, step_data
        )

        updated_session = await self._session_repo.update_session_info(
            user_id,
            step_data.current_step_id,
            updated_dialog_history,
        )
        return updated_session

    async def _update_content_json(
        self, dialog_history: dict, step_data: PutStepSession
    ) -> dict:
        def create_message(user: str, message: str) -> dict:
            return {
                "user": user,
                "message": message,
                "date": datetime.now(timezone.utc).isoformat(),
            }

        new_speech = [
            create_message("system", step_data.command_for_maintainer),
            create_message("tech", step_data.maintainer_reply),
        ]

        updated_dialog_history = dialog_history.copy()

        if not updated_dialog_history.get("messages"):
            updated_dialog_history["messages"] = [{step_data.aircraft_part: new_speech}]
        else:
            last_message = updated_dialog_history["messages"][-1]

            if step_data.aircraft_part in last_message:
                last_message[step_data.aircraft_part].extend(new_speech)
            else:
                updated_dialog_history["messages"].append(
                    {step_data.aircraft_part: new_speech}
                )

        return updated_dialog_history


class PatchCompletedSessionService:
    def __init__(
        self, session_repo: SessionRepoProtocol, common_service: CommonServiceProtocol
    ) -> None:
        self._session_repo = session_repo
        self._common_service = common_service

    async def __call__(
        self,
        request: Request,
    ) -> GetComplitedSession:
        user_id = await self._common_service._get_user_id(request)

        return await self._session_repo.completed_session(user_id)
