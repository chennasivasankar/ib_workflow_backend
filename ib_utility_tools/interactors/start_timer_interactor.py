import datetime

from ib_utility_tools.exceptions.custom_exceptions import TimerIsAlreadyRunning
from ib_utility_tools.interactors.presenter_interfaces \
    .timer_presenter_interface import TimerPresenterInterface
from ib_utility_tools.interactors.storage_interfaces.dtos import \
    TimerEntityDTO, TimerDetailsDTO
from ib_utility_tools.interactors.storage_interfaces \
    .timer_storage_interface import TimerStorageInterface


class StartTimerInteractor:

    def __init__(self, timer_storage: TimerStorageInterface):
        self.timer_storage = timer_storage

    def start_timer_wrapper(
            self, timer_entity_dto: TimerEntityDTO,
            presenter: TimerPresenterInterface
    ):
        try:
            timer_details_dto = self.start_timer(
                timer_entity_dto=timer_entity_dto
            )
            response = presenter.get_response_for_get_timer_details(
                timer_details_dto=timer_details_dto
            )
        except TimerIsAlreadyRunning:
            response = presenter \
                .get_response_for_timer_is_already_running_exception()
        return response

    def start_timer(
            self, timer_entity_dto: TimerEntityDTO
    ) -> TimerDetailsDTO:
        timer_details_dto = self.timer_storage.get_timer_details_dto(
            timer_entity_dto=timer_entity_dto
        )
        if timer_details_dto.is_running is True:
            raise TimerIsAlreadyRunning
        timer_details_dto.start_datetime = datetime.datetime.now()
        timer_details_dto.is_running = True
        self.timer_storage.update_timer(
            timer_entity_dto=timer_entity_dto,
            timer_details_dto=timer_details_dto
        )
        return timer_details_dto
