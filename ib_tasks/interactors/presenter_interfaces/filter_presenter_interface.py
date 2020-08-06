import abc

from ib_tasks.interactors.filter_dtos import FilterCompleteDetailsDTO


class FilterPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_get_filters_details(
            self, filter_complete_details: FilterCompleteDetailsDTO):
        pass