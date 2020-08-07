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
        response = presenter.get_success_response_with_timer_details_dto(
            timer_details_dto=timer_details_dto)
        return response

    def get_timer(self, timer_entity_dto: TimerEntityDTO):
        timer_details_dto = self.timer_storage.get_timer_details_dto(
            timer_entity_dto=timer_entity_dto)
        if timer_details_dto.is_running is False:
            return timer_details_dto
        start_datetime, duration_in_seconds = self.timer_storage \
            .get_start_datetime_and_duration(timer_entity_dto=timer_entity_dto)
        present_datetime = datetime.datetime.now()
        time_delta = present_datetime - start_datetime
        duration_in_seconds = duration_in_seconds + time_delta.seconds
        self.timer_storage.update_start_datetime_to_present_and_duration(
            present_datetime=present_datetime,
            duration_in_seconds=duration_in_seconds)
        timer_details_dto = TimerDetailsDTO(
            duration_in_seconds=duration_in_seconds,
            is_running=False)

        return timer_details_dto
