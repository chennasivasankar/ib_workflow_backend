import abc
from typing import Optional

from ib_utility_tools.interactors.storage_interfaces.dtos import \
    TimerEntityDTO, TimerDetailsDTO


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
