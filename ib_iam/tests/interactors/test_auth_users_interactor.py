from unittest.mock import Mock, create_autospec

import pytest


class TestAuthUsersInteractor:

    @pytest.fixture()
    def user_storage_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        storage = create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture()
    def elastic_storage_mock(self):
        from unittest import mock
        from ib_iam.interactors.storage_interfaces.elastic_storage_interface \
            import ElasticSearchStorageInterface
        storage = mock.create_autospec(ElasticSearchStorageInterface)
        return storage

    @pytest.fixture()
    def team_member_level_storage_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.storage_interfaces.team_member_level_storage_interface import \
            TeamMemberLevelStorageInterface
        storage = create_autospec(TeamMemberLevelStorageInterface)
        return storage

    @pytest.fixture()
    def team_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.team_storage_interface import \
            TeamStorageInterface
        from unittest.mock import create_autospec
        team_storage_mock = create_autospec(TeamStorageInterface)
        return team_storage_mock

    @pytest.fixture()
    def project_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.project_storage_interface import \
            ProjectStorageInterface
        project_storage_mock = create_autospec(ProjectStorageInterface)
        return project_storage_mock

    @pytest.fixture()
    def interactor(
            self, user_storage_mock, elastic_storage_mock, team_storage_mock,
            team_member_level_storage_mock, project_storage_mock
    ):
        from ib_iam.interactors.auth_users_interactor import AuthUsersInteractor
        interactor = AuthUsersInteractor(
            user_storage=user_storage_mock,
            elastic_storage=elastic_storage_mock,
            team_storage=team_storage_mock,
            team_member_level_storage=team_member_level_storage_mock,
            project_storage=project_storage_mock
        )
        return interactor

    def test_with_valid_details_create_data(
            self, interactor, user_storage_mock, elastic_storage_mock, mocker,
            team_member_level_storage_mock, team_storage_mock,
            project_storage_mock
    ):
        # Arrange
        project_id = "FIN_MAN"
        from ib_iam.tests.factories.interactor_dtos import AuthUserDTOFactory
        auth_user_dtos = AuthUserDTOFactory.create_batch(size=3)

        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            create_user_account_with_email_mock, create_user_profile_mock
        create_user_account_with_email_mock = \
            create_user_account_with_email_mock(mocker)
        create_user_profile_mock = create_user_profile_mock(mocker)

        team_storage_mock.get_or_create_team_with_name.return_value = Mock(), False

        # Act
        interactor.auth_user_dtos(
            auth_user_dtos=auth_user_dtos,
            project_id=project_id
        )

        # Assert
        assert create_user_account_with_email_mock.call_count == 3
        assert create_user_profile_mock.call_count == 3
        assert user_storage_mock.create_user.call_count == 3
        assert user_storage_mock.create_auth_user.call_count == 3
        assert elastic_storage_mock.create_elastic_user.call_count == 3
        team_storage_mock.get_or_create_team_with_name.assert_called_once()
        team_storage_mock.add_users_to_team.assert_called_once()
        team_member_level_storage_mock. \
            get_or_create_team_member_level_hierarchy.assert_called_once()
        team_member_level_storage_mock. \
            add_members_to_levels_for_a_team.assert_called_once()