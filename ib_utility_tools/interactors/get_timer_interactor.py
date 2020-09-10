import datetime

from ib_utility_tools.interactors.presenter_interfaces \
    .timer_presenter_interface import TimerPresenterInterface
from ib_utility_tools.interactors.storage_interfaces.dtos import \
    TimerEntityDTO, TimerDetailsDTO
from ib_utility_tools.interactors.storage_interfaces \
    .timer_storage_interface import TimerStorageInterface


class GetTimerInteractor:
    def __init__(self, timer_storage: TimerStorageInterface):
        self.timer_storage = timer_storage

    def get_timer_wrapper(self, timer_entity_dto: TimerEntityDTO,
                          presenter: TimerPresenterInterface):
        timer_details_dto = self.get_timer(timer_entity_dto=timer_entity_dto)
        response = presenter.get_response_for_get_timer_details(
            timer_details_dto=timer_details_dto)
        return response

    def get_timer(self, timer_entity_dto: TimerEntityDTO):
        is_created = self._create_timer_if_not_exists(timer_entity_dto)
        if is_created:
            return TimerDetailsDTO(duration_in_seconds=0, is_running=False)
        timer_details_dto = self.timer_storage.get_timer_details_dto(
            timer_entity_dto=timer_entity_dto)
        if timer_details_dto.is_running is False:
            return timer_details_dto
        present_datetime = datetime.datetime.now()
        time_delta = present_datetime - timer_details_dto.start_datetime
        duration_in_seconds = \
            timer_details_dto.duration_in_seconds + time_delta.seconds
        timer_details_dto = TimerDetailsDTO(
            duration_in_seconds=duration_in_seconds,
            start_datetime=present_datetime,
            is_running=True)
        self.timer_storage.update_timer(timer_entity_dto=timer_entity_dto,
                                        timer_details_dto=timer_details_dto)
        return timer_details_dto

    def _create_timer_if_not_exists(self, timer_entity_dto: TimerEntityDTO):
        timer_id = self.timer_storage.get_timer_id_if_exists(
            timer_entity_dto=timer_entity_dto)
        if timer_id is None:
            _ = self.timer_storage.create_timer(
                timer_entity_dto=timer_entity_dto)
            return True
        return False
