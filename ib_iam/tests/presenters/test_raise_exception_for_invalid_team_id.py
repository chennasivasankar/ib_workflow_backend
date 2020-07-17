from ib_iam.presenters.team_presenter_implementation import TeamPresenterImplementation
from ib_iam.constants.exception_messages import INVALID_TEAM_ID


class TestRaiseExceptionForInvalidTeamId:
    def test_whether_it_returns_error_object(self, snapshot):
        json_presenter = TeamPresenterImplementation()
        import json
        expected_response = INVALID_TEAM_ID[0]
        expected_res_status = INVALID_TEAM_ID[1]
        expected_http_status_code = 404

        result = json_presenter.raise_exception_for_invalid_team_id()
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code
