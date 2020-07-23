class RollsDetails:

    @staticmethod
    def add_roles_details_to_database(spread_sheet_name, sub_sheet_name):
        from ib_iam.populate.spreedsheet_utils import SpreadSheetUtil
        spreedsheet_utils = SpreadSheetUtil()
        roles_details = spreedsheet_utils. \
            read_spread_sheet_data_and_get_row_wise_dicts(
            spread_sheet_name=spread_sheet_name, sub_sheet_name=sub_sheet_name
        )
        from ib_iam.storages.add_roles_storage_implementation import AddRolesStorageImplementation
        storage = AddRolesStorageImplementation()
        from ib_iam.interactors.roles_interactor import RolesInteractor
        interactor = RolesInteractor(storage=storage)
        interactor.add_roles(roles=roles_details)
