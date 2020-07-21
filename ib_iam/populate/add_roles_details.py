class RollsDetails:

    @staticmethod
    def add_roles_details_to_database():
        from ib_iam.populate.spreedsheet_utils import SpreadSheetUtil
        spreedsheet_utils = SpreadSheetUtil()
        roles_details = spreedsheet_utils. \
            read_spread_sheet_data_and_get_row_wise_dicts(
            spread_sheet_name="roles", sub_sheet_name="Sheet1"
        )
        from ib_iam.storages.storage_implementation import StorageImplementation
        storage = StorageImplementation()
        from ib_iam.interactors.roles_interactor import RolesInteractor
        interactor = RolesInteractor(storage=storage)
        interactor.add_roles(roles=roles_details)
