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
