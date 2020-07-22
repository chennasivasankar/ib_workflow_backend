from ib_iam.exceptions.exceptions import UserIsNotAdmin
from ib_iam.interactors.presenter_interfaces.delete_user_presenter_interface import \
    DeleteUserPresenterInterface
from ib_iam.interactors.storage_interfaces.delete_user_storage_interface import \
    DeleteUserStorageInterface


class DeleteUserInteractor:
    def __init__(self, storage: DeleteUserStorageInterface):
        self.storage = storage

    def delete_user_wrapper(self, user_id: str, delete_user_id: str,
                            presenter: DeleteUserPresenterInterface):
        try:
            self.delete_user(user_id=user_id, delete_user_id=delete_user_id)
            response = presenter.get_delete_user_response()
        except UserIsNotAdmin:
            response = presenter.raise_user_is_not_admin_exception()
        return response

    def delete_user(self, user_id: str, delete_user_id: str):
        self._validate_delete_user_details(user_id=user_id,
                                           delete_user_id=delete_user_id)
        self.storage.delete_user(user_id=delete_user_id)
        self.storage.delete_user_roles(user_id=delete_user_id)
        self.storage.delete_user_teams(user_id=delete_user_id)

    def _validate_delete_user_details(self, user_id: str, delete_user_id: str):
        self._validate_user_is_admin(user_id=user_id)

    def _validate_user_is_admin(self, user_id: str):
        is_admin_user = self.storage.is_admin_user(user_id=user_id)
        print(is_admin_user)
        if not is_admin_user:
            raise UserIsNotAdmin()
