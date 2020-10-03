from typing import List

from django.db import transaction

from ib_iam.interactors.dtos.dtos import PMAndSubUsersAuthTokensDTO


class RemovePMAndSubUsersDefaultTeam:

    @transaction.atomic()
    def remove_pm_and_sub_users_default_team(
            self, spread_sheet_name: str, sub_sheet_name: str, project_id: str
    ):
        from ib_iam.populate.spreedsheet_utils import SpreadSheetUtil
        spreadsheet_utils = SpreadSheetUtil()
        pm_and_sub_users = spreadsheet_utils \
            .read_spread_sheet_data_and_get_row_wise_dicts(
            spread_sheet_name=spread_sheet_name,
            sub_sheet_name=sub_sheet_name
        )
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        user_storage = UserStorageImplementation()
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        from ib_iam.storages.project_storage_implementation import \
            ProjectStorageImplementation
        project_storage = ProjectStorageImplementation()
        team_storage = TeamStorageImplementation()
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        team_member_level_storage = TeamMemberLevelStorageImplementation()
        pm_and_sub_user_auth_tokens = []
        for pm_and_sub_user in pm_and_sub_users:
            pm_and_sub_user_auth_tokens.extend([
                pm_and_sub_user['pm_auth_token'],
                pm_and_sub_user['user_auth_token']
            ])

        from ib_iam.interactors.users.add_pm_and_sub_users_interactor import \
            PMAndSubUsersInteractor
        interactor = PMAndSubUsersInteractor(
            project_storage=project_storage,
            user_storage=user_storage,
            team_storage=team_storage,
            team_member_level_storage=team_member_level_storage
        )
        interactor.remove_user_default_team(
            pm_and_sub_user_auth_tokens=pm_and_sub_user_auth_tokens
        )