from unittest.mock import create_autospec

import pytest

from ib_iam.interactors.project_interactor import ProjectInteractor


class TestAddProjectsInteractor:

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
    def interactor(
            self, project_storage_mock, user_storage_mock, team_storage_mock
    ):
        interactor = ProjectInteractor(
            project_storage=project_storage_mock,
            user_storage=user_storage_mock, team_storage=team_storage_mock
        )
        return interactor

    def test_given_valid_project_dtos_adds_projects_to_db_successfully(
            self, interactor, project_storage_mock, user_storage_mock,
            team_storage_mock
    ):
        # Arrange
        from ib_iam.tests.factories.storage_dtos import ProjectDTOFactory
        project_dtos = ProjectDTOFactory.create_batch(size=2)

        # Act
        interactor.add_projects(project_dtos=project_dtos)

        # Assert
        project_storage_mock.add_projects.assert_called_once_with(
            project_dtos=project_dtos
        )
