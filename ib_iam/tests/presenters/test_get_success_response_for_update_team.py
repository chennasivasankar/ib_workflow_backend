from ib_iam.presenters.update_team_presenter_implementation import (
    UpdateTeamPresenterImplementation
)


class TestGetSuccessResponseForUpdateTeam:
    def test_when_it_is_called_it_returns_empty_dict_http_response(self):
        json_presenter = UpdateTeamPresenterImplementation()
        import json
        expected_response = {}

        result = json_presenter.get_success_response_for_update_team()

        actual_response = json.loads(result.content)
        assert actual_response == expected_response
