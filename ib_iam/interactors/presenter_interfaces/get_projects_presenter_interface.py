import abc

from ib_iam.interactors.presenter_interfaces.dtos import ProjectWithTeamsDTO


class GetProjectsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_get_projects(
            self, project_with_teams_dto: ProjectWithTeamsDTO):
        pass
