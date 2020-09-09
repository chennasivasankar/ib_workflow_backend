from typing import Optional, List

from ib_utility_tools.interactors.storage_interfaces.dtos import \
    TimerEntityDTO, TimerDetailsDTO, CompleteTimerDetailsDTO
from ib_utility_tools.interactors.storage_interfaces \
    .timer_storage_interface import TimerStorageInterface
from ib_utility_tools.models import Timer


class TimerStorageImplementation(TimerStorageInterface):

    def get_timer_id_if_exists(
            self, timer_entity_dto: TimerEntityDTO
    ) -> Optional[str]:
        try:
            timer_object = Timer.objects.get(
                entity_id=timer_entity_dto.entity_id,
                entity_type=timer_entity_dto.entity_type
            )
        except Timer.DoesNotExist:
            return None
        return str(timer_object.timer_id)

    def create_timer(self, timer_entity_dto: TimerEntityDTO) -> str:
        timer_object = Timer.objects.create(
            entity_id=timer_entity_dto.entity_id,
            entity_type=timer_entity_dto.entity_type
        )
        return str(timer_object.timer_id)

    def get_timer_details_dto(
            self, timer_entity_dto: TimerEntityDTO
    ) -> TimerDetailsDTO:
        timer_object = Timer.objects.get(
            entity_id=timer_entity_dto.entity_id,
            entity_type=timer_entity_dto.entity_type
        )
        timer_details_dto = self._prepare_timer_details_dto(
            timer_object=timer_object
        )
        return timer_details_dto

    def update_timer(
            self, timer_entity_dto: TimerEntityDTO,
            timer_details_dto: TimerDetailsDTO
    ):
        Timer.objects.filter(
            entity_id=timer_entity_dto.entity_id,
            entity_type=timer_entity_dto.entity_type
        ).update(
            start_datetime=timer_details_dto.start_datetime,
            duration_in_seconds=timer_details_dto.duration_in_seconds,
            is_running=timer_details_dto.is_running
        )

    def get_timer_details_dtos(
            self, timer_entity_dtos: List[TimerEntityDTO]
    ) -> List[CompleteTimerDetailsDTO]:
        entity_q_objects = self._prepare_entity_q_objects_for_given_dtos(
            dtos=timer_entity_dtos
        )
        timer_objects = Timer.objects.filter(entity_q_objects)
        timer_details_dtos = [
            self._prepare_complete_timer_details_dto(timer_object=timer_object)
            for timer_object in timer_objects
        ]
        return timer_details_dtos

    @staticmethod
    def _prepare_timer_details_dto(timer_object) -> TimerDetailsDTO:
        timer_details_dto = TimerDetailsDTO(
            duration_in_seconds=timer_object.duration_in_seconds,
            is_running=timer_object.is_running,
            start_datetime=timer_object.start_datetime
        )
        return timer_details_dto

    @staticmethod
    def _prepare_complete_timer_details_dto(
            timer_object
    ) -> CompleteTimerDetailsDTO:
        timer_details_dto = CompleteTimerDetailsDTO(
            entity_id=timer_object.entity_id,
            entity_type=timer_object.entity_type,
            duration_in_seconds=timer_object.duration_in_seconds,
            is_running=timer_object.is_running,
            start_datetime=timer_object.start_datetime
        )
        return timer_details_dto

    @staticmethod
    def _prepare_entity_q_objects_for_given_dtos(dtos):
        from django.db.models import Q
        entity_q_objects = Q()
        for dto in dtos:
            entity_q_objects |= Q(
                entity_id=dto.entity_id, entity_type=dto.entity_type
            )
        return entity_q_objects
