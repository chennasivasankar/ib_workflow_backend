from ib_iam.presenters.update_team_presenter_implementation import (
    UpdateTeamPresenterImplementation
)
from ib_iam.constants.exception_messages import INVALID_USERS_FOR_UPDATE_TEAM


class TestRaiseExceptionForInvalidMembers:
    def test_when_it_is_called_it_returns_http_response(self):
        json_presenter = UpdateTeamPresenterImplementation()
        import json
        expected_response = INVALID_USERS_FOR_UPDATE_TEAM[0]
        expected_res_status = INVALID_USERS_FOR_UPDATE_TEAM[1]
        expected_http_status_code = 404

        result = json_presenter.get_invalid_users_response_for_update_team()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
