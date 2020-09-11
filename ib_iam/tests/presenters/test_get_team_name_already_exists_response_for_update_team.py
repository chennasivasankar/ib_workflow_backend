import json
from ib_iam.exceptions.custom_exceptions import TeamNameAlreadyExists
from ib_iam.presenters.update_team_presenter_implementation import (
    UpdateTeamPresenterImplementation
)
from ib_iam.constants.exception_messages import (
    TEAM_NAME_ALREADY_EXISTS_FOR_UPDATE_TEAM
)


class TestRaiseExceptionIfTeamNameAlreadyExistsForUpdateTeam:
    def test_whether_it_returns_team_name_already_exists_http_response(self):
        json_presenter = UpdateTeamPresenterImplementation()
        team_name = "team_name1"
        expected_response = TEAM_NAME_ALREADY_EXISTS_FOR_UPDATE_TEAM[0] % team_name
        expected_res_status = TEAM_NAME_ALREADY_EXISTS_FOR_UPDATE_TEAM[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.BAD_REQUEST.value

        result = json_presenter \
            .response_for_team_name_already_exists_exception(
                err=TeamNameAlreadyExists(team_name=team_name)
            )
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
