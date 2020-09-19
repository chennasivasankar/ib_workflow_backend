from unittest.mock import create_autospec

import pytest

from ib_iam.interactors.project_interactor import ProjectInteractor


class TestIsValidUserForGivenProject:
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
            self, project_storage_mock, user_storage_mock, team_storage_mock):
        interactor = ProjectInteractor(
            project_storage=project_storage_mock,
            user_storage=user_storage_mock, team_storage=team_storage_mock
        )
        return interactor

    def test_check_is_valid_user_id_given_project_then_return_bool_value_as_true(
            self, interactor, project_storage_mock, user_storage_mock,
            team_storage_mock
    ):
        # Arrange
        user_id = "1"
        project_id = "1"
        user_storage_mock.is_user_exist.return_value = True
        project_storage_mock.get_valid_project_ids. \
            return_value = [project_id]
        project_storage_mock.is_user_exist_given_project.return_value = True

        # Act
        interactor.is_valid_user_id_for_given_project(
            user_id=user_id, project_id=project_id
        )

        # Assert
        user_storage_mock.is_user_exist.assert_called_once_with(
            user_id=user_id
        )
        project_storage_mock.get_valid_project_ids. \
            assert_called_once_with(project_ids=[project_id])
        project_storage_mock.is_user_exist_given_project. \
            assert_called_once_with(user_id=user_id, project_id=project_id)

    def test_check_is_valid_user_id_given_invalid_project_id__then_raise_exception(
            self, interactor, project_storage_mock, user_storage_mock,
            team_storage_mock
    ):
        # Arrange
        user_id = "1"
        invalid_project_id = "1"
        user_storage_mock.is_user_exist.return_value = True
        project_storage_mock.get_valid_project_ids. \
            return_value = []

        # Act
        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        with pytest.raises(InvalidProjectId):
            interactor.is_valid_user_id_for_given_project(
                user_id=user_id, project_id=invalid_project_id
            )

        # Assert
        user_storage_mock.is_user_exist.assert_called_once_with(
            user_id=user_id
        )
        project_storage_mock.get_valid_project_ids. \
            assert_called_once_with(project_ids=[invalid_project_id])

    def test_check_is_valid_user_id_given_invalid_user_id__then_raise_exception(
            self, interactor, project_storage_mock, user_storage_mock,
            team_storage_mock
    ):
        # Arrange
        user_id = "1"
        project_id = "1"
        user_storage_mock.is_user_exist.return_value = False

        # Act
        from ib_iam.exceptions.custom_exceptions import InvalidUserId
        with pytest.raises(InvalidUserId):
            interactor.is_valid_user_id_for_given_project(
                user_id=user_id, project_id=project_id
            )

        # Assert
        user_storage_mock.is_user_exist.assert_called_once_with(
            user_id=user_id
        )
