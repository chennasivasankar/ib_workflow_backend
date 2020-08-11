from unittest.mock import Mock

import pytest

from ib_iam.interactors.add_new_user_interactor import AddNewUserInteractor
from ib_iam.tests.factories.interactor_dtos import \
    UserDetailsWithTeamRoleAndCompanyIdsDTOFactory


class TestAddNewUserIneractor:

    @pytest.fixture
    def storage_mock(self):
        from unittest import mock

        from ib_iam.interactors.storage_interfaces.user_storage_interface \
            import UserStorageInterface
        storage = mock.create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from unittest import mock
        from ib_iam.interactors.presenter_interfaces.add_new_user_presenter_inerface \
            import AddUserPresenterInterface
        storage = mock.create_autospec(AddUserPresenterInterface)
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

        interactor = AddNewUserInteractor(user_storage=storage_mock)
        storage_mock.is_user_admin.return_value = False
        presenter_mock.raise_user_is_not_admin_exception.return_value = Mock()

        user_details_with_team_role_and_company_ids_dto \
            = UserDetailsWithTeamRoleAndCompanyIdsDTOFactory(
            name=name, email=email, team_ids=team_ids, role_ids=role_ids,
            company_id=company_id
        )

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id,
            user_details_with_team_role_and_company_ids_dto \
                =user_details_with_team_role_and_company_ids_dto,
            presenter=presenter_mock)

        # Assert
        storage_mock.is_user_admin.assert_called_once_with(user_id=user_id)
        presenter_mock.raise_user_is_not_admin_exception.assert_called_once()

    def test_validate_name_when_contains_special_characters_and_numbers_throw_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        user_id = "user_1"
        name = "user@1"
        email = "user@email.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'
        interactor = AddNewUserInteractor(user_storage=storage_mock)
        storage_mock.is_user_admin.return_value = True
        presenter_mock \
            .raise_name_should_not_contain_special_characters_exception \
            .return_value = Mock()

        user_details_with_team_role_and_company_ids_dto \
            = UserDetailsWithTeamRoleAndCompanyIdsDTOFactory(
            name=name, email=email, team_ids=team_ids, role_ids=role_ids,
            company_id=company_id
        )

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id,
            user_details_with_team_role_and_company_ids_dto \
                =user_details_with_team_role_and_company_ids_dto,
            presenter=presenter_mock)

        # Assert
        presenter_mock. \
            raise_name_should_not_contain_special_characters_exception. \
            assert_called_once()

    def test_validate_name_returns_should_contain_minimum_5_characters_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        user_id = "user_1"
        name = "user"
        email = "user@email.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'
        interactor = AddNewUserInteractor(user_storage=storage_mock)
        storage_mock.is_user_admin.return_value = True
        presenter_mock.raise_invalid_name_length_exception_for_update_user_profile \
            .return_value = Mock()

        user_details_with_team_role_and_company_ids_dto \
            = UserDetailsWithTeamRoleAndCompanyIdsDTOFactory(
            name=name, email=email, team_ids=team_ids, role_ids=role_ids,
            company_id=company_id
        )

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id,
            user_details_with_team_role_and_company_ids_dto \
                =user_details_with_team_role_and_company_ids_dto,
            presenter=presenter_mock)

        # Assert
        presenter_mock.raise_invalid_name_length_exception_for_update_user_profile. \
            assert_called_once()

    def test_validate_email_and_throw_exception(self, storage_mock,
                                                presenter_mock):
        # Arrange
        user_id = "user_1"
        name = "username"
        email = ""
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'
        interactor = AddNewUserInteractor(user_storage=storage_mock)
        storage_mock.is_user_admin.return_value = True
        presenter_mock.raise_invalid_email_exception.return_value = Mock()

        user_details_with_team_role_and_company_ids_dto \
            = UserDetailsWithTeamRoleAndCompanyIdsDTOFactory(
            name=name, email=email, team_ids=team_ids, role_ids=role_ids,
            company_id=company_id
        )

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id,
            user_details_with_team_role_and_company_ids_dto \
                =user_details_with_team_role_and_company_ids_dto,
            presenter=presenter_mock)

        # Assert
        presenter_mock.raise_invalid_email_exception.assert_called_once()

    def test_validate_roles_and_throw_exception(self, storage_mock,
                                                presenter_mock):
        # Arrange
        user_id = "user_1"
        name = "username"
        email = "user@gmail.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'
        interactor = AddNewUserInteractor(user_storage=storage_mock)
        storage_mock.check_are_valid_role_ids.return_value = False
        presenter_mock.raise_role_ids_are_invalid.return_value = Mock()

        user_details_with_team_role_and_company_ids_dto \
            = UserDetailsWithTeamRoleAndCompanyIdsDTOFactory(
            name=name, email=email, team_ids=team_ids, role_ids=role_ids,
            company_id=company_id
        )

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id,
            user_details_with_team_role_and_company_ids_dto \
                =user_details_with_team_role_and_company_ids_dto,
            presenter=presenter_mock)

        # Assert
        storage_mock.check_are_valid_role_ids.assert_called_once()
        presenter_mock.raise_role_ids_are_invalid.assert_called_once()

    def test_validate_teams_and_throw_exception(self, storage_mock,
                                                presenter_mock):
        # Arrange
        user_id = "user_1"
        name = "username"
        email = "user@gmail.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'
        interactor = AddNewUserInteractor(user_storage=storage_mock)
        storage_mock.check_are_valid_team_ids.return_value = False
        presenter_mock.raise_team_ids_are_invalid.return_value = Mock()

        user_details_with_team_role_and_company_ids_dto \
            = UserDetailsWithTeamRoleAndCompanyIdsDTOFactory(
            name=name, email=email, team_ids=team_ids, role_ids=role_ids,
            company_id=company_id
        )

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id,
            user_details_with_team_role_and_company_ids_dto \
                =user_details_with_team_role_and_company_ids_dto,
            presenter=presenter_mock)

        # Assert
        storage_mock.check_are_valid_team_ids.assert_called_once()
        presenter_mock.raise_team_ids_are_invalid.assert_called_once()

    def test_validate_company_id_and_throw_exception(self, storage_mock,
                                                     presenter_mock):
        # Arrange
        user_id = "user_1"
        name = "username"
        email = "user@gmail.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'
        interactor = AddNewUserInteractor(user_storage=storage_mock)
        storage_mock.check_is_exists_company_id.return_value = False
        presenter_mock.raise_company_ids_is_invalid.return_value = Mock()

        user_details_with_team_role_and_company_ids_dto \
            = UserDetailsWithTeamRoleAndCompanyIdsDTOFactory(
            name=name, email=email, team_ids=team_ids, role_ids=role_ids,
            company_id=company_id
        )

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id,
            user_details_with_team_role_and_company_ids_dto \
                =user_details_with_team_role_and_company_ids_dto,
            presenter=presenter_mock)

        # Assert
        storage_mock.check_is_exists_company_id.assert_called_once()
        presenter_mock.raise_company_ids_is_invalid.assert_called_once()

    def test_create_user_account_with_email_already_exist_throws_exception(
            self, storage_mock, presenter_mock, mocker):
        # Arrange
        user_id = "user_1"
        name = "username"
        email = "user@email.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'
        interactor = AddNewUserInteractor(user_storage=storage_mock)
        storage_mock.is_user_admin.return_value = True
        presenter_mock.raise_user_account_already_exist_with_this_email_exception. \
            return_value = Mock()
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import email_exist_adapter_mock
        adapter_mock = email_exist_adapter_mock(mocker=mocker)

        user_details_with_team_role_and_company_ids_dto \
            = UserDetailsWithTeamRoleAndCompanyIdsDTOFactory(
            name=name, email=email, team_ids=team_ids, role_ids=role_ids,
            company_id=company_id
        )

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id,
            user_details_with_team_role_and_company_ids_dto \
                =user_details_with_team_role_and_company_ids_dto,
            presenter=presenter_mock)

        # Assert
        adapter_mock.assert_called_once()
        presenter_mock.raise_user_account_already_exist_with_this_email_exception. \
            assert_called_once()

    def test_get_role_objs_ids_returns_ids_of_role(
            self, storage_mock, presenter_mock, mocker):
        # Arrange
        user_id = "user_1"
        name = "username"
        email = "user@email.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        ids_of_role_objs = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                            "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
        company_id = 'company0'
        interactor = AddNewUserInteractor(user_storage=storage_mock)
        storage_mock.is_user_admin.return_value = True
        storage_mock.get_role_objs_ids.return_value = ids_of_role_objs
        presenter_mock.raise_user_account_already_exist_with_this_email_exception. \
            return_value = Mock()
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import create_user_account_adapter_mock, \
            create_user_profile_adapter_mock
        user_account_adapter_mock = \
            create_user_account_adapter_mock(mocker=mocker)
        user_profile_adapter_mock = \
            create_user_profile_adapter_mock(mocker=mocker)

        user_details_with_team_role_and_company_ids_dto \
            = UserDetailsWithTeamRoleAndCompanyIdsDTOFactory(
            name=name, email=email, team_ids=team_ids, role_ids=role_ids,
            company_id=company_id
        )

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id,
            user_details_with_team_role_and_company_ids_dto \
                =user_details_with_team_role_and_company_ids_dto,
            presenter=presenter_mock)

        # Assert
        storage_mock.get_role_objs_ids.assert_called_once()
        user_account_adapter_mock.assert_called_once()
        user_profile_adapter_mock.assert_called_once()

    def test_create_ib_user_with_given_valid_details(
            self, storage_mock, presenter_mock, mocker):
        # Arrange
        user_id = "user_1"
        name = "username"
        email = "user@email.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'
        interactor = AddNewUserInteractor(user_storage=storage_mock)
        storage_mock.is_user_admin.return_value = True
        presenter_mock.raise_user_account_already_exist_with_this_email_exception. \
            return_value = Mock()
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import create_user_account_adapter_mock, \
            create_user_profile_adapter_mock
        user_account_adapter_mock = \
            create_user_account_adapter_mock(mocker=mocker)
        user_profile_adapter_mock = \
            create_user_profile_adapter_mock(mocker=mocker)

        user_details_with_team_role_and_company_ids_dto \
            = UserDetailsWithTeamRoleAndCompanyIdsDTOFactory(
            name=name, email=email, team_ids=team_ids, role_ids=role_ids,
            company_id=company_id
        )

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id,
            user_details_with_team_role_and_company_ids_dto \
                =user_details_with_team_role_and_company_ids_dto,
            presenter=presenter_mock)

        # Assert
        user_account_adapter_mock.assert_called_once()
        user_profile_adapter_mock.assert_called_once()

    def test_add_new_user(
            self, storage_mock, presenter_mock, mocker):
        # Arrange
        user_id = "user_1"
        name = "username"
        email = "user@email.com"
        team_ids = ['team0', 'team1']
        role_ids = ['role0', 'role1']
        company_id = 'company0'
        interactor = AddNewUserInteractor(user_storage=storage_mock)
        storage_mock.is_user_admin.return_value = True
        presenter_mock.user_created_response.return_value = Mock()
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import create_user_account_adapter_mock, \
            create_user_profile_adapter_mock
        user_account_adapter_mock = \
            create_user_account_adapter_mock(mocker=mocker)
        user_profile_adapter_mock = \
            create_user_profile_adapter_mock(mocker=mocker)

        user_details_with_team_role_and_company_ids_dto \
            = UserDetailsWithTeamRoleAndCompanyIdsDTOFactory(
            name=name, email=email, team_ids=team_ids, role_ids=role_ids,
            company_id=company_id
        )

        # Act
        interactor.add_new_user_wrapper(
            user_id=user_id,
            user_details_with_team_role_and_company_ids_dto \
                =user_details_with_team_role_and_company_ids_dto,
            presenter=presenter_mock)

        # Assert
        user_account_adapter_mock.assert_called_once()
        user_profile_adapter_mock.assert_called_once()
        presenter_mock.user_created_response.assert_called_once()
        storage_mock.create_user.assert_called_once()
        storage_mock.add_user_to_the_teams.assert_called_once()
        storage_mock.add_roles_to_the_user.assert_called_once()
