import pytest
from mock import create_autospec, Mock

from ib_iam.exceptions.custom_exceptions import UserHasNoAccess
from ib_iam.interactors.get_companies_interactor import GetCompaniesInteractor
from ib_iam.interactors.presenter_interfaces \
    .get_companies_presenter_interface import (GetCompaniesPresenterInterface,
                                               CompanyWithEmployeesDetailsDTO)
from ib_iam.interactors.storage_interfaces.company_storage_interface import \
    CompanyStorageInterface


@pytest.fixture
def expected_company_dtos():
    from ib_iam.tests.factories.storage_dtos import CompanyDTOFactory
    CompanyDTOFactory.reset_sequence(1, force=True)
    company_dtos = [CompanyDTOFactory(company_id=str(i)) for i in range(1, 3)]
    return company_dtos


@pytest.fixture
def expected_user_dtos():
    from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
    UserProfileDTOFactory.reset_sequence(1)
    user_profile_dtos = [UserProfileDTOFactory() for _ in range(3)]
    return user_profile_dtos


@pytest.fixture
def expected_company_employee_ids_dtos():
    from ib_iam.tests.factories.storage_dtos import \
        CompanyIdWithEmployeeIdsDTOFactory
    CompanyIdWithEmployeeIdsDTOFactory.reset_sequence(1)
    expected_company_id_with_employee_id_dtos = [
        CompanyIdWithEmployeeIdsDTOFactory(company_id=str(i))
        for i in range(1, 3)
    ]
    return expected_company_id_with_employee_id_dtos


@pytest.fixture
def expected_employee_dtos():
    from ib_iam.tests.factories.storage_dtos import EmployeeDTOFactory
    EmployeeDTOFactory.reset_sequence(1)
    employee_dtos = [EmployeeDTOFactory() for _ in range(1, 4)]
    return employee_dtos


class TestGetCompaniesInteractor:
    def test_if_user_is_not_admin_returns_user_has_no_access_response(self):
        storage = create_autospec(CompanyStorageInterface)
        presenter = create_autospec(GetCompaniesPresenterInterface)
        interactor = GetCompaniesInteractor(storage=storage)
        user_id = "1"
        storage.validate_is_user_admin.side_effect = UserHasNoAccess
        presenter.get_user_has_no_access_response_for_get_companies \
            .return_value = Mock()

        interactor.get_companies_wrapper(user_id=user_id, presenter=presenter)

        storage.validate_is_user_admin.assert_called_once_with(user_id=user_id)
        presenter.get_user_has_no_access_response_for_get_companies \
            .assert_called_once()

    def test_if_user_is_admin_it_returns_companies_details_response(
            self,
            mocker,
            expected_company_dtos,
            expected_company_employee_ids_dtos,
            expected_user_dtos,
            expected_employee_dtos,
    ):
        from ib_iam.tests.common_fixtures.adapters.user_service_mocks import (
            prepare_user_profile_dtos_mock)
        storage = create_autospec(CompanyStorageInterface)
        presenter = create_autospec(GetCompaniesPresenterInterface)
        user_id = "4"
        company_ids = ["1", "2"]
        interactor = GetCompaniesInteractor(storage=storage)
        storage.get_company_dtos.return_value = expected_company_dtos
        storage.get_company_employee_ids_dtos \
            .return_value = expected_company_employee_ids_dtos
        mock = prepare_user_profile_dtos_mock(mocker)
        mock.return_value = expected_user_dtos
        company_details_dto = CompanyWithEmployeesDetailsDTO(
            company_dtos=expected_company_dtos,
            company_id_with_employee_ids_dtos
            =expected_company_employee_ids_dtos,
            employee_dtos=expected_employee_dtos)
        presenter.get_response_for_get_companies.return_value = Mock()

        interactor.get_companies_wrapper(user_id=user_id, presenter=presenter)

        storage.get_company_dtos.assert_called_once()
        storage.get_company_employee_ids_dtos.assert_called_once_with(
            company_ids=company_ids)
        presenter.get_response_for_get_companies.assert_called_once_with(
            company_details_dtos=company_details_dto)