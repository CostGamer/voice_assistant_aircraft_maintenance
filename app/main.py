from logging import getLogger

from dishka.integrations.fastapi import setup_dishka
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.exception_responses.exceptions import (
    invalid_username_password_error,
    refresh_token_expect_error,
    user_already_exists_error,
)
from app.api.v1.controllers.auth_controller import auth_router
from app.core.configs import all_settings
from app.core.custom_exceptions import (
    ExpectRefreshTokenError,
    InvalidUsernameOrPasswordError,
    UserWithThisLoginExistsError,
)
from app.core.utils.logger import init_logger
from app.dependencies.container import container
from app.middleware.logging_middleware import LoggerMiddleware

logger = getLogger(__name__)


# @asynccontextmanager
# async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
#     async with container() as request_container:
#         # app.state.dishka_container = request_container
#         # app.state.jwt_service = await request_container.get(JWTServiceProtocol)

#         consumer_service: ConsumerService = await request_container.get(ConsumerService)
#         bg_task_service: BackgroundTasksServiceProtocol = await request_container.get(
#             BackgroundTasksServiceProtocol
#         )

#         async def run_tasks() -> None:
#             await asyncio.gather(
#                 consumer_service.consume_forever(),
#                 bg_task_service.monitor_periodically(),
#             )

#         tasks: asyncio.Task = asyncio.create_task(run_tasks())

#         yield
#         tasks.cancel()


def register_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(UserWithThisLoginExistsError, user_already_exists_error)  # type: ignore
    app.add_exception_handler(ExpectRefreshTokenError, refresh_token_expect_error)  # type: ignore
    app.add_exception_handler(InvalidUsernameOrPasswordError, invalid_username_password_error)  # type: ignore


def init_routers(app: FastAPI) -> None:
    # http_bearer = HTTPBearer(auto_error=True)
    app.include_router(auth_router, prefix="/v1")


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
    # app.add_middleware(CheckJWTAccessMiddleware)


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
