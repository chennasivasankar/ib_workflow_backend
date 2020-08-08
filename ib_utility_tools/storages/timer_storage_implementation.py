import datetime
from typing import Optional

from ib_utility_tools.interactors.storage_interfaces.dtos import \
    TimerEntityDTO, TimerDetailsDTO
from ib_utility_tools.interactors.storage_interfaces \
    .timer_storage_interface import TimerStorageInterface
from ib_utility_tools.models import Timer


class TimerStorageImplementation(TimerStorageInterface):

    def get_timer_id_if_exists(self, timer_entity_dto: TimerEntityDTO) -> \
            Optional[str]:
        try:
            timer_object = Timer.objects.get(
                entity_id=timer_entity_dto.entity_id,
                entity_type=timer_entity_dto.entity_type)
        except Timer.DoesNotExist:
            return None
        return str(timer_object.timer_id)

    def create_timer(self, timer_entity_dto: TimerEntityDTO) -> str:
        timer_object = Timer.objects.create(
            entity_id=timer_entity_dto.entity_id,
            entity_type=timer_entity_dto.entity_type)
        return str(timer_object.timer_id)

    def update_start_datetime_to_present_time_and_timer_status_to_true(
            self, timer_entity_dto: TimerEntityDTO):
        Timer.objects.filter(entity_id=timer_entity_dto.entity_id,
                             entity_type=timer_entity_dto.entity_type
                             ).update(start_datetime=datetime.datetime.now(),
                                      is_running=True)

    def get_timer_details_dto(
            self, timer_entity_dto: TimerEntityDTO) -> TimerDetailsDTO:
        timer_object = Timer.objects.get(
            entity_id=timer_entity_dto.entity_id,
            entity_type=timer_entity_dto.entity_type)
        timer_details_dto = self._prepare_timer_details_dto(
            timer_object=timer_object)
        return timer_details_dto

    def get_start_datetime_and_duration(self,
                                        timer_entity_dto: TimerEntityDTO):
        timer_object = Timer.objects.get(
            entity_id=timer_entity_dto.entity_id,
            entity_type=timer_entity_dto.entity_type)
        return timer_object.start_datetime, timer_object.duration_in_seconds

    def update_timer_while_stopping_timer(
            self, timer_entity_dto: TimerEntityDTO, duration_in_seconds: int):
        Timer.objects.filter(entity_id=timer_entity_dto.entity_id,
                             entity_type=timer_entity_dto.entity_type
                             ).update(start_datetime=None,
                                      is_running=False,
                                      duration_in_seconds=duration_in_seconds)

    def update_start_datetime_to_present_and_duration(
            self, timer_entity_dto: TimerEntityDTO,
            present_datetime: datetime,
            duration_in_seconds: int):
        Timer.objects.filter(entity_id=timer_entity_dto.entity_id,
                             entity_type=timer_entity_dto.entity_type
                             ).update(start_datetime=present_datetime,
                                      duration_in_seconds=duration_in_seconds)

    @staticmethod
    def _prepare_timer_details_dto(timer_object) -> TimerDetailsDTO:
        from ib_utility_tools.interactors.storage_interfaces.dtos import \
            TimerDetailsDTO
        timer_details_dto = TimerDetailsDTO(
            duration_in_seconds=timer_object.duration_in_seconds,
            is_running=timer_object.is_running)
        return timer_details_dto
