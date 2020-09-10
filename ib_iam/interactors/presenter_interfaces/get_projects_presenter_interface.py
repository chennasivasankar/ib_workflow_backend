import abc

from ib_iam.interactors.presenter_interfaces.dtos import \
    ProjectsWithTeamsAndRolesDTO


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
