from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_utility_tools.interactors.presenter_interfaces \
    .timer_presenter_interface import TimerPresenterInterface
from ib_utility_tools.interactors.storage_interfaces.dtos import \
    TimerDetailsDTO


class TimerPresenterImplementation(TimerPresenterInterface, HTTPResponseMixin):
    def get_success_response_with_timer_details_dto(
            self, timer_details_dto: TimerDetailsDTO):
        timer_details_dict = {
            "duration_in_seconds": timer_details_dto.duration_in_seconds,
            "is_running": timer_details_dto.is_running
        }
        return self.prepare_200_success_response(
            response_dict=timer_details_dict)
