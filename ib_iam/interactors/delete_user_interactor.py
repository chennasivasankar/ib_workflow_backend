from ib_iam.exceptions.custom_exceptions import UserIsNotAdmin, UserNotFound, \
    UserDoesNotHaveDeletePermission
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces.delete_user_presenter_interface import \
    DeleteUserPresenterInterface
from ib_iam.interactors.storage_interfaces.delete_user_storage_interface import \
    DeleteUserStorageInterface
from ib_iam.interactors.storage_interfaces.elastic_storage_interface \
    import ElasticSearchStorageInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class DeleteUserInteractor(ValidationMixin):
    def __init__(self, storage: DeleteUserStorageInterface,
                 user_storage: UserStorageInterface,
                 elastic_storage: ElasticSearchStorageInterface):
        self.elastic_storage = elastic_storage
        self.user_storage = user_storage
        self.storage = storage

    def delete_user_wrapper(self, user_id: str, delete_user_id: str,
                            presenter: DeleteUserPresenterInterface):
        try:
            self.delete_user(user_id=user_id, delete_user_id=delete_user_id)
            response = presenter.get_delete_user_response()
        except UserIsNotAdmin:
            response = presenter.response_for_user_is_not_admin_exception()
        except UserNotFound:
            response = presenter.raise_user_is_not_found_exception()
        except UserDoesNotHaveDeletePermission:
            response = presenter.raise_user_does_not_have_delete_permission_exception()
        return response

    def delete_user(self, user_id: str, delete_user_id: str):
        self._validate_delete_user_details(user_id=user_id,
                                           delete_user_id=delete_user_id)
        self.storage.delete_user(user_id=delete_user_id)
        # self.storage.delete_user_roles(user_id=delete_user_id)
        self.storage.delete_user_teams(user_id=delete_user_id)
        self._deactivate_delete_user_id_in_ib_users(
            delete_user_id=delete_user_id)
        self.elastic_storage.delete_elastic_user(user_id=delete_user_id)

    def _validate_delete_user_details(self, user_id: str, delete_user_id: str):
        self._validate_is_user_admin(user_id=user_id)
        self._validate_delete_user_id(delete_user_id=delete_user_id)

    def _validate_delete_user_id(self, delete_user_id: str):
        user_details_dto = self.storage.get_user_details(
            user_id=delete_user_id)
        if user_details_dto.is_admin:
            raise UserDoesNotHaveDeletePermission

    @staticmethod
    def _deactivate_delete_user_id_in_ib_users(delete_user_id: str):
        from ib_iam.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        service_adapter.user_service. \
            deactivate_delete_user_id_in_ib_users(user_id=delete_user_id)
