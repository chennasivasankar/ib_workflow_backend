from django_swagger_utils.utils.http_response_mixin import HTTPResponseMixin

from ib_utility_tools.constants.enum import StatusCode
from ib_utility_tools.interactors.presenter_interfaces \
    .timer_presenter_interface import TimerPresenterInterface
from ib_utility_tools.interactors.storage_interfaces.dtos import \
    TimerDetailsDTO


class TimerPresenterImplementation(TimerPresenterInterface, HTTPResponseMixin):

    def get_response_for_get_timer_details(
            self, timer_details_dto: TimerDetailsDTO
    ):
        timer_details_dict = {
            "duration_in_seconds": timer_details_dto.duration_in_seconds,
            "is_running": timer_details_dto.is_running
        }
        return self.prepare_200_success_response(
            response_dict=timer_details_dict
        )

    def get_response_for_timer_is_already_running_exception(self):
        from ib_utility_tools.constants.exception_messages import \
            TIMER_IS_ALREADY_RUNNING
        response_dict = {
            "response": TIMER_IS_ALREADY_RUNNING[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": TIMER_IS_ALREADY_RUNNING[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )

    def get_response_for_timer_is_already_stopped_exception(self):
        from ib_utility_tools.constants.exception_messages import \
            TIMER_IS_ALREADY_STOPPED
        response_dict = {
            "response": TIMER_IS_ALREADY_STOPPED[0],
            "http_status_code": StatusCode.BAD_REQUEST.value,
            "res_status": TIMER_IS_ALREADY_STOPPED[1]
        }
        return self.prepare_400_bad_request_response(
            response_dict=response_dict
        )
