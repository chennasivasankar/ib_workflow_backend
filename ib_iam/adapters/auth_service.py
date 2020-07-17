import dataclasses


@dataclasses.dataclass
class EmailAndPasswordDTO:
    email: str
    password: str


@dataclasses.dataclass
class UserTokensDTO:
    access_token: str
    refresh_token: str
    expires_in_seconds: int
    user_id: str


class AuthService:

    def get_user_tokens_dto_for_given_email_and_password_dto(
            self, email_and_password_dto: EmailAndPasswordDTO
    ) -> UserTokensDTO:
        pass

    def user_log_out_from_a_device(self, user_id: int):
        pass

    def get_token_for_reset_password(self, email: str,
                                     expires_in_sec: int) -> str:
        pass

    def update_user_password_with_reset_password_token(
            self, reset_password_token: str, password: str
    ):
        pass
