from ib_iam.interactors.presenter_interfaces.get_specific_team_details_presenter_interface import \
    GetSpecificTeamDetailsPresenterInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class GetSpecificTeamDetailsInteractor:

    def __init__(self, user_storage: UserStorageInterface):
        self.user_storage = user_storage

    def get_specific_team_details_wrapper(
            self, team_id: str,
            presenter: GetSpecificTeamDetailsPresenterInterface):
        response = self._get_specific_team_details_response(
            team_id=team_id,
            presenter=presenter)
        return response

    def _get_specific_team_details_response(
            self, team_id: str,
            presenter: GetSpecificTeamDetailsPresenterInterface):
        basic_user_details_dtos, user_role_dtos = \
            self.get_specific_team_details(
                team_id=team_id
            )
        response = \
            presenter.prepare_success_response_for_get_specific_team_details(
                basic_user_details_dtos=basic_user_details_dtos,
                user_role_dtos=user_role_dtos
            )
        return response

    def get_specific_team_details(self, team_id: str):
        '''
        TODO: validate team_id
        '''
        basic_user_details_dtos = self.user_storage.get_team_basic_user_dtos(
            team_id=team_id)
        user_ids = [
            basic_user_details_dto.user_id
            for basic_user_details_dto in basic_user_details_dtos
        ]
        user_role_dtos = self.user_storage.get_user_role_dtos_of_a_team(
            user_ids=user_ids, team_id=team_id
        )
        return basic_user_details_dtos, user_role_dtos
