from fastapi import Request, status
from fastapi.responses import JSONResponse

from app.core.custom_exceptions import (
    ExpectRefreshTokenError,
    FormatError,
    InvalidUsernameOrPasswordError,
    SpeachGenerationError,
    SpeachRecognitionError,
    UserHasNotPermissionToAircraftError,
    UserWithThisLoginExistsError,
)


async def invalid_username_password_error(
    request: Request, exc: InvalidUsernameOrPasswordError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": "Invalid password or username"},
    )


async def user_already_exists_error(
    request: Request, exc: UserWithThisLoginExistsError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": "This login already in the system"},
    )


async def refresh_token_expect_error(
    request: Request, exc: ExpectRefreshTokenError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"detail": "Expect refresh jwt"},
    )


async def speach_generation_error(
    request: Request, exc: SpeachGenerationError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": "Speach can not be generated"},
    )


async def is_directory_error(request: Request, exc: IsADirectoryError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": "Is a directory, not a file"},
    )


async def format_error(request: Request, exc: FormatError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": "The file format is incorrect"},
    )


async def speach_recognition_error(
    request: Request, exc: SpeachRecognitionError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": "The file can not be recognized"},
    )


async def no_permission_error(
    request: Request, exc: UserHasNotPermissionToAircraftError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_403_FORBIDDEN,
        content={"detail": "User has not permission to this aircraft"},
    )
