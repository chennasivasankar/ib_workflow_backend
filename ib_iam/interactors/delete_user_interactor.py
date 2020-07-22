from ib_iam.interactors.presenter_interfaces.delete_user_presenter_interface import \
    DeleteUserPresenterInterface
from ib_iam.interactors.storage_interfaces.delete_user_storage_interface import \
    DeleteUserStorageInterface


class DeleteUserInteractor:
    def __init__(self, storage: DeleteUserStorageInterface):
        self.storage = storage

    def delete_user_wrapper(self, user_id: str, delete_user_id: str,
                            presenter: DeleteUserPresenterInterface):
        self.delete_user(user_id=user_id, delete_user_id=delete_user_id)
        response = presenter.get_delete_user_response()
        return response

    def delete_user(self, user_id: str, delete_user_id: str):
        self.storage.delete_user(user_id=user_id,
                                 delete_user_id=delete_user_id)
