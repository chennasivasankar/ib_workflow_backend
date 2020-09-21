import json
import pytest


class TestGetCompaniesPresenterImplementation:

    @pytest.fixture
    def presenter(self):
        from ib_iam.presenters.get_companies_presenter_implementation import (
            GetCompaniesPresenterImplementation
        )
        return GetCompaniesPresenterImplementation()

    @pytest.fixture
    def get_company_details_dtos(
            self, expected_user_dtos,
            expected_company_and_company_employee_ids_dto
    ):
        from ib_iam.interactors.presenter_interfaces.dtos import \
            CompanyWithEmployeeIdsAndUserDetailsDTO
        company_dtos = expected_company_and_company_employee_ids_dto[0]
        company_id_with_employee_ids_dtos = \
            expected_company_and_company_employee_ids_dto[1]
        company_details_dtos = CompanyWithEmployeeIdsAndUserDetailsDTO(
            company_dtos=company_dtos, user_dtos=expected_user_dtos,
            company_id_with_employee_ids_dtos=company_id_with_employee_ids_dtos
        )
        return company_details_dtos

    @pytest.fixture
    def expected_user_dtos(self):
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        UserProfileDTOFactory.reset_sequence(1)
        employee_ids = [
            '2bdb417e-4632-419a-8ddd-085ea272c6eb',
            '548a803c-7b48-47ba-a700-24f2ea0d1280',
            '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
            '7ee2c7b4-34c8-4d65-a83a-f87da75db24e'
        ]
        user_dtos = [
            UserProfileDTOFactory(user_id=employee_id)
            for employee_id in employee_ids
        ]
        return user_dtos

    @pytest.fixture
    def expected_company_and_company_employee_ids_dto(self, companies_data):
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
                CompanyDTOFactory(company_id=company["company_id"])
            )
            for employee_id in company["employees_ids"]:
                employee_ids.append(employee_id)
            company_id_with_employee_ids_dtos.append(
                CompanyIdWithEmployeeIdsDTOFactory(
                    company_id=company["company_id"], employee_ids=employee_ids
                )
            )
        return company_dtos, company_id_with_employee_ids_dtos

    @pytest.fixture
    def companies_data(self):
        companies = [
            {
                "company_id": "f2c02d98-f311-4ab2-8673-3daa00757002",
                "employees_ids": [
                    '2bdb417e-4632-419a-8ddd-085ea272c6eb',
                    '548a803c-7b48-47ba-a700-24f2ea0d1280',
                    '4b8fb6eb-fa7d-47c1-8726-cd917901104e'
                ]
            },
            {
                "company_id": "aa66c40f-6d93-484a-b418-984716514c7b",
                "employees_ids": [
                    '2bdb417e-4632-419a-8ddd-085ea272c6eb',
                    '7ee2c7b4-34c8-4d65-a83a-f87da75db24e'
                ]
            }
        ]
        return companies

    def test_it_returns_user_has_no_access_for_get_companies_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.constants.exception_messages import \
            USER_HAS_NO_ACCESS_FOR_GET_COMPANIES
        expected_response = USER_HAS_NO_ACCESS_FOR_GET_COMPANIES[0]
        expected_res_status = USER_HAS_NO_ACCESS_FOR_GET_COMPANIES[1]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.UNAUTHORIZED.value

        # Act
        result = presenter.response_for_user_has_no_access_exception()

        # Assert
        response_dict = json.loads(result.content)
        actual_response = response_dict["response"]
        actual_res_status = response_dict["res_status"]
        actual_http_status_code = response_dict["http_status_code"]

        assert actual_response == expected_response
        assert actual_res_status == expected_res_status
        assert expected_http_status_code == actual_http_status_code

    def test_given_valid_company_with_employee_details_dto_returns_http_response(
            self, get_company_details_dtos, snapshot, presenter
    ):
        # Act
        http_response = presenter.get_response_for_get_companies(
            company_details_dtos=get_company_details_dtos)

        # Assert
        response = json.loads(http_response.content)
        snapshot.assert_match(response, "response")

    def test_given_zero_companies_exists_returns_http_response(
            self, presenter
    ):
        # Arrange
        from ib_iam.interactors.presenter_interfaces.dtos import \
            CompanyWithEmployeeIdsAndUserDetailsDTO
        company_details_dtos = CompanyWithEmployeeIdsAndUserDetailsDTO(
            company_dtos=[], company_id_with_employee_ids_dtos=[], user_dtos=[]
        )

        # Act
        http_response = presenter.get_response_for_get_companies(
            company_details_dtos=company_details_dtos
        )

        # Assert
        response = json.loads(http_response.content)
        assert response == {'companies': []}
