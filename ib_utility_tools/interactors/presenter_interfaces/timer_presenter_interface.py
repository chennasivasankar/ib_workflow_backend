import abc

from ib_utility_tools.interactors.storage_interfaces.dtos import \
    TimerDetailsDTO


class TimerPresenterInterface(abc.ABC):

    @abc.abstractmethod
    def get_response_for_get_timer_details(
            self, timer_details_dto: TimerDetailsDTO
    ):
        pass

    @abc.abstractmethod
    def get_response_for_timer_is_already_running_exception(self):
        pass

    @abc.abstractmethod
    def get_response_for_timer_is_already_stopped_exception(self):
        pass
