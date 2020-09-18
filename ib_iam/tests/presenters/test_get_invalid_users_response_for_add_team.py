import json

from ib_iam.constants.exception_messages import INVALID_USER_IDS_FOR_ADD_TEAM
from ib_iam.presenters.team_presenter_implementation import (
    TeamPresenterImplementation
)


class TestRaiseExceptionForInvalidUsersForAddTeam:
    def test_whether_it_returns_invalid_users_http_response(self):
        # Arrange
        json_presenter = TeamPresenterImplementation()
        expected_response = INVALID_USER_IDS_FOR_ADD_TEAM[0]
        expected_res_status = INVALID_USER_IDS_FOR_ADD_TEAM[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.NOT_FOUND.value

        # Act
        result = json_presenter.get_invalid_users_response_for_add_team()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]
        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
