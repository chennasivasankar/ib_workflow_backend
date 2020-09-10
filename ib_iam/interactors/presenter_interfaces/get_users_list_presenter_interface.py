import abc

from ib_iam.interactors.presenter_interfaces.dtos import ListOfCompleteUsersDTO, \
    ListOfCompleteUsersWithRolesDTO


class GetUsersListPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def response_for_user_is_not_admin_exception(self):
        pass

    @abc.abstractmethod
    def raise_invalid_offset_value_exception(self):
        pass

    @abc.abstractmethod
    def raise_invalid_limit_value_exception(self):
        pass

    @abc.abstractmethod
    def response_for_get_users(
            self, complete_user_details_dtos: ListOfCompleteUsersWithRolesDTO):
        pass

    @abc.abstractmethod
    def raise_invalid_user(self):
        pass
