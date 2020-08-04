from mock import create_autospec, Mock
from ib_iam.interactors.presenter_interfaces \
    .delete_company_presenter_interface import DeleteCompanyPresenterInterface
from ib_iam.interactors.storage_interfaces.company_storage_interface import (
    CompanyStorageInterface
)
from ib_iam.interactors.company_interactor import CompanyInteractor


class TestDeleteCompany:

    def test_if_user_not_admin_raises_unauthorized_exception(self):
        from ib_iam.exceptions.custom_exceptions import UserHasNoAccess
        storage = create_autospec(CompanyStorageInterface)
        presenter = create_autospec(DeleteCompanyPresenterInterface)
        interactor = CompanyInteractor(storage=storage)
        user_id = "1"
        storage.validate_is_user_admin.side_effect = UserHasNoAccess
        presenter.get_user_has_no_access_response_for_delete_company \
                 .side_effect = Mock()

        interactor.delete_company_wrapper(
            user_id=user_id, company_id="1", presenter=presenter
        )

        storage.validate_is_user_admin.assert_called_once_with(user_id=user_id)
        presenter.get_user_has_no_access_response_for_delete_company \
                 .assert_called_once()

    def test_if_invalid_company_id_raises_not_found_exception(self):
        from ib_iam.exceptions.custom_exceptions import InvalidCompanyId
        storage = create_autospec(CompanyStorageInterface)
        presenter = create_autospec(DeleteCompanyPresenterInterface)
        interactor = CompanyInteractor(storage=storage)
        user_id = "1"
        company_id = "1"
        storage.validate_is_company_exists.side_effect = InvalidCompanyId
        presenter.get_invalid_company_response_for_delete_company \
                 .side_effect = Mock()

        interactor.delete_company_wrapper(
            user_id=user_id, company_id=company_id, presenter=presenter
        )

        storage.validate_is_company_exists \
            .assert_called_once_with(company_id=company_id)
        presenter.get_invalid_company_response_for_delete_company \
                 .assert_called_once()

    def test_given_valid_details_deletion_will_happen(self):
        storage = create_autospec(CompanyStorageInterface)
        presenter = create_autospec(DeleteCompanyPresenterInterface)
        interactor = CompanyInteractor(storage=storage)
        user_id = "1"
        company_id = "1"
        presenter.get_success_response_for_delete_company.return_value = Mock()

        interactor.delete_company_wrapper(
            user_id=user_id, company_id=company_id, presenter=presenter
        )

        storage.delete_company.assert_called_once_with(
            company_id=company_id
        )
        presenter.get_success_response_for_delete_company.assert_called_once()
