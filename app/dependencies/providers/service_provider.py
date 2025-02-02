from dishka import Provider, Scope, provide

from app.core.configs.settings import Settings
from app.core.schemas.repo_protocols import AuthRepoProtocol, CommonRepoProtocol
from app.core.schemas.service_protocols import (
    CommonServiceProtocol,
    FileServiceProtocol,
    JWTServiceProtocol,
    LoginAuthServiceProtocol,
    RegisterAuthServiceProtocol,
    ReissueTokenServiceProtocol,
    SynthesizeServiceProtocol,
)
from app.services import (
    CommonService,
    FileService,
    JWTService,
    LoginAuthService,
    RegisterAuthService,
    ReissueTokenService,
    SynthesizeService,
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

    @provide(scope=Scope.REQUEST)
    async def get_synthesize_service(
        self,
        settings: Settings,
        file_service: FileServiceProtocol,
    ) -> SynthesizeServiceProtocol:
        return SynthesizeService(settings, file_service)

    @provide(scope=Scope.REQUEST)
    async def get_file_service(
        self,
    ) -> FileServiceProtocol:
        return FileService()
