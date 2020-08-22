from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.interactors.presenter_interfaces \
    .get_projects_presenter_interface import GetProjectsPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import ProjectDTO


class GetProjectsPresenterImplementation(GetProjectsPresenterInterface,
                                         HTTPResponseMixin):

    def get_response_for_get_projects(self, project_dtos: List[ProjectDTO]):
        projects = [
            self._convert_to_project_dictionary(project_dto=project_dto)
            for project_dto in project_dtos]
        return self.prepare_200_success_response(response_dict=projects)

    @staticmethod
    def _convert_to_project_dictionary(project_dto: ProjectDTO):
        project_dictionary = {"project_id": project_dto.project_id,
                              "name": project_dto.name,
                              "description": project_dto.description,
                              "logo_url": project_dto.logo_url}
        return project_dictionary
