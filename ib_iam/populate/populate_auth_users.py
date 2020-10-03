from typing import List

from django.db import transaction

from ib_iam.interactors.dtos.dtos import AuthUserDTO


class AuthUsers:

    @transaction.atomic
    def populate_auth_users(self, spread_sheet_name: str, sub_sheet_name: str,
                            project_id: str, role_ids: List[str],
                            is_assign_auth_token_users_to_team: bool):
        from ib_iam.populate.spreedsheet_utils import SpreadSheetUtil
        spreadsheet_utils = SpreadSheetUtil()
        auth_users = spreadsheet_utils \
            .read_spread_sheet_data_and_get_row_wise_dicts(
            spread_sheet_name=spread_sheet_name,
            sub_sheet_name=sub_sheet_name
        )
        auth_user_dtos = self._convert_auth_user_dtos(
            auth_users=auth_users
        )
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.storages.elastic_storage_implementation import \
            ElasticStorageImplementation
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        from ib_iam.interactors.auth_users_interactor import \
            AuthUsersInteractor
        from ib_iam.storages.project_storage_implementation import \
            ProjectStorageImplementation

        user_storage = UserStorageImplementation()
        elastic_storage = ElasticStorageImplementation()
        team_storage = TeamStorageImplementation()
        team_member_level_storage = TeamMemberLevelStorageImplementation()
        project_storage = ProjectStorageImplementation()

        interactor = AuthUsersInteractor(
            user_storage=user_storage,
            elastic_storage=elastic_storage,
            team_storage=team_storage,
            team_member_level_storage=team_member_level_storage,
            project_storage=project_storage
        )
        interactor.auth_user_dtos(
            auth_user_dtos=auth_user_dtos, project_id=project_id,
            role_ids=role_ids,
            is_assign_auth_token_users_to_team=is_assign_auth_token_users_to_team)
        return

    @staticmethod
    def _convert_auth_user_dtos(auth_users) -> List[AuthUserDTO]:
        auth_user_dtos = [
            AuthUserDTO(
                token=auth_user["auth_token"],
                email=auth_user["email"],
                name=auth_user["name"],
                auth_token_user_id=auth_user["user_id"]
            )
            for auth_user in auth_users
        ]
        return auth_user_dtos

    def test_user_interactor(self):
        test_data = [
            AuthUserDTO(token="tt2", name="tt2", auth_token_user_id="tt2",
                        email=""),
            AuthUserDTO(token="tt1", name="tt1", auth_token_user_id="tt1",
                        email=""),
            AuthUserDTO(token="tt3", name="tt3", auth_token_user_id="tt3",
                        email=""),
            AuthUserDTO(token="tt4", name="tt4", auth_token_user_id="tt4",
                        email=""),
            AuthUserDTO(token="tt5", name="tt5", auth_token_user_id="tt5",
                        email="")
        ]
        auth_user_dtos = test_data
        project_id = "FIN_MAN"
        role_ids = []
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.storages.elastic_storage_implementation import \
            ElasticStorageImplementation
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        from ib_iam.interactors.auth_users_interactor import \
            AuthUsersInteractor
        from ib_iam.storages.project_storage_implementation import \
            ProjectStorageImplementation

        user_storage = UserStorageImplementation()
        elastic_storage = ElasticStorageImplementation()
        team_storage = TeamStorageImplementation()
        team_member_level_storage = TeamMemberLevelStorageImplementation()
        project_storage = ProjectStorageImplementation()

        interactor = AuthUsersInteractor(
            user_storage=user_storage,
            elastic_storage=elastic_storage,
            team_storage=team_storage,
            team_member_level_storage=team_member_level_storage,
            project_storage=project_storage
        )
        interactor.auth_user_dtos(auth_user_dtos=auth_user_dtos,
                                  project_id=project_id, role_ids=role_ids)

    def test_pm_interactor(self):
        test_data = [
            AuthUserDTO(token="pt1", name="pt1", auth_token_user_id="pt1",
                        email=""),
            AuthUserDTO(token="pt2", name="pt2", auth_token_user_id="pt2",
                        email="")
        ]
        auth_user_dtos = test_data
        project_id = "FIN_MAN"
        role_ids = []
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        from ib_iam.storages.elastic_storage_implementation import \
            ElasticStorageImplementation
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        from ib_iam.interactors.auth_users_interactor import \
            AuthUsersInteractor
        from ib_iam.storages.project_storage_implementation import \
            ProjectStorageImplementation

        user_storage = UserStorageImplementation()
        elastic_storage = ElasticStorageImplementation()
        team_storage = TeamStorageImplementation()
        team_member_level_storage = TeamMemberLevelStorageImplementation()
        project_storage = ProjectStorageImplementation()

        interactor = AuthUsersInteractor(
            user_storage=user_storage,
            elastic_storage=elastic_storage,
            team_storage=team_storage,
            team_member_level_storage=team_member_level_storage,
            project_storage=project_storage
        )
        interactor.auth_user_dtos(auth_user_dtos=auth_user_dtos,
                                  project_id=project_id, role_ids=role_ids)
