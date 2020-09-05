from typing import List, Optional

from ib_iam.interactors.dtos.dtos import UserIdWithProjectIdAndStatusDTO
from ib_iam.interactors.storage_interfaces.dtos import (
    ProjectWithoutIdDTO, RoleNameAndDescriptionDTO, RoleDTO,
    ProjectWithDisplayIdDTO, ProjectsWithTotalCountDTO, PaginationDTO,
    ProjectTeamIdsDTO, ProjectRoleDTO, ProjectDTO)
from ib_iam.interactors.storage_interfaces.project_storage_interface import \
    ProjectStorageInterface
from ib_iam.models import Project, ProjectTeam, ProjectRole


class ProjectStorageImplementation(ProjectStorageInterface):

    def add_projects(self, project_dtos: List[ProjectWithDisplayIdDTO]):
        projects = [
            Project(project_id=project_dto.project_id,
                    display_id=project_dto.display_id,
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

    def get_projects_with_total_count_dto(
            self, pagination_dto: PaginationDTO) -> ProjectsWithTotalCountDTO:
        project_objects = Project.objects.all()
        total_projects_count = len(project_objects)
        offset = pagination_dto.offset
        project_objects = project_objects[offset:offset + pagination_dto.limit]
        project_dtos = [self._convert_to_project_with_display_id_dto(
            project_object=project_object)
            for project_object in project_objects]
        projects_with_total_count = ProjectsWithTotalCountDTO(
            projects=project_dtos,
            total_projects_count=total_projects_count)
        return projects_with_total_count

    def get_project_team_ids_dtos(
            self, project_ids: List[str]) -> List[ProjectTeamIdsDTO]:
        project_teams = ProjectTeam.objects.filter(
            project__project_id__in=project_ids
        ).values_list('project__project_id', 'team__team_id')
        from collections import defaultdict
        project_team_ids_dictionary = defaultdict(list)
        for project_team in project_teams:
            project_id = str(project_team[0])
            project_team_ids_dictionary[project_id].extend(
                [str(project_team[1])])
        project_teams_ids_dtos = [
            ProjectTeamIdsDTO(
                project_id=project_id,
                team_ids=project_team_ids_dictionary[project_id],
            ) for project_id in project_ids
        ]
        return project_teams_ids_dtos

    @staticmethod
    def _convert_to_project_with_display_id_dto(project_object):
        project_dto = ProjectWithDisplayIdDTO(
            project_id=project_object.project_id,
            display_id=project_object.display_id,
            name=project_object.name,
            description=project_object.description,
            logo_url=project_object.logo_url)
        return project_dto

    @staticmethod
    def _convert_to_project_dto(project_object):
        project_dto = ProjectDTO(project_id=project_object.project_id,
                                 name=project_object.name,
                                 description=project_object.description,
                                 logo_url=project_object.logo_url)
        return project_dto

    def get_project_dtos_for_given_project_ids(self, project_ids: List[str]):
        project_objects = Project.objects.filter(project_id__in=project_ids)
        project_dtos = [
            self._convert_to_project_dto(project_object=project_object)
            for project_object in project_objects]
        return project_dtos

    def is_team_exists_in_project(self, project_id: str, team_id: str) -> bool:
        try:
            ProjectTeam.objects.get(project_id=project_id, team_id=team_id)
        except ProjectTeam.DoesNotExist:
            return False
        return True

    def is_user_exists_in_team(self, team_id: str, user_id: str) -> bool:
        from ib_iam.models import TeamUser
        try:
            TeamUser.objects.get(team_id=team_id, user_id=user_id)
        except TeamUser.DoesNotExist:
            return False
        return True

    def get_team_name(self, team_id: str) -> str:
        from ib_iam.models import Team
        team_object = Team.objects.get(team_id=team_id)
        return team_object.name

    def is_user_exist_given_project(
            self, user_id: str, project_id: str) -> bool:
        return ProjectTeam.objects.filter(
            project__project_id=project_id,
            team__users__user_id=user_id
        ).exists()

    def get_user_role_ids(self, user_id: str, project_id: str):
        from ib_iam.models import UserRole
        role_ids = UserRole.objects.filter(
            user_id=user_id, project_role__project_id=project_id
        ).values_list("project_role__role_id", flat=True)
        return list(role_ids)

    def is_user_in_a_project(
            self, user_id: str, project_id: str) -> bool:
        team_ids = ProjectTeam.objects.filter(
            project_id=project_id
        ).values_list(
            "team_id", flat=True
        )
        from ib_iam.models import TeamUser
        user_team_objects = TeamUser.objects.filter(
            team_id__in=team_ids, user_id=user_id
        )
        return user_team_objects.exists()

    def is_valid_project_id(self, project_id: str) -> bool:
        project_objects = Project.objects.filter(project_id=project_id)
        return project_objects.exists()

    def get_valid_team_ids_for_given_project(
            self, project_id: str, team_ids: List[str]) -> List[str]:
        team_ids = list(ProjectTeam.objects.filter(
            project_id=project_id, team_id__in=team_ids
        ).values_list('team__team_id', flat=True))
        return list(map(str, team_ids))

    def get_valid_team_ids(self, project_id) -> List[str]:
        team_ids = list(ProjectTeam.objects.filter(
            project_id=project_id
        ).values_list('team__team_id', flat=True))
        return list(map(str, team_ids))

    def get_all_project_roles(self) -> List[ProjectRoleDTO]:
        project_role_objects = ProjectRole.objects.all()
        project_role_dtos = [self._get_project_role_dto(project_role_object)
                             for project_role_object in project_role_objects]
        return project_role_dtos

    @staticmethod
    def _get_project_role_dto(project_role_object):
        project_role_dto = ProjectRoleDTO(
            project_id=project_role_object.project_id,
            role_id=project_role_object.role_id,
            name=project_role_object.name,
            description=project_role_object.description)
        return project_role_dto

    def add_project(self, project_without_id_dto: ProjectWithoutIdDTO) -> str:
        project_object = Project.objects.create(
            name=project_without_id_dto.name,
            display_id=project_without_id_dto.display_id,
            description=project_without_id_dto.description,
            logo_url=project_without_id_dto.logo_url)
        return project_object.project_id

    def assign_teams_to_projects(self, project_id: str, team_ids: List[str]):
        project_teams = [ProjectTeam(project_id=project_id, team_id=team_id)
                         for team_id in team_ids]
        ProjectTeam.objects.bulk_create(project_teams)

    def add_project_roles(self, project_id: str,
                          roles: List[RoleNameAndDescriptionDTO]):
        project_roles = [ProjectRole(project_id=project_id,
                                     name=role.name,
                                     description=role.description)
                         for role in roles]
        ProjectRole.objects.bulk_create(project_roles)

    def update_project(self, project_dto: ProjectDTO):
        Project.objects.filter(project_id=project_dto.project_id) \
            .update(name=project_dto.name,
                    description=project_dto.description,
                    logo_url=project_dto.logo_url)

    def remove_teams_from_project(self, project_id: str, team_ids: List[str]):
        ProjectTeam.objects.filter(project_id=project_id,
                                   team_id__in=team_ids).delete()

    def get_project_role_ids(self, project_id: str) -> List[str]:
        project_role_ids = ProjectRole.objects.filter(project_id=project_id) \
            .values_list("role_id", flat=True)
        return list(project_role_ids)

    def update_project_roles(self, roles: List[RoleDTO]):
        # todo have to know whether there is any better way to update
        role_ids = [role_dto.role_id for role_dto in roles]
        role_objects = ProjectRole.objects.filter(role_id__in=role_ids)
        for role_object in role_objects:
            for role_dto in roles:
                if role_dto.role_id == role_object.role_id:
                    role_object.name = role_dto.name
                    role_object.description = role_dto.description
        ProjectRole.objects.bulk_update(role_objects, ["name", "description"])

    def delete_project_roles(self, role_ids: List[str]):
        ProjectRole.objects.filter(role_id__in=role_ids).delete()

    def get_project_id_if_project_name_already_exists(
            self, name: str) -> Optional[str]:
        try:
            project_object = Project.objects.get(name=name)
        except Project.DoesNotExist:
            return None
        return project_object.project_id

    def get_project_id_if_display_id_already_exists(
            self, display_id: str) -> Optional[str]:
        try:
            project_object = Project.objects.get(display_id=display_id)
        except Project.DoesNotExist:
            return None
        return project_object.project_id

    def get_user_status_for_given_projects(
            self, user_id: str, project_ids: List[str]
    ) -> List[UserIdWithProjectIdAndStatusDTO]:
        valid_project_ids = list(ProjectTeam.objects.filter(
            project_id__in=project_ids, team__users__user_id=user_id
        ).values_list('project_id', flat=True))
        return [
            UserIdWithProjectIdAndStatusDTO(
                user_id=user_id,
                project_id=project_id,
                is_exist=project_id in valid_project_ids
            ) for project_id in project_ids
        ]

    def get_valid_role_names_from_given_role_names(
            self, role_names: List[str]) -> List[str]:
        valid_role_names = ProjectRole.objects.filter(name__in=role_names) \
            .values_list("name", flat=True)
        return list(valid_role_names)
