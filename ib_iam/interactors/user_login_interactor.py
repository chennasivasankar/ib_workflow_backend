from django.http import HttpResponse

from ib_iam.adapters.auth_service import EmailAndPasswordDTO, TokensDTO
from ib_iam.interactors.presenter_interfaces.presenter_interface import \
    AuthPresenterInterface
from ib_iam.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class UserAccountDoesNotExist(Exception):
    pass


class IncorrectPassword(Exception):
    pass


class InvalidEmail(Exception):
    pass


class PasswordMinLength(Exception):
    pass


class PasswordAtLeastOneSpecialCharacter(Exception):
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
            return response
        except InvalidEmail:
            return presenter.raise_exception_for_invalid_email()
        except IncorrectPassword:
            return presenter.raise_exception_for_incorrect_password()
        except UserAccountDoesNotExist:
            return presenter.raise_exception_for_user_account_does_not_exists()
        except PasswordMinLength:
            return presenter.raise_exception_for_password_min_length_required()
        except PasswordAtLeastOneSpecialCharacter:
            return presenter.raise_exception_for_password_at_least_one_special_character_required ()

    def _get_login_response(self, email_and_password_dto: EmailAndPasswordDTO,
                            presenter: AuthPresenterInterface
                            ):
        tokens_dto, is_admin = self.get_tokens_dto_and_is_admin(
            email_and_password_dto=email_and_password_dto
        )
        response = presenter.prepare_response_for_tokens_dto(
            tokens_dto=tokens_dto, is_admin=is_admin
        )
        return response

    def get_tokens_dto_and_is_admin(
            self, email_and_password_dto: EmailAndPasswordDTO
    ):
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        user_id = service_adapter.auth_service. \
            get_user_id_from_email_and_password_dto(email_and_password_dto)
        is_admin = self.storage.get_is_admin_of_given_user_id(user_id=user_id)
        tokens_dto = service_adapter.auth_service.get_tokens_dto_from_user_id(
            user_id=user_id,
        )

        return tokens_dto, is_admin
