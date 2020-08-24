class Project:

    def add_projects_to_database(
            self, spread_sheet_name: str, sub_sheet_name: str):
        from ib_iam.populate.spreedsheet_utils import SpreadSheetUtil
        spreadsheet_utils = SpreadSheetUtil()
        projects = spreadsheet_utils \
            .read_spread_sheet_data_and_get_row_wise_dicts(
            spread_sheet_name=spread_sheet_name,
            sub_sheet_name=sub_sheet_name
        )
        from ib_iam.storages.project_storage_implementation import \
            ProjectStorageImplementation
        project_storage = ProjectStorageImplementation()
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        user_storage = UserStorageImplementation()
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        team_storage = TeamStorageImplementation()
        from ib_iam.interactors.project_interactor import ProjectInteractor
        interactor = ProjectInteractor(
            project_storage=project_storage,
            user_storage=user_storage,
            team_storage=team_storage
        )
        project_dtos = self._convert_to_project_dtos(projects=projects)
        interactor.add_projects(project_dtos=project_dtos)

    @staticmethod
    def _convert_to_project_dtos(projects):
        from ib_iam.interactors.storage_interfaces.dtos import ProjectDTO
        project_dtos = [
            ProjectDTO(project_id=project['project_id'],
                       name=project['project_name'],
                       description=project.get('description', None),
                       logo_url=project.get('project_logo_url', None)
                       ) for project in projects
        ]
        return project_dtos
