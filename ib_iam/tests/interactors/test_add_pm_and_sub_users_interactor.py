from unittest.mock import create_autospec

import pytest

from ib_workflows_backend.settings.base_swagger_utils import \
    JGC_DRIVE_PROJECT_ID


class TestPMAndSubUsersInteractor:

    @pytest.fixture()
    def user_storage_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        storage = create_autospec(UserStorageInterface)
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
            self, user_storage_mock, team_storage_mock,
            team_member_level_storage_mock, project_storage_mock
    ):
        from ib_iam.interactors.users.add_pm_and_sub_users_interactor import \
            PMAndSubUsersInteractor
        interactor = PMAndSubUsersInteractor(
            user_storage=user_storage_mock,
            team_storage=team_storage_mock,
            team_member_level_storage=team_member_level_storage_mock,
            project_storage=project_storage_mock
        )
        return interactor

    @pytest.fixture
    def pm_and_sub_user_dtos(self):
        from ib_iam.interactors.dtos.dtos import PMAndSubUsersAuthTokensDTO
        return [
            PMAndSubUsersAuthTokensDTO(
                pm_auth_token="pm_token_1",
                sub_user_auth_token="sub_user_token_1"
            ),
            PMAndSubUsersAuthTokensDTO(
                pm_auth_token="pm_token_2",
                sub_user_auth_token="sub_user_token_2"
            ),
            PMAndSubUsersAuthTokensDTO(
                pm_auth_token="pm_token_2",
                sub_user_auth_token="sub_user_token_3"
            )
        ]

    @pytest.fixture
    def user_id_with_token_dtos(self):
        from ib_iam.interactors.storage_interfaces.dtos import \
            UserIdWithTokenDTO
        return [
            UserIdWithTokenDTO(user_id="user_id_1", token="pm_token_1"),
            UserIdWithTokenDTO(user_id="user_id_2", token="sub_user_token_1"),
            UserIdWithTokenDTO(user_id="user_id_3", token="pm_token_2"),
            UserIdWithTokenDTO(user_id="user_id_4", token="sub_user_token_2"),
            UserIdWithTokenDTO(user_id="user_id_5", token="sub_user_token_3")
        ]

    def test_given_valid_data_it_maps_and_creates_pms_and_their_sub_users(
            self, interactor, user_storage_mock, team_storage_mock,
            team_member_level_storage_mock, project_storage_mock,
            pm_and_sub_user_dtos, user_id_with_token_dtos, mocker
    ):
        # Arrange
        project_id = JGC_DRIVE_PROJECT_ID
        # team_ids = ["team_id_1", "team_id_2"]
        team_creation_values = [("team_id_1", False), ("team_id_2", False)]
        user_storage_mock.get_user_and_token_dtos.return_value = \
            user_id_with_token_dtos
        team_storage_mock.get_or_create_team_with_name.side_effect = \
            team_creation_values

        # Act
        interactor.add_pm_and_sub_users(
            pm_and_sub_user_dtos=pm_and_sub_user_dtos, project_id=project_id
        )

        # Assert
        user_storage_mock.get_user_and_token_dtos.assert_called_once()
        assert team_storage_mock.get_or_create_team_with_name.call_count == 2
        assert team_storage_mock.add_users_to_team.call_count == 2
        project_storage_mock.assign_teams_to_projects.assert_not_called()
        assert team_member_level_storage_mock \
                   .get_or_create_team_member_level_hierarchy.call_count == 4
        assert team_member_level_storage_mock \
                   .add_members_to_levels_for_a_team.call_count == 2
        assert team_member_level_storage_mock \
                   .add_members_to_superiors.call_count == 2
