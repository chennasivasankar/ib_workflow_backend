from typing import List

from ib_iam.interactors.presenter_interfaces \
    .get_projects_presenter_interface import GetProjectsPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import ProjectDTO, \
    ProjectTeamIdsDTO, PaginationDTO
from ib_iam.interactors.storage_interfaces.project_storage_interface import \
    ProjectStorageInterface
from ib_iam.interactors.storage_interfaces.team_storage_interface import \
    TeamStorageInterface


class GetProjectsInteractor:

    def __init__(self, project_storage: ProjectStorageInterface,
                 team_storage: TeamStorageInterface):
        self.team_storage = team_storage
        self.project_storage = project_storage

    def get_projects_wrapper(self, pagination_dto: PaginationDTO,
                             presenter: GetProjectsPresenterInterface):
        project_with_teams_dto = self.get_projects(
            pagination_dto=pagination_dto)
        return presenter.get_response_for_get_projects(
            project_with_teams_dto=project_with_teams_dto)

    def get_projects(self, pagination_dto: PaginationDTO):
        # todo check if there is any permissions or
        #  any different flow for user and admin
        # todo : validate pagination details
        # self._validate_pagination_details(
        #    limit=pagination_dto.limit, offset=pagination_dto.offset)
        projects_with_total_count = self.project_storage \
            .get_projects_with_total_count_dto(pagination_dto=pagination_dto)
        project_ids = self._get_project_ids_from_project_dtos(
            project_dtos=projects_with_total_count.projects)
        project_team_ids_dtos = self.project_storage.get_project_team_ids_dtos(
            project_ids=project_ids)
        team_ids = self._get_all_team_ids_ids_from_project_team_ids_dtos(
            project_team_ids_dtos=project_team_ids_dtos)
        team_dtos = self.team_storage.get_team_dtos(team_ids=team_ids)
        from ib_iam.interactors.presenter_interfaces.dtos import \
            ProjectWithTeamsDTO
        project_with_teams_dto = ProjectWithTeamsDTO(
            total_projects_count=projects_with_total_count.total_projects_count,
            project_dtos=projects_with_total_count.projects,
            project_team_ids_dtos=project_team_ids_dtos,
            team_dtos=team_dtos)
        return project_with_teams_dto

    @staticmethod
    def _get_project_ids_from_project_dtos(
            project_dtos: List[ProjectDTO]) -> List[str]:
        project_ids = [project_dto.project_id for project_dto in project_dtos]
        return project_ids

    @staticmethod
    def _get_all_team_ids_ids_from_project_team_ids_dtos(
            project_team_ids_dtos: List[ProjectTeamIdsDTO]) -> List[str]:
        team_ids = []
        for project_team_ids_dto in project_team_ids_dtos:
            team_ids.extend(project_team_ids_dto.team_ids)
        unique_team_ids = list(set(team_ids))
        unique_team_ids.sort()
        return unique_team_ids
