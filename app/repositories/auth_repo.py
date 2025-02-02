import bcrypt
from pydantic import UUID4
from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.models.pydantic_models import RegisterUser
from app.core.models.sqlalchemy_models import Users


class AuthRepo:
    def __init__(self, con: AsyncSession) -> None:
        self._con = con

    async def register_user(self, user: RegisterUser) -> UUID4:
        query = (
            insert(Users)
            .values(
                login=user.login,
                password=self._hash_password(user.password),
                name=user.name,
            )
            .returning(Users.id)
        )
        query_res = (await self._con.execute(query)).scalar_one()
        return query_res

    def _hash_password(self, password: str) -> bytes:
        salt = bcrypt.gensalt()
        pwd_bytes: bytes = password.encode()
        return bcrypt.hashpw(pwd_bytes, salt=salt)
