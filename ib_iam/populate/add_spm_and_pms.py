class AddSpmAndPms:

    def add_spm_and_pms(
            self, spread_sheet_name: str, sub_sheet_name: str, project_id: str
    ):
        from ib_iam.populate.spreedsheet_utils import SpreadSheetUtil
        spreadsheet_utils = SpreadSheetUtil()
        spm_and_pm_users = spreadsheet_utils \
            .read_spread_sheet_data_and_get_row_wise_dicts(
            spread_sheet_name=spread_sheet_name,
            sub_sheet_name=sub_sheet_name
        )
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        user_storage = UserStorageImplementation()
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        team_storage = TeamStorageImplementation()
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        team_member_level_storage = TeamMemberLevelStorageImplementation()

        spm_and_pm_user_auth_id_dtos = self._convert_spm_and_pm_user_auth_id_dtos(
            spm_and_pm_users
        )

        from ib_iam.interactors.add_spm_and_pms_interactor import \
            AddSpmAndPmsInteractor
        interactor = AddSpmAndPmsInteractor(
            team_storage=team_storage,
            user_storage=user_storage,
            team_member_level_storage=team_member_level_storage
        )
        interactor.app_spm_and_pms(
            spm_and_pm_users_auth_token_dtos=spm_and_pm_user_auth_id_dtos,
            project_id=project_id
        )
        return

    @staticmethod
    def _convert_spm_and_pm_user_auth_id_dtos(spm_and_pm_users):
        from ib_iam.interactors.dtos.dtos import SpmAndPmUsersAuthTokensDTO
        spm_and_pm_users_dtos = [
            SpmAndPmUsersAuthTokensDTO(
                pm_auth_token_user_id=spm_and_pm_user['pm_user_id'],
                spm_auth_token_user_id=spm_and_pm_user["spm_user_id"]
            )
            for spm_and_pm_user in spm_and_pm_users
        ]
        return spm_and_pm_users_dtos
