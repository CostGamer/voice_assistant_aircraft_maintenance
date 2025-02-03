from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.schemas.repo_protocols import (
    AuthRepoProtocol,
    CommonRepoProtocol,
    UserRepoProtocol,
)
from app.repositories import AuthRepo, CommonRepo, UserRepo


class RepoProviders(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_auth_repo(self, con: AsyncSession) -> AuthRepoProtocol:
        return AuthRepo(con)

    @provide(scope=Scope.REQUEST)
    async def get_common_repo(self, con: AsyncSession) -> CommonRepoProtocol:
        return CommonRepo(con)

    @provide(scope=Scope.REQUEST)
    async def get_user_repo(self, con: AsyncSession) -> UserRepoProtocol:
        return UserRepo(con)
