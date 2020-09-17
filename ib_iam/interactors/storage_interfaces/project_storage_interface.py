import abc
from typing import List, Optional

from ib_iam.interactors.dtos.dtos import UserIdWithProjectIdAndStatusDTO
from ib_iam.interactors.storage_interfaces.dtos import (
    ProjectWithoutIdDTO, RoleNameAndDescriptionDTO, RoleDTO,
    ProjectWithDisplayIdDTO, UserIdAndTeamIdsDTO, ProjectTeamIdsDTO,
    ProjectsWithTotalCountDTO, PaginationDTO, ProjectRoleDTO, ProjectDTO
)


class ProjectStorageInterface(abc.ABC):

    @abc.abstractmethod
    def add_projects(self, project_dtos: List[ProjectWithDisplayIdDTO]):
        pass

    @abc.abstractmethod
    def get_valid_project_ids(
            self, project_ids: List[str]
    ) -> List[str]:
        pass

    @abc.abstractmethod
    def get_projects_with_total_count_dto(
            self, pagination_dto: PaginationDTO
    ) -> ProjectsWithTotalCountDTO:
        pass

    @abc.abstractmethod
    def get_project_team_ids_dtos(
            self, project_ids: List[str]
    ) -> List[ProjectTeamIdsDTO]:
        pass

    @abc.abstractmethod
    def is_team_exists_in_project(self, project_id: str, team_id: str) -> bool:
        pass

    @abc.abstractmethod
    def is_user_exists_in_team(self, team_id: str, user_id: str) -> bool:
        pass

    @abc.abstractmethod
    def get_team_name(self, team_id: str) -> str:
        pass

    @abc.abstractmethod
    def get_project_dtos(self, project_ids: List[str]) -> List[ProjectDTO]:
        pass

    @abc.abstractmethod
    def is_user_exist_given_project(
            self, user_id: str, project_id: str
    ) -> bool:
        pass

    @abc.abstractmethod
    def get_user_role_ids(self, user_id: str, project_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def get_all_project_roles(self) -> List[ProjectRoleDTO]:
        pass

    @abc.abstractmethod
    def add_project(self, project_without_id_dto: ProjectWithoutIdDTO) -> str:
        pass

    @abc.abstractmethod
    def assign_teams_to_projects(self, project_id: str, team_ids: List[str]):
        pass

    @abc.abstractmethod
    def add_project_roles(
            self, project_id: str,
            roles: List[RoleNameAndDescriptionDTO]
    ):
        pass

    @abc.abstractmethod
    def is_user_in_a_project(
            self, user_id: str, project_id: str
    ) -> bool:
        pass

    @abc.abstractmethod
    def is_valid_project_id(self, project_id: str) -> bool:
        pass

    @abc.abstractmethod
    def get_valid_team_ids(
            self, project_id: str, team_ids: List[str]
    ) -> List[str]:
        pass

    @abc.abstractmethod
    def get_team_ids(self, project_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def get_user_status_for_given_projects(
            self, user_id: str, project_ids: List[str]
    ) -> List[UserIdWithProjectIdAndStatusDTO]:
        pass

    @abc.abstractmethod
    def update_project(self, project_dto: ProjectDTO):
        pass

    @abc.abstractmethod
    def remove_teams(self, project_id: str, team_ids: List[str]):
        pass

    @abc.abstractmethod
    def get_project_role_ids(self, project_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def update_project_roles(self, roles: List[RoleDTO]):
        pass

    @abc.abstractmethod
    def delete_project_roles(self, role_ids: List[str]):
        pass

    @abc.abstractmethod
    def get_project_id(self, name: str) -> Optional[str]:
        pass

    @abc.abstractmethod
    def is_exists_display_id(self, display_id: str) -> Optional[str]:
        pass

    @abc.abstractmethod
    def get_valid_role_names(
            self, role_names: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_user_id_with_teams_ids_dtos(
            self, project_id: str
    ) -> List[UserIdAndTeamIdsDTO]:
        pass

    @abc.abstractmethod
    def remove_user_roles(
            self, project_id: str, user_ids: List[str]
    ):
        pass

    @abc.abstractmethod
    def get_user_project_dtos(self, user_id: str):
        pass
