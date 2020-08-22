from ib_iam.interactors.presenter_interfaces \
    .get_projects_presenter_interface import GetProjectsPresenterInterface
from ib_iam.interactors.storage_interfaces.project_storage_interface import \
    ProjectStorageInterface


class GetProjectsInteractor:

    def __init__(self, project_storage: ProjectStorageInterface):
        self.project_storage = project_storage

    def get_projects_wrapper(self,
                             presenter: GetProjectsPresenterInterface):
        project_dtos = self.get_projects()
        return presenter.get_response_for_get_projects(
            project_dtos=project_dtos)

    def get_projects(self):
        # todo check if there is any permissions or
        #  any different flow for user and admin
        return self.project_storage.get_project_dtos()
