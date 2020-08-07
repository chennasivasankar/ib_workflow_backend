from mock import create_autospec, Mock
from ib_iam.interactors.presenter_interfaces \
    .delete_company_presenter_interface import DeleteCompanyPresenterInterface
from ib_iam.interactors.storage_interfaces.company_storage_interface import (
    CompanyStorageInterface
)
from ib_iam.interactors.company_interactor import CompanyInteractor
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface


class TestDeleteCompany:

    def test_if_user_not_admin_raises_unauthorized_exception(self):
        from ib_iam.exceptions.custom_exceptions import UserHasNoAccess
        company_storage = create_autospec(CompanyStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(DeleteCompanyPresenterInterface)
        interactor = CompanyInteractor(company_storage=company_storage,
                                       user_storage=user_storage)
        user_id = "1"
        user_storage.is_user_admin.return_value = False
        presenter.get_user_has_no_access_response_for_delete_company \
                 .side_effect = Mock()

        interactor.delete_company_wrapper(
            user_id=user_id, company_id="1", presenter=presenter)

        user_storage.is_user_admin.assert_called_once_with(user_id=user_id)
        presenter.get_user_has_no_access_response_for_delete_company \
                 .assert_called_once()

    def test_if_invalid_company_id_raises_not_found_exception(self):
        from ib_iam.exceptions.custom_exceptions import InvalidCompanyId
        company_storage = create_autospec(CompanyStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(DeleteCompanyPresenterInterface)
        interactor = CompanyInteractor(company_storage=company_storage,
                                       user_storage=user_storage)
        user_id = "1"
        company_id = "1"
        company_storage.validate_is_company_exists.side_effect = \
            InvalidCompanyId
        presenter.get_invalid_company_response_for_delete_company \
                 .side_effect = Mock()

        interactor.delete_company_wrapper(
            user_id=user_id, company_id=company_id, presenter=presenter
        )

        company_storage.validate_is_company_exists \
            .assert_called_once_with(company_id=company_id)
        presenter.get_invalid_company_response_for_delete_company \
                 .assert_called_once()

    def test_given_valid_details_deletion_will_happen(self):
        company_storage = create_autospec(CompanyStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(DeleteCompanyPresenterInterface)
        interactor = CompanyInteractor(company_storage=company_storage,
                                       user_storage=user_storage)
        user_id = "1"
        company_id = "1"
        presenter.get_success_response_for_delete_company.return_value = Mock()

        interactor.delete_company_wrapper(
            user_id=user_id, company_id=company_id, presenter=presenter)

        company_storage.delete_company.assert_called_once_with(
            company_id=company_id)
        presenter.get_success_response_for_delete_company.assert_called_once()
