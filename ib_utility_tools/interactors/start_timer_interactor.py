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
        timer_details_dto = self.start_timer(timer_entity_dto=timer_entity_dto)
        response = presenter.get_success_response_with_timer_details_dto(
            timer_details_dto=timer_details_dto)
        return response

    def start_timer(self, timer_entity_dto: TimerEntityDTO):
        self.timer_storage \
            .update_start_datetime_to_present_time_and_timer_status_to_true(
            timer_entity_dto=timer_entity_dto)
        timer_details_dto = self.timer_storage.get_timer_details_dto(
            timer_entity_dto=timer_entity_dto)

        return timer_details_dto
