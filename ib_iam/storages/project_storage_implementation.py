from typing import List

from ib_iam.app_interfaces.dtos import UserIdWithTeamIDAndNameDTO
from ib_iam.interactors.storage_interfaces.dtos import ProjectDTO
from ib_iam.interactors.storage_interfaces.project_storage_interface import \
    ProjectStorageInterface
from ib_iam.models import Project, ProjectTeam, UserTeam


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

    def get_project_dtos(self) -> List[ProjectDTO]:
        project_objects = Project.objects.all()
        project_dtos = [
            self._convert_to_project_dto(project_object=project_object)
            for project_object in project_objects]
        return project_dtos

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
        from ib_iam.models import UserTeam
        try:
            UserTeam.objects.get(team_id=team_id, user_id=user_id)
        except UserTeam.DoesNotExist:
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
        from ib_iam.models import UserRole
        user_role_objects = UserRole.objects.filter(
            user_id=user_id, project_role__project_id=project_id
        )
        return user_role_objects.exists()

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

    def is_user_in_a_project(
            self, user_id: str, project_id: str) -> bool:
        from ib_iam.models import UserRole
        user_role_objects = UserRole.objects.filter(
            user_id=user_id, project_role__project_id=project_id
        )
        return user_role_objects.exists()

    def is_valid_project_id(self, project_id: str) -> bool:
        project_objects = Project.objects.filter(project_id=project_id)
        return project_objects.exists()
