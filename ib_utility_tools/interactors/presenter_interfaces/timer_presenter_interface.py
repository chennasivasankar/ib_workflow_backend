import abc

from ib_utility_tools.interactors.storage_interfaces.dtos import \
    TimerDetailsDTO


class TimerPresenterInterface(abc.ABC):
    @abc.abstractmethod
    def get_success_response_with_timer_details_dto(
            self, timer_details_dto: TimerDetailsDTO):
        pass
