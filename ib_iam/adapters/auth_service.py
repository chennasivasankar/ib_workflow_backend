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
    def get_user_id_from_email_and_password_dto(
            self, email_and_password_dto: EmailAndPasswordDTO
    ):
        pass

    def get_tokens_dto_from_user_id(self, user_id: int):
        pass

    def user_log_out_from_a_device(self, user_id: int):
        pass

    def get_token_for_reset_password(self, email: str,
                                     expires_in_sec: int):
        pass

    def update_user_password(self, token: str, password: str):
        pass
