from mock import create_autospec, Mock
from ib_iam.interactors.presenter_interfaces.update_company_presenter_interface import (
    UpdateCompanyPresenterInterface
)
from ib_iam.interactors.storage_interfaces.company_storage_interface import CompanyStorageInterface
from ib_iam.interactors.company_interactor import CompanyInteractor
from ib_iam.interactors.storage_interfaces.dtos import CompanyDTO
from ib_iam.tests.factories.storage_dtos import CompanyDTOFactory
from ib_iam.tests.factories.storage_dtos import CompanyWithUserIdsDTOFactory


class TestUpdateCompanyDetails:

    def test_if_user_not_admin_returns_unauthorized_exception_response(self):
        from ib_iam.exceptions.custom_exceptions import UserHasNoAccess
        storage = create_autospec(CompanyStorageInterface)
        presenter = create_autospec(UpdateCompanyPresenterInterface)
        interactor = CompanyInteractor(storage=storage)
        user_id = "1"
        company_with_user_ids_dto = \
            CompanyWithUserIdsDTOFactory(company_id="1")
        storage.validate_is_user_admin.side_effect = UserHasNoAccess
        presenter.get_user_has_no_access_response_for_update_company \
            .side_effect = Mock()

        interactor.update_company_details_wrapper(
            user_id=user_id,
            company_with_user_ids_dto=company_with_user_ids_dto,
            presenter=presenter)

        storage.validate_is_user_admin.assert_called_once_with(user_id=user_id)
        presenter.get_user_has_no_access_response_for_update_company \
                 .assert_called_once()

    def test_if_invalid_company_id_raises_not_found_exception_response(self):
        from ib_iam.exceptions.custom_exceptions import InvalidCompany
        storage = create_autospec(CompanyStorageInterface)
        presenter = create_autospec(UpdateCompanyPresenterInterface)
        interactor = CompanyInteractor(storage=storage)
        user_id = "1"
        company_id = "2"
        company_with_user_ids_dto = \
            CompanyWithUserIdsDTOFactory(company_id="2")
        storage.validate_is_company_exists.side_effect = InvalidCompany
        presenter.get_invalid_company_response_for_update_company \
            .side_effect = Mock()

        interactor.update_company_details_wrapper(
            user_id=user_id,
            company_with_user_ids_dto=company_with_user_ids_dto,
            presenter=presenter)

        storage.validate_is_company_exists \
            .assert_called_once_with(company_id=company_id)
        presenter.get_invalid_company_response_for_update_company.assert_called_once()

    def test_given_duplicate_users_returns_duplicate_users_response(self):
        storage = create_autospec(CompanyStorageInterface)
        presenter = create_autospec(UpdateCompanyPresenterInterface)
        interactor = CompanyInteractor(storage=storage)
        user_id = "1"
        company_name = "company1"
        user_ids = ["2", "2", "3", "1"]
        company_with_user_ids_dto = \
            CompanyWithUserIdsDTOFactory(company_id="3", user_ids=user_ids)
        storage.validate_is_company_exists.return_value = None
        presenter.get_duplicate_users_response_for_update_company \
            .return_value = Mock()

        interactor.update_company_details_wrapper(
            user_id=user_id,
            company_with_user_ids_dto=company_with_user_ids_dto,
            presenter=presenter)

        presenter.get_duplicate_users_response_for_update_company \
                 .assert_called_once()

    def test_given_invalid_users_returns_invalid_users_response(self):
        storage = create_autospec(CompanyStorageInterface)
        presenter = create_autospec(UpdateCompanyPresenterInterface)
        interactor = CompanyInteractor(storage=storage)
        user_id = "1"
        company_name = "company1"
        user_ids = ["2", "3", "1"]
        valid_user_ids = ["2", "3"]
        company_with_user_ids_dto = \
            CompanyWithUserIdsDTOFactory(company_id="3", user_ids=user_ids)
        storage.validate_is_company_exists.return_value = None
        storage.get_valid_user_ids_among_the_given_user_ids \
               .return_value = valid_user_ids
        presenter.get_invalid_users_response_for_update_company \
            .return_value = Mock()

        interactor.update_company_details_wrapper(
            user_id=user_id,
            company_with_user_ids_dto=company_with_user_ids_dto,
            presenter=presenter)

        storage.get_valid_user_ids_among_the_given_user_ids \
               .assert_called_once_with(user_ids=user_ids)
        presenter.get_invalid_users_response_for_update_company \
                 .assert_called_once()

    def test_if_company_name_already_exists_raises_bad_request_exception_response(
            self):
        storage = create_autospec(CompanyStorageInterface)
        presenter = create_autospec(UpdateCompanyPresenterInterface)
        interactor = CompanyInteractor(storage=storage)
        user_id = "1"
        company_name = "company4"
        expected_company_name_from_error = company_name
        user_ids = ["2", "3", "1"]
        company_with_user_ids_dto = CompanyWithUserIdsDTOFactory(
                company_id="3", name=company_name, user_ids=user_ids)
        storage.get_valid_user_ids_among_the_given_user_ids \
            .return_value = user_ids
        storage.get_company_id_if_company_name_already_exists.return_value = "2"
        presenter.get_company_name_already_exists_response_for_update_company \
                 .side_effect = Mock()

        interactor.update_company_details_wrapper(
            user_id=user_id,
            company_with_user_ids_dto=company_with_user_ids_dto,
            presenter=presenter)

        storage.get_company_id_if_company_name_already_exists \
            .assert_called_once_with(name=company_name)
        call_obj = presenter \
            .get_company_name_already_exists_response_for_update_company.call_args
        error_obj = call_obj.args[0]
        actual_company_name_from_error = error_obj.company_name
        assert actual_company_name_from_error == expected_company_name_from_error

    def test_company_requested_for_its_own_name_then_updation_will_be_done(
            self):
        storage = create_autospec(CompanyStorageInterface)
        presenter = create_autospec(UpdateCompanyPresenterInterface)
        interactor = CompanyInteractor(storage=storage)
        user_id = "1"
        user_ids = ["2", "3", "1"]
        company_id = "3"
        CompanyWithUserIdsDTOFactory.reset_sequence(1, force=True)
        company_with_user_ids_dto = CompanyWithUserIdsDTOFactory(
                company_id=company_id, user_ids=user_ids)
        CompanyDTOFactory.reset_sequence(1, force=True)
        company_dto = CompanyDTOFactory(company_id=company_id)
        storage.get_valid_user_ids_among_the_given_user_ids \
            .return_value = user_ids
        storage.get_company_id_if_company_name_already_exists \
            .return_value = company_id
        presenter.get_success_response_for_update_company.return_value = Mock()

        interactor.update_company_details_wrapper(
            user_id=user_id,
            company_with_user_ids_dto=company_with_user_ids_dto,
            presenter=presenter)

        storage.update_company_details.assert_called_once_with(
            company_dto=company_dto)
        storage.delete_all_existing_employees_of_company \
            .assert_called_once_with(company_id=company_id)
        storage.add_users_to_company.assert_called_once_with(
            user_ids=user_ids, company_id=company_id)
        presenter.get_success_response_for_update_company.assert_called_once()

    def test_given_company_name_not_exists_then_updation_will_be_done(
                self):
        storage = create_autospec(CompanyStorageInterface)
        presenter = create_autospec(UpdateCompanyPresenterInterface)
        interactor = CompanyInteractor(storage=storage)
        user_ids = ["2", "3", "1"]
        company_id = "3"
        CompanyWithUserIdsDTOFactory.reset_sequence(1, force=True)
        company_with_user_ids_dto = CompanyWithUserIdsDTOFactory(
            company_id=company_id, user_ids=user_ids)
        CompanyDTOFactory.reset_sequence(1, force=True)
        company_dto = CompanyDTOFactory(company_id=company_id)
        storage.get_valid_user_ids_among_the_given_user_ids \
            .return_value = user_ids
        storage.get_company_id_if_company_name_already_exists.return_value = None
        presenter.get_success_response_for_update_company.return_value = Mock()

        interactor.update_company_details_wrapper(
            user_id="1",
            company_with_user_ids_dto=company_with_user_ids_dto,
            presenter=presenter)

        storage.update_company_details.assert_called_once_with(
            company_dto=company_dto)
        storage.delete_all_existing_employees_of_company \
            .assert_called_once_with(company_id=company_id)
        storage.add_users_to_company.assert_called_once_with(
            user_ids=user_ids, company_id=company_id)
        presenter.get_success_response_for_update_company.assert_called_once()
