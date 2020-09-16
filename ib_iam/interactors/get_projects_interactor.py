from typing import List

from ib_iam.exceptions.custom_exceptions import UserIsNotAdmin, \
    InvalidLimitValue, InvalidOffsetValue
from ib_iam.interactors.mixins.validation import ValidationMixin
from ib_iam.interactors.presenter_interfaces.dtos import \
    ProjectsWithTeamsAndRolesDTO
from ib_iam.interactors.presenter_interfaces \
    .get_projects_presenter_interface import GetProjectsPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import ProjectTeamIdsDTO, \
    PaginationDTO, ProjectWithDisplayIdDTO
from ib_iam.interactors.storage_interfaces.project_storage_interface import \
    ProjectStorageInterface
from ib_iam.interactors.storage_interfaces.team_storage_interface import \
    TeamStorageInterface
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class GetProjectsInteractor(ValidationMixin):

    def __init__(
            self, project_storage: ProjectStorageInterface,
            team_storage: TeamStorageInterface,
            user_storage: UserStorageInterface
    ):
        self.team_storage = team_storage
        self.project_storage = project_storage
        self.user_storage = user_storage

    def get_projects_wrapper(
            self, pagination_dto: PaginationDTO, user_id: str,
            presenter: GetProjectsPresenterInterface
    ):
        try:
            project_with_teams_dto = self.get_projects(
                pagination_dto=pagination_dto, user_id=user_id
            )
            response = presenter.get_response_for_get_projects(
                project_with_teams_dto=project_with_teams_dto
            )
        except UserIsNotAdmin:
            response = presenter.response_for_user_have_not_permission_exception()
        except InvalidLimitValue:
            response = presenter.response_for_invalid_limit_exception()
        except InvalidOffsetValue:
            response = presenter.response_for_invalid_offset_exception()
        return response

    def get_projects(
            self, pagination_dto: PaginationDTO, user_id: str
    ) -> ProjectsWithTeamsAndRolesDTO:
        self._validate_get_projects_details(
            pagination_dto=pagination_dto, user_id=user_id
        )
        projects_with_total_count = self.project_storage \
            .get_projects_with_total_count_dto(pagination_dto=pagination_dto)
        project_ids = self._get_project_ids_from_project_dtos(
            project_dtos=projects_with_total_count.projects
        )
        project_team_ids_dtos = self.project_storage.get_project_team_ids_dtos(
            project_ids=project_ids
        )
        team_ids = self._get_all_team_ids_ids_from_project_team_ids_dtos(
            project_team_ids_dtos=project_team_ids_dtos
        )
        team_dtos = self.team_storage.get_team_dtos(team_ids=team_ids)
        project_role_dtos = self.project_storage.get_all_project_roles()
        project_with_teams_dto = ProjectsWithTeamsAndRolesDTO(
            total_projects_count=projects_with_total_count.total_projects_count,
            project_dtos=projects_with_total_count.projects,
            project_team_ids_dtos=project_team_ids_dtos,
            team_dtos=team_dtos, project_role_dtos=project_role_dtos
        )
        return project_with_teams_dto

    def _validate_get_projects_details(
            self, pagination_dto: PaginationDTO, user_id: str
    ):
        self._validate_pagination_details(
            limit=pagination_dto.limit, offset=pagination_dto.offset
        )
        self._validate_is_user_admin(user_id=user_id)

    @staticmethod
    def _get_project_ids_from_project_dtos(
            project_dtos: List[ProjectWithDisplayIdDTO]
    ) -> List[str]:
        project_ids = [project_dto.project_id for project_dto in project_dtos]
        return project_ids

    @staticmethod
    def _get_all_team_ids_ids_from_project_team_ids_dtos(
            project_team_ids_dtos: List[ProjectTeamIdsDTO]
    ) -> List[str]:
        team_ids = []
        for project_team_ids_dto in project_team_ids_dtos:
            team_ids.extend(project_team_ids_dto.team_ids)
        unique_team_ids = list(set(team_ids))
        return unique_team_ids
