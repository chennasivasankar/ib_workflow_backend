import abc

from ib_iam.interactors.presenter_interfaces.dtos import UserOptionsDetailsDTO


class GetUserOptionsPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def response_for_user_is_not_admin_exception(self):
        pass

    @abc.abstractmethod
    def get_user_options_details_response(
            self, configuration_details_dto: UserOptionsDetailsDTO
    ):
        pass
