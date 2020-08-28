from unittest.mock import create_autospec

import pytest

from ib_iam.interactors.project_interactor import ProjectInteractor


class TestGetProjectDTOs:
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

    def test_get_project_dtos_for_give_project_ids(
            self, init_interactor, project_storage_mock, user_storage_mock,
            team_storage_mock):
        # Arrange
        interactor = init_interactor
        project_ids = ["1"]
        from ib_iam.tests.factories.storage_dtos import ProjectDTOFactory
        project_dtos = [
            ProjectDTOFactory.create(project_id=project_id)
            for project_id in project_ids]
        project_storage_mock.get_project_dtos_for_given_project_ids.return_value = \
            project_dtos

        # Act
        interactor.get_project_dtos_bulk(
            project_ids=project_ids)

        # Assert
        project_storage_mock.get_project_dtos_for_given_project_ids.\
            assert_called_once_with(project_ids=project_ids)

    def test_get_project_dtos_for_give_invalid_project_ids_then_raise_exception(
            self, init_interactor, project_storage_mock, user_storage_mock,
            team_storage_mock):
        project_ids = ["1", "2"]
        interactor = init_interactor
        from ib_iam.exceptions.custom_exceptions import InvalidProjectIds
        project_storage_mock.get_project_dtos_for_given_project_ids.side_effect = \
            InvalidProjectIds(project_ids=project_ids)

        with pytest.raises(InvalidProjectIds):
            interactor.get_project_dtos_bulk(project_ids=project_ids)
