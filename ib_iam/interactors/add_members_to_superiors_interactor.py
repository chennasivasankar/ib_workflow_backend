from typing import List

from ib_iam.interactors.dtos.dtos import ImmediateSuperiorUserIdWithUserIdsDTO
from ib_iam.interactors.presenter_interfaces.level_presenter_interface import \
    AddMembersToSuperiorsPresenterInterface
from ib_iam.interactors.storage_interfaces.level_storage_interface import \
    TeamMemberLevelStorageInterface


class AddMembersToSuperiorsInteractor:

    def __init__(self,
                 team_member_level_storage: TeamMemberLevelStorageInterface):
        self.team_member_level_storage = team_member_level_storage

    def add_members_to_superiors_wrapper(
            self, team_id: str, level_hierarchy: int,
            presenter: AddMembersToSuperiorsPresenterInterface,
            immediate_superior_user_id_with_member_ids_dtos: List[
                ImmediateSuperiorUserIdWithUserIdsDTO]
    ):
        response = self._add_members_to_superiors_response(
            team_id=team_id, level_hierarchy=level_hierarchy,
            presenter=presenter,
            immediate_superior_user_id_with_member_ids_dtos=immediate_superior_user_id_with_member_ids_dtos
        )
        return response

    def _add_members_to_superiors_response(
            self, team_id: str, level_hierarchy: int,
            presenter: AddMembersToSuperiorsPresenterInterface,
            immediate_superior_user_id_with_member_ids_dtos: List[
                ImmediateSuperiorUserIdWithUserIdsDTO]
    ):
        self.add_members_to_superiors(
            team_id=team_id, level_hierarchy=level_hierarchy,
            immediate_superior_user_id_with_member_ids_dtos=immediate_superior_user_id_with_member_ids_dtos
        )
        response = \
            presenter.prepare_success_response_for_add_members_superiors()
        return response

    def add_members_to_superiors(
            self, team_id: str, level_hierarchy: int,
            immediate_superior_user_id_with_member_ids_dtos: List[
                ImmediateSuperiorUserIdWithUserIdsDTO]
    ):
        self.team_member_level_storage.add_members_to_superiors(
            team_id=team_id, level_hierarchy=level_hierarchy,
            immediate_superior_user_id_with_member_ids_dtos=immediate_superior_user_id_with_member_ids_dtos
        )
        return
