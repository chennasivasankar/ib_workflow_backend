import json
import pytest
from ib_iam.presenters.get_companies_presenter_implementation import (
    GetCompaniesPresenterImplementation
)


class TestGetResponseForGetCompanies:
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


@pytest.fixture
def get_company_details_dtos():
    from ib_iam.tests.factories.storage_dtos import CompanyDTOFactory, CompanyNameLogoAndDescriptionDTOFactory
    from ib_iam.tests.factories.storage_dtos import CompanyWithEmployeesCountDTOFactory
    from ib_iam.interactors.presenter_interfaces \
        .get_companies_presenter_interface import CompanyDetailsWithEmployeesCountDTO
    company_ids = [
        "f2c02d98-f311-4ab2-8673-3daa00757003",
        "aa66c40f-6d93-484a-b418-984716514c7c",
        "c982032b-53a7-4dfa-a627-4701a5230767"
    ]
    CompanyDTOFactory.reset_sequence(1, force=True)
    company_dtos = [
        CompanyDTOFactory(company_id=company_id) for company_id in company_ids
    ]
    company_with_employees_count_dtos = [
        CompanyWithEmployeesCountDTOFactory(
            company_id=company_id,
            no_of_employees=i
        ) for company_id, i in zip(company_ids, range(3, 7, 2))
    ]

    company_details_dtos = CompanyDetailsWithEmployeesCountDTO(
        company_dtos=company_dtos,
        company_with_employees_count_dtos=company_with_employees_count_dtos
    )
    return company_details_dtos
