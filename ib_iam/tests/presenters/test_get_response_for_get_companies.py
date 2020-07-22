import json
from ib_iam.presenters.get_companies_presenter_implementation import (
    GetCompaniesPresenterImplementation
)


class TestGetResponseForGetListOfTeams:
    def test_given_valid_team_with_members_details_dto_returns_http_response(
            self, get_company_details_dtos, snapshot
    ):
        json_presenter = GetCompaniesPresenterImplementation()

        http_response = json_presenter.get_response_for_get_companies(
            company_details_dtos=get_company_details_dtos
        )

        response = json.loads(http_response.content)

        snapshot.assert_match(response, "response")

    def test_given_zero_teams_exists_returns_http_response(self):
        from ib_iam.interactors.presenter_interfaces.get_companies_presenter_interface import \
            CompanyDetailsWithEmployeesCountDTO

        json_presenter = GetCompaniesPresenterImplementation()
        http_response = json_presenter.get_response_for_get_companies(
            company_details_dtos=CompanyDetailsWithEmployeesCountDTO(
                company_dtos=[],
                company_with_employees_count_dtos=[]
            )
        )

        response = json.loads(http_response.content)
        assert response == {'companies': []}
