from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
    GetUserProfilePresenterInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class GetUserProfileInteractor:
    def __init__(self, storage: UserStorageInterface):
        self.storage = storage

    def get_user_profile_wrapper(self, user_id: str,
                                 presenter: GetUserProfilePresenterInterface):
        from ib_iam.adapters.user_service import InvalidUserId
        from ib_iam.adapters.user_service import UserAccountDoesNotExist
        try:
            response = self._get_user_profile_response(
                user_id=user_id, presenter=presenter
            )
        except InvalidUserId:
            response = presenter.raise_exception_for_invalid_user_id()
        except UserAccountDoesNotExist:
            response \
                = presenter.raise_exception_for_user_account_does_not_exist()
        return response

    def _get_user_profile_response(self, user_id: str,
                                   presenter: GetUserProfilePresenterInterface):
        user_profile_dto = self.get_user_profile_dto(user_id=user_id)
        response = presenter.prepare_response_for_user_profile_dto(
            user_profile_dto=user_profile_dto
        )
        return response

    def get_user_profile_dto(self, user_id: str):
        from ib_iam.adapters.service_adapter import get_service_adapter
        user_service = get_service_adapter().user_service
        user_profile_dto = user_service.get_user_profile_dto(user_id=user_id)
        is_admin = self.storage.check_is_admin_user(user_id=user_id)
        user_profile_dto.is_admin = is_admin
        return user_profile_dto
