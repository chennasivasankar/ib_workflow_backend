import json
import pytest
from ib_iam.presenters.get_companies_presenter_implementation import (
    GetCompaniesPresenterImplementation
)


class TestGetResponseForGetCompanies:
    def test_given_valid_company_with_employee_details_dto_returns_http_response(
            self, get_company_details_dtos, snapshot
    ):
        json_presenter = GetCompaniesPresenterImplementation()

        http_response = json_presenter.get_response_for_get_companies(
            company_details_dtos=get_company_details_dtos)

        response = json.loads(http_response.content)

        snapshot.assert_match(response, "response")

    def test_given_zero_companies_exists_returns_http_response(self):
        from ib_iam.interactors.presenter_interfaces \
            .get_companies_presenter_interface import \
            CompanyWithEmployeesDetailsDTO

        json_presenter = GetCompaniesPresenterImplementation()
        http_response = json_presenter.get_response_for_get_companies(
            company_details_dtos=CompanyWithEmployeesDetailsDTO(
                company_dtos=[],
                company_id_with_employee_ids_dtos=[],
                employee_dtos=[])
        )

        response = json.loads(http_response.content)
        assert response == {'companies': []}


@pytest.fixture
def get_company_details_dtos(
        expected_employee_dtos,
        expected_comapny_and_company_employee_ids_dto):
    from ib_iam.interactors.presenter_interfaces \
        .get_companies_presenter_interface import \
        CompanyWithEmployeesDetailsDTO

    company_dtos = expected_comapny_and_company_employee_ids_dto[0]
    company_id_with_employee_ids_dtos = \
        expected_comapny_and_company_employee_ids_dto[1]
    employee_dtos = expected_employee_dtos
    company_details_dtos = CompanyWithEmployeesDetailsDTO(
        company_dtos=company_dtos,
        company_id_with_employee_ids_dtos=company_id_with_employee_ids_dtos,
        employee_dtos=employee_dtos
    )
    return company_details_dtos


@pytest.fixture
def expected_employee_dtos():
    from ib_iam.tests.factories.storage_dtos import EmployeeDTOFactory
    EmployeeDTOFactory.reset_sequence(1)
    employee_ids = [
        '2bdb417e-4632-419a-8ddd-085ea272c6eb',
        '548a803c-7b48-47ba-a700-24f2ea0d1280',
        '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
        '7ee2c7b4-34c8-4d65-a83a-f87da75db24e']
    employee_dtos = [EmployeeDTOFactory(employee_id=employee_id)
                     for employee_id in employee_ids]
    return employee_dtos


@pytest.fixture
def expected_comapny_and_company_employee_ids_dto(companies_data):
    from ib_iam.tests.factories.storage_dtos import CompanyDTOFactory, \
        CompanyIdWithEmployeeIdsDTOFactory
    CompanyDTOFactory.reset_sequence(1, force=True)
    CompanyIdWithEmployeeIdsDTOFactory.reset_sequence(1)
    companies = companies_data
    company_dtos = []
    company_id_with_employee_ids_dtos = []
    for company in companies:
        employee_ids = []
        company_dtos.append(
            CompanyDTOFactory(company_id=company["company_id"]))
        for employee_id in company["employees_ids"]:
            employee_ids.append(employee_id)
        company_id_with_employee_ids_dtos.append(
            CompanyIdWithEmployeeIdsDTOFactory(
                company_id=company["company_id"],
                employee_ids=employee_ids)
        )
    return company_dtos, company_id_with_employee_ids_dtos


@pytest.fixture
def companies_data():
    companies = [
        {
            "company_id": "f2c02d98-f311-4ab2-8673-3daa00757002",
            "employees_ids": ['2bdb417e-4632-419a-8ddd-085ea272c6eb',
                              '548a803c-7b48-47ba-a700-24f2ea0d1280',
                              '4b8fb6eb-fa7d-47c1-8726-cd917901104e']
        },
        {
            "company_id": "aa66c40f-6d93-484a-b418-984716514c7b",
            "employees_ids": ['2bdb417e-4632-419a-8ddd-085ea272c6eb',
                              '7ee2c7b4-34c8-4d65-a83a-f87da75db24e']
        }
    ]
    return companies
