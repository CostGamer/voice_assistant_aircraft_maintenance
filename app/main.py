from logging import getLogger

from dishka.integrations.fastapi import setup_dishka
from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBearer
from sqlalchemy.exc import NoResultFound

from app.api.exception_responses.exceptions import (
    aircraft_part_not_found_error,
    fill_only_one_gap_error,
    fill_some_gap_error,
    format_error,
    invalid_username_password_error,
    is_directory_error,
    no_open_session_error,
    no_permission_error,
    open_session_error,
    refresh_token_expect_error,
    report_exists_error,
    report_not_found_error,
    session_not_found_error,
    speach_generation_error,
    speach_recognition_error,
    step_not_found_error,
    user_already_exists_error,
    user_has_no_session_error,
)
from app.api.v1.controllers.auth_controller import auth_router
from app.api.v1.controllers.maintenance_controller import maintenance_router
from app.api.v1.controllers.report_controller import report_router
from app.api.v1.controllers.session_controllers import session_router
from app.api.v1.controllers.user_controllers import user_router
from app.api.v1.controllers.voice_controller import voice_router
from app.core.configs import all_settings
from app.core.custom_exceptions import (
    AircraftPartNotExistsError,
    ExpectRefreshTokenError,
    FillOnlyOneParamError,
    FillSomeIDError,
    FormatError,
    HaveOpenSessionError,
    InvalidUsernameOrPasswordError,
    ReportExistsError,
    ReportNotExistsError,
    SessionNotExistsError,
    SpeachGenerationError,
    SpeachRecognitionError,
    StepNotExistsError,
    UserHasNoSessionError,
    UserHasNotPermissionToAircraftError,
    UserWithThisLoginExistsError,
)
from app.core.utils.logger import init_logger
from app.dependencies.container import container
from app.middleware.check_jwt_middleware import CheckJWTAccessMiddleware
from app.middleware.logging_middleware import LoggerMiddleware

logger = getLogger(__name__)


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(UserWithThisLoginExistsError, user_already_exists_error)  # type: ignore
    app.add_exception_handler(ExpectRefreshTokenError, refresh_token_expect_error)  # type: ignore
    app.add_exception_handler(InvalidUsernameOrPasswordError, invalid_username_password_error)  # type: ignore
    app.add_exception_handler(SpeachGenerationError, speach_generation_error)  # type: ignore
    app.add_exception_handler(IsADirectoryError, is_directory_error)  # type: ignore
    app.add_exception_handler(FormatError, format_error)  # type: ignore
    app.add_exception_handler(SpeachRecognitionError, speach_recognition_error)  # type: ignore
    app.add_exception_handler(UserHasNotPermissionToAircraftError, no_permission_error)  # type: ignore
    app.add_exception_handler(HaveOpenSessionError, open_session_error)  # type: ignore
    app.add_exception_handler(UserHasNoSessionError, user_has_no_session_error)  # type: ignore
    app.add_exception_handler(StepNotExistsError, step_not_found_error)  # type: ignore
    app.add_exception_handler(AircraftPartNotExistsError, aircraft_part_not_found_error)  # type: ignore
    app.add_exception_handler(SessionNotExistsError, session_not_found_error)  # type: ignore
    app.add_exception_handler(ReportNotExistsError, report_not_found_error)  # type: ignore
    app.add_exception_handler(FillSomeIDError, fill_some_gap_error)  # type: ignore
    app.add_exception_handler(FillOnlyOneParamError, fill_only_one_gap_error)  # type: ignore
    app.add_exception_handler(ReportExistsError, report_exists_error)  # type: ignore
    app.add_exception_handler(NoResultFound, no_open_session_error)  # type: ignore


def init_routers(app: FastAPI) -> None:
    http_bearer = HTTPBearer(auto_error=True)
    app.include_router(auth_router, prefix="/v1")
    app.include_router(voice_router, prefix="/v1", dependencies=[Depends(http_bearer)])
    app.include_router(user_router, prefix="/v1", dependencies=[Depends(http_bearer)])
    app.include_router(
        session_router, prefix="/v1", dependencies=[Depends(http_bearer)]
    )
    app.include_router(
        maintenance_router, prefix="/v1", dependencies=[Depends(http_bearer)]
    )
    app.include_router(report_router, prefix="/v1", dependencies=[Depends(http_bearer)])


def init_middlewares(app: FastAPI) -> None:
    origins = all_settings.different.origins

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    app.add_middleware(LoggerMiddleware)
    app.add_middleware(CheckJWTAccessMiddleware)


def setup_app() -> FastAPI:
    app = FastAPI(
        title="Betting API",
        description="API for betting on sport events",
        version="0.1.0",
    )
    init_logger(all_settings.logging)
    setup_dishka(app=app, container=container)
    init_routers(app)
    init_middlewares(app)
    register_exception_handlers(app)
    logger.info("App created", extra={"app_version": app.version})
    return app
