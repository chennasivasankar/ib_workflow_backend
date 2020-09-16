import dataclasses

from ib_users.validators.base_validator import CustomException

from ib_iam.interactors.update_user_password_interactor import \
    CurrentAndNewPasswordDTO


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


class AccessTokenNotFound(Exception):
    pass


class UserAccountNotFound(Exception):
    pass


class RefreshTokenHasExpired(Exception):
    pass


class RefreshTokenHasNotFound(Exception):
    pass


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
            self._raise_exception_for_invalid_email(error_type=err.error_type)
            self._raise_exception_for_invalid_password(
                error_type=err.error_type)
            self._raise_exception_for_account_id_deactivated(
                error_type=err.error_type)
        else:
            converted_user_tokens_dto = self._convert_to_user_tokens_dto(
                user_auth_tokens_dto)
            return converted_user_tokens_dto

    @staticmethod
    def _raise_exception_for_account_id_deactivated(error_type: str):
        from ib_users.exceptions.custom_exception_constants import (
            USER_ACCOUNT_IS_DEACTIVATED, NOT_REGISTERED_USER
        )
        from ib_iam.exceptions.custom_exceptions import \
            UserAccountDoesNotExist

        if error_type == USER_ACCOUNT_IS_DEACTIVATED.code:
            raise UserAccountDoesNotExist
        if error_type == NOT_REGISTERED_USER.code:
            raise UserAccountDoesNotExist

    @staticmethod
    def _raise_exception_for_invalid_email(error_type: str):
        from ib_users.exceptions.custom_exception_constants import (
            INVALID_EMAIL
        )
        if error_type == INVALID_EMAIL.code:
            from ib_iam.exceptions.custom_exceptions import InvalidEmail
            raise InvalidEmail

    @staticmethod
    def _raise_exception_for_invalid_password(error_type: str):
        from ib_iam.interactors.user_login_interactor import (
            IncorrectPassword
        )
        from ib_users.exceptions.custom_exception_constants import (
            PASSWORD_AT_LEAST_1_SPECIAL_CHARACTER,
            INCORRECT_PASSWORD, PASSWORD_MIN_LENGTH_IS
        )

        if error_type == PASSWORD_AT_LEAST_1_SPECIAL_CHARACTER.code:
            raise IncorrectPassword
        if error_type == PASSWORD_MIN_LENGTH_IS.code:
            raise IncorrectPassword
        if error_type == INCORRECT_PASSWORD.code:
            raise IncorrectPassword

    def user_log_out_from_a_device(self, user_id: str):
        self.interface.logout_in_all_devices(user_id=user_id)

    def get_reset_password_token(self, email: str, expires_in_sec: int) -> str:
        from ib_users.interactors.exceptions.user_credentials_exceptions import (
            AccountWithEmailDoesntExistException)
        from ib_users.exceptions.custom_exception_constants import (
            INVALID_EMAIL)
        from ib_iam.exceptions.custom_exceptions import (
            UserAccountDoesNotExist, InvalidEmail)

        try:
            reset_password_token = self.interface. \
                get_reset_password_token_for_reset_password(
                email=email, token_expiry_in_seconds=expires_in_sec)
            return reset_password_token
        except CustomException as err:
            if err.error_type == INVALID_EMAIL.code:
                raise InvalidEmail
        except AccountWithEmailDoesntExistException:
            raise UserAccountDoesNotExist

    def update_user_password_with_reset_password_token(
            self, reset_password_token: str, password: str):
        from ib_users.interactors.exceptions.user_credentials_exceptions import (
            InvalidTokenException, TokenExpiredException)
        from ib_users.exceptions.custom_exception_constants import (
            PASSWORD_AT_LEAST_1_SPECIAL_CHARACTER, PASSWORD_MIN_LENGTH_IS)
        from ib_iam.interactors.reset_user_password_interactor import (
            PasswordAtLeastOneSpecialCharacter, PasswordMinLength,
            TokenDoesNotExist, TokenHasExpired
        )
        try:
            self.interface.reset_password_for_given_user_password_reset_token(
                token=reset_password_token, new_password=password)
        except CustomException as err:
            if err.error_type == PASSWORD_AT_LEAST_1_SPECIAL_CHARACTER.code:
                raise PasswordAtLeastOneSpecialCharacter
            if err.error_type == PASSWORD_MIN_LENGTH_IS.code:
                raise PasswordMinLength
        except InvalidTokenException:
            raise TokenDoesNotExist
        except TokenExpiredException:
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

    def update_user_password(
            self, user_id: str,
            current_and_new_password_dto: CurrentAndNewPasswordDTO):
        from ib_users.interactors.user_credentials.exceptions.user_credentials_exceptions import (
            InvalidCurrentPasswordException, InvalidNewPasswordException
        )
        from ib_users.interactors.exceptions.user_credentials_exceptions import (
            CurrentPasswordMismatchException)
        from ib_iam.exceptions.custom_exceptions import (
            InvalidNewPassword, CurrentPasswordMismatch,
            InvalidCurrentPassword)
        try:
            self.interface.update_password(
                user_id=user_id,
                new_password=current_and_new_password_dto.new_password,
                current_password=current_and_new_password_dto.current_password
            )
        except InvalidCurrentPasswordException:
            raise InvalidCurrentPassword
        except InvalidNewPasswordException:
            raise InvalidNewPassword
        except CurrentPasswordMismatchException:
            raise CurrentPasswordMismatch

    def get_refresh_auth_tokens_dto(
            self, access_token: str, refresh_token: str
    ) -> UserTokensDTO:
        from ib_users.constants.custom_exception_messages import (
            INVALID_ACCESS_TOKEN)
        from django_swagger_utils.drf_server.exceptions import NotFound
        from ib_users.exceptions.custom_exception_constants import (
            USER_ACCOUNT_IS_DEACTIVATED)
        from ib_users.exceptions.oauth2_exceptions import RefreshTokenExpired
        from ib_users.exceptions.oauth2_exceptions import RefreshTokenNotFound

        try:
            user_auth_tokens_dto = \
                self.interface.refresh_auth_tokens(
                    access_token=access_token, refresh_token=refresh_token
                )
        except NotFound as err:
            if err.res_status == INVALID_ACCESS_TOKEN.code:
                raise AccessTokenNotFound
        except RefreshTokenExpired:
            raise RefreshTokenHasExpired
        except RefreshTokenNotFound:
            raise RefreshTokenHasNotFound
        except CustomException as err:
            if err.error_type == USER_ACCOUNT_IS_DEACTIVATED.code:
                raise UserAccountNotFound
        else:
            converted_user_tokens_dto = self._convert_to_user_tokens_dto(
                user_auth_tokens_dto)
            return converted_user_tokens_dto

    def create_auth_tokens_for_user(
            self, user_id: str, expiry_in_seconds: int) -> UserTokensDTO:
        user_auth_tokens_dto = self.interface.create_auth_tokens_for_user(
            user_id=user_id,
            expiry_in_seconds=expiry_in_seconds)
        converted_user_tokens_dto = self._convert_to_user_tokens_dto(
            user_auth_tokens_dto)
        return converted_user_tokens_dto

    def update_is_email_verified_value_in_ib_user(
            self, user_id: str, is_email_verified: bool
    ):
        from ib_users.interactors.user_profile_interactor import UserProfileDTO
        user_profile = UserProfileDTO(
            is_email_verified=is_email_verified
        )
        self.interface.update_user_profile(
            user_id=user_id, user_profile=user_profile)
