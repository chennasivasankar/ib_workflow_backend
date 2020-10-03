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
                       project_id: str, role_ids: List[str],
                       is_assign_auth_token_users_to_team: bool):
        user_ids = []
        # role_ids = self.project_storage.get_project_role_ids(
        #     project_id=project_id
        # )
        for auth_user_dto in auth_user_dtos:
            try:
                user_id = self._create_auth_user_details(
                    auth_user_dto=auth_user_dto, role_ids=role_ids
                )
            except:
                continue
            user_ids.append(user_id)
        if is_assign_auth_token_users_to_team:
            self.add_auth_users_to_team_and_team_member_levels(
                user_ids=user_ids, project_id=project_id)
        return

    def _create_auth_user_details(
            self, auth_user_dto: AuthUserDTO, role_ids: List[str]
    ):
        from ib_iam.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        is_auth_token_empty = not auth_user_dto.token
        if is_auth_token_empty:
            auth_user_dto.token = self._generate_uuid4()
        is_auth_token_user_id_empty = not auth_user_dto.auth_token_user_id
        if is_auth_token_user_id_empty:
            auth_user_dto.auth_token_user_id = self._generate_uuid4()
        is_country_code_empty = not auth_user_dto.country_code
        if is_country_code_empty:
            auth_user_dto.country_code = "91"
        is_phone_number_empty = not auth_user_dto.phone_number
        if is_phone_number_empty:
            auth_user_dto.phone_number = None
            auth_user_dto.country_code = None

        is_email_empty = not auth_user_dto.email
        if is_email_empty:
            auth_user_dto.email = auth_user_dto.token + "@gmail.com"
        from ib_iam.constants.config import DEFAULT_PASSWORD
        user_id = service_adapter.user_service.create_user_account_with_email(
            email=auth_user_dto.email, password=DEFAULT_PASSWORD
        )
        from ib_iam.adapters.dtos import UserProfileDTO
        user_profile_dto = UserProfileDTO(
            user_id=user_id, name=auth_user_dto.name,
            email=auth_user_dto.email, country_code=auth_user_dto.country_code,
            phone_number=auth_user_dto.phone_number
        )

        service_adapter.user_service.create_user_profile(
            user_id=user_id, user_profile_dto=user_profile_dto
        )
        self.user_storage.create_user(
            user_id=user_id, name=auth_user_dto.name, is_admin=False
        )
        self.user_storage.create_auth_user(
            user_id=user_id, token=auth_user_dto.token,
            auth_token_user_id=auth_user_dto.auth_token_user_id,
            invitation_code=auth_user_dto.invitation_code
        )
        self._create_elastic_user(
            user_id=user_id, name=auth_user_dto.name,
            email=auth_user_dto.email
        )
        self.user_storage.add_roles_to_the_user(
            user_id=user_id, role_ids=role_ids
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
        team_id, is_created = self.team_storage.get_or_create_team_with_name(
            name=DEFAULT_CONFIGURATION_TEAM_NAME
        )
        if is_created:
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

    @staticmethod
    def _generate_uuid4():
        import uuid
        return str(uuid.uuid4())
