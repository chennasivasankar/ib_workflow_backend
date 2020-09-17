from unittest.mock import Mock

import pytest

from ib_iam.interactors.edit_user_interactor import EditUserInteractor
from ib_iam.tests.factories.interactor_dtos import \
    AddUserDetailsDTOFactory


class TestEditNewUserInteractor:
    @pytest.fixture
    def storage_mock(self):
        from unittest import mock
        from ib_iam.interactors.storage_interfaces. \
            user_storage_interface import UserStorageInterface
        storage = mock.create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture()
    def elastic_storage(self):
        from unittest import mock
        from ib_iam.interactors.storage_interfaces.elastic_storage_interface \
            import ElasticSearchStorageInterface
        storage = mock.create_autospec(ElasticSearchStorageInterface)
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from unittest import mock

        from ib_iam.interactors.presenter_interfaces. \
            user_presenter_interface import EditUserPresenterInterface
        storage = mock.create_autospec(EditUserPresenterInterface)
        return storage

    def test_create_user_when_user_is_not_admin_then_throw_exception(
            self, storage_mock, presenter_mock, elastic_storage
    ):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "username"
        email = "user@email.com"
        team_ids = ['team0', 'team1']
        company_id = 'company0'

        interactor = EditUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        storage_mock.is_user_admin.return_value = False
        presenter_mock.response_for_user_is_not_admin_exception.return_value = Mock()

        add_user_details_dto = AddUserDetailsDTOFactory(
            name=name, email=email, team_ids=team_ids, company_id=company_id
        )

        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id,
            add_user_details_dto=add_user_details_dto, presenter=presenter_mock
        )

        # Assert
        storage_mock.is_user_admin.assert_called_once_with(
            user_id=admin_user_id
        )
        presenter_mock.response_for_user_is_not_admin_exception.assert_called_once()

    def test_validate_name_returns_should_contain_minimum_5_characters_exception(
            self, storage_mock, presenter_mock, elastic_storage
    ):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "user"
        email = "user@email.com"
        team_ids = ['team0', 'team1']
        company_id = 'company0'

        interactor = EditUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        storage_mock.is_user_admin.return_value = True
        presenter_mock.response_for_invalid_name_length_exception \
            .return_value = Mock()

        add_user_details_dto = AddUserDetailsDTOFactory(
            name=name, email=email, team_ids=team_ids, company_id=company_id
        )

        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id,
            add_user_details_dto=add_user_details_dto, presenter=presenter_mock
        )

        # Assert
        presenter_mock.response_for_invalid_name_length_exception. \
            assert_called_once()

    def test_validate_name_when_contains_special_characters_and_numbers_throw_exception(
            self, storage_mock, presenter_mock, elastic_storage
    ):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "user@2"
        email = "user@email.com"
        team_ids = ['team0', 'team1']
        company_id = 'company0'

        interactor = EditUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        storage_mock.is_user_admin.return_value = True
        presenter_mock.response_for_name_contains_special_character_exception \
            .return_value = Mock()

        add_user_details_dto = AddUserDetailsDTOFactory(
            name=name, email=email, team_ids=team_ids,
            company_id=company_id
        )

        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id,
            add_user_details_dto=add_user_details_dto, presenter=presenter_mock
        )

        # Assert
        presenter_mock.response_for_name_contains_special_character_exception. \
            assert_called_once()

    def test_validate_email_and_throw_exception(
            self, storage_mock, presenter_mock, elastic_storage
    ):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "username"
        email = ""
        team_ids = ['team0', 'team1']
        company_id = 'company0'

        interactor = EditUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        storage_mock.is_user_admin.return_value = True
        presenter_mock.response_for_invalid_email_exception.return_value = Mock()

        add_user_details_dto = AddUserDetailsDTOFactory(
            name=name, email=email, team_ids=team_ids, company_id=company_id
        )

        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id,
            add_user_details_dto=add_user_details_dto, presenter=presenter_mock
        )

        # Assert
        presenter_mock.response_for_invalid_email_exception.assert_called_once()

    # def test_validate_roles_and_throw_exception(
    #         self, storage_mock, presenter_mock, elastic_storage):
    #     # Arrange
    #     user_id = "user_1"
    #     admin_user_id = "user_0"
    #     name = "username"
    #     email = "user@gmail.com"
    #     team_ids = ['team0', 'team1']
    #     role_ids = ['role0', 'role1']
    #     company_id = 'company0'
    #
    #     interactor = EditUserInteractor(
    #         user_storage=storage_mock, elastic_storage=elastic_storage
    #     )
    #     storage_mock.is_user_admin.return_value = True
    #     storage_mock.check_are_valid_role_ids.return_value = False
    #     storage_mock.check_are_valid_team_ids.return_value = True
    #     storage_mock.check_is_exists_company_id.return_value = True
    #     presenter_mock.response_for_invalid_role_ids_exception.return_value = Mock()
    #
    #     add_user_details_dto = AddUserDetailsDTOFactory(
    #         name=name, email=email, team_ids=team_ids,
    #         company_id=company_id
    #     )
    #
    #     # Act
    #     interactor.edit_user_wrapper(
    #         admin_user_id=admin_user_id, user_id=user_id,
    #         add_user_details_dto=add_user_details_dto,
    #         presenter=presenter_mock)
    #
    #     # Assert
    #     storage_mock.check_are_valid_role_ids.assert_called_once()
    #     presenter_mock.response_for_invalid_role_ids_exception.assert_called_once()

    def test_validate_teams_and_throw_exception(
            self, storage_mock, presenter_mock, elastic_storage
    ):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "username"
        email = "user@gmail.com"
        team_ids = ['team0', 'team1']
        company_id = 'company0'

        interactor = EditUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        storage_mock.is_user_admin.return_value = True
        storage_mock.check_are_valid_team_ids.return_value = False
        presenter_mock.response_for_invalid_team_ids_exception.return_value = Mock()

        add_user_details_dto = AddUserDetailsDTOFactory(
            name=name, email=email, team_ids=team_ids, company_id=company_id
        )

        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id,
            add_user_details_dto=add_user_details_dto, presenter=presenter_mock
        )

        # Assert
        storage_mock.check_are_valid_team_ids.assert_called_once()
        presenter_mock.response_for_invalid_team_ids_exception.assert_called_once()

    def test_validate_company_id_and_throw_exception(
            self, storage_mock, presenter_mock, elastic_storage
    ):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "username"
        email = "user@gmail.com"
        team_ids = ['team0', 'team1']
        company_id = 'company0'

        interactor = EditUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        storage_mock.is_user_admin.return_value = True
        storage_mock.check_are_valid_team_ids.return_value = True
        storage_mock.check_is_exists_company_id.return_value = False
        presenter_mock.response_for_invalid_company_ids_exception.return_value = Mock()

        add_user_details_dto = AddUserDetailsDTOFactory(
            name=name, email=email, team_ids=team_ids, company_id=company_id
        )

        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id,
            add_user_details_dto=add_user_details_dto, presenter=presenter_mock
        )

        # Assert
        storage_mock.check_is_exists_company_id.assert_called_once_with(
            company_id=company_id
        )
        presenter_mock.response_for_invalid_company_ids_exception.assert_called_once()

    def test_edit_user_when_user_does_not_exist_raise_exception(
            self, storage_mock, presenter_mock, elastic_storage
    ):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "username"
        email = "user@gmail.com"
        team_ids = ['team0', 'team1']
        company_id = 'company0'

        interactor = EditUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        storage_mock.is_user_admin.return_value = True
        storage_mock.is_user_exist.return_value = False
        presenter_mock.raise_user_does_not_exist.return_value = Mock()

        add_user_details_dto = AddUserDetailsDTOFactory(
            name=name, email=email, team_ids=team_ids,
            company_id=company_id
        )

        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id,
            add_user_details_dto=add_user_details_dto, presenter=presenter_mock
        )

        # Assert
        storage_mock.is_user_exist.assert_called_once_with(user_id=user_id)
        presenter_mock.raise_user_does_not_exist.assert_called_once()

    def test_edit_user_update_user_details_with_valid_details(
            self, storage_mock, presenter_mock, mocker, elastic_storage
    ):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "username"
        email = "user@gmail.com"
        team_ids = ['team0', 'team1']
        company_id = 'company0'

        interactor = EditUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        storage_mock.is_user_admin.return_value = True
        storage_mock.is_user_exist.return_value = True
        presenter_mock.raise_user_does_not_exist.return_value = Mock()
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import update_user_profile_adapter_mock
        adapter_mock = update_user_profile_adapter_mock(mocker=mocker)

        add_user_details_dto = AddUserDetailsDTOFactory(
            name=name, email=email, team_ids=team_ids, company_id=company_id
        )

        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id,
            add_user_details_dto=add_user_details_dto, presenter=presenter_mock
        )

        # Assert
        storage_mock.is_user_exist.assert_called_once_with(user_id=user_id)
        adapter_mock.assert_called_once()
        elastic_storage.update_elastic_user.assert_called_once_with(
            user_id=user_id, name=name
        )

    def test_edit_user_unassign_existing_stats_for_user(
            self, storage_mock, presenter_mock, mocker, elastic_storage
    ):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "username"
        email = "user@gmail.com"
        team_ids = ['team0', 'team1']
        company_id = 'company0'

        interactor = EditUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import update_user_profile_adapter_mock
        adapter_mock = update_user_profile_adapter_mock(mocker=mocker)

        add_user_details_dto = AddUserDetailsDTOFactory(
            name=name, email=email, team_ids=team_ids, company_id=company_id
        )

        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id,
            add_user_details_dto=add_user_details_dto, presenter=presenter_mock
        )

        # Assert
        adapter_mock.assert_called_once()
        storage_mock.remove_teams_for_user.assert_called_once_with(
            user_id=user_id
        )

    def test_edit_user_assign_existing_stats_for_user_after_unassigning_returns_success_response(
            self, storage_mock, presenter_mock, mocker, elastic_storage
    ):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "username"
        email = "user@gmail.com"
        team_ids = ['team0', 'team1']
        company_id = 'company0'

        interactor = EditUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import update_user_profile_adapter_mock
        adapter_mock = update_user_profile_adapter_mock(mocker=mocker)
        presenter_mock.edit_user_success_response.return_value = Mock()

        add_user_details_dto = AddUserDetailsDTOFactory(
            name=name, email=email, team_ids=team_ids,
            company_id=company_id
        )

        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id,
            add_user_details_dto=add_user_details_dto,
            presenter=presenter_mock)

        # Assert
        adapter_mock.assert_called_once()
        storage_mock.add_user_to_the_teams.assert_called_once_with(
            user_id=user_id, team_ids=team_ids
        )
        storage_mock.update_user_details.assert_called_once_with(
            user_id=user_id, name=name, company_id=company_id
        )
        presenter_mock.edit_user_success_response.assert_called_once()

    def test_edit_user_given_company_is_none_returns_success_response(
            self, storage_mock, presenter_mock, mocker, elastic_storage
    ):
        # Arrange
        user_id = "user_1"
        admin_user_id = "user_0"
        name = "username"
        email = "user@gmail.com"
        team_ids = ['team0', 'team1']
        company_id = None

        interactor = EditUserInteractor(
            user_storage=storage_mock, elastic_storage=elastic_storage
        )
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import update_user_profile_adapter_mock
        adapter_mock = update_user_profile_adapter_mock(mocker=mocker)
        presenter_mock.edit_user_success_response.return_value = Mock()

        add_user_details_dto = AddUserDetailsDTOFactory(
            name=name, email=email, team_ids=team_ids,
            company_id=company_id
        )

        # Act
        interactor.edit_user_wrapper(
            admin_user_id=admin_user_id, user_id=user_id,
            add_user_details_dto=add_user_details_dto, presenter=presenter_mock
        )

        # Assert
        adapter_mock.assert_called_once()
        storage_mock.add_user_to_the_teams.assert_called_once_with(
            user_id=user_id, team_ids=team_ids
        )
        storage_mock.update_user_details.assert_called_once_with(
            user_id=user_id, name=name, company_id=company_id
        )
        presenter_mock.edit_user_success_response.assert_called_once()
