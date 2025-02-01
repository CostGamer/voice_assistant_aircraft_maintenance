from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models.pydantic_models import JWTUser
from app.core.models.sqlalchemy_models import Users


class CommonRepo:
    def __init__(self, con: AsyncSession) -> None:
        self._con = con

    async def check_user_exists_by_login(self, login: str) -> bool:
        query = select(Users).where(Users.login == login)
        query_res = (await self._con.execute(query)).scalar_one_or_none()
        return query_res is not None

    async def get_user_data(self, login: str) -> JWTUser:
        query = select(Users).where(Users.login == login)
        query_res = (await self._con.execute(query)).scalar_one()
        res = JWTUser.model_validate(query_res)
        return res

    async def get_user_data_by_token_sub(self, payload: dict) -> JWTUser:
        user_uuid = payload.get("sub")
        query = select(Users).where(Users.id == user_uuid)
        query_res = (await self._con.execute(query)).scalar_one()
        res = JWTUser.model_validate(query_res)
        return res
