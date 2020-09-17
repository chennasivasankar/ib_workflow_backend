import pytest
from mock import create_autospec, Mock

from ib_iam.interactors.storage_interfaces.dtos import \
    CompanyNameLogoAndDescriptionDTO
from ib_iam.tests.factories.storage_dtos import \
    CompanyWithUserIdsDTOFactory


class TestAddCompanyInteractor:

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
            AddCompanyPresenterInterface
        return create_autospec(AddCompanyPresenterInterface)

    @pytest.fixture
    def interactor(self, company_storage_mock, user_storage_mock):
        from ib_iam.interactors.company_interactor import CompanyInteractor
        return CompanyInteractor(
            company_storage=company_storage_mock,
            user_storage=user_storage_mock
        )

    def test_if_user_not_admin_returns_unauthorized_exception_response(
            self, interactor, company_storage_mock, user_storage_mock,
            presenter
    ):
        # Arrange
        user_id = "1"
        company_with_user_ids_dto = CompanyWithUserIdsDTOFactory()
        user_storage_mock.is_user_admin.return_value = False
        presenter.response_for_user_has_no_access_exception \
            .return_value = Mock()

        # Act
        interactor.add_company_wrapper(
            user_id=user_id, presenter=presenter,
            company_with_user_ids_dto=company_with_user_ids_dto,
        )

        # Assert
        user_storage_mock.is_user_admin \
            .assert_called_once_with(user_id=user_id)
        presenter.response_for_user_has_no_access_exception \
            .assert_called_once()

    def test_given_duplicate_users_returns_duplicate_users_response(
            self, interactor, company_storage_mock, user_storage_mock,
            presenter
    ):
        # Arrange
        user_id = "1"
        user_ids = ["2", "2", "3", "1"]
        company_with_user_ids_dto = CompanyWithUserIdsDTOFactory(
            name="company1", user_ids=user_ids)
        company_storage_mock.get_company_id_if_company_name_already_exists \
            .return_value = None
        presenter.response_for_duplicate_user_ids_exception \
            .return_value = Mock()

        # Act
        interactor.add_company_wrapper(
            user_id=user_id, presenter=presenter,
            company_with_user_ids_dto=company_with_user_ids_dto,
        )

        # Assert
        presenter.response_for_duplicate_user_ids_exception.assert_called_once()

    def test_given_invalid_users_returns_invalid_users_response(
            self, interactor, company_storage_mock, user_storage_mock,
            presenter
    ):
        # Arrange
        user_id = "1"
        valid_user_ids = ["2", "3"]
        invalid_user_ids = ["2", "3", "4"]
        company_with_user_ids_dto = CompanyWithUserIdsDTOFactory(
            name="company1", user_ids=invalid_user_ids)
        company_storage_mock.get_company_id_if_company_name_already_exists \
            .return_value = None
        user_storage_mock.get_valid_user_ids_among_the_given_user_ids \
            .return_value = valid_user_ids
        presenter.response_for_invalid_user_ids_exception.return_value = Mock()

        # Act
        interactor.add_company_wrapper(
            user_id=user_id, presenter=presenter,
            company_with_user_ids_dto=company_with_user_ids_dto,
        )

        # Assert
        user_storage_mock.get_valid_user_ids_among_the_given_user_ids \
            .assert_called_once_with(user_ids=invalid_user_ids)
        presenter.response_for_invalid_user_ids_exception \
            .assert_called_once()

    def test_company_name_exists_returns_company_name_already_exists_response(
            self, interactor, company_storage_mock, user_storage_mock,
            presenter
    ):
        # Arrange
        user_id = "1"
        company_name = "company1"
        user_ids = ["1"]
        expected_company_name_from_company_name_already_exists_error = company_name
        user_storage_mock.get_valid_user_ids_among_the_given_user_ids \
            .return_value = user_ids
        company_with_user_ids_dto = CompanyWithUserIdsDTOFactory(
            name="company1", user_ids=user_ids
        )
        company_storage_mock.get_company_id_if_company_name_already_exists \
            .return_value = "1"
        presenter.response_for_company_name_already_exists_exception \
            .return_value = Mock()

        # Act
        interactor.add_company_wrapper(
            user_id=user_id, presenter=presenter,
            company_with_user_ids_dto=company_with_user_ids_dto,
        )

        # Assert
        company_storage_mock.get_company_id_if_company_name_already_exists \
            .assert_called_once_with(name=company_with_user_ids_dto.name)
        call_args = presenter \
            .response_for_company_name_already_exists_exception.call_args
        error_obj = call_args[0][0]
        actual_company_name_from_company_name_already_exists_error = \
            error_obj.company_name
        assert actual_company_name_from_company_name_already_exists_error == \
               expected_company_name_from_company_name_already_exists_error

    def test_given_valid_details_then_returns_company_id(
            self, interactor, company_storage_mock, user_storage_mock,
            presenter
    ):
        # Arrange
        user_id = "1"
        company_id = "1"
        user_ids = ["2", "3"]
        company_with_user_ids_dto = CompanyWithUserIdsDTOFactory()
        company_name_logo_and_description_dto = \
            CompanyNameLogoAndDescriptionDTO(
                name=company_with_user_ids_dto.name,
                description=company_with_user_ids_dto.description,
                logo_url=company_with_user_ids_dto.logo_url
            )
        company_storage_mock.get_company_id_if_company_name_already_exists \
            .return_value = None
        user_storage_mock.get_valid_user_ids_among_the_given_user_ids \
            .return_value = user_ids
        company_storage_mock.add_company.return_value = company_id
        presenter.get_response_for_add_company.return_value = Mock()

        # Act
        interactor.add_company_wrapper(
            user_id=user_id, presenter=presenter,
            company_with_user_ids_dto=company_with_user_ids_dto,
        )

        # Assert
        company_storage_mock.add_company.assert_called_once_with(
            company_name_logo_and_description_dto=company_name_logo_and_description_dto
        )
        company_storage_mock.add_users_to_company(
            company_id=company_id, user_ids=user_ids
        )
        presenter.get_response_for_add_company \
            .assert_called_once_with(company_id=company_id)
