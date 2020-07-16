import pytest
from ib_iam.presenters.team_presenter_implementation import TeamPresenterImplementation
from ib_iam.tests.storages.conftest import team1_id


class TestGetResponseForAddTeam:
    def test_whether_it_returns_team_id(self):

        json_presenter = TeamPresenterImplementation()
        expected_json_response = {"team_id": team1_id}

        http_response = json_presenter.get_response_for_add_team(
            team_id=team1_id
        )

        import json
        actual_json_response = json.loads(http_response.content)

        assert actual_json_response == expected_json_response
