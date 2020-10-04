from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import AuthPresenterInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import UserStorageInterface


class GetUserInvitationCodeInteractor:
    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def get_user_invitation_code_wrapper(
            self, user_id: str, presenter: AuthPresenterInterface):
        invitation_code = self.get_user_invitation_code(
            user_id)
        response = presenter.get_success_response(invitation_code)
        return response

    def get_user_invitation_code(self, user_id) -> str:
        invitation_code = self.user_storage.get_user_invitation_code(user_id)
        return invitation_code
