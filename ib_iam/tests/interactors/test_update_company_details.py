from mock import create_autospec, Mock
from ib_iam.interactors.presenter_interfaces \
    .update_company_presenter_interface import UpdateCompanyPresenterInterface
from ib_iam.interactors.storage_interfaces .company_storage_interface import \
    CompanyStorageInterface
from ib_iam.interactors.company_interactor import CompanyInteractor
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface
from ib_iam.tests.factories.storage_dtos import CompanyDTOFactory
from ib_iam.tests.factories.storage_dtos import \
    CompanyWithCompanyIdAndUserIdsDTOFactory


class TestUpdateCompanyDetails:

    # TODO: write repeated lines in a fixtures.
    def test_if_user_not_admin_returns_unauthorized_exception_response(self):
        company_storage = create_autospec(CompanyStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UpdateCompanyPresenterInterface)
        interactor = CompanyInteractor(company_storage=company_storage,
                                       user_storage=user_storage)
        user_id = "1"
        company_with_company_id_and_user_ids_dto = \
            CompanyWithCompanyIdAndUserIdsDTOFactory(company_id="1")
        user_storage.is_user_admin.return_value = False
        presenter.get_user_has_no_access_response_for_update_company \
            .side_effect = Mock()

        interactor.update_company_details_wrapper(
            user_id=user_id,
            company_with_company_id_and_user_ids_dto=company_with_company_id_and_user_ids_dto,
            presenter=presenter)

        user_storage.is_user_admin.assert_called_once_with(user_id=user_id)
        presenter.get_user_has_no_access_response_for_update_company \
                 .assert_called_once()

    def test_if_invalid_company_id_raises_not_found_exception_response(self):
        from ib_iam.exceptions.custom_exceptions import InvalidCompanyId
        company_storage = create_autospec(CompanyStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UpdateCompanyPresenterInterface)
        interactor = CompanyInteractor(company_storage=company_storage,
                                       user_storage=user_storage)
        user_id = "1"
        company_id = "2"
        company_with_company_id_and_user_ids_dto = \
            CompanyWithCompanyIdAndUserIdsDTOFactory(company_id="2")
        company_storage.validate_is_company_exists.side_effect = \
            InvalidCompanyId
        presenter.get_invalid_company_response_for_update_company \
            .side_effect = Mock()

        interactor.update_company_details_wrapper(
            user_id=user_id,
            company_with_company_id_and_user_ids_dto=company_with_company_id_and_user_ids_dto,
            presenter=presenter)

        company_storage.validate_is_company_exists \
            .assert_called_once_with(company_id=company_id)
        presenter.get_invalid_company_response_for_update_company.assert_called_once()

    def test_given_duplicate_users_returns_duplicate_users_response(self):
        company_storage = create_autospec(CompanyStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UpdateCompanyPresenterInterface)
        interactor = CompanyInteractor(company_storage=company_storage,
                                       user_storage=user_storage)
        user_id = "1"
        user_ids = ["2", "2", "3", "1"]
        expected_user_ids_from_exception = ["2"]
        company_with_company_id_and_user_ids_dto = \
            CompanyWithCompanyIdAndUserIdsDTOFactory(company_id="3", user_ids=user_ids)
        company_storage.validate_is_company_exists.return_value = None
        presenter.get_duplicate_users_response_for_update_company \
            .return_value = Mock()

        interactor.update_company_details_wrapper(
            user_id=user_id,
            company_with_company_id_and_user_ids_dto=company_with_company_id_and_user_ids_dto,
            presenter=presenter)

        call_args = \
            presenter.get_duplicate_users_response_for_update_company.call_args
        error_obj = call_args[0][0]
        actual_user_ids_from_exception = error_obj.user_ids
        assert actual_user_ids_from_exception == \
               expected_user_ids_from_exception

    def test_given_invalid_users_returns_invalid_users_response(self):
        company_storage = create_autospec(CompanyStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UpdateCompanyPresenterInterface)
        interactor = CompanyInteractor(company_storage=company_storage,
                                       user_storage=user_storage)
        user_id = "1"
        user_ids = ["2", "3", "1"]
        valid_user_ids = ["2", "3"]
        expected_user_ids_from_exception = ["1"]
        company_with_company_id_and_user_ids_dto = \
            CompanyWithCompanyIdAndUserIdsDTOFactory(company_id="3", user_ids=user_ids)
        company_storage.validate_is_company_exists.return_value = None
        user_storage.get_valid_user_ids_among_the_given_user_ids \
               .return_value = valid_user_ids
        presenter.get_invalid_users_response_for_update_company \
            .return_value = Mock()

        interactor.update_company_details_wrapper(
            user_id=user_id,
            company_with_company_id_and_user_ids_dto=company_with_company_id_and_user_ids_dto,
            presenter=presenter)

        user_storage.get_valid_user_ids_among_the_given_user_ids \
               .assert_called_once_with(user_ids=user_ids)
        call_args = \
            presenter.get_invalid_users_response_for_update_company.call_args
        error_obj = call_args[0][0]
        actual_user_ids_from_exception = error_obj.user_ids
        assert actual_user_ids_from_exception == \
               expected_user_ids_from_exception

    def test_if_company_name_already_exists_raises_bad_request_exception_response(
            self):
        company_storage = create_autospec(CompanyStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UpdateCompanyPresenterInterface)
        interactor = CompanyInteractor(company_storage=company_storage,
                                       user_storage=user_storage)
        user_id = "1"
        company_name = "company4"
        expected_company_name_from_error = company_name
        user_ids = ["2", "3", "1"]
        company_with_company_id_and_user_ids_dto = CompanyWithCompanyIdAndUserIdsDTOFactory(
                company_id="3", name=company_name, user_ids=user_ids)
        user_storage.get_valid_user_ids_among_the_given_user_ids \
            .return_value = user_ids
        company_storage.get_company_id_if_company_name_already_exists \
            .return_value = "2"
        presenter.get_company_name_already_exists_response_for_update_company \
                 .side_effect = Mock()

        interactor.update_company_details_wrapper(
            user_id=user_id,
            company_with_company_id_and_user_ids_dto=company_with_company_id_and_user_ids_dto,
            presenter=presenter)

        company_storage.get_company_id_if_company_name_already_exists \
            .assert_called_once_with(name=company_name)
        call_args = presenter \
            .get_company_name_already_exists_response_for_update_company.call_args
        error_obj = call_args[0][0]
        actual_company_name_from_error = error_obj.company_name
        assert actual_company_name_from_error == expected_company_name_from_error

    def test_company_requested_for_its_own_name_then_updation_will_be_done(
            self):
        company_storage = create_autospec(CompanyStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UpdateCompanyPresenterInterface)
        interactor = CompanyInteractor(company_storage=company_storage,
                                       user_storage=user_storage)
        user_id = "1"
        user_ids = ["2", "3", "1"]
        company_id = "3"
        CompanyWithCompanyIdAndUserIdsDTOFactory.reset_sequence(1, force=True)
        company_with_company_id_and_user_ids_dto = CompanyWithCompanyIdAndUserIdsDTOFactory(
                company_id=company_id, user_ids=user_ids)
        CompanyDTOFactory.reset_sequence(1, force=True)
        company_dto = CompanyDTOFactory(company_id=company_id)
        user_storage.get_valid_user_ids_among_the_given_user_ids \
            .return_value = user_ids
        company_storage.get_company_id_if_company_name_already_exists \
            .return_value = company_id
        presenter.get_success_response_for_update_company.return_value = Mock()

        interactor.update_company_details_wrapper(
            user_id=user_id,
            company_with_company_id_and_user_ids_dto=company_with_company_id_and_user_ids_dto,
            presenter=presenter)

        company_storage.update_company_details.assert_called_once_with(
            company_dto=company_dto)
        company_storage.delete_all_existing_employees_of_company \
            .assert_called_once_with(company_id=company_id)
        company_storage.add_users_to_company.assert_called_once_with(
            user_ids=user_ids, company_id=company_id)
        presenter.get_success_response_for_update_company.assert_called_once()

    def test_given_company_name_not_exists_then_updation_will_be_done(
                self):
        company_storage = create_autospec(CompanyStorageInterface)
        user_storage = create_autospec(UserStorageInterface)
        presenter = create_autospec(UpdateCompanyPresenterInterface)
        interactor = CompanyInteractor(company_storage=company_storage,
                                       user_storage=user_storage)
        user_ids = ["2", "3", "1"]
        company_id = "3"
        CompanyWithCompanyIdAndUserIdsDTOFactory.reset_sequence(1, force=True)
        company_with_company_id_and_user_ids_dto = CompanyWithCompanyIdAndUserIdsDTOFactory(
            company_id=company_id, user_ids=user_ids)
        CompanyDTOFactory.reset_sequence(1, force=True)
        company_dto = CompanyDTOFactory(company_id=company_id)
        user_storage.get_valid_user_ids_among_the_given_user_ids \
            .return_value = user_ids
        company_storage.get_company_id_if_company_name_already_exists\
            .return_value = None
        presenter.get_success_response_for_update_company.return_value = Mock()

        interactor.update_company_details_wrapper(
            user_id="1",
            company_with_company_id_and_user_ids_dto=company_with_company_id_and_user_ids_dto,
            presenter=presenter)

        company_storage.update_company_details.assert_called_once_with(
            company_dto=company_dto)
        company_storage.delete_all_existing_employees_of_company \
            .assert_called_once_with(company_id=company_id)
        company_storage.add_users_to_company.assert_called_once_with(
            user_ids=user_ids, company_id=company_id)
        presenter.get_success_response_for_update_company.assert_called_once()
