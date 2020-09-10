import json
from ib_iam.presenters.team_presenter_implementation import (
    TeamPresenterImplementation
)
from ib_iam.constants.exception_messages import (
    INVALID_OFFSET_FOR_GET_LIST_OF_TEAMS
)


class TestRaiseExceptionForInvalidOffsetForGetListOfTeams:
    def test_whether_it_returns_invalid_offset_exception_http_response(self):
        json_presenter = TeamPresenterImplementation()
        expected_response = INVALID_OFFSET_FOR_GET_LIST_OF_TEAMS[0]
        expected_res_status = INVALID_OFFSET_FOR_GET_LIST_OF_TEAMS[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        result = json_presenter.get_invalid_offset_response_for_get_list_of_teams()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
