from dishka import Provider, Scope, provide

from app.core.schemas.repo_protocols import AuthRepoProtocol, CommonRepoProtocol
from app.core.schemas.service_protocols import (
    CommonServiceProtocol,
    JWTServiceProtocol,
    LoginAuthServiceProtocol,
    RegisterAuthServiceProtocol,
    ReissueTokenServiceProtocol,
)
from app.services import (
    CommonService,
    JWTService,
    LoginAuthService,
    RegisterAuthService,
    ReissueTokenService,
)


class ServiceProviders(Provider):
    @provide(scope=Scope.REQUEST)
    async def get_jwt_service(
        self, common_repo: CommonRepoProtocol
    ) -> JWTServiceProtocol:
        return JWTService(common_repo)

    @provide(scope=Scope.REQUEST)
    async def get_register_service(
        self, auth_repo: AuthRepoProtocol, common_repo: CommonRepoProtocol
    ) -> RegisterAuthServiceProtocol:
        return RegisterAuthService(auth_repo, common_repo)

    @provide(scope=Scope.REQUEST)
    async def get_login_service(
        self, jwt_service: JWTServiceProtocol
    ) -> LoginAuthServiceProtocol:
        return LoginAuthService(jwt_service)

    @provide(scope=Scope.REQUEST)
    async def get_reissue_service(
        self, jwt_service: JWTServiceProtocol, common_repo: CommonRepoProtocol
    ) -> ReissueTokenServiceProtocol:
        return ReissueTokenService(jwt_service, common_repo)

    @provide(scope=Scope.REQUEST)
    async def get_common_service(
        self, jwt_service: JWTServiceProtocol
    ) -> CommonServiceProtocol:
        return CommonService(jwt_service)
