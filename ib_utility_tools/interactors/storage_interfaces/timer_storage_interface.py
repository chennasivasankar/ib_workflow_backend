import abc
from typing import Optional, List

from ib_utility_tools.interactors.storage_interfaces.dtos import \
    TimerEntityDTO, TimerDetailsDTO, CompleteTimerDetailsDTO


class TimerStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_timer_id_if_exists(self, timer_entity_dto: TimerEntityDTO) -> \
            Optional[str]:
        pass

    @abc.abstractmethod
    def create_timer(self, timer_entity_dto: TimerEntityDTO) -> str:
        pass

    @abc.abstractmethod
    def update_timer(self,
                     timer_entity_dto: TimerEntityDTO,
                     timer_details_dto: TimerDetailsDTO):
        pass

    @abc.abstractmethod
    def get_timer_details_dto(
            self, timer_entity_dto: TimerEntityDTO) -> TimerDetailsDTO:
        pass

    @abc.abstractmethod
    def get_timer_details_dtos_for_given_entities(
            self, timer_entity_dtos: List[TimerEntityDTO]) -> \
            List[CompleteTimerDetailsDTO]:
        pass

    @abc.abstractmethod
    def update_timers_bulk(self, complete_timer_details_dtos: List[
        CompleteTimerDetailsDTO]):
        pass
