from ib_iam.adapters.auth_service import EmailAndPasswordDTO
from ib_iam.interactors.presenter_interfaces.presenter_interface import \
    AuthPresenterInterface
from ib_iam.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class InvalidEmail(Exception):
    pass


class InvalidPassword(Exception):
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
            return presenter.raise_invalid_email()
        except InvalidPassword:
            return presenter.raise_invalid_password()

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
