import dataclasses
from ib_iam.interactors.storage_interfaces import \
    StorageInterface
from ib_iam.interactors.presenter_interfaces import \
    PresenterInterface

class InvalidEmail(Exception):
    pass

@dataclasses.dataclass
class EmailAndPasswordDTO:
    email: str
    password: str

class LoginInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def login_wrapper(self, presenter: PresenterInterface,
                      email_and_password_dto: EmailAndPasswordDTO
                      ):
        try:
            self._get_login_response(
                email_and_password_dto=email_and_password_dto, presenter=presenter
            )
            return response
        except:
            pass

    def _get_login_response(self, email_and_password_dto: EmailAndPasswordDTO,
                            presenter: PresenterInterface
                            ):
        token_dto = self.get_token_dto(email_and_password_dto=email_and_password_dto)

    def get_token_dto(self, email_and_password_dto: EmailAndPasswordDTO):
        from ib_iam.adapters import ServiceAdapter
        service_adapter = ServiceAdapter()
        user_id = service_adapter.auth_service.get_user_id_for_email_and_password_dto(
            email_and_password_dto
        )

        return


