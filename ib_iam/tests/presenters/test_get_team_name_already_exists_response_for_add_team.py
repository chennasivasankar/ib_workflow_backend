from ib_iam.exceptions.custom_exceptions import TeamNameAlreadyExists
from ib_iam.presenters.team_presenter_implementation import (
    TeamPresenterImplementation
)
from ib_iam.constants.exception_messages import (
    TEAM_NAME_ALREADY_EXISTS_FOR_ADD_TEAM
)


class TestRaiseExceptionIfTeamNameAlreadyExistsForAddTeam:
    def test_whether_it_returns_team_name_already_exists_http_response(self):
        json_presenter = TeamPresenterImplementation()
        team_name = "team_name1"
        import json
        expected_response = TEAM_NAME_ALREADY_EXISTS_FOR_ADD_TEAM[0] % team_name
        expected_res_status = TEAM_NAME_ALREADY_EXISTS_FOR_ADD_TEAM[1]
        expected_http_status_code = 400

        result = \
            json_presenter.get_team_name_already_exists_response_for_add_team(
                exception=TeamNameAlreadyExists(team_name=team_name)
            )
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
