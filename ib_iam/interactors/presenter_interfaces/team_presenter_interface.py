import abc
from ib_iam.interactors.presenter_interfaces.dtos import \
    TeamWithUsersDetailsDTO


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
    def response_for_duplicate_user_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_user_ids_exception(self):
        pass


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


class GetTeamsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def response_for_user_has_no_access_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_limit_value_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_offset_value_exception(self):
        pass

    @abc.abstractmethod
    def get_response_for_get_list_of_teams(
            self, team_details_dtos: TeamWithUsersDetailsDTO
    ):
        pass


class AddTeamPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def response_for_user_has_no_access_exception(self):
        pass

    @abc.abstractmethod
    def response_for_invalid_user_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_duplicate_user_ids_exception(self):
        pass

    @abc.abstractmethod
    def response_for_team_name_already_exists_exception(self, err):
        pass

    @abc.abstractmethod
    def get_response_for_add_team(self, team_id: str):
        pass
