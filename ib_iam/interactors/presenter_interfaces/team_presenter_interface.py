from abc import ABC
from abc import abstractmethod

from ib_iam.interactors.presenter_interfaces.dtos import (
    TeamWithMembersDetailsDTO
)


class TeamPresenterInterface(ABC):

    @abstractmethod
    def get_user_has_no_access_response_for_get_list_of_teams(self):
        pass

    @abstractmethod
    def get_invalid_limit_response_for_get_list_of_teams(self):
        pass

    @abstractmethod
    def get_invalid_offset_response_for_get_list_of_teams(self):
        pass

    @abstractmethod
    def get_response_for_get_list_of_teams(
            self, team_details_dtos: TeamWithMembersDetailsDTO
    ):
        pass

    @abstractmethod
    def get_user_has_no_access_response_for_add_team(self):
        pass

    @abstractmethod
    def get_invalid_users_response_for_add_team(self):
        pass

    @abstractmethod
    def get_duplicate_users_response_for_add_team(self):
        pass

    @abstractmethod
    def get_team_name_already_exists_response_for_add_team(self, exception):
        pass

    @abstractmethod
    def get_response_for_add_team(self, team_id: str):
        pass

    @abstractmethod
    def make_empty_http_success_response(self):
        pass

    @abstractmethod
    def get_invalid_team_response_for_update_team(self):
        pass

    @abstractmethod
    def get_team_name_already_exists_response_for_update_team(self, exception):
        pass
