import pytest
from mock import create_autospec, Mock

from ib_iam.exceptions import UserHasNoAccess
from ib_iam.interactors.get_companies import GetCompaniesInteractor
from ib_iam.interactors.presenter_interfaces.get_companies_presenter_interface import GetCompaniesPresenterInterface, \
    CompanyDetailsWithEmployeesCountDTO
from ib_iam.interactors.storage_interfaces.company_storage_interface import CompanyStorageInterface


@pytest.fixture
def expected_company_dtos():
    from ib_iam.tests.factories.storage_dtos import CompanyDTOFactory
    CompanyDTOFactory.reset_sequence(1, force=True)
    company_dtos = [
        CompanyDTOFactory(company_id=str(i)) for i in range(1, 3)
    ]
    return company_dtos


@pytest.fixture
def expected_company_with_employees_count_dtos():
    from ib_iam.tests.factories.storage_dtos import CompanyWithEmployeesCountDTOFactory
    CompanyWithEmployeesCountDTOFactory.reset_sequence(1)
    expected_company_with_employees_count_dtos = [
        CompanyWithEmployeesCountDTOFactory(company_id=str(i)) for i in range(1, 3)
    ]
    return expected_company_with_employees_count_dtos


class TestGetCompaniesInteractor:
    def test_if_user_is_not_admin_returns_user_has_no_access_response(self):
        storage = create_autospec(CompanyStorageInterface)
        presenter = create_autospec(GetCompaniesPresenterInterface)
        interactor = GetCompaniesInteractor(storage=storage)
        user_id = "1"
        storage.validate_is_user_admin.side_effect = UserHasNoAccess
        presenter.get_user_has_no_access_response_for_get_companies.return_value = Mock()

        interactor.get_companies_wrapper(user_id=user_id, presenter=presenter)

        storage.validate_is_user_admin.assert_called_once_with(user_id=user_id)
        presenter.get_user_has_no_access_response_for_get_companies \
            .assert_called_once()

    def test_if_user_is_admin_it_returns_companies_details_response(
            self,
            expected_company_dtos,
            expected_company_with_employees_count_dtos
    ):
        storage = create_autospec(CompanyStorageInterface)
        presenter = create_autospec(GetCompaniesPresenterInterface)
        interactor = GetCompaniesInteractor(storage=storage)
        user_id = "1"
        company_ids = ["1", "2"]
        storage.get_company_dtos.return_value = expected_company_dtos
        storage.get_company_with_employees_count_dtos \
            .return_value = expected_company_with_employees_count_dtos
        company_details_dto = CompanyDetailsWithEmployeesCountDTO(
            company_dtos=expected_company_dtos,
            company_with_employees_count_dtos=expected_company_with_employees_count_dtos
        )
        presenter.get_response_for_get_companies.return_value = Mock()

        interactor.get_companies_wrapper(user_id=user_id, presenter=presenter)

        storage.get_company_dtos.assert_called_once()
        storage.get_company_with_employees_count_dtos.assert_called_once_with(
            company_ids=company_ids
        )
        presenter.get_response_for_get_companies.assert_called_once_with(
            company_details_dtos=company_details_dto
        )
