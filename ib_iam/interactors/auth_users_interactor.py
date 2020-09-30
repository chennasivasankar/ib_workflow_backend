from typing import List

from ib_iam.interactors.dtos.dtos import AuthUserDTO, \
    TeamMemberLevelIdWithMemberIdsDTO
from ib_iam.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticSearchStorageInterface
from ib_iam.interactors.storage_interfaces.project_storage_interface import \
    ProjectStorageInterface
from ib_iam.interactors.storage_interfaces.team_member_level_storage_interface import \
    TeamMemberLevelStorageInterface
from ib_iam.interactors.storage_interfaces.team_storage_interface import \
    TeamStorageInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class AuthUsersInteractor:

    def __init__(
            self, user_storage: UserStorageInterface,
            elastic_storage: ElasticSearchStorageInterface,
            team_storage: TeamStorageInterface,
            team_member_level_storage: TeamMemberLevelStorageInterface,
            project_storage: ProjectStorageInterface
    ):
        self.user_storage = user_storage
        self.elastic_storage = elastic_storage
        self.team_storage = team_storage
        self.team_member_level_storage = team_member_level_storage
        self.project_storage = project_storage

    def auth_user_dtos(self, auth_user_dtos: List[AuthUserDTO],
                       project_id: str):
        user_ids = []
        for auth_user_dto in auth_user_dtos:
            try:
                user_id = self._create_auth_user_details(
                    auth_user_dto=auth_user_dto)
            except:
                continue
            user_ids.append(user_id)
        from ib_iam.constants.config import IS_ASSIGN_AUTH_TOKEN_USERS_TO_TEAM
        if IS_ASSIGN_AUTH_TOKEN_USERS_TO_TEAM:
            self.add_auth_users_to_team_and_team_member_levels(
                user_ids=user_ids, project_id=project_id)
        return

    def _create_auth_user_details(self, auth_user_dto: AuthUserDTO):
        from ib_iam.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_id = service_adapter.user_service.create_user_account_with_email(
            email=auth_user_dto.email, password=auth_user_dto.password
        )
        from ib_iam.adapters.dtos import UserProfileDTO
        user_profile_dto = UserProfileDTO(
            user_id=user_id, name=auth_user_dto.name,
            email=auth_user_dto.email
        )

        service_adapter.user_service.create_user_profile(
            user_id=user_id, user_profile_dto=user_profile_dto
        )
        self.user_storage.create_user(
            user_id=user_id, name=auth_user_dto.name, is_admin=False
        )
        self.user_storage.create_auth_user(
            user_id=user_id, token=auth_user_dto.token,
            auth_token_user_id=auth_user_dto.auth_token_user_id
        )
        self._create_elastic_user(
            user_id=user_id, name=auth_user_dto.name,
            email=auth_user_dto.email
        )
        return user_id

    def _create_elastic_user(self, user_id: str, name: str, email: str):
        elastic_user_id = self.elastic_storage.create_elastic_user(
            user_id=user_id, name=name, email=email
        )
        self.elastic_storage.create_elastic_user_intermediary(
            elastic_user_id=elastic_user_id, user_id=user_id
        )

    def add_auth_users_to_team_and_team_member_levels(
            self, user_ids: List[str], project_id: str
    ):
        from ib_iam.constants.config import \
            DEFAULT_CONFIGURATION_TEAM_NAME, LEVEL_0_HIERARCHY, LEVEL_0_NAME
        team_id, is_created = self.team_storage.get_or_create(
            name=DEFAULT_CONFIGURATION_TEAM_NAME
        )
        self.project_storage.assign_teams_to_projects(
            project_id=project_id, team_ids=[team_id]
        )
        self.team_storage.add_users_to_team(
            team_id=team_id, user_ids=user_ids
        )
        team_member_level_0 = self.team_member_level_storage \
            .get_or_create_team_member_level_hierarchy(
            team_id=team_id, level_hierarchy=LEVEL_0_HIERARCHY,
            level_name=LEVEL_0_NAME
        )
        team_member_level_id_with_member_ids_dtos = [
            TeamMemberLevelIdWithMemberIdsDTO(
                team_member_level_id=team_member_level_0,
                member_ids=user_ids
            )
        ]
        self.team_member_level_storage.add_members_to_levels_for_a_team(
            team_member_level_id_with_member_ids_dtos=
            team_member_level_id_with_member_ids_dtos,
        )
        return
