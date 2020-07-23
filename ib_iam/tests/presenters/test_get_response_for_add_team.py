import json
from ib_iam.presenters.team_presenter_implementation import (
    TeamPresenterImplementation
)


class TestGetResponseForAddTeam:
    def test_given_team_id_it_return_http_response_with_team_id(self):
        json_presenter = TeamPresenterImplementation()
        team_id = "f2c02d98-f311-4ab2-8673-3daa00757002"
        expected_json_response = {"team_id": team_id}

        http_response = json_presenter.get_response_for_add_team(
            team_id=team_id
        )

        actual_json_response = json.loads(http_response.content)
        assert actual_json_response == expected_json_response
