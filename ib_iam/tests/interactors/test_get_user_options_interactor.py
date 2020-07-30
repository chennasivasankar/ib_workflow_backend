from unittest.mock import Mock

import pytest

from ib_iam.interactors.get_user_options_interactor \
    import GetUserOptionsDetails
from ib_iam.tests.common_fixtures.storages import reset_sequence


class TestGetUserOptionsInteractor:

    @pytest.fixture()
    def company_dtos(self):
        reset_sequence()
        from ib_iam.tests.factories.storage_dtos import CompanyIdAndNameDTOFactory
        company_dtos = CompanyIdAndNameDTOFactory.create_batch(4)
        return company_dtos

    @pytest.fixture()
    def team_dtos(self):
        reset_sequence()
        from ib_iam.tests.factories.storage_dtos import TeamDTOFactory
        team_dtos = TeamDTOFactory.create_batch(4)
        return team_dtos

    @pytest.fixture()
    def role_dtos(self):
        reset_sequence()
        from ib_iam.tests.factories.storage_dtos import RoleDTOFactory
        role_dtos = RoleDTOFactory.create_batch(4)
        return role_dtos

    @pytest.fixture
    def storage_mock(self):
        from unittest import mock
        from ib_iam.interactors.storage_interfaces.\
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

    def test_get_companies_details(
            self, company_dtos, storage_mock, presenter_mock):
        # Arrange
        storage_mock.get_companies.return_value = company_dtos
        interactor = GetUserOptionsDetails(storage=storage_mock)

        # Act
        interactor.get_configuration_details_wrapper(presenter=presenter_mock,
                                                     user_id="user0")

        # Assert
        storage_mock.get_companies.assert_called_once()

    def test_get_teams_details(
            self, team_dtos, storage_mock, presenter_mock):
        # Arrange
        storage_mock.get_teams.return_value = team_dtos
        interactor = GetUserOptionsDetails(storage=storage_mock)

        # Act
        interactor.get_configuration_details_wrapper(presenter=presenter_mock,
                                                     user_id="user0")

        # Assert
        storage_mock.get_teams.assert_called_once()

    def test_get_roles_details(
            self, role_dtos, storage_mock, presenter_mock):
        # Arrange
        storage_mock.get_roles.return_value = role_dtos
        interactor = GetUserOptionsDetails(storage=storage_mock)

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
        storage_mock.get_teams.return_value = team_dtos
        storage_mock.get_roles.return_value = role_dtos
        interactor = GetUserOptionsDetails(storage=storage_mock)
        presenter_mock.return_value = Mock()

        # Act
        interactor.get_configuration_details_wrapper(presenter=presenter_mock,
                                                     user_id="user0")

        # Assert
        presenter_mock.get_user_options_details_response.assert_called_once()
