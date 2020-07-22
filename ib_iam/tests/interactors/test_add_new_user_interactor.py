from unittest.mock import Mock

import pytest

from ib_iam.interactors.add_new_user_interactor import AddNewUserInteractor


class TestAddNewUserIneractor:

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

    def test_create_user_when_user_is_not_admin_then_throw_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        user_id = "user_1"
        name = "username"
        email = "user@email.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'

        interactor = AddNewUserInteractor(storage=storage_mock)
        storage_mock.is_admin_user.return_value = False
        presenter_mock.raise_user_is_not_admin_exception.return_value = Mock()
        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id, name=name, email=email,
            teams=team_ids, roles=role_ids, company_id=company_id,
            presenter=presenter_mock)

        # Assert
        storage_mock.is_admin_user.assert_called_once_with(
            user_id=user_id)
        presenter_mock.raise_user_is_not_admin_exception.assert_called_once()

    def test_validate_name_when_empty_throw_exception(self, storage_mock,
                                                      presenter_mock):
        # Arrange
        user_id = "user_1"
        name = ""
        email = "user@email.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'
        interactor = AddNewUserInteractor(storage=storage_mock)
        storage_mock.is_admin_user.return_value = True
        presenter_mock.raise_invalid_name_exception.return_value = Mock()

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id, name=name, email=email,
            teams=team_ids, roles=role_ids, company_id=company_id,
            presenter=presenter_mock)

        # Assert
        presenter_mock.raise_invalid_name_exception.assert_called_once()

    #
    def test_validate_name_when_contains_special_characters_and_numbers_throw_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        user_id = "user_1"
        name = "user@2"
        email = "user@email.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'
        interactor = AddNewUserInteractor(storage=storage_mock)
        storage_mock.is_admin_user.return_value = True
        presenter_mock.raise_invalid_name_exception.return_value = Mock()

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id, name=name, email=email,
            teams=team_ids, roles=role_ids, company_id=company_id,
            presenter=presenter_mock)

        # Assert
        presenter_mock. \
            raise_name_should_not_contain_special_characters_exception. \
            assert_called_once()

    def test_validate_email_and_throw_exception(self, storage_mock,
                                                presenter_mock):
        # Arrange
        user_id = "user_1"
        name = "name"
        email = ""
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'
        interactor = AddNewUserInteractor(storage=storage_mock)
        storage_mock.is_admin_user.return_value = True
        presenter_mock.raise_invalid_name_exception.return_value = Mock()

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id, name=name, email=email,
            teams=team_ids, roles=role_ids, company_id=company_id,
            presenter=presenter_mock)

        # Assert
        presenter_mock.raise_invalid_email_exception.assert_called_once()

    def test_validate_roles_and_throw_exception(self, storage_mock,
                                                presenter_mock):
        # Arrange
        user_id = "user_1"
        name = "name"
        email = "user@gmail.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'
        interactor = AddNewUserInteractor(storage=storage_mock)
        storage_mock.validate_roles.return_value = False
        presenter_mock.raise_role_ids_are_invalid.return_value = Mock()

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id, name=name, email=email,
            teams=team_ids, roles=role_ids, company_id=company_id,
            presenter=presenter_mock)

        # Assert
        storage_mock.validate_roles.assert_called_once()
        presenter_mock.raise_role_ids_are_invalid.assert_called_once()

    def test_validate_teams_and_throw_exception(self, storage_mock,
                                                presenter_mock):
        # Arrange
        user_id = "user_1"
        name = "name"
        email = "user@gmail.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'
        interactor = AddNewUserInteractor(storage=storage_mock)
        storage_mock.validate_teams.return_value = False
        presenter_mock.raise_team_ids_are_invalid.return_value = Mock()

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id, name=name, email=email,
            teams=team_ids, roles=role_ids, company_id=company_id,
            presenter=presenter_mock)

        # Assert
        storage_mock.validate_teams.assert_called_once()
        presenter_mock.raise_team_ids_are_invalid.assert_called_once()

    def test_validate_company_id_and_throw_exception(self, storage_mock,
                                                     presenter_mock):
        # Arrange
        user_id = "user_1"
        name = "name"
        email = "user@gmail.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'
        interactor = AddNewUserInteractor(storage=storage_mock)
        storage_mock.validate_company.return_value = False
        presenter_mock.raise_company_ids_is_invalid.return_value = Mock()

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id, name=name, email=email,
            teams=team_ids, roles=role_ids, company_id=company_id,
            presenter=presenter_mock)

        # Assert
        storage_mock.validate_company.assert_called_once()
        presenter_mock.raise_company_ids_is_invalid.assert_called_once()

    def test_create_user_account_with_email_already_exist_throws_exception(
            self, storage_mock, presenter_mock, mocker):
        # Arrange
        user_id = "user_1"
        name = "user"
        email = "user@email.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'
        interactor = AddNewUserInteractor(storage=storage_mock)
        storage_mock.is_admin_user.return_value = True
        presenter_mock.raise_user_account_already_exist_with_this_email_exception. \
            return_value = Mock()
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import email_exist_adapter_mock
        adapter_mock = email_exist_adapter_mock(mocker=mocker)

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id, name=name, email=email,
            teams=team_ids, roles=role_ids, company_id=company_id,
            presenter=presenter_mock)

        # Assert
        adapter_mock.assert_called_once()
        presenter_mock.raise_user_account_already_exist_with_this_email_exception. \
            assert_called_once()

    def test_create_ib_user_with_given_valid_details(
            self, storage_mock, presenter_mock, mocker):
        # Arrange
        user_id = "user_1"
        name = "user"
        email = "user@email.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'
        interactor = AddNewUserInteractor(storage=storage_mock)
        storage_mock.is_admin_user.return_value = True
        presenter_mock.raise_user_account_already_exist_with_this_email_exception. \
            return_value = Mock()
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import create_user_account_adapter_mock, \
            create_user_profile_adapter_mock
        user_account_adapter_mock = \
            create_user_account_adapter_mock(mocker=mocker)
        user_profile_adapter_mock = \
            create_user_profile_adapter_mock(mocker=mocker)

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id, name=name, email=email,
            teams=team_ids, roles=role_ids, company_id=company_id,
            presenter=presenter_mock)

        # Assert
        user_account_adapter_mock.assert_called_once()
        user_profile_adapter_mock.assert_called_once()

    def test_add_new_user(
            self, storage_mock, presenter_mock, mocker):
        # Arrange
        user_id = "user_1"
        name = "user"
        email = "user@email.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'
        interactor = AddNewUserInteractor(storage=storage_mock)
        storage_mock.is_admin_user.return_value = True
        presenter_mock.raise_user_account_already_exist_with_this_email_exception. \
            return_value = Mock()
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import create_user_account_adapter_mock, \
            create_user_profile_adapter_mock
        user_account_adapter_mock = \
            create_user_account_adapter_mock(mocker=mocker)
        user_profile_adapter_mock = \
            create_user_profile_adapter_mock(mocker=mocker)

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id, name=name, email=email,
            teams=team_ids, roles=role_ids, company_id=company_id,
            presenter=presenter_mock)

        # Assert
        storage_mock.add_new_user.assert_called_once()
        user_account_adapter_mock.assert_called_once()
        user_profile_adapter_mock.assert_called_once()
