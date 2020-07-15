from abc import abstractmethod


from ib_iam.interactors.presenter_interfaces.dtos import TeamWithMembersDetailsDTO


class TeamPresenterInterface:

    @abstractmethod
    def raise_exception_for_user_has_no_access(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_limit(self):
        pass

    @abstractmethod
    def raise_exception_for_invalid_offset(self):
        pass

    @abstractmethod
    def get_response_for_get_list_of_teams(
            self, team_details_dtos: TeamWithMembersDetailsDTO
    ):
        pass
