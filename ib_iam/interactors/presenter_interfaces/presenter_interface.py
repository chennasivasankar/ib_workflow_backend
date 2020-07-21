from abc import abstractmethod, ABC

from ib_iam.adapters.dtos import UserProfileDTO
from ib_iam.interactors.presenter_interfaces.dtos \
    import CompleteUserDetailsDTO


class PresenterInterface(ABC):
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
    def raise_offset_value_is_greater_than_limit_value_exception(self):
        pass

    @abstractmethod
    def response_for_get_users(
            self, complete_user_details_dtos: CompleteUserDetailsDTO):
        pass


class GetUserProfilePresenterInterface(ABC):
    @abstractmethod
    def raise_exception_for_invalid_user_id(self):
        pass

    @abstractmethod
    def raise_exception_for_user_account_does_not_exist(self):
        pass

    @abstractmethod
    def prepare_response_for_user_profile_dto(self,
                                              user_profile_dto: UserProfileDTO):
        pass
