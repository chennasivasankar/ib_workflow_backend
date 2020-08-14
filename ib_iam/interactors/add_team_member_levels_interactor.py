from typing import List

from ib_iam.interactors.dtos.dtos import TeamMemberLevelDTO
from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    AddTeamMemberLevelsPresenterInterface
from ib_iam.interactors.storage_interfaces.level_storage_interface import \
    TeamMemberLevelStorageInterface


class AddTeamMemberLevelsInteractor:

    def __init__(self, level_storage: TeamMemberLevelStorageInterface):
        self.level_storage = level_storage

    def add_team_member_levels_wrapper(
            self, team_id: str, team_member_level_dtos: List[TeamMemberLevelDTO],
            presenter: AddTeamMemberLevelsPresenterInterface
    ):
        '''
        TODO:
        Invalid TeamID
        InvalidOrder -- negative
        unique level order
        unique level names
        '''
        response = self._add_team_member_levels_response(
            team_id=team_id,
            team_member_level_dtos=team_member_level_dtos,
            presenter=presenter
        )
        return response

    def _add_team_member_levels_response(
            self, team_id: str, team_member_level_dtos: List[TeamMemberLevelDTO],
            presenter: AddTeamMemberLevelsPresenterInterface
    ):
        self.add_team_member_levels(team_id=team_id, team_member_level_dtos=team_member_level_dtos)
        response = presenter. \
            prepare_success_response_for_add_team_member_levels_to_team()
        return response

    def add_team_member_levels(
            self, team_id: str,
            team_member_level_dtos: List[TeamMemberLevelDTO]
    ):
        self.level_storage.add_team_member_levels(
            team_id=team_id, team_member_level_dtos=team_member_level_dtos
        )
        return
