from ib_iam.adapters.auth_service import EmailAndPasswordDTO
from ib_iam.exceptions.custom_exceptions import InvalidEmail, \
    UserAccountDoesNotExist
from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
    AuthPresenterInterface

from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class IncorrectPassword(Exception):
    pass


class EmailIsNotVerify(Exception):
    pass


class LoginInteractor:
    def __init__(self, storage: UserStorageInterface):
        self.storage = storage

    def login_wrapper(
            self, presenter: AuthPresenterInterface,
            email_and_password_dto: EmailAndPasswordDTO
    ):
        try:
            response = self._get_login_response(
                email_and_password_dto=email_and_password_dto,
                presenter=presenter
            )
        except InvalidEmail:
            response = presenter.raise_exception_for_invalid_email()
        except UserAccountDoesNotExist:
            response = presenter.raise_exception_for_user_account_does_not_exists()
        except IncorrectPassword:
            response = presenter.raise_exception_for_incorrect_password()
        except EmailIsNotVerify:
            response = presenter.raise_exception_for_login_with_not_verify_email()
        return response

    def _get_login_response(
            self, email_and_password_dto: EmailAndPasswordDTO,
            presenter: AuthPresenterInterface
    ):
        self._validate_email(email=email_and_password_dto.email)
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        user_id = service_adapter.user_service.get_user_id_for_given_email(
            email=email_and_password_dto.email
        )
        user_profile_dto = service_adapter.user_service.get_user_profile_dto(
            user_id=user_id
        )
        is_email_not_verified = not user_profile_dto.is_email_verify
        if is_email_not_verified:
            raise EmailIsNotVerify
        user_tokens_dto, is_admin = self.get_user_tokens_dto_and_is_admin(
            email_and_password_dto=email_and_password_dto
        )
        response = presenter.prepare_response_for_user_tokens_dto_and_is_admin(
            tokens_dto=user_tokens_dto, is_admin=is_admin
        )
        return response

    def get_user_tokens_dto_and_is_admin(
            self, email_and_password_dto: EmailAndPasswordDTO
    ):
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        user_tokens_dto = service_adapter.auth_service.get_user_tokens_dto_for_given_email_and_password_dto(
            email_and_password_dto=email_and_password_dto
        )
        is_admin = self.storage.is_user_admin(user_id=user_tokens_dto.user_id)

        return user_tokens_dto, is_admin

    @staticmethod
    def _validate_email(email: str):
        import re
        from ib_iam.constants.config import EMAIL_DOMAIN_VALIDATION_EXPRESSION
        pattern = EMAIL_DOMAIN_VALIDATION_EXPRESSION
        is_invalid_email = not re.search(pattern, email)
        if is_invalid_email:
            raise InvalidEmail
