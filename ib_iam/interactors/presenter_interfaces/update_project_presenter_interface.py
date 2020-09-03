import abc


class UpdateProjectPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_success_response_for_update_project(self):
        pass
