from typing import List

from ib_iam.interactors.storage_interfaces.dtos import ProjectDTO
from ib_iam.interactors.storage_interfaces.project_storage_interface import \
    ProjectStorageInterface
from ib_iam.models import Project


class ProjectStorageImplementation(ProjectStorageInterface):

    def add_projects(self, project_dtos: List[ProjectDTO]):
        projects = [
            Project(project_id=project_dto.project_id,
                    name=project_dto.name,
                    description=project_dto.description,
                    logo_url=project_dto.logo_url)
            for project_dto in project_dtos
        ]
        Project.objects.bulk_create(projects)

    def get_valid_project_ids_from_given_project_ids(
            self, project_ids: List[str]) -> List[str]:
        project_ids = Project.objects.filter(project_id__in=project_ids) \
            .values_list("project_id", flat=True)
        return list(project_ids)
