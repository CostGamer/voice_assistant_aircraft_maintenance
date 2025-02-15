from dishka import Provider, Scope, provide

from app.core.configs.settings import Settings
from app.core.schemas.repo_protocols import (
    AuthRepoProtocol,
    CommonRepoProtocol,
    MaintenanceRepoProtocol,
    SessionRepoProtocol,
    UserRepoProtocol,
)
from app.core.schemas.service_protocols import (
    CommonServiceProtocol,
    FileServiceProtocol,
    GetCompletedUserSessionServiceProtocol,
    GetCurrentSessionServiceProtocol,
    GetUserServiceProtocol,
    JWTServiceProtocol,
    LoginAuthServiceProtocol,
    MaintenanceServiceProtocol,
    PatchCompletedSessionServiceProtocol,
    PatchStepSessionServiceProtocol,
    PostSessionServiceProtocol,
    RecognitionServiceProtocol,
    RegisterAuthServiceProtocol,
    ReissueTokenServiceProtocol,
    SynthesizeServiceProtocol,
)
from app.services import (
    CommonService,
    FileService,
    GetCompletedUserSessionService,
    GetCurrentSessionService,
    GetUserService,
    JWTService,
    LoginAuthService,
    MaintenanceService,
    PatchCompletedSessionService,
    PatchStepSessionService,
    PostSessionService,
    RecognitionService,
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

    @provide(scope=Scope.REQUEST)
    async def get_user_service(
        self,
        user_repo: UserRepoProtocol,
        common_service: CommonServiceProtocol,
    ) -> GetUserServiceProtocol:
        return GetUserService(user_repo, common_service)

    @provide(scope=Scope.REQUEST)
    async def get_recognize_service(
        self,
        settings: Settings,
        file_service: FileServiceProtocol,
    ) -> RecognitionServiceProtocol:
        return RecognitionService(settings, file_service)

    @provide(scope=Scope.REQUEST)
    async def get_maintenance_service(
        self,
        maintenance_repo: MaintenanceRepoProtocol,
        common_service: CommonServiceProtocol,
    ) -> MaintenanceServiceProtocol:
        return MaintenanceService(maintenance_repo, common_service)

    @provide(scope=Scope.REQUEST)
    async def get_post_session_service(
        self,
        session_repo: SessionRepoProtocol,
        common_repo: CommonRepoProtocol,
        common_service: CommonServiceProtocol,
    ) -> PostSessionServiceProtocol:
        return PostSessionService(session_repo, common_service, common_repo)

    @provide(scope=Scope.REQUEST)
    async def get_current_session_service(
        self,
        session_repo: SessionRepoProtocol,
        common_service: CommonServiceProtocol,
    ) -> GetCurrentSessionServiceProtocol:
        return GetCurrentSessionService(session_repo, common_service)

    @provide(scope=Scope.REQUEST)
    async def get_complited_sessions_service(
        self,
        session_repo: SessionRepoProtocol,
        common_service: CommonServiceProtocol,
    ) -> GetCompletedUserSessionServiceProtocol:
        return GetCompletedUserSessionService(session_repo, common_service)

    @provide(scope=Scope.REQUEST)
    async def get_step_session_service(
        self,
        session_repo: SessionRepoProtocol,
        common_service: CommonServiceProtocol,
    ) -> PatchStepSessionServiceProtocol:
        return PatchStepSessionService(session_repo, common_service)

    @provide(scope=Scope.REQUEST)
    async def get_complete_session_service(
        self,
        session_repo: SessionRepoProtocol,
        common_service: CommonServiceProtocol,
    ) -> PatchCompletedSessionServiceProtocol:
        return PatchCompletedSessionService(session_repo, common_service)
