from pydantic import UUID4, BaseModel, ConfigDict, Field


class RegisterUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    login: str = Field(..., description="user login")
    password: str = Field(..., description="user password")
    name: str = Field(..., description="user fullname")


class JWTUser(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: UUID4 = Field(..., description="user ID")
    login: str = Field(..., description="user login")
    password: bytes = Field(..., description="user hashed password")


class JWTTokenInfo(BaseModel):
    access_token: str = Field(..., description="JWT access token")
    refresh_token: str | None = Field(default=None, description="JWT refresh token")
    token_type: str | None = Field(default="Bearer", description="token type")
