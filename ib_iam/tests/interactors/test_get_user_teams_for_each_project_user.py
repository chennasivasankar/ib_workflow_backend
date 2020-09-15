from unittest.mock import create_autospec

import pytest


class TestGetUserTeamsForEachProjectUser:

    @pytest.fixture
    def project_storage_mock(self):
        from ib_iam.interactors.storage_interfaces \
            .project_storage_interface import ProjectStorageInterface
        return create_autospec(ProjectStorageInterface)

    @pytest.fixture
    def user_storage_mock(self):
        from ib_iam.interactors.storage_interfaces \
            .user_storage_interface import UserStorageInterface
        return create_autospec(UserStorageInterface)

    @pytest.fixture
    def team_storage_mock(self):
        from ib_iam.interactors.storage_interfaces \
            .team_storage_interface import TeamStorageInterface
        return create_autospec(TeamStorageInterface)

    @pytest.fixture
    def interactor(
            self, project_storage_mock, user_storage_mock, team_storage_mock
    ):
        from ib_iam.interactors.project_interactor import ProjectInteractor
        return ProjectInteractor(
            project_storage=project_storage_mock,
            user_storage=user_storage_mock,
            team_storage=team_storage_mock
        )

    def test_given_invalid_project_id_raises_invalid_project_id_exception(
            self, interactor, project_storage_mock
    ):
        # Arrange
        project_id = "project_1"
        project_storage_mock.get_valid_project_ids.return_value = []

        # Act
        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        with pytest.raises(InvalidProjectId):
            interactor.get_user_teams_for_each_project_user(
                user_ids=["1"], project_id=project_id
            )

        # Assert
        project_storage_mock.get_valid_project_ids.assert_called_once_with(
            project_ids=[project_id]
        )

    def test_given_invalid_user_ids_raises_invalid_user_ids_exception(
            self, interactor, user_storage_mock, project_storage_mock
    ):
        # Arrange
        project_id = "project_1"
        user_ids = ["user_1"]
        project_storage_mock.get_valid_project_ids.return_value = [project_id]
        user_storage_mock.get_valid_user_ids.return_value = []

        # Act
        from ib_iam.exceptions.custom_exceptions import InvalidUserIds
        with pytest.raises(InvalidUserIds) as err:
            interactor.get_user_teams_for_each_project_user(
                user_ids=user_ids, project_id=project_id
            )

        # Assert
        user_storage_mock.get_valid_user_ids.assert_called_once_with(
            user_ids=user_ids
        )
        assert err.value.user_ids == user_ids

    def test_given_non_project_users_raises_users_not_exists_for_given_project_exception(
            self, interactor, user_storage_mock, project_storage_mock,
            team_storage_mock
    ):
        # Arrange
        project_id = "project_1"
        user_ids = ["user_1"]
        team_ids = ["team_1"]
        project_storage_mock.get_valid_project_ids.return_value = [project_id]
        user_storage_mock.get_valid_user_ids.return_value = user_ids
        project_storage_mock.get_team_ids.return_value = team_ids
        team_storage_mock.get_team_user_dtos.return_value = []

        # Act
        from ib_iam.interactors.project_interactor import \
            UsersNotExistsForGivenProject
        with pytest.raises(UsersNotExistsForGivenProject) as err:
            interactor.get_user_teams_for_each_project_user(
                user_ids=user_ids, project_id=project_id
            )

        # Assert
        project_storage_mock.get_team_ids.assert_called_once_with(
            project_id=project_id
        )
        team_storage_mock.get_team_user_dtos.assert_called_once_with(
            user_ids=user_ids, team_ids=team_ids
        )
        assert err.value.user_ids == user_ids

    def test_given_valid_details_returns_user_team_dtos(
            self, interactor, user_storage_mock, project_storage_mock,
            team_storage_mock
    ):
        # Arrange
        project_id = "project_1"
        user_ids = ["user_1"]
        team_ids = ["team_1"]
        project_storage_mock.get_valid_project_ids.return_value = [project_id]
        user_storage_mock.get_valid_user_ids.return_value = user_ids
        project_storage_mock.get_team_ids.return_value = team_ids
        from ib_iam.tests.factories.storage_dtos import UserTeamDTOFactory
        UserTeamDTOFactory.reset_sequence(1)
        user_team_dtos = [
            UserTeamDTOFactory(user_id=user_ids[0], team_id=team_ids[0])
        ]
        team_storage_mock.get_team_user_dtos.return_value = user_team_dtos
        from ib_iam.app_interfaces.dtos import UserTeamsDTO
        from ib_iam.interactors.storage_interfaces.dtos import TeamIdAndNameDTO
        user_teams = [TeamIdAndNameDTO(team_id='team_1', team_name='team 1')]
        expected_response = [
            UserTeamsDTO(user_id='user_1', user_teams=user_teams)
        ]

        # Act
        actual_response = interactor.get_user_teams_for_each_project_user(
            user_ids=user_ids, project_id=project_id
        )

        # Assert
        project_storage_mock.get_team_ids.assert_called_once_with(
            project_id=project_id
        )
        team_storage_mock.get_team_user_dtos.assert_called_once_with(
            user_ids=user_ids, team_ids=team_ids
        )
        assert actual_response == expected_response
