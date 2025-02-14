class UserWithThisLoginExistsError(Exception):
    pass


class ExpectRefreshTokenError(Exception):
    pass


class InvalidUsernameOrPasswordError(Exception):
    pass


class SpeachGenerationError(Exception):
    pass


class MissingOrBadJWTError(Exception):
    pass


class ExpectAccessTokenError(Exception):
    pass


class SpeachRecognitionError(Exception):
    pass


class FormatError(Exception):
    pass


class UserHasNotPermissionToAircraftError(Exception):
    pass


class UserHasNoSessionError(Exception):
    pass


class HaveOpenSessionError(Exception):
    pass


class StepNotExistsError(Exception):
    pass


class AircraftPartNotExistsError(Exception):
    pass
