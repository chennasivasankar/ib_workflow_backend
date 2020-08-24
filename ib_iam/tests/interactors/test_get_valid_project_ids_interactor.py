from unittest.mock import create_autospec

import pytest

from ib_iam.interactors.project_interactor import ProjectInteractor


class TestGetValidProjectIdsInteractor:

    @pytest.fixture
    def project_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.project_storage_interface import \
            ProjectStorageInterface
        project_storage_mock = create_autospec(ProjectStorageInterface)
        return project_storage_mock

    @pytest.fixture
    def user_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        user_storage_mock = create_autospec(UserStorageInterface)
        return user_storage_mock

    @pytest.fixture
    def team_storage_mock(self):
        from ib_iam.interactors.storage_interfaces.team_storage_interface import \
            TeamStorageInterface
        team_storage_mock = create_autospec(TeamStorageInterface)
        return team_storage_mock

    @pytest.fixture
    def init_interactor(
            self, project_storage_mock, user_storage_mock, team_storage_mock):
        interactor = ProjectInteractor(
            project_storage=project_storage_mock,
            user_storage=user_storage_mock,
            team_storage=team_storage_mock
        )
        return interactor

    def test_given_valid_project_dtos_adds_projects_to_db_successfully(
            self, init_interactor, project_storage_mock, user_storage_mock,
            team_storage_mock):
        # Arrange
        interactor = init_interactor
        project_ids = ["1", "2", "3"]
        valid_project_ids = ["1", "2"]
        project_storage_mock.get_valid_project_ids_from_given_project_ids \
            .return_value = valid_project_ids
        expected_response = valid_project_ids

        # Act
        response = interactor.get_valid_project_ids(project_ids=project_ids)

        # Assert
        project_storage_mock.get_valid_project_ids_from_given_project_ids \
            .assert_called_once_with(project_ids=project_ids)
        assert response == expected_response
