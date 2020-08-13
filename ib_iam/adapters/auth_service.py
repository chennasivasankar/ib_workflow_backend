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
        from ib_users.exceptions.custom_exception_constants import \
            USER_ACCOUNT_IS_DEACTIVATED
        if error_type == USER_ACCOUNT_IS_DEACTIVATED.code:
            from ib_iam.exceptions.custom_exceptions import \
                UserAccountDoesNotExist
            raise UserAccountDoesNotExist

    @staticmethod
    def _raise_exception_for_invalid_email(error_type: str):
        from ib_users.exceptions.custom_exception_constants import \
            INVALID_EMAIL
        if error_type == INVALID_EMAIL.code:
            from ib_iam.exceptions.custom_exceptions import InvalidEmail
            raise InvalidEmail

    @staticmethod
    def _raise_exception_for_invalid_password(error_type: str):
        from ib_iam.interactors.user_login_interactor import \
            IncorrectPassword
        from ib_users.exceptions.custom_exception_constants import \
            PASSWORD_AT_LEAST_1_SPECIAL_CHARACTER
        if error_type == PASSWORD_AT_LEAST_1_SPECIAL_CHARACTER.code:
            raise IncorrectPassword
        from ib_users.exceptions.custom_exception_constants import \
            PASSWORD_MIN_LENGTH_IS
        if error_type == PASSWORD_MIN_LENGTH_IS.code:
            raise IncorrectPassword
        from ib_users.exceptions.custom_exception_constants import \
            INCORRECT_PASSWORD
        if error_type == INCORRECT_PASSWORD.code:
            raise IncorrectPassword

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
                from ib_iam.interactors.reset_user_password_interactor import \
                    PasswordAtLeastOneSpecialCharacter
                raise PasswordAtLeastOneSpecialCharacter
            from ib_users.exceptions.custom_exception_constants import \
                PASSWORD_MIN_LENGTH_IS
            if err.error_type == PASSWORD_MIN_LENGTH_IS.code:
                from ib_iam.interactors.reset_user_password_interactor import \
                    PasswordMinLength
                raise PasswordMinLength
        except InvalidTokenException:
            from ib_iam.interactors.reset_user_password_interactor import \
                TokenDoesNotExist
            raise TokenDoesNotExist
        except TokenExpiredException:
            from ib_iam.interactors.reset_user_password_interactor import \
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

    def update_user_password(
            self, user_id: str,
            current_and_new_password_dto: CurrentAndNewPasswordDTO):
        from ib_users.interactors.user_credentials.exceptions \
            .user_credentials_exceptions import InvalidCurrentPasswordException
        from ib_users.interactors.user_credentials.exceptions \
            .user_credentials_exceptions import InvalidNewPasswordException
        from ib_users.interactors.exceptions \
            .user_credentials_exceptions import \
            CurrentPasswordMismatchException
        try:
            self.interface.update_password(
                user_id=user_id,
                new_password=current_and_new_password_dto.new_password,
                current_password=current_and_new_password_dto.current_password
            )
        except InvalidCurrentPasswordException:
            from ib_iam.exceptions.custom_exceptions import \
                InvalidCurrentPassword
            raise InvalidCurrentPassword
        except InvalidNewPasswordException:
            from ib_iam.exceptions.custom_exceptions import InvalidNewPassword
            raise InvalidNewPassword
        except CurrentPasswordMismatchException:
            from ib_iam.exceptions.custom_exceptions import \
                CurrentPasswordMismatch
            raise CurrentPasswordMismatch
