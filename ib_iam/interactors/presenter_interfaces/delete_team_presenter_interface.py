from abc import ABC
from abc import abstractmethod


class DeleteTeamPresenterInterface(ABC):

    @abstractmethod
    def get_success_response_for_delete_team(self):
        pass

    @abstractmethod
    def get_user_has_no_access_response_for_delete_team(self):
        pass

    @abstractmethod
    def get_invalid_team_response_for_delete_team(self):
        pass
