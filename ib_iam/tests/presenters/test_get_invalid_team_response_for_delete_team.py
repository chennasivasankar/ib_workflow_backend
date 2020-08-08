import json
from ib_iam.presenters.delete_team_presenter_implementation import (
    DeleteTeamPresenterImplementation
)
from ib_iam.constants.exception_messages import INVALID_TEAM_ID_FOR_DELETE_TEAM


class TestRaiseExceptionForInvalidTeamIdForDeleteTeam:
    def test_whether_it_returns_invalid_team_http_response(self):
        json_presenter = DeleteTeamPresenterImplementation()
        expected_response = INVALID_TEAM_ID_FOR_DELETE_TEAM[0]
        expected_res_status = INVALID_TEAM_ID_FOR_DELETE_TEAM[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.NOT_FOUND.value

        result = json_presenter.get_invalid_team_response_for_delete_team()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
