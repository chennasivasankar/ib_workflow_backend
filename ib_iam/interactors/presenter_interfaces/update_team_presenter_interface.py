import abc


class UpdateTeamPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_success_response_for_update_team(self):
        pass

    @abc.abstractmethod
    def response_for_user_has_no_access_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_team_id_exception(self):
        pass

    @abc.abstractmethod
    def response_for_team_name_already_exists_exception(self, err):
        pass

    @abc.abstractmethod
    def response_for_duplicate_user_ids_exception(self, err):
        pass

    @abc.abstractmethod
    def response_for_invalid_user_ids_exception(self, err):
        pass
