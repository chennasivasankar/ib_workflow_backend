import dataclasses


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

    def get_tokens_dto_for_given_email_and_password_dto(
            self, email_and_password_dto: EmailAndPasswordDTO
    ) -> TokensDTO:
        pass
