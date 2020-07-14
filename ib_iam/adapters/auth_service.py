import dataclasses
from datetime import datetime


@dataclasses.dataclass
class EmailAndPasswordDTO:
    email: str
    password: str


@dataclasses.dataclass
class TokensDTO:
    access_token: str
    refresh_token: str
    expires_in_seconds: int


class AuthService:
    def get_user_id_from_email_and_password_dto(self):
        pass

    def get_tokens_dto_from_user_id(self, user_id: int):
        pass
