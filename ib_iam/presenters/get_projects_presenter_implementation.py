from typing import List

from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_iam.interactors.presenter_interfaces.dtos import ProjectWithTeamsDTO
from ib_iam.interactors.presenter_interfaces \
    .get_projects_presenter_interface import GetProjectsPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import ProjectDTO, \
    ProjectTeamIdsDTO, ProjectRoleDTO


class GetProjectsPresenterImplementation(GetProjectsPresenterInterface,
                                         HTTPResponseMixin):

    def get_response_for_get_projects(
            self, project_with_teams_dto: ProjectWithTeamsDTO):
        projects = self._convert_project_with_teams_dto_to_projects_list(
            project_with_teams_dto=project_with_teams_dto)
        response_dict = {"total_projects_count":
                             project_with_teams_dto.total_projects_count,
                         "projects": projects}
        return self.prepare_200_success_response(response_dict=response_dict)

    def _convert_project_with_teams_dto_to_projects_list(
            self, project_with_teams_dto: ProjectWithTeamsDTO):
        project_dtos = project_with_teams_dto.project_dtos
        project_team_ids_dtos = project_with_teams_dto.project_team_ids_dtos
        team_dtos = project_with_teams_dto.team_dtos
        project_role_dtos = project_with_teams_dto.project_role_dtos
        teams_dictionary = self._get_teams_dictionary(team_dtos=team_dtos)
        project_team_ids_dict = \
            self._get_project_teams_dict_from_project_team_ids_dtos(
                project_team_ids_dtos=project_team_ids_dtos)
        projects = [
            self._convert_to_project_details_dictionary(
                project_team_ids_dict=project_team_ids_dict,
                teams_dictionary=teams_dictionary,
                project_dto=project_dto,
                project_role_dtos=project_role_dtos
            ) for project_dto in project_dtos
        ]
        return projects

    @staticmethod
    def _get_project_teams_dict_from_project_team_ids_dtos(
            project_team_ids_dtos: List[ProjectTeamIdsDTO]):
        from collections import defaultdict
        project_team_ids_dict = defaultdict(list)
        for project_team_ids_dto in project_team_ids_dtos:
            project_team_ids_dict[project_team_ids_dto.project_id] = \
                project_team_ids_dto.team_ids
        return project_team_ids_dict

    def _convert_to_project_details_dictionary(
            self,
            project_team_ids_dict, teams_dictionary, project_dto: ProjectDTO,
            project_role_dtos: List[ProjectRoleDTO]):
        project_teams = self._get_teams(
            team_ids=project_team_ids_dict[project_dto.project_id],
            teams_dictionary=teams_dictionary)
        project_roles = self._get_project_roles_dictionary(
            project_id=project_dto.project_id,
            project_role_dtos=project_role_dtos)
        project_dictionary = self._convert_to_project_dictionary(
            project_dto=project_dto)
        project_dictionary["teams"] = project_teams
        project_dictionary["roles"] = project_roles
        return project_dictionary

    @staticmethod
    def _get_teams(team_ids: List[str], teams_dictionary):
        teams = [teams_dictionary[team_id] for team_id in team_ids]
        return teams

    @staticmethod
    def _get_teams_dictionary(team_dtos):
        from collections import defaultdict
        teams_dictionary = defaultdict()
        for team_dto in team_dtos:
            teams_dictionary[team_dto.team_id] = {"team_id": team_dto.team_id,
                                                  "team_name": team_dto.name}
        return teams_dictionary

    @staticmethod
    def _convert_to_project_dictionary(project_dto: ProjectDTO):
        project_dictionary = {"project_id": project_dto.project_id,
                              "name": project_dto.name,
                              "description": project_dto.description,
                              "logo_url": project_dto.logo_url}
        return project_dictionary

    def _get_project_roles_dictionary(self, project_id: str,
                                      project_role_dtos: List[ProjectRoleDTO]):
        project_roles = [
            self._convert_to_project_role_dictionary(project_role_dto)
            for project_role_dto in project_role_dtos
            if project_role_dto.project_id == project_id
        ]
        return project_roles

    @staticmethod
    def _convert_to_project_role_dictionary(project_role_dto: ProjectRoleDTO):
        project_role_dictionary = {"role_id": project_role_dto.role_id,
                                   "role_name": project_role_dto.name,
                                   "description": project_role_dto.description}
        return project_role_dictionary
