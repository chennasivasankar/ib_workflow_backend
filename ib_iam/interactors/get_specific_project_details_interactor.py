from ib_iam.interactors.presenter_interfaces.get_specific_project_details_presenter_interface import \
    GetSpecificProjectDetailsPresenterInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class GetSpecificProjectDetailsInteractor:

    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def get_specific_project_details_wrapper(
            self, project_id: str,
            presenter: GetSpecificProjectDetailsPresenterInterface):
        response = self._get_specific_project_details_response(
            project_id=project_id,
            presenter=presenter)
        return response

    def _get_specific_project_details_response(
            self, project_id: str,
            presenter: GetSpecificProjectDetailsPresenterInterface):
        basic_user_details_dtos, user_role_dtos = \
            self.get_specific_project_details(
                project_id=project_id
            )
        response = \
            presenter.prepare_success_response_for_get_specific_team_details(
                basic_user_details_dtos=basic_user_details_dtos,
                user_role_dtos=user_role_dtos
            )
        return response

    def get_specific_project_details(self, project_id: str):
        '''
        TODO: validate team_id
        '''
        basic_user_details_dtos = self.user_storage.get_team_basic_user_dtos(
            project_id=project_id)
        user_ids = [
            basic_user_details_dto.user_id
            for basic_user_details_dto in basic_user_details_dtos
        ]
        user_role_dtos = self.user_storage.get_user_role_dtos_of_a_team(
            user_ids=user_ids, project_id=project_id
        )
        return basic_user_details_dtos, user_role_dtos
