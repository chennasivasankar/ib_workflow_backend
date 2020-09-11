from unittest.mock import Mock

import pytest

from ib_iam.interactors.get_user_options_interactor \
    import GetUserOptionsDetails


class TestGetUserOptionsInteractor:

    @pytest.fixture()
    def company_dtos(self):
        from ib_iam.tests.common_fixtures.reset_fixture import \
            reset_sequence_for_company_dto_factory
        reset_sequence_for_company_dto_factory()
        from ib_iam.tests.factories.storage_dtos import \
            CompanyIdAndNameDTOFactory
        company_dtos = CompanyIdAndNameDTOFactory.create_batch(4)
        return company_dtos

    @pytest.fixture()
    def team_dtos(self):
        from ib_iam.tests.common_fixtures.reset_fixture import \
            reset_sequence_for_team_dto_factory
        reset_sequence_for_team_dto_factory()
        from ib_iam.tests.factories.storage_dtos import TeamDTOFactory
        team_dtos = TeamDTOFactory.create_batch(4)
        return team_dtos

    @pytest.fixture()
    def role_dtos(self):
        from ib_iam.tests.common_fixtures.reset_fixture import \
            reset_sequence_for_role_dto_factory
        reset_sequence_for_role_dto_factory()
        from ib_iam.tests.factories.storage_dtos import RoleDTOFactory
        role_dtos = RoleDTOFactory.create_batch(4)
        return role_dtos

    @pytest.fixture
    def storage_mock(self):
        from unittest import mock
        from ib_iam.interactors.storage_interfaces. \
            user_storage_interface import \
            UserStorageInterface
        storage = mock.create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from unittest import mock
        from ib_iam.interactors.presenter_interfaces.get_user_options_presenter_interface \
            import GetUserOptionsPresenterInterface
        storage = mock.create_autospec(GetUserOptionsPresenterInterface)
        return storage

    def test_create_user_when_user_is_not_admin_then_throw_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        interactor = GetUserOptionsDetails(user_storage=storage_mock)
        storage_mock.is_user_admin.return_value = False
        presenter_mock.response_for_user_is_not_admin_exception.return_value = Mock()

        # Act
        interactor.get_configuration_details_wrapper(presenter=presenter_mock,
                                                     user_id="user0")

        # Assert
        storage_mock.is_user_admin.assert_called_once_with(user_id="user0")
        presenter_mock.response_for_user_is_not_admin_exception.assert_called_once()

    def test_get_companies_details(
            self, company_dtos, storage_mock, presenter_mock):
        # Arrange
        storage_mock.get_companies.return_value = company_dtos
        interactor = GetUserOptionsDetails(user_storage=storage_mock)

        # Act
        interactor.get_configuration_details_wrapper(presenter=presenter_mock,
                                                     user_id="user0")

        # Assert
        storage_mock.get_companies.assert_called_once()

    def test_get_teams_details(
            self, team_dtos, storage_mock, presenter_mock):
        # Arrange
        storage_mock.get_team_id_and_name_dtos.return_value = team_dtos
        interactor = GetUserOptionsDetails(user_storage=storage_mock)

        # Act
        interactor.get_configuration_details_wrapper(presenter=presenter_mock,
                                                     user_id="user0")

        # Assert
        storage_mock.get_team_id_and_name_dtos.assert_called_once()

    def test_get_roles_details(
            self, role_dtos, storage_mock, presenter_mock):
        # Arrange
        storage_mock.get_roles.return_value = role_dtos
        interactor = GetUserOptionsDetails(user_storage=storage_mock)

        # Act
        interactor.get_configuration_details_wrapper(presenter=presenter_mock,
                                                     user_id="user0")

        # Assert
        storage_mock.get_roles.assert_called_once()

    def test_get_configuration_details_returns_response(
            self, role_dtos, team_dtos, company_dtos, storage_mock,
            presenter_mock):
        # Arrange
        storage_mock.get_companies.return_value = company_dtos
        storage_mock.get_team_id_and_name_dtos.return_value = team_dtos
        storage_mock.get_roles.return_value = role_dtos
        interactor = GetUserOptionsDetails(user_storage=storage_mock)
        presenter_mock.return_value = Mock()

        # Act
        interactor.get_configuration_details_wrapper(presenter=presenter_mock,
                                                     user_id="user0")

        # Assert
        presenter_mock.get_user_options_details_response.assert_called_once()
