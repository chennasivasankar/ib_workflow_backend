import datetime
from typing import List

from ib_utility_tools.interactors.storage_interfaces.dtos import TimerEntityDTO
from ib_utility_tools.interactors.storage_interfaces \
    .timer_storage_interface import TimerStorageInterface


class GetTimersBulkInteractor:
    def __init__(self, timer_storage: TimerStorageInterface):
        self.timer_storage = timer_storage

    def get_timers_bulk(self, timer_entity_dtos: List[TimerEntityDTO]):
        complete_timer_details_dtos = \
            self.timer_storage.get_timer_details_dtos_for_given_entities(
                timer_entity_dtos=timer_entity_dtos)
        is_invalid_entities_exist = \
            len(timer_entity_dtos) != len(complete_timer_details_dtos)
        if is_invalid_entities_exist:
            from ib_utility_tools.exceptions.custom_exceptions import \
                InvalidEntities
            raise InvalidEntities
        complete_timer_details_dtos_to_update = []
        for complete_timer_details_dto in complete_timer_details_dtos:
            if complete_timer_details_dto.is_running is True:
                complete_timer_details_dto = self._update_and_get_timer_details_dto(
                    timer_details_dto=complete_timer_details_dto)
                complete_timer_details_dtos_to_update.append(complete_timer_details_dto)
        is_complete_timer_details_dtos_to_update_not_empty = \
            len(complete_timer_details_dtos_to_update) > 0
        if is_complete_timer_details_dtos_to_update_not_empty:
            self.timer_storage.update_timers_bulk(
                complete_timer_details_dtos=complete_timer_details_dtos_to_update)
        return complete_timer_details_dtos

    @staticmethod
    def _update_and_get_timer_details_dto(timer_details_dto):
        present_datetime = datetime.datetime.now()
        time_delta = \
            present_datetime - timer_details_dto.start_datetime
        duration_in_seconds = \
            timer_details_dto.duration_in_seconds + time_delta.seconds
        timer_details_dto.duration_in_seconds = duration_in_seconds
        timer_details_dto.start_datetime = present_datetime
        return timer_details_dto
