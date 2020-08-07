import json
from ib_iam.presenters.delete_team_presenter_implementation import (
    DeleteTeamPresenterImplementation
)


class TestGetSuccessResponseForDeleteTeam:
    def test_when_it_is_called_it_returns_empty_dict_http_response(self):
        json_presenter = DeleteTeamPresenterImplementation()
        expected_response = {}

        result = json_presenter.get_success_response_for_delete_team()

        actual_response = json.loads(result.content)
        assert actual_response == expected_response
