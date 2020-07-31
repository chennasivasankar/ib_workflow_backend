from abc import ABC, abstractmethod

from ib_iam.interactors.presenter_interfaces.dtos import ListOfCompleteUsersDTO


class GetUsersListPresenterInterface(ABC):
    @abstractmethod
    def raise_user_is_not_admin_exception(self):
        pass

    @abstractmethod
    def raise_invalid_offset_value_exception(self):
        pass

    @abstractmethod
    def raise_invalid_limit_value_exception(self):
        pass

    @abstractmethod
    def response_for_get_users(
            self, complete_user_details_dtos: ListOfCompleteUsersDTO):
        pass

    @abstractmethod
    def raise_invalid_user(self):
        pass
