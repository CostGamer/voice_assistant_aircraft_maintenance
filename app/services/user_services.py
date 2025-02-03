from fastapi import Request

from app.core.models.pydantic_models import GetUser
from app.core.schemas.repo_protocols import UserRepoProtocol
from app.core.schemas.service_protocols import CommonServiceProtocol


class GetUserService:
    def __init__(
        self, user_repo: UserRepoProtocol, common_service: CommonServiceProtocol
    ) -> None:
        self._user_repo = user_repo
        self._common_service = common_service

    async def __call__(self, request: Request) -> GetUser:
        user_id = await self._common_service._get_user_id(request)
        get_user_data = await self._user_repo.get_user_data(user_id)

        get_user_airlines = await self._user_repo.get_all_airlines_related_to_user(
            user_id
        )
        get_user_aircrafts = await self._user_repo.get_all_aircraft_related_to_user(
            user_id
        )

        return GetUser(
            login=get_user_data.login,
            name=get_user_data.name,
            airlines=get_user_airlines,
            aircrafts=get_user_aircrafts,
        )
