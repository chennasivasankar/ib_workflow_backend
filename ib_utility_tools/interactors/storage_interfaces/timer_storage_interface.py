import abc
import datetime
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
    def update_start_datetime_to_present_time_and_timer_status_to_true(
            self, timer_entity_dto: TimerEntityDTO):
        pass

    @abc.abstractmethod
    def get_timer_details_dto(
            self, timer_entity_dto: TimerEntityDTO) -> TimerDetailsDTO:
        pass

    @abc.abstractmethod
    def get_start_datetime_and_duration(self,
                                        timer_entity_dto: TimerEntityDTO):
        pass

    @abc.abstractmethod
    def update_timer_while_stopping_timer(
            self, timer_entity_dto: TimerEntityDTO, duration_in_seconds: int):
        pass

    @abc.abstractmethod
    def update_start_datetime_to_present_and_duration(
            self, timer_entity_dto: TimerEntityDTO,
            present_datetime: datetime.datetime,
            duration_in_seconds: int):
        pass
