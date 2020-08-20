import datetime
from typing import List

from ib_utility_tools.interactors.storage_interfaces.dtos import \
    TimerEntityDTO, CompleteTimerDetailsDTO, EntityWithTimerDTO
from ib_utility_tools.interactors.storage_interfaces \
    .timer_storage_interface import TimerStorageInterface


class GetTimersBulkInteractor:
    def __init__(self, timer_storage: TimerStorageInterface):
        self.timer_storage = timer_storage

    def get_timers_bulk(self, timer_entity_dtos: List[TimerEntityDTO]) \
            -> List[EntityWithTimerDTO]:
        complete_timer_details_dtos = \
            self.timer_storage.get_timer_details_dtos_for_given_entities(
                timer_entity_dtos=timer_entity_dtos)
        self._validate_timer_entity_dtos(
            complete_timer_details_dtos=complete_timer_details_dtos,
            timer_entity_dtos=timer_entity_dtos)
        complete_timer_details_dtos_to_update = \
            self._get_complete_timer_details_dtos_to_update(
                complete_timer_details_dtos=complete_timer_details_dtos)
        is_complete_timer_details_dtos_to_update_not_empty = \
            len(complete_timer_details_dtos_to_update) > 0
        if is_complete_timer_details_dtos_to_update_not_empty:
            self.timer_storage.update_timers_bulk(
                complete_timer_details_dtos=
                complete_timer_details_dtos_to_update)
        entity_with_timer_dtos = [
            self._convert_complete_timer_details_dto_to_entity_with_timer_dto(
                complete_timer_details_dto=complete_timer_details_dto
            ) for complete_timer_details_dto in complete_timer_details_dtos
        ]
        return entity_with_timer_dtos

    @staticmethod
    def _convert_complete_timer_details_dto_to_entity_with_timer_dto(
            complete_timer_details_dto: CompleteTimerDetailsDTO) \
            -> EntityWithTimerDTO:
        entity_with_timer_dto = EntityWithTimerDTO(
            entity_id=complete_timer_details_dto.entity_id,
            entity_type=complete_timer_details_dto.entity_type,
            duration_in_seconds=complete_timer_details_dto.duration_in_seconds,
            is_running=complete_timer_details_dto.is_running
        )
        return entity_with_timer_dto

    def _get_complete_timer_details_dtos_to_update(
            self, complete_timer_details_dtos: List[CompleteTimerDetailsDTO]) \
            -> List[CompleteTimerDetailsDTO]:
        complete_timer_details_dtos_to_update = [
            self._update_and_get_timer_details_dto(
                complete_timer_details_dto=complete_timer_details_dto)
            for complete_timer_details_dto in complete_timer_details_dtos
            if complete_timer_details_dto.is_running is True
        ]
        return complete_timer_details_dtos_to_update

    @staticmethod
    def _validate_timer_entity_dtos(
            complete_timer_details_dtos: List[CompleteTimerDetailsDTO],
            timer_entity_dtos: List[TimerEntityDTO]):
        is_invalid_entities_exist = \
            len(timer_entity_dtos) != len(complete_timer_details_dtos)
        if is_invalid_entities_exist:
            from ib_utility_tools.exceptions.custom_exceptions import \
                InvalidEntities
            raise InvalidEntities

    @staticmethod
    def _update_and_get_timer_details_dto(
            complete_timer_details_dto: CompleteTimerDetailsDTO):
        present_datetime = datetime.datetime.now()
        time_delta = \
            present_datetime - complete_timer_details_dto.start_datetime
        duration_in_seconds = \
            complete_timer_details_dto.duration_in_seconds + time_delta.seconds
        complete_timer_details_dto.duration_in_seconds = duration_in_seconds
        complete_timer_details_dto.start_datetime = present_datetime
        return complete_timer_details_dto
