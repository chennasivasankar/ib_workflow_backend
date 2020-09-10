from mock import create_autospec, Mock
from ib_iam.interactors.company_interactor import CompanyInteractor
from ib_iam.interactors.presenter_interfaces \
    .add_company_presenter_interface import AddCompanyPresenterInterface
from ib_iam.interactors.storage_interfaces.dtos import \
    CompanyNameLogoAndDescriptionDTO
from ib_iam.interactors.storage_interfaces.user_storage_interface import \
    UserStorageInterface
from ib_iam.tests.factories.storage_dtos import \
    CompanyWithUserIdsDTOFactory
from ib_iam.interactors.storage_interfaces.company_storage_interface import \
    CompanyStorageInterface


class TestAddCompanyInteractor:

    # TODO: Repeated lines write in fixtures.
    def test_if_user_not_admin_returns_unauthorized_exception_response(self):
        user_storage = create_autospec(UserStorageInterface)
        company_storage = create_autospec(CompanyStorageInterface)
        presenter = create_autospec(AddCompanyPresenterInterface)
        interactor = CompanyInteractor(company_storage=company_storage,
                                       user_storage=user_storage)
        user_id = "1"
        company_with_user_ids_dto = CompanyWithUserIdsDTOFactory()
        user_storage.is_user_admin.return_value = False
        presenter.get_user_has_no_access_response_for_add_company \
            .return_value = Mock()

        interactor.add_company_wrapper(
            user_id=user_id,
            company_with_user_ids_dto=company_with_user_ids_dto,
            presenter=presenter)

        user_storage.is_user_admin \
            .assert_called_once_with(user_id=user_id)
        presenter.get_user_has_no_access_response_for_add_company \
            .assert_called_once()

    def test_given_duplicate_users_returns_duplicate_users_response(self):
        user_storage = create_autospec(UserStorageInterface)
        company_storage = create_autospec(CompanyStorageInterface)
        presenter = create_autospec(AddCompanyPresenterInterface)
        interactor = CompanyInteractor(company_storage=company_storage,
                                       user_storage=user_storage)
        user_id = "1"
        user_ids = ["2", "2", "3", "1"]
        expected_user_ids_from_exception = ["2"]
        company_with_user_ids_dto = CompanyWithUserIdsDTOFactory(
            name="company1", user_ids=user_ids)
        company_storage.get_company_id_if_company_name_already_exists\
            .return_value\
            = \
            None
        presenter.get_duplicate_users_response_for_add_company \
            .return_value = Mock()

        interactor.add_company_wrapper(
            user_id=user_id,
            company_with_user_ids_dto=company_with_user_ids_dto,
            presenter=presenter)

        call_args = \
            presenter.get_duplicate_users_response_for_add_company.call_args
        error_obj = call_args[0][0]
        actual_user_ids_from_exception = error_obj.user_ids
        assert actual_user_ids_from_exception == \
               expected_user_ids_from_exception

    def test_given_invalid_users_returns_invalid_users_response(self):
        user_storage = create_autospec(UserStorageInterface)
        company_storage = create_autospec(CompanyStorageInterface)
        presenter = create_autospec(AddCompanyPresenterInterface)
        interactor = CompanyInteractor(company_storage=company_storage,
                                       user_storage=user_storage)
        user_id = "1"
        valid_user_ids = ["2", "3"]
        invalid_user_ids = ["2", "3", "4"]
        expected_user_ids_from_exception = ["4"]
        company_with_user_ids_dto = CompanyWithUserIdsDTOFactory(
            name="company1", user_ids=invalid_user_ids)
        company_storage.get_company_id_if_company_name_already_exists\
            .return_value = None
        user_storage.get_valid_user_ids_among_the_given_user_ids \
            .return_value = valid_user_ids
        presenter.get_invalid_users_response_for_add_company.return_value = Mock()

        interactor.add_company_wrapper(
            user_id=user_id,
            company_with_user_ids_dto=company_with_user_ids_dto,
            presenter=presenter)

        user_storage.get_valid_user_ids_among_the_given_user_ids \
            .assert_called_once_with(user_ids=invalid_user_ids)
        call_args = \
            presenter.get_invalid_users_response_for_add_company.call_args
        error_obj = call_args[0][0]
        actual_user_ids_from_exception = error_obj.user_ids
        assert actual_user_ids_from_exception == \
               expected_user_ids_from_exception

    def test_company_name_exists_returns_company_name_already_exists_response(
            self):
        user_storage = create_autospec(UserStorageInterface)
        company_storage = create_autospec(CompanyStorageInterface)
        presenter = create_autospec(AddCompanyPresenterInterface)
        interactor = CompanyInteractor(company_storage=company_storage,
                                       user_storage=user_storage)
        user_id = "1"
        company_name = "company1"
        user_ids = ["1"]
        expected_company_name_from_company_name_already_exists_error = company_name
        user_storage.get_valid_user_ids_among_the_given_user_ids \
            .return_value = user_ids
        company_with_user_ids_dto = CompanyWithUserIdsDTOFactory(
            name="company1", user_ids=user_ids)
        company_storage.get_company_id_if_company_name_already_exists\
            .return_value = "1"
        presenter.get_company_name_already_exists_response_for_add_company \
            .return_value = Mock()

        interactor.add_company_wrapper(
            user_id=user_id,
            company_with_user_ids_dto=company_with_user_ids_dto,
            presenter=presenter)

        company_storage.get_company_id_if_company_name_already_exists \
            .assert_called_once_with(name=company_with_user_ids_dto.name)
        call_args = presenter \
            .get_company_name_already_exists_response_for_add_company.call_args
        error_obj = call_args[0][0]
        actual_company_name_from_company_name_already_exists_error = \
            error_obj.company_name
        assert actual_company_name_from_company_name_already_exists_error == \
               expected_company_name_from_company_name_already_exists_error

    def test_given_valid_details_then_returns_company_id(self):
        user_storage = create_autospec(UserStorageInterface)
        company_storage = create_autospec(CompanyStorageInterface)
        presenter = create_autospec(AddCompanyPresenterInterface)
        interactor = CompanyInteractor(company_storage=company_storage,
                                       user_storage=user_storage)
        user_id = "1"
        company_id = "1"
        user_ids = ["2", "3"]
        company_with_user_ids_dto = CompanyWithUserIdsDTOFactory()
        company_name_logo_and_description_dto = \
            CompanyNameLogoAndDescriptionDTO(
                name=company_with_user_ids_dto.name,
                description=company_with_user_ids_dto.description,
                logo_url=company_with_user_ids_dto.logo_url)
        company_storage.get_company_id_if_company_name_already_exists\
            .return_value = None
        user_storage.get_valid_user_ids_among_the_given_user_ids \
            .return_value = user_ids
        company_storage.add_company.return_value = company_id
        presenter.get_response_for_add_company.return_value = Mock()

        interactor.add_company_wrapper(
            user_id=user_id,
            company_with_user_ids_dto=company_with_user_ids_dto,
            presenter=presenter)

        company_storage.add_company.assert_called_once_with(
            company_name_logo_and_description_dto=company_name_logo_and_description_dto)
        company_storage.add_users_to_company(company_id=company_id,
                                             user_ids=user_ids)
        presenter.get_response_for_add_company \
            .assert_called_once_with(company_id=company_id)
