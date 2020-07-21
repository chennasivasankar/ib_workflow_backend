from abc import ABC
from abc import abstractmethod


class UpdateTeamPresenterInterface(ABC):

    @abstractmethod
    def get_success_response_for_update_team(self):
        pass

    @abstractmethod
    def get_user_has_no_access_response_for_update_team(self):
        pass

    @abstractmethod
    def get_invalid_team_response_for_update_team(self):
        pass

    @abstractmethod
    def get_team_name_already_exists_response_for_update_team(self, exception):
        pass

    @abstractmethod
    def get_duplicate_users_response_for_update_team(self):
        pass

    @abstractmethod
    def get_invalid_users_response_for_update_team(self):
        pass
