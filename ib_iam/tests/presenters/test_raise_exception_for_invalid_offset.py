import pytest
from ib_iam.presenters.team_presenter_implementation import TeamPresenterImplementation
from ib_iam.constants.exception_messages import INVALID_OFFSET


class TestRaiseExceptionForUserHasNoAccess:
    def test_when_it_is_called_it_returns_http_response(self, snapshot):
        json_presenter = TeamPresenterImplementation()
        import json
        expected_response = INVALID_OFFSET[0]
        expected_res_status = INVALID_OFFSET[1]
        expected_http_status_code = 400

        result = json_presenter.raise_exception_for_invalid_offset()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
