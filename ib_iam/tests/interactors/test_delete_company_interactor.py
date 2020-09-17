import pytest
from mock import create_autospec, Mock


class TestDeleteCompany:

    @pytest.fixture
    def user_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        return create_autospec(UserStorageInterface)

    @pytest.fixture
    def company_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.company_storage_interface import \
            CompanyStorageInterface
        return create_autospec(CompanyStorageInterface)

    @pytest.fixture
    def presenter(self):
        from ib_iam.interactors.presenter_interfaces.company_presenter_interface import \
            DeleteCompanyPresenterInterface
        return create_autospec(DeleteCompanyPresenterInterface)

    @pytest.fixture
    def interactor(self, company_storage_mock, user_storage_mock):
        from ib_iam.interactors.company_interactor import CompanyInteractor
        return CompanyInteractor(
            company_storage=company_storage_mock,
            user_storage=user_storage_mock
        )

    def test_if_user_not_admin_raises_unauthorized_exception(
            self, interactor, company_storage_mock, user_storage_mock,
            presenter
    ):
        # Arrange
        user_id = "1"
        user_storage_mock.is_user_admin.return_value = False
        presenter.response_for_user_has_no_access_exception \
            .side_effect = Mock()

        # Act
        interactor.delete_company_wrapper(
            user_id=user_id, company_id="1", presenter=presenter
        )

        # Assert
        user_storage_mock.is_user_admin.assert_called_once_with(
            user_id=user_id)
        presenter.response_for_user_has_no_access_exception \
            .assert_called_once()

    def test_if_invalid_company_id_raises_not_found_exception(
            self, interactor, company_storage_mock, user_storage_mock,
            presenter
    ):
        # Arrange
        user_id = "1"
        company_id = "1"
        from ib_iam.exceptions.custom_exceptions import InvalidCompanyId
        company_storage_mock.validate_is_company_exists.side_effect = \
            InvalidCompanyId
        presenter.response_for_invalid_company_id_exception \
            .side_effect = Mock()

        # Act
        interactor.delete_company_wrapper(
            user_id=user_id, company_id=company_id, presenter=presenter
        )

        # Assert
        company_storage_mock.validate_is_company_exists \
            .assert_called_once_with(company_id=company_id)
        presenter.response_for_invalid_company_id_exception \
            .assert_called_once()

    def test_given_valid_details_deletion_will_happen(
            self, interactor, company_storage_mock, user_storage_mock,
            presenter
    ):
        # Arrange
        user_id = "1"
        company_id = "1"
        presenter.get_success_response_for_delete_company.return_value = Mock()

        # Act
        interactor.delete_company_wrapper(
            user_id=user_id, company_id=company_id, presenter=presenter
        )

        # Assert
        company_storage_mock.delete_company.assert_called_once_with(
            company_id=company_id)
        presenter.get_success_response_for_delete_company.assert_called_once()
