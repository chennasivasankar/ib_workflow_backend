import json

from ib_utility_tools.presenters.timer_presenter_implementation import \
    TimerPresenterImplementation


class TestTimerPresenterImplementation:

    def test_whether_it_returns_timer_details_http_response(self):
        json_presenter = TimerPresenterImplementation()
        from ib_utility_tools.tests.factories.storage_dtos import \
            TimerDetailsDTOFactory
        timer_details_dto = TimerDetailsDTOFactory()
        expected_duration_in_seconds = timer_details_dto.duration_in_seconds
        expected_is_running = timer_details_dto.is_running

        result = json_presenter.get_success_response_with_timer_details_dto(
            timer_details_dto=timer_details_dto)

        actual_response = json.loads(result.content)
        actual_duration_in_seconds = actual_response["duration_in_seconds"]
        actual_is_running = actual_response["is_running"]
        assert actual_duration_in_seconds == expected_duration_in_seconds
        assert actual_is_running == expected_is_running

    def test_whether_it_returns_timer_is_already_running_http_response(self):
        json_presenter = TimerPresenterImplementation()
        from ib_utility_tools.constants.exception_messages import \
            TIMER_IS_ALREADY_RUNNING
        expected_response = TIMER_IS_ALREADY_RUNNING[0]
        expected_res_status = TIMER_IS_ALREADY_RUNNING[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        result = \
            json_presenter.raise_timer_is_already_running_exception()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
