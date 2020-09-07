class ProjectRoleDetails:

    def add_project_roles_details_to_database(
            self, spread_sheet_name: str, sub_sheet_name: str):
        from ib_iam.populate.spreedsheet_utils import SpreadSheetUtil
        spreadsheet_utils = SpreadSheetUtil()
        roles_details = spreadsheet_utils. \
            read_spread_sheet_data_and_get_row_wise_dicts(
                spread_sheet_name=spread_sheet_name,
                sub_sheet_name=sub_sheet_name
            )
        from ib_iam.storages.roles_storage_implementation import \
            RolesStorageImplementation
        storage = RolesStorageImplementation()
        from ib_iam.interactors.roles_interactor import RolesInteractor
        interactor = RolesInteractor(storage=storage)
        project_id = roles_details[0]["project_id"]
        role_dtos = self._convert_to_role_dtos(roles_details=roles_details)
        interactor.add_project_roles(role_dtos=role_dtos, project_id=project_id)

    @staticmethod
    def _convert_to_role_dtos(roles_details):
        from ib_iam.interactors.storage_interfaces.dtos import RoleDTO
        role_dtos = [
            RoleDTO(
                role_id=role['role_id'],
                name=role['role_name'],
                description=role['description']
            )
            for role in roles_details
        ]
        return role_dtos
