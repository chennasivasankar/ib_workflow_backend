from unittest.mock import create_autospec

import pytest

from ib_iam.interactors.project_interactor import ProjectInteractor


class TestGetProjectRoleIds:
    @pytest.fixture
    def project_storage(self):
        from ib_iam.interactors.storage_interfaces \
            .project_storage_interface import ProjectStorageInterface
        project_storage_mock = create_autospec(ProjectStorageInterface)
        return project_storage_mock

    @pytest.fixture
    def user_storage(self):
        from ib_iam.interactors.storage_interfaces \
            .user_storage_interface import UserStorageInterface
        user_storage_mock = create_autospec(UserStorageInterface)
        return user_storage_mock

    @pytest.fixture
    def team_storage(self):
        from ib_iam.interactors.storage_interfaces \
            .team_storage_interface import TeamStorageInterface
        team_storage_mock = create_autospec(TeamStorageInterface)
        return team_storage_mock

    @pytest.fixture
    def interactor(
            self, project_storage, user_storage, team_storage):
        interactor = ProjectInteractor(project_storage=project_storage,
                                       user_storage=user_storage,
                                       team_storage=team_storage)
        return interactor

    def test_given_invalid_project_id_raises_invalid_project_id_exception(
            self, interactor, project_storage):
        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        project_id = "project_1"
        project_storage.is_valid_project_id.return_value = False

        with pytest.raises(InvalidProjectId):
            interactor.get_project_role_ids(project_id=project_id)

        project_storage.is_valid_project_id.assert_called_once_with(
            project_id=project_id)

    def test_get_project_role_ids_returns_role_ids(
            self, interactor, project_storage):
        project_id = "project_1"
        expected_project_role_ids = ["role_1", "role_2"]
        project_storage.get_project_role_ids \
            .return_value = expected_project_role_ids

        actual_project_role_ids = interactor.get_project_role_ids(
            project_id=project_id)

        project_storage.is_valid_project_id.assert_called_once_with(
            project_id=project_id)
        project_storage.get_project_role_ids.assert_called_once_with(
            project_id=project_id)
        assert actual_project_role_ids == expected_project_role_ids
