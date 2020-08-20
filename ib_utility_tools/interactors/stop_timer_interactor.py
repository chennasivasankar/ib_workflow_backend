import datetime

from ib_utility_tools.exceptions.custom_exceptions import TimerIsAlreadyStopped
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
        try:
            timer_details_dto = self.stop_timer(
                timer_entity_dto=timer_entity_dto)
            response = presenter.get_success_response_with_timer_details_dto(
                timer_details_dto=timer_details_dto)
        except TimerIsAlreadyStopped:
            response = presenter.raise_timer_is_already_stopped_exception()
        return response

    def stop_timer(self, timer_entity_dto: TimerEntityDTO):
        timer_details_dto = self.timer_storage.get_timer_details_dto(
            timer_entity_dto=timer_entity_dto)
        print("&"*80)
        print("HI")
        print(timer_details_dto)
        if timer_details_dto.is_running is False:
            print("I am in false")
            raise TimerIsAlreadyStopped
        stop_datetime = datetime.datetime.now()
        time_delta = stop_datetime - timer_details_dto.start_datetime
        duration_in_seconds = \
            timer_details_dto.duration_in_seconds + time_delta.seconds
        timer_details_dto = TimerDetailsDTO(
            duration_in_seconds=duration_in_seconds,
            is_running=False)
        print("IAm before update")
        self.timer_storage.update_timer(
            timer_entity_dto=timer_entity_dto,
            timer_details_dto=timer_details_dto)
        print("IAm After update")
        return timer_details_dto
