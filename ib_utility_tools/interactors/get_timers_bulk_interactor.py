import datetime
from typing import List

from ib_utility_tools.interactors.storage_interfaces.dtos import \
    TimerEntityDTO, CompleteTimerDetailsDTO, EntityWithTimerDTO
from ib_utility_tools.interactors.storage_interfaces \
    .timer_storage_interface import TimerStorageInterface


class GetTimersBulkInteractor:

    def __init__(self, timer_storage: TimerStorageInterface):
        self.timer_storage = timer_storage

    def get_timers_bulk(
            self, timer_entity_dtos: List[TimerEntityDTO]
    ) -> List[EntityWithTimerDTO]:
        complete_timer_details_dtos = \
            self.timer_storage.get_timer_details_dtos(
                timer_entity_dtos=timer_entity_dtos
            )
        self._calculate_and_update_duration_seconds_for_running_timers(
            complete_timer_details_dtos=complete_timer_details_dtos
        )
        entity_with_timer_dtos = [
            self._convert_complete_timer_details_dto_to_entity_with_timer_dto(
                complete_timer_details_dto=complete_timer_details_dto
            ) for complete_timer_details_dto in complete_timer_details_dtos
        ]
        entity_with_timer_dtos.extend(
            self._add_timer_details_info_for_invalid_timer_entities(
                complete_timer_details_dtos=complete_timer_details_dtos,
                timer_entity_dtos=timer_entity_dtos)
        )
        return entity_with_timer_dtos

    @staticmethod
    def _convert_complete_timer_details_dto_to_entity_with_timer_dto(
            complete_timer_details_dto: CompleteTimerDetailsDTO
    ) -> EntityWithTimerDTO:
        entity_with_timer_dto = EntityWithTimerDTO(
            entity_id=complete_timer_details_dto.entity_id,
            entity_type=complete_timer_details_dto.entity_type,
            duration_in_seconds=complete_timer_details_dto.duration_in_seconds,
            is_running=complete_timer_details_dto.is_running
        )
        return entity_with_timer_dto

    def _calculate_and_update_duration_seconds_for_running_timers(
            self, complete_timer_details_dtos: List[CompleteTimerDetailsDTO]
    ):
        for complete_timer_details_dto in complete_timer_details_dtos:
            if complete_timer_details_dto.is_running is True:
                self._calculate_and_update_duration_seconds_for_running_timer(
                    complete_timer_details_dto=complete_timer_details_dto
                )

    @staticmethod
    def _calculate_and_update_duration_seconds_for_running_timer(
            complete_timer_details_dto: CompleteTimerDetailsDTO
    ):
        present_datetime = datetime.datetime.now()
        time_delta = present_datetime - complete_timer_details_dto.start_datetime
        duration_in_seconds = (
                complete_timer_details_dto.duration_in_seconds + time_delta.seconds
        )
        complete_timer_details_dto.duration_in_seconds = duration_in_seconds
        complete_timer_details_dto.start_datetime = present_datetime

    def _add_timer_details_info_for_invalid_timer_entities(
            self, timer_entity_dtos: List[TimerEntityDTO],
            complete_timer_details_dtos: List[CompleteTimerDetailsDTO],
    ) -> List[EntityWithTimerDTO]:
        entity_with_timer_dtos = []
        entity_ids_from_timer_dtos = [
            timer_dto.entity_id for timer_dto in complete_timer_details_dtos
        ]
        for entity_dto in timer_entity_dtos:
            if entity_dto.entity_id not in entity_ids_from_timer_dtos:
                entity_with_timer_dtos.append(
                    self._get_default_entity_with_timer_dto(
                        timer_entity_dto=entity_dto
                    )
                )
        return entity_with_timer_dtos

    @staticmethod
    def _get_default_entity_with_timer_dto(
            timer_entity_dto: TimerEntityDTO
    ) -> EntityWithTimerDTO:
        entity_with_timer_dto = EntityWithTimerDTO(
            entity_id=timer_entity_dto.entity_id,
            entity_type=timer_entity_dto.entity_type,
            duration_in_seconds=0, is_running=False
        )
        return entity_with_timer_dto
