from ib_iam.exceptions.custom_exceptions import UserIsNotAdmin, UserNotFound
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
        except UserNotFound:
            response = presenter.raise_user_is_not_found_exception()
        return response

    def delete_user(self, user_id: str, delete_user_id: str):
        self._validate_delete_user_details(user_id=user_id,
                                           delete_user_id=delete_user_id)
        self.storage.delete_user(user_id=delete_user_id)
        self.storage.delete_user_roles(user_id=delete_user_id)
        self.storage.delete_user_teams(user_id=delete_user_id)

    def _validate_delete_user_details(self, user_id: str, delete_user_id: str):
        self._validate_user_is_admin(user_id=user_id)
        self._validate_delete_user_id(delete_user_id=delete_user_id)

    def _validate_user_is_admin(self, user_id: str):
        is_admin_user = self.storage.check_is_admin_user(user_id=user_id)
        if not is_admin_user:
            raise UserIsNotAdmin()

    def _validate_delete_user_id(self, delete_user_id: str):
        self.storage.get_user_details(user_id=delete_user_id)
