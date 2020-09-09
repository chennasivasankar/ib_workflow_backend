from typing import List

from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    GetTeamMemberLevelsPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import TeamMemberLevelDetailsDTO
from ib_iam.interactors.storage_interfaces.team_member_level_storage_interface import \
    TeamMemberLevelStorageInterface


class GetTeamMemberLevelsInteractor:

    def __init__(self,
                 team_member_level_storage: TeamMemberLevelStorageInterface):
        self.team_member_level_storage = team_member_level_storage

    def get_team_member_levels_wrapper(
            self, team_id: str,
            presenter: GetTeamMemberLevelsPresenterInterface):
        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        try:
            response = self._get_team_member_levels_response(
                team_id=team_id, presenter=presenter)
        except InvalidTeamId:
            response = presenter.response_for_invalid_team_id()
        return response

    def _get_team_member_levels_response(
            self, team_id: str,
            presenter: GetTeamMemberLevelsPresenterInterface):
        team_member_level_details_dtos = self.get_team_member_levels(
            team_id=team_id)
        response = presenter.response_for_team_member_level_details_dtos(
            team_member_level_details_dtos=team_member_level_details_dtos
        )
        return response

    def get_team_member_levels(self, team_id: str) \
            -> List[TeamMemberLevelDetailsDTO]:
        self.team_member_level_storage.validate_team_id(team_id=team_id)
        team_member_level_details_dtos = \
            self.team_member_level_storage.get_team_member_level_details_dtos(
                team_id=team_id
            )
        return team_member_level_details_dtos
