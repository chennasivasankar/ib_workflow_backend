import abc


class DeleteTeamPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_success_response_for_delete_team(self):
        pass

    @abc.abstractmethod
    def response_for_user_has_no_access_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_team_id_exception(self):
        pass
