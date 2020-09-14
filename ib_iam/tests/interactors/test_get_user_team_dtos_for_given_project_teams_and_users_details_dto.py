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
        from ib_iam.tests.factories.adapter_dtos import \
            ProjectTeamsAndUsersDTOFactory
        project_teams_and_users_dto = ProjectTeamsAndUsersDTOFactory(
            project_id=project_id
        )
        project_storage_mock.get_valid_project_ids.return_value = []

        # Act
        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        with pytest.raises(InvalidProjectId):
            interactor.get_user_team_dtos_for_given_project_teams_and_users_details_dto(
                project_teams_and_users_dto=project_teams_and_users_dto
            )

        # Assert
        project_storage_mock.get_valid_project_ids.assert_called_once_with(
            project_ids=[project_id]
        )

    def test_given_invalid_team_ids_raises_invalid_team_ids_exception(
            self, interactor, project_storage_mock
    ):
        # Arrange
        project_id = "project_1"
        team_ids = ["team_1"]
        from ib_iam.tests.factories.adapter_dtos import \
            ProjectTeamsAndUsersDTOFactory, UserIdWithTeamIdDTOFactory
        user_id_with_team_id_dtos = [
            UserIdWithTeamIdDTOFactory(team_id=team_ids[0])
        ]
        project_teams_and_users_dto = ProjectTeamsAndUsersDTOFactory(
            project_id=project_id,
            user_id_with_team_id_dtos=user_id_with_team_id_dtos
        )
        project_storage_mock.get_valid_project_ids.return_value = [project_id]
        project_storage_mock.get_valid_team_ids.return_value = []

        # Act
        from ib_iam.interactors.project_interactor import \
            TeamsNotExistForGivenProject
        with pytest.raises(TeamsNotExistForGivenProject) as err:
            interactor.get_user_team_dtos_for_given_project_teams_and_users_details_dto(
                project_teams_and_users_dto=project_teams_and_users_dto
            )

        # Assert
        project_storage_mock.get_valid_team_ids.assert_called_once_with(
            project_id=project_id, team_ids=team_ids
        )
        assert err.value.team_ids == team_ids

    def test_given_invalid_user_ids_raises_invalid_user_ids_exception(
            self, interactor, project_storage_mock, team_storage_mock
    ):
        # Arrange
        project_id = "project_1"
        team_ids = ["team_1"]
        user_ids = ["user_1"]
        from ib_iam.tests.factories.adapter_dtos import \
            ProjectTeamsAndUsersDTOFactory, UserIdWithTeamIdDTOFactory
        user_id_with_team_id_dtos = [
            UserIdWithTeamIdDTOFactory(
                team_id=team_ids[0], user_id=user_ids[0]
            )
        ]
        project_teams_and_users_dto = ProjectTeamsAndUsersDTOFactory(
            project_id=project_id,
            user_id_with_team_id_dtos=user_id_with_team_id_dtos
        )
        project_storage_mock.get_valid_project_ids.return_value = [project_id]
        project_storage_mock.get_valid_team_ids.return_value = team_ids
        team_storage_mock.get_team_user_dtos.return_value = []

        # Act
        from ib_iam.interactors.project_interactor import \
            UsersNotExistsForGivenTeams
        with pytest.raises(UsersNotExistsForGivenTeams) as err:
            interactor.get_user_team_dtos_for_given_project_teams_and_users_details_dto(
                project_teams_and_users_dto=project_teams_and_users_dto
            )

        # Assert
        team_storage_mock.get_team_user_dtos.assert_called_once_with(
            team_ids=team_ids, user_ids=user_ids
        )
        assert err.value.user_ids == user_ids

    def test_given_valid_details_returns_team_user_dtos(
            self, interactor, project_storage_mock, team_storage_mock
    ):
        # Arrange
        project_id = "project_1"
        team_ids = ["team_1"]
        user_ids = ["user_1"]
        from ib_iam.tests.factories.adapter_dtos import \
            ProjectTeamsAndUsersDTOFactory, UserIdWithTeamIdDTOFactory
        user_id_with_team_id_dtos = [
            UserIdWithTeamIdDTOFactory(
                team_id=team_ids[0], user_id=user_ids[0]
            )
        ]
        from ib_iam.tests.factories.storage_dtos import UserTeamDTOFactory
        team_user_dtos = [
            UserTeamDTOFactory(user_id=user_ids[0], team_id=team_ids[0])
        ]
        project_teams_and_users_dto = ProjectTeamsAndUsersDTOFactory(
            project_id=project_id,
            user_id_with_team_id_dtos=user_id_with_team_id_dtos
        )
        project_storage_mock.get_valid_project_ids.return_value = [
            project_id]
        project_storage_mock.get_valid_team_ids.return_value = team_ids
        team_storage_mock.get_team_user_dtos.return_value = team_user_dtos

        # Act
        actual_team_user_dtos = interactor.get_user_team_dtos_for_given_project_teams_and_users_details_dto(
            project_teams_and_users_dto=project_teams_and_users_dto
        )

        # Assert
        team_storage_mock.get_team_user_dtos.assert_called_once_with(
            user_ids=user_ids, team_ids=team_ids
        )
        assert actual_team_user_dtos == team_user_dtos
