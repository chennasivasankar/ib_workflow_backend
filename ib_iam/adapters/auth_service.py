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

    @property
    def interface(self):
        from ib_users.interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()
        return service_interface

    def get_user_tokens_dto_for_given_email_and_password_dto(
            self, email_and_password_dto: EmailAndPasswordDTO
    ) -> UserTokensDTO:
        user_auth_tokens_dto = self.interface.get_user_auth_tokens_for_login_with_email_and_password(
            email=email_and_password_dto.email,
            password=email_and_password_dto.password
        )
        converted_user_tokens_dto = self._convert_to_user_tokens_dto(
            user_auth_tokens_dto)
        return converted_user_tokens_dto

    def user_log_out_from_a_device(self, user_id: int):
        pass

    def get_reset_password_token(self, email: str,
                                 expires_in_sec: int) -> str:
        reset_password_token = self.interface.get_reset_password_token_for_reset_password(
            email=email, token_expiry_in_seconds=expires_in_sec
        )
        return reset_password_token

    def update_user_password_with_reset_password_token(
            self, reset_password_token: str, password: str
    ):
        self.interface.reset_password_for_given_user_password_reset_token(
            token=reset_password_token, new_password=password
        )

    @staticmethod
    def _convert_to_user_tokens_dto(user_auth_tokens_dto):
        from datetime import datetime
        converted_user_tokens_dto = UserTokensDTO(
            user_id=user_auth_tokens_dto.user_id,
            access_token=user_auth_tokens_dto.access_token,
            refresh_token=user_auth_tokens_dto.refresh_token,
            expires_in_seconds=(
                    user_auth_tokens_dto.expires_in-datetime.now()
            ).total_seconds()
        )
        return converted_user_tokens_dto
