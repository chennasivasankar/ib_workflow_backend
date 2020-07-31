import json
from ib_iam.presenters.team_presenter_implementation import (
    TeamPresenterImplementation
)


class TestGetResponseForGetListOfTeams:
    def test_given_valid_team_with_members_details_dto_returns_http_response(
            self, snapshot, get_list_of_team_dtos
    ):
        json_presenter = TeamPresenterImplementation()

        http_response = json_presenter.get_response_for_get_list_of_teams(
            team_details_dtos=get_list_of_team_dtos
        )

        response = json.loads(http_response.content)

        snapshot.assert_match(response, "response")

    def test_given_zero_teams_exists_returns_http_response(self):
        json_presenter = TeamPresenterImplementation()
        from ib_iam.interactors.presenter_interfaces.dtos import \
            TeamWithUsersDetailsDTO

        http_response = json_presenter.get_response_for_get_list_of_teams(
            team_details_dtos=TeamWithUsersDetailsDTO(
                total_teams_count=0,
                team_dtos=[],
                team_user_ids_dtos=[],
                user_dtos=[]
            )
        )

        response = json.loads(http_response.content)
        assert response == {'teams': [], 'total_teams_count': 0}
