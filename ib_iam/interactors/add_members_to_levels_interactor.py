from typing import List

from ib_iam.interactors.dtos.dtos import TeamMemberLevelIdWithMemberIdsDTO
from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    AddMembersToLevelPresenterInterface
from ib_iam.interactors.storage_interfaces.level_storage_interface import \
    LevelStorageInterface


class AddMembersToLevelsInteractor:

    def __init__(self, level_storage: LevelStorageInterface):
        self.level_storage = level_storage

    def add_members_to_levels_wrapper(
            self, presenter: AddMembersToLevelPresenterInterface, team_id: str,
            team_member_level_id_with_member_ids_dtos: List[TeamMemberLevelIdWithMemberIdsDTO]
    ):
        '''
        validate team id
        validate level ids
        invalid member ids of team
        invalid member id
        '''
        response = self._add_members_to_levels_response(
            team_member_level_id_with_member_ids_dtos=team_member_level_id_with_member_ids_dtos,
            presenter=presenter, team_id=team_id
        )
        return response

    def _add_members_to_levels_response(
            self, presenter: AddMembersToLevelPresenterInterface,
            team_member_level_id_with_member_ids_dtos: List[TeamMemberLevelIdWithMemberIdsDTO],
            team_id: str
    ):
        self.add_members_to_levels(
            team_member_level_id_with_member_ids_dtos=team_member_level_id_with_member_ids_dtos,
            team_id=team_id
        )
        response = \
            presenter.prepare_success_response_for_add_members_to_levels()
        return response

    def add_members_to_levels(
            self, team_member_level_id_with_member_ids_dtos: List[TeamMemberLevelIdWithMemberIdsDTO],
            team_id: str
    ):
        self.level_storage.add_members_to_levels_for_a_team(
            team_member_level_id_with_member_ids_dtos=team_member_level_id_with_member_ids_dtos,
        )
        return
