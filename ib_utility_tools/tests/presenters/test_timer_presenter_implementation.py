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
