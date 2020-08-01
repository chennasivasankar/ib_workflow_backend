from unittest.mock import Mock

import pytest

from ib_iam.interactors.edit_user_interactor import EditUserInteractor


class TestEditNewUserInteractor:
    @pytest.fixture
    def storage_mock(self):
        from unittest import mock
        from ib_iam.interactors.storage_interfaces. \
            user_storage_interface \
            import UserStorageInterface
        storage = mock.create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from unittest import mock

        from ib_iam.interactors.presenter_interfaces. \
            edit_user_presenter_interface \
            import EditUserPresenterInterface
        storage = mock.create_autospec(EditUserPresenterInterface)
        return storage

    def test_create_user_when_user_is_not_admin_then_throw_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "username"
        email = "user@email.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'

        interactor = EditUserInteractor(storage=storage_mock)
        storage_mock.check_is_admin_user.return_value = False
        presenter_mock.raise_user_is_not_admin_exception.return_value = Mock()
        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id, name=name,
            email=email, teams=team_ids, roles=role_ids,
            company_id=company_id,
            presenter=presenter_mock)

        # Assert
        storage_mock.check_is_admin_user.assert_called_once_with(
            user_id=admin_user_id)
        presenter_mock.raise_user_is_not_admin_exception.assert_called_once()

    def test_validate_name_when_empty_throw_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = ""
        email = "user@email.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'

        interactor = EditUserInteractor(storage=storage_mock)
        storage_mock.check_is_admin_user.return_value = True
        presenter_mock.raise_invalid_name_exception.return_value = Mock()

        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id, name=name,
            email=email, teams=team_ids, roles=role_ids,
            company_id=company_id,
            presenter=presenter_mock)

        # Assert
        presenter_mock.raise_invalid_name_exception.assert_called_once()

    def test_validate_name_when_contains_special_characters_and_numbers_throw_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "user@2"
        email = "user@email.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'

        interactor = EditUserInteractor(storage=storage_mock)
        storage_mock.check_is_admin_user.return_value = True
        presenter_mock.raise_invalid_name_exception.return_value = Mock()

        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id, name=name,
            email=email, teams=team_ids, roles=role_ids,
            company_id=company_id,
            presenter=presenter_mock)

        # Assert
        presenter_mock. \
            raise_name_should_not_contain_special_characters_exception. \
            assert_called_once()

    def test_validate_email_and_throw_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "name"
        email = ""
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'

        interactor = EditUserInteractor(storage=storage_mock)
        storage_mock.check_is_admin_user.return_value = True
        presenter_mock.raise_invalid_email_exception.return_value = Mock()

        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id, name=name,
            email=email, teams=team_ids, roles=role_ids,
            company_id=company_id,
            presenter=presenter_mock)

        # Assert
        presenter_mock.raise_invalid_email_exception.assert_called_once()

    def test_validate_roles_and_throw_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "name"
        email = "user@gmail.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'

        interactor = EditUserInteractor(storage=storage_mock)
        storage_mock.check_is_admin_user.return_value = True
        storage_mock.check_are_valid_role_ids.return_value = False
        storage_mock.check_are_valid_team_ids.return_value = True
        storage_mock.check_is_exists_company_id.return_value = True
        presenter_mock.raise_role_ids_are_invalid.return_value = Mock()

        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id, name=name,
            email=email, teams=team_ids, roles=role_ids,
            company_id=company_id,
            presenter=presenter_mock)

        # Assert
        storage_mock.check_are_valid_role_ids.assert_called_once()
        presenter_mock.raise_role_ids_are_invalid.assert_called_once()

    def test_validate_teams_and_throw_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "name"
        email = "user@gmail.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'

        interactor = EditUserInteractor(storage=storage_mock)
        storage_mock.check_is_admin_user.return_value = True
        storage_mock.check_are_valid_team_ids.return_value = False
        presenter_mock.raise_team_ids_are_invalid.return_value = Mock()

        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id, name=name,
            email=email, teams=team_ids, roles=role_ids,
            company_id=company_id,
            presenter=presenter_mock)

        # Assert
        storage_mock.check_are_valid_team_ids.assert_called_once()
        presenter_mock.raise_team_ids_are_invalid.assert_called_once()

    def test_validate_company_id_and_throw_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "name"
        email = "user@gmail.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'

        interactor = EditUserInteractor(storage=storage_mock)
        storage_mock.check_is_admin_user.return_value = True
        storage_mock.check_are_valid_role_ids.return_value = True
        storage_mock.check_are_valid_team_ids.return_value = True
        storage_mock.check_is_exists_company_id.return_value = False
        presenter_mock.raise_company_ids_is_invalid.return_value = Mock()

        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id, name=name,
            email=email, teams=team_ids, roles=role_ids,
            company_id=company_id,
            presenter=presenter_mock)

        # Assert
        storage_mock.check_is_exists_company_id.assert_called_once()
        presenter_mock.raise_company_ids_is_invalid.assert_called_once()

    def test_edit_user_when_user_does_not_exist_raise_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "name"
        email = "user@gmail.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'

        interactor = EditUserInteractor(storage=storage_mock)
        storage_mock.check_is_admin_user.return_value = True
        storage_mock.is_user_exist.return_value = False
        presenter_mock.raise_user_does_not_exist.return_value = Mock()

        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id, name=name,
            email=email, teams=team_ids, roles=role_ids,
            company_id=company_id,
            presenter=presenter_mock)

        # Assert
        storage_mock.is_user_exist.assert_called_once()
        presenter_mock.raise_user_does_not_exist.assert_called_once()

    def test_edit_user_update_user_details_with_valid_details(
            self, storage_mock, presenter_mock, mocker):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "name"
        email = "user@gmail.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'

        interactor = EditUserInteractor(storage=storage_mock)
        storage_mock.check_is_admin_user.return_value = True
        storage_mock.is_user_exist.return_value = True
        presenter_mock.raise_user_does_not_exist.return_value = Mock()
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import update_user_profile_adapter_mock
        adapter_mock = update_user_profile_adapter_mock(mocker=mocker)
        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id, name=name,
            email=email, teams=team_ids, roles=role_ids,
            company_id=company_id,
            presenter=presenter_mock)

        # Assert
        storage_mock.is_user_exist.assert_called_once()
        adapter_mock.assert_called_once()

    def test_edit_user_unassign_existing_stats_for_user(
            self, storage_mock, presenter_mock, mocker):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "name"
        email = "user@gmail.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'

        interactor = EditUserInteractor(storage=storage_mock)
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import update_user_profile_adapter_mock
        adapter_mock = update_user_profile_adapter_mock(mocker=mocker)
        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id, name=name,
            email=email, teams=team_ids, roles=role_ids,
            company_id=company_id,
            presenter=presenter_mock)

        # Assert
        adapter_mock.assert_called_once()
        storage_mock.remove_roles_for_user.assert_called_once()
        storage_mock.remove_teams_for_user.assert_called_once()

    def test_edit_user_assign_existing_stats_for_user_after_unassigning_returns_success_response(
            self, storage_mock, presenter_mock, mocker):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "name"
        email = "user@gmail.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'

        interactor = EditUserInteractor(storage=storage_mock)
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import update_user_profile_adapter_mock
        adapter_mock = update_user_profile_adapter_mock(mocker=mocker)
        presenter_mock.edit_user_success_response.return_value = Mock()
        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id, name=name,
            email=email, teams=team_ids, roles=role_ids,
            company_id=company_id,
            presenter=presenter_mock)

        # Assert
        adapter_mock.assert_called_once()
        storage_mock.add_roles_to_the_user.assert_called_once()
        storage_mock.add_user_to_the_teams.assert_called_once()
        storage_mock.update_user_details.assert_called_once()
        presenter_mock.edit_user_success_response.assert_called_once()
