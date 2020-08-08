import datetime

from ib_utility_tools.interactors.presenter_interfaces \
    .timer_presenter_interface import TimerPresenterInterface
from ib_utility_tools.interactors.storage_interfaces.dtos import \
    TimerEntityDTO, TimerDetailsDTO
from ib_utility_tools.interactors.storage_interfaces \
    .timer_storage_interface import TimerStorageInterface


class StopTimerInteractor:
    def __init__(self, timer_storage: TimerStorageInterface):
        self.timer_storage = timer_storage

    def stop_timer_wrapper(self, timer_entity_dto: TimerEntityDTO,
                           presenter: TimerPresenterInterface):
        timer_details_dto = self.stop_timer(timer_entity_dto=timer_entity_dto)
        response = presenter.get_success_response_with_timer_details_dto(
            timer_details_dto=timer_details_dto)
        return response

    def stop_timer(self, timer_entity_dto: TimerEntityDTO):
        start_datetime, duration_in_seconds_from_db = self.timer_storage \
            .get_start_datetime_and_duration(timer_entity_dto=timer_entity_dto)
        stop_datetime = datetime.datetime.now()
        time_delta = stop_datetime - start_datetime
        duration_in_seconds = duration_in_seconds_from_db + time_delta.seconds
        self.timer_storage.update_timer_while_stopping_timer(
            timer_entity_dto=timer_entity_dto,
            duration_in_seconds=duration_in_seconds)
        timer_details_dto = TimerDetailsDTO(
            duration_in_seconds=duration_in_seconds,
            is_running=False)

        return timer_details_dto
