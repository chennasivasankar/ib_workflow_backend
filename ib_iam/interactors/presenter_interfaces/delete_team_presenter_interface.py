import abc



class DeleteTeamPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_success_response_for_delete_team(self):
        pass

    @abc.abstractmethod
    def get_user_has_no_access_response_for_delete_team(self):
        pass

    @abc.abstractmethod
    def get_invalid_team_response_for_delete_team(self):
        pass
