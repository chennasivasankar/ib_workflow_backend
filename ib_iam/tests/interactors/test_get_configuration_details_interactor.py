from unittest.mock import Mock

import pytest

from ib_iam.interactors.get_configuration_details_interactor \
    import GetConfigurationDetails
from ib_iam.tests.common_fixtures.storages \
    import company_dtos, team_dtos, role_dtos

class TestGetConfigurationDetailInteractor:
    @pytest.fixture
    def storage_mock(self):
        from unittest import mock
        from ib_iam.interactors.storage_interfaces.storage_interface \
            import StorageInterface
        storage = mock.create_autospec(StorageInterface)
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from unittest import mock
        from ib_iam.interactors.presenter_interfaces.presenter_interface \
            import PresenterInterface
        storage = mock.create_autospec(PresenterInterface)
        return storage

    def test_get_companies_details(
            self, company_dtos, storage_mock, presenter_mock):
        # Arrange
        storage_mock.get_companies.return_value = company_dtos
        interactor = GetConfigurationDetails(storage=storage_mock)

        # Act
        interactor.get_configuration_details_wrapper(presenter=presenter_mock, user_id="user0")

        # Assert
        storage_mock.get_companies.assert_called_once()

    def test_get_teams_details(
            self, team_dtos, storage_mock, presenter_mock):
        # Arrange
        storage_mock.get_teams.return_value = team_dtos
        interactor = GetConfigurationDetails(storage=storage_mock)

        # Act
        interactor.get_configuration_details_wrapper(presenter=presenter_mock, user_id="user0")

        # Assert
        storage_mock.get_teams.assert_called_once()

    def test_get_roles_details(
            self, role_dtos, storage_mock, presenter_mock):
        # Arrange
        storage_mock.get_roles.return_value = role_dtos
        interactor = GetConfigurationDetails(storage=storage_mock)

        # Act
        interactor.get_configuration_details_wrapper(presenter=presenter_mock, user_id="user0")

        # Assert
        storage_mock.get_roles.assert_called_once()

    def test_get_configuration_details_returns_response(
            self, role_dtos, team_dtos, company_dtos, storage_mock,
            presenter_mock):
        # Arrange
        storage_mock.get_companies.return_value = company_dtos
        storage_mock.get_teams.return_value = team_dtos
        storage_mock.get_roles.return_value = role_dtos
        interactor = GetConfigurationDetails(storage=storage_mock)
        presenter_mock.return_value = Mock()

        # Act
        interactor.get_configuration_details_wrapper(presenter=presenter_mock, user_id="user0")

        # Assert
        presenter_mock.response_for_get_configuration_details.assert_called_once()
