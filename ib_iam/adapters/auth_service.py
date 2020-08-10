import dataclasses
from ib_users.validators.base_validator import CustomException


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
        try:
            user_auth_tokens_dto = self.interface. \
                get_user_auth_tokens_for_login_with_email_and_password(
                email=email_and_password_dto.email,
                password=email_and_password_dto.password)
        except CustomException as err:
            from ib_users.exceptions.custom_exception_constants import \
                INVALID_EMAIL
            from ib_iam.interactors.user_login_interactor import \
                IncorrectPassword
            if err.error_type == INVALID_EMAIL.code:
                from ib_iam.exceptions.custom_exceptions import InvalidEmail
                raise InvalidEmail
            from ib_users.exceptions.custom_exception_constants import \
                PASSWORD_AT_LEAST_1_SPECIAL_CHARACTER
            if err.error_type == PASSWORD_AT_LEAST_1_SPECIAL_CHARACTER.code:
                raise IncorrectPassword
            from ib_users.exceptions.custom_exception_constants import \
                PASSWORD_MIN_LENGTH_IS
            if err.error_type == PASSWORD_MIN_LENGTH_IS.code:
                raise IncorrectPassword
            from ib_users.exceptions.custom_exception_constants import \
                USER_ACCOUNT_IS_DEACTIVATED
            if err.error_type == USER_ACCOUNT_IS_DEACTIVATED.code:
                from ib_iam.exceptions.custom_exceptions import \
                    UserAccountDoesNotExist
                raise UserAccountDoesNotExist
        else:
            converted_user_tokens_dto = self._convert_to_user_tokens_dto(
                user_auth_tokens_dto)
            return converted_user_tokens_dto

    def user_log_out_from_a_device(self, user_id: str):
        self.interface.logout_in_all_devices(user_id=user_id)

    def get_reset_password_token(self, email: str, expires_in_sec: int) -> str:
        from ib_users.interactors.exceptions.user_credentials_exceptions import \
            AccountWithEmailDoesntExistException
        try:
            reset_password_token = self.interface. \
                get_reset_password_token_for_reset_password(
                email=email, token_expiry_in_seconds=expires_in_sec)
            return reset_password_token
        except CustomException as err:
            from ib_users.exceptions.custom_exception_constants import \
                INVALID_EMAIL
            if err.error_type == INVALID_EMAIL.code:
                from ib_iam.exceptions.custom_exceptions import InvalidEmail
                raise InvalidEmail
        except AccountWithEmailDoesntExistException:
            from ib_iam.exceptions.custom_exceptions import \
                UserAccountDoesNotExist
            raise UserAccountDoesNotExist

    def update_user_password_with_reset_password_token(
            self, reset_password_token: str, password: str):
        from ib_users.interactors.exceptions.user_credentials_exceptions import \
            InvalidTokenException
        from ib_users.interactors.exceptions.user_credentials_exceptions import \
            TokenExpiredException
        try:
            self.interface.reset_password_for_given_user_password_reset_token(
                token=reset_password_token, new_password=password)
        except CustomException as err:
            from ib_users.exceptions.custom_exception_constants import \
                PASSWORD_AT_LEAST_1_SPECIAL_CHARACTER
            if err.error_type == PASSWORD_AT_LEAST_1_SPECIAL_CHARACTER.code:
                from ib_iam.interactors.update_user_password_interactor import \
                    PasswordAtLeastOneSpecialCharacter
                raise PasswordAtLeastOneSpecialCharacter
            from ib_users.exceptions.custom_exception_constants import \
                PASSWORD_MIN_LENGTH_IS
            if err.error_type == PASSWORD_MIN_LENGTH_IS.code:
                from ib_iam.interactors.update_user_password_interactor import \
                    PasswordMinLength
                raise PasswordMinLength
        except InvalidTokenException:
            from ib_iam.interactors.update_user_password_interactor import \
                TokenDoesNotExist
            raise TokenDoesNotExist
        except TokenExpiredException:
            from ib_iam.interactors.update_user_password_interactor import \
                TokenHasExpired
            raise TokenHasExpired

    @staticmethod
    def _convert_to_user_tokens_dto(user_auth_tokens_dto):
        converted_user_tokens_dto = UserTokensDTO(
            user_id=user_auth_tokens_dto.user_id,
            access_token=user_auth_tokens_dto.access_token,
            refresh_token=user_auth_tokens_dto.refresh_token,
            expires_in_seconds=user_auth_tokens_dto.expires_in
        )
        return converted_user_tokens_dto
