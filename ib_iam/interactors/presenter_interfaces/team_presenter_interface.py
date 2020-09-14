import abc

from ib_iam.interactors.presenter_interfaces.dtos import \
    TeamWithUsersDetailsDTO


class TeamPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_user_has_no_access_response_for_get_list_of_teams(self):
        pass

    @abc.abstractmethod
    def get_invalid_limit_response_for_get_list_of_teams(self):
        pass

    @abc.abstractmethod
    def get_invalid_offset_response_for_get_list_of_teams(self):
        pass

    @abc.abstractmethod
    def get_response_for_get_list_of_teams(
            self, team_details_dtos: TeamWithUsersDetailsDTO
    ):
        pass

    @abc.abstractmethod
    def get_user_has_no_access_response_for_add_team(self):
        pass

    @abc.abstractmethod
    def get_invalid_users_response_for_add_team(self):
        pass

    @abc.abstractmethod
    def get_duplicate_users_response_for_add_team(self):
        pass

    @abc.abstractmethod
    def get_team_name_already_exists_response_for_add_team(self, err):
        pass

    @abc.abstractmethod
    def get_response_for_add_team(self, team_id: str):
        pass
