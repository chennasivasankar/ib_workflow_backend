import pytest
from ib_iam.presenters.team_presenter_implementation import TeamPresenterImplementation


class TestGetResponseForGetListOfTeams:
    def test_whether_it_returns_list_of_team_details_dict(
            self, snapshot, get_list_of_team_dtos
    ):
        json_presenter = TeamPresenterImplementation()

        http_response = json_presenter.get_response_for_get_list_of_teams(
            team_details_dtos=get_list_of_team_dtos
        )

        import json
        response = json.loads(http_response.content)

        snapshot.assert_match(response, "list_of_teams_details_dict")

    def test_whether_it_returns_list_of_team_details(
            self,
    ):
        json_presenter = TeamPresenterImplementation()
        from ib_iam.interactors.presenter_interfaces.dtos import TeamWithMembersDetailsDTO

        http_response = json_presenter.get_response_for_get_list_of_teams(
            team_details_dtos=TeamWithMembersDetailsDTO(
                team_dtos=[],
                team_member_ids_dtos=[],
                member_dtos=[]
            )
        )

        import json
        response = json.loads(http_response.content)
        assert response == []
