import pytest

from ib_iam.exceptions import DuplicateTeamName
from ib_iam.presenters.team_presenter_implementation import TeamPresenterImplementation
from ib_iam.constants.exception_messages import DUPLICATE_TEAM_NAME


class TestRaiseExceptionForDuplicateTeamName:
    def test_whether_it_returns_error_object(self, snapshot):
        json_presenter = TeamPresenterImplementation()
        team_name = "team_name1"
        import json
        expected_response = DUPLICATE_TEAM_NAME[0] % team_name
        expected_res_status = DUPLICATE_TEAM_NAME[1]
        expected_http_status_code = 400

        result = json_presenter.raise_exception_for_duplicate_team_name(
            exception=DuplicateTeamName(team_name=team_name)
        )
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
