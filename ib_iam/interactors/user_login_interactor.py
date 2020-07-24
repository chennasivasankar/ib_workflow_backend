from ib_iam.adapters.auth_service import EmailAndPasswordDTO
from ib_iam.exceptions.custom_exceptions import InvalidEmail, \
    UserAccountDoesNotExist
from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
    AuthPresenterInterface

from ib_iam.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class IncorrectPassword(Exception):
    pass


class LoginInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def login_wrapper(self, presenter: AuthPresenterInterface,
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
        return response

    def _get_login_response(self, email_and_password_dto: EmailAndPasswordDTO,
                            presenter: AuthPresenterInterface
                            ):
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
            email_and_password_dto=email_and_password_dto,
        )
        user_id = user_tokens_dto.user_id
        is_admin = self.storage.check_is_admin_user(user_id=user_id)

        return user_tokens_dto, is_admin
