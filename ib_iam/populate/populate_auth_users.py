from typing import List

from django.db import transaction

from ib_iam.interactors.dtos.dtos import AuthUserDTO


class AuthUsers:

    def populate_auth_users(self, spread_sheet_name: str, sub_sheet_name: str,
                            project_id: str, role_ids: List[str]):
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
        from ib_iam.interactors.auth_users_interactor import AuthUsersInteractor
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
                                  project_id=project_id, role_ids=role_ids
                                  )
        return

    @staticmethod
    def _convert_auth_user_dtos(auth_users) -> List[AuthUserDTO]:
        auth_user_dtos = [
            AuthUserDTO(
                token=auth_user["auth_token"],
                email=auth_user["email"],
                name=auth_user["name"],
                auth_token_user_id=auth_user["auth_token_user_id"]
            )
            for auth_user in auth_users
        ]
        return auth_user_dtos
