from dishka import Provider, Scope, provide
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.schemas.repo_protocols import (
    AuthRepoProtocol,
    CommonRepoProtocol,
    MaintenanceRepoProtocol,
    SessionRepoProtocol,
    UserRepoProtocol,
)
from app.repositories import (
    AuthRepo,
    CommonRepo,
    MaintenanceRepo,
    SessionRepo,
    UserRepo,
)


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

    @provide(scope=Scope.REQUEST)
    async def get_maintenance_repo(self, con: AsyncSession) -> MaintenanceRepoProtocol:
        return MaintenanceRepo(con)

    @provide(scope=Scope.REQUEST)
    async def get_session_repo(self, con: AsyncSession) -> SessionRepoProtocol:
        return SessionRepo(con)
