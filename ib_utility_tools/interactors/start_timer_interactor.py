from ib_utility_tools.exceptions.custom_exceptions import TimerIsAlreadyRunning
from ib_utility_tools.interactors.presenter_interfaces \
    .timer_presenter_interface import TimerPresenterInterface
from ib_utility_tools.interactors.storage_interfaces.dtos import TimerEntityDTO
from ib_utility_tools.interactors.storage_interfaces \
    .timer_storage_interface import TimerStorageInterface


class StartTimerInteractor:
    def __init__(self, timer_storage: TimerStorageInterface):
        self.timer_storage = timer_storage

    def start_timer_wrapper(self, timer_entity_dto: TimerEntityDTO,
                            presenter: TimerPresenterInterface):
        try:
            timer_details_dto = self.start_timer(
                timer_entity_dto=timer_entity_dto)
            response = presenter.get_success_response_with_timer_details_dto(
                timer_details_dto=timer_details_dto)
        except TimerIsAlreadyRunning:
            response = presenter.raise_timer_is_already_running_exception()
        return response

    def start_timer(self, timer_entity_dto: TimerEntityDTO):
        timer_details_dto = self.timer_storage.get_timer_details_dto(
            timer_entity_dto=timer_entity_dto)
        if timer_details_dto.is_running is True:
            raise TimerIsAlreadyRunning
        self.timer_storage \
            .update_start_datetime_to_present_time_and_timer_status_to_true(
            timer_entity_dto=timer_entity_dto)
        timer_details_dto.is_running = True
        return timer_details_dto
