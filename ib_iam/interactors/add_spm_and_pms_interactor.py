from typing import List

from ib_iam.interactors.dtos.dtos import SpmAndPmUsersAuthTokensDTO, \
    ImmediateSuperiorUserIdWithUserIdsDTO
from ib_iam.interactors.storage_interfaces.dtos import UserIdWithTokenDTO
from ib_iam.interactors.storage_interfaces.team_member_level_storage_interface import \
    TeamMemberLevelStorageInterface
from ib_iam.interactors.storage_interfaces.team_storage_interface import \
    TeamStorageInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class AddSpmAndPmsInteractor:

    def __init__(
            self,
            team_storage: TeamStorageInterface,
            team_member_level_storage: TeamMemberLevelStorageInterface,
            user_storage: UserStorageInterface
    ):
        self.team_storage = team_storage
        self.team_member_level_storage = team_member_level_storage
        self.user_storage = user_storage

    def app_spm_and_pms(
            self,
            spm_and_pm_users_auth_token_dtos: List[SpmAndPmUsersAuthTokensDTO],
            project_id: str
    ):
        user_tokens = self._get_all_user_tokens(
            spm_and_pm_users_auth_token_dtos=spm_and_pm_users_auth_token_dtos
        )
        user_id_with_token_dtos = self.user_storage.get_user_and_token_dtos(
            tokens=user_tokens
        )

        spm_id_and_pm_id_dict = self._get_spm_id_and_pm_id_dict(
            user_id_with_token_dtos=user_id_with_token_dtos,
            spm_and_pm_users_auth_token_dtos=spm_and_pm_users_auth_token_dtos
        )
        user_id_with_team_id_dtos = self.team_storage.get_user_with_team_dtos(
            user_ids=list(spm_id_and_pm_id_dict.keys())
        )
        user_id_with_team_id_dict = {
            user_id_with_team_id_dto.user_id: user_id_with_team_id_dto.team_id
            for user_id_with_team_id_dto in user_id_with_team_id_dtos
        }

        for spm_user_id, pm_user_id in spm_id_and_pm_id_dict.items():
            team_id = user_id_with_team_id_dict[pm_user_id]
            self._add_user_to_team(team_id=team_id, user_id=spm_user_id)
            self._add_spm_to_pm_as_superior(
                pm_user_id=pm_user_id, spm_user_id=spm_user_id,
                team_id=team_id
            )

    @staticmethod
    def _get_all_user_tokens(
            spm_and_pm_users_auth_token_dtos: List[SpmAndPmUsersAuthTokensDTO]
    ):
        user_tokens = []
        for spm_and_pm_users_auth_token_dto in spm_and_pm_users_auth_token_dtos:
            user_tokens.extend(
                [spm_and_pm_users_auth_token_dto.pm_auth_token,
                 spm_and_pm_users_auth_token_dto.spm_auth_token]
            )
        user_tokens = list(set(user_tokens))
        return user_tokens

    @staticmethod
    def _get_spm_id_and_pm_id_dict(
            user_id_with_token_dtos: List[UserIdWithTokenDTO],
            spm_and_pm_users_auth_token_dtos: List[SpmAndPmUsersAuthTokensDTO]
    ):
        token_with_user_id_dict = {
            user_id_with_token_dto.token: user_id_with_token_dto.user_id
            for user_id_with_token_dto in user_id_with_token_dtos
        }

        spm_id_and_pm_id_dict = {
            token_with_user_id_dict[
                spm_and_pm_users_auth_token_dto.spm_auth_token]:
                token_with_user_id_dict[
                    spm_and_pm_users_auth_token_dto.pm_auth_token]
            for spm_and_pm_users_auth_token_dto in
            spm_and_pm_users_auth_token_dtos
        }

        return spm_id_and_pm_id_dict

    def _add_user_to_team(self, team_id: str, user_id: str):
        from ib_iam.constants.config import LEVEL_2_HIERARCHY, LEVEL_2_NAME
        team_member_level_two_id = self.team_member_level_storage \
            .get_or_create_team_member_level_hierarchy(
            team_id=team_id, level_hierarchy=LEVEL_2_HIERARCHY,
            level_name=LEVEL_2_NAME
        )
        self.team_storage.add_user_to_team(
            user_id=user_id, team_id=team_id,
            team_member_level_id=team_member_level_two_id
        )

    def _add_spm_to_pm_as_superior(
            self, pm_user_id: str, spm_user_id: str, team_id: str):
        member_level_hierarchy = 0
        immediate_superior_user_id_with_member_ids_dtos = [
            ImmediateSuperiorUserIdWithUserIdsDTO(
                immediate_superior_user_id=spm_user_id,
                member_ids=[pm_user_id]
            )
        ]
        self.team_member_level_storage.add_members_to_superiors(
            team_id=team_id, member_level_hierarchy=member_level_hierarchy,
            immediate_superior_user_id_with_member_ids_dtos=
            immediate_superior_user_id_with_member_ids_dtos
        )
        return
