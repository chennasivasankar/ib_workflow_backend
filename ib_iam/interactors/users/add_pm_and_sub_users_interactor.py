from collections import defaultdict
from typing import List

from ib_iam.constants.config import LEVEL_0_HIERARCHY, LEVEL_0_NAME, \
    LEVEL_1_HIERARCHY, LEVEL_1_NAME
from ib_iam.interactors.dtos.dtos import PMAndSubUsersAuthTokensDTO, \
    TeamMemberLevelIdWithMemberIdsDTO, ImmediateSuperiorUserIdWithUserIdsDTO, \
    PMAndSubUsersAuthIdsDTO
from ib_iam.interactors.storage_interfaces.dtos import UserIdWithTokenDTO, \
    UserIdAndAuthUserIdDTO
from ib_iam.interactors.storage_interfaces.project_storage_interface import \
    ProjectStorageInterface
from ib_iam.interactors.storage_interfaces \
    .team_member_level_storage_interface import TeamMemberLevelStorageInterface
from ib_iam.interactors.storage_interfaces.team_storage_interface import \
    TeamStorageInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class PMAndSubUsersInteractor:

    def __init__(
            self,
            team_storage: TeamStorageInterface,
            project_storage: ProjectStorageInterface,
            user_storage: UserStorageInterface,
            team_member_level_storage: TeamMemberLevelStorageInterface
    ):
        self.project_storage = project_storage
        self.team_storage = team_storage
        self.team_member_level_storage = team_member_level_storage
        self.user_storage = user_storage

    def add_pm_and_sub_users(
            self, pm_and_sub_user_auth_ids_dtos: List[PMAndSubUsersAuthIdsDTO],
            project_id: str
    ):
        auth_user_ids = self._get_all_auth_user_ids(
            pm_and_sub_user_auth_ids_dtos=pm_and_sub_user_auth_ids_dtos
        )
        user_id_with_auth_user_id_dtos = self.user_storage \
            .get_user_id_and_auth_user_id(auth_user_ids=auth_user_ids)
        pm_id_and_sub_user_ids_dictionary = self.get_pm_and_sub_users(
            user_id_with_auth_user_id_dtos=user_id_with_auth_user_id_dtos,
            pm_and_sub_user_auth_ids_dtos=pm_and_sub_user_auth_ids_dtos
        )

        for pm_id, user_ids in pm_id_and_sub_user_ids_dictionary.items():
            team_id, is_created = self.team_storage.get_or_create(
                name="team_name_{pm_id}".format(pm_id=pm_id)
            )
            self.team_storage.add_users_to_team(
                team_id=team_id, user_ids=user_ids + [pm_id]
            )
            if is_created:
                self.project_storage.assign_teams_to_projects(
                    project_id=project_id, team_ids=[team_id]
                )
            self.add_pm_and_sub_users_to_levels_for_a_team(
                pm_id=pm_id, sub_user_ids=user_ids, team_id=team_id
            )
            self.add_pm_and_sub_users_as_superior_and_members(
                pm_id=pm_id, sub_user_ids=user_ids, team_id=team_id
            )

    @staticmethod
    def _get_all_auth_user_ids(
            pm_and_sub_user_auth_ids_dtos: List[PMAndSubUsersAuthIdsDTO]
    ):
        auth_user_ids = []
        for pm_and_sub_user_auth_ids_dto in pm_and_sub_user_auth_ids_dtos:
            auth_user_ids.extend(
                [pm_and_sub_user_auth_ids_dto.pm_auth_user_id,
                 pm_and_sub_user_auth_ids_dto.sub_user_auth_user_id]
            )
        auth_user_ids = list(set(auth_user_ids))
        return auth_user_ids

    def add_pm_and_sub_users_as_superior_and_members(
            self, pm_id: str, sub_user_ids: List[str], team_id: str
    ):
        member_level_hierarchy = 0
        immediate_superior_user_id_with_member_ids_dtos = [
            ImmediateSuperiorUserIdWithUserIdsDTO(
                immediate_superior_user_id=pm_id,
                member_ids=sub_user_ids
            )
        ]
        self.team_member_level_storage.add_members_to_superiors(
            team_id=team_id, member_level_hierarchy=member_level_hierarchy,
            immediate_superior_user_id_with_member_ids_dtos=
            immediate_superior_user_id_with_member_ids_dtos
        )

    def add_pm_and_sub_users_to_levels_for_a_team(
            self, pm_id: str, sub_user_ids: List[str],
            team_id: str
    ):
        team_member_level_0 = self.team_member_level_storage \
            .get_or_create_team_member_level_hierarchy(
            team_id=team_id, level_hierarchy=LEVEL_0_HIERARCHY,
            level_name=LEVEL_0_NAME
        )
        team_member_level_1 = self.team_member_level_storage \
            .get_or_create_team_member_level_hierarchy(
            team_id=team_id, level_hierarchy=LEVEL_1_HIERARCHY,
            level_name=LEVEL_1_NAME
        )
        team_member_level_id_with_member_ids_dtos = [
            TeamMemberLevelIdWithMemberIdsDTO(
                team_member_level_id=team_member_level_0,
                member_ids=[pm_id]
            ),
            TeamMemberLevelIdWithMemberIdsDTO(
                team_member_level_id=team_member_level_1,
                member_ids=sub_user_ids
            )
        ]
        self.team_member_level_storage.add_members_to_levels_for_a_team(
            team_member_level_id_with_member_ids_dtos=
            team_member_level_id_with_member_ids_dtos,
        )

    @staticmethod
    def get_pm_and_sub_users(
            user_id_with_auth_user_id_dtos: List[UserIdAndAuthUserIdDTO],
            pm_and_sub_user_auth_ids_dtos: List[PMAndSubUsersAuthIdsDTO]
    ):
        user_auth_id_and_user_id_dictionary = {}
        for user_id_with_auth_user_id_dto in user_id_with_auth_user_id_dtos:
            user_auth_id_and_user_id_dictionary[
                user_id_with_auth_user_id_dto.auth_user_id
            ] = user_id_with_auth_user_id_dto.user_id

        pm_id_and_sub_user_ids_dictionary = defaultdict(list)
        for pm_and_sub_user_auth_ids_dto in pm_and_sub_user_auth_ids_dtos:
            pm_id_and_sub_user_ids_dictionary[
                user_auth_id_and_user_id_dictionary[
                    pm_and_sub_user_auth_ids_dto.pm_auth_user_id]
            ].append(
                user_auth_id_and_user_id_dictionary[
                    pm_and_sub_user_auth_ids_dto.sub_user_auth_user_id
                ]
            )
        return pm_id_and_sub_user_ids_dictionary
