from pydantic import BaseModel, ConfigDict, JsonValue


class CustomPydanticBase(BaseModel):
    model_config = ConfigDict(
        strict=True,
        frozen=True,
        extra='forbid',
        from_attributes=True,
        revalidate_instances='always',
        validate_default=True,
        validate_return=True,
        validate_assignment=True,
    )


class UserModel(CustomPydanticBase):
    id: int
    name: str
    password_text: str
    device_type: str
    remember_token: str


class ResponseModel(CustomPydanticBase):
    response: str | JsonValue


class APIResponseModel(CustomPydanticBase):
    success: bool


class APIErrorResponseModel(APIResponseModel):
    success: bool = False
    message: str


class APISuccessResponseModel(APIResponseModel):
    success: bool = True
    data: JsonValue
