from fastapi import Request, status
from fastapi.responses import JSONResponse
from sqlalchemy.exc import NoResultFound

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


async def open_session_error(
    request: Request, exc: HaveOpenSessionError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": "You already have open session"},
    )


async def user_has_no_session_error(
    request: Request, exc: UserHasNoSessionError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "This user has no open session right now"},
    )


async def step_not_found_error(
    request: Request, exc: StepNotExistsError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "This maintenance steps does not exist"},
    )


async def aircraft_part_not_found_error(
    request: Request, exc: AircraftPartNotExistsError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "This aircraft part does not exist"},
    )


async def session_not_found_error(
    request: Request, exc: SessionNotExistsError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "This session does not exist"},
    )


async def report_not_found_error(
    request: Request, exc: ReportNotExistsError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "This report does not exist"},
    )


async def fill_some_gap_error(request: Request, exc: FillSomeIDError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": "You have to fill one of two params"},
    )


async def fill_only_one_gap_error(
    request: Request, exc: FillOnlyOneParamError
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={"detail": "You have to fill only one param"},
    )


async def report_exists_error(request: Request, exc: ReportExistsError) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_409_CONFLICT,
        content={"detail": "Report for this session is already exists"},
    )


async def no_open_session_error(request: Request, exc: NoResultFound) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content={"detail": "There is no open session"},
    )
