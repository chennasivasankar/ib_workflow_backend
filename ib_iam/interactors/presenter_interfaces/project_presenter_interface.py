import abc
from typing import List

from ib_iam.interactors.storage_interfaces.dtos import ProjectWithDisplayIdDTO
from ib_iam.interactors.presenter_interfaces.dtos import \
    ProjectsWithTeamsAndRolesDTO


class GetProjectBriefInfoPresenterInterface(abc.ABC):

    # @abc.abstractmethod
    # def response_for_invalid_offset(self):
    #     pass
    #
    # @abc.abstractmethod
    # def response_for_invalid_limit(self):
    #     pass

    @abc.abstractmethod
    def response_for_user_does_not_exist(self):
        pass

    @abc.abstractmethod
    def success_response_for_get_project_brief_info(
            self, project_dtos: List[ProjectWithDisplayIdDTO]
    ):
        pass


class GetProjectsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_get_projects(
            self, project_with_teams_dto: ProjectsWithTeamsAndRolesDTO
    ):
        pass

    @abc.abstractmethod
    def response_for_user_have_not_permission_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_limit_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_offset_exception(self):
        pass


class UpdateProjectPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_success_response_for_update_project(self):
        pass

    @abc.abstractmethod
    def response_for_user_has_no_access_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_project_id_exception(self):
        pass

    @abc.abstractmethod
    def response_for_project_name_already_exists_exception(self):
        pass

    @abc.abstractmethod
    def response_for_duplicate_team_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_team_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_duplicate_role_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_role_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_duplicate_role_names_exception(self):
        pass

    @abc.abstractmethod
    def response_for_role_names_already_exists_exception(self, exception):
        pass


class AddProjectPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_success_response_for_add_project(self):
        pass

    @abc.abstractmethod
    def response_for_user_has_no_access_exception(self):
        pass

    @abc.abstractmethod
    def response_for_project_name_already_exists_exception(self):
        pass

    @abc.abstractmethod
    def response_for_project_display_id_already_exists_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_team_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_duplicate_team_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_duplicate_role_names_exception(self):
        pass

    @abc.abstractmethod
    def response_for_role_names_already_exists_exception(self, err):
        pass
