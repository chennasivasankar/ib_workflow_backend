import abc


class AddProjectPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_success_response_for_add_project(self):
        pass

    @abc.abstractmethod
    def get_project_name_already_exists_response(self):
        pass

    @abc.abstractmethod
    def get_project_display_id_already_exists_response(self):
        pass

    @abc.abstractmethod
    def get_invalid_team_ids_response(self, exception):
        pass

    @abc.abstractmethod
    def get_duplicate_team_ids_response(self):
        pass
