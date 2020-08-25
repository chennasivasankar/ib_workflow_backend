import abc


class AddProjectPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_success_response_for_add_project(self, project_id: str):
        pass
