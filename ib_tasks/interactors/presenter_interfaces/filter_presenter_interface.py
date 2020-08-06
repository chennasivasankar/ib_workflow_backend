import abc

from ib_tasks.constants.enum import Status
from ib_tasks.interactors.filter_dtos import FilterCompleteDetailsDTO


class FilterPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_get_filters_details(
            self, filter_complete_details: FilterCompleteDetailsDTO):
        pass

    @abc.abstractmethod
    def get_response_for_invalid_filter_id(self):
        pass

    @abc.abstractmethod
    def get_response_for_invalid_user_to_update_filter_status(self):
        pass

    @abc.abstractmethod
    def get_response_for_update_filter_status(
            self, filter_id: int, is_selected: Status):
        pass