from unittest.mock import create_autospec

import pytest

from ib_iam.interactors.project_interactor import ProjectInteractor


class TestGetUserStatusForGivenProjects:
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

    def test_get_user_status_for_given_project_valid_details_then_return_response_dto(
            self, init_interactor, project_storage_mock, user_storage_mock,
            team_storage_mock
    ):
        user_id = "1"
        project_ids = ["1", "2"]
        project_ids = list(set(project_ids))
        from ib_iam.interactors.dtos.dtos import \
            UserIdWithProjectIdAndStatusDTO
        valid_user_exist_project_ids = ["1"]
        expected_result = [
            UserIdWithProjectIdAndStatusDTO(
                user_id=user_id,
                project_id=project_id,
                is_exist=project_id in valid_user_exist_project_ids
            ) for project_id in project_ids
        ]
        interactor = init_interactor
        user_storage_mock.is_user_exist.return_value = True
        project_storage_mock.get_valid_project_ids_from_given_project_ids. \
            return_value = project_ids
        project_storage_mock.get_user_status_for_given_projects.return_value = \
            expected_result

        interactor.get_user_status_for_given_projects(
            user_id=user_id, project_ids=project_ids)

        user_storage_mock.is_user_exist.assert_called_once_with(
            user_id=user_id)
        project_storage_mock.get_valid_project_ids_from_given_project_ids. \
            assert_called_once_with(project_ids=project_ids)
        project_storage_mock.get_user_status_for_given_projects. \
            assert_called_once_with(user_id=user_id, project_ids=project_ids)

    def test_given_invalid_user_id_then_raise_exception(
            self, init_interactor, project_storage_mock, user_storage_mock,
            team_storage_mock
    ):
        user_id = "1"
        project_ids = ["1", "2"]
        interactor = init_interactor
        user_storage_mock.is_user_exist.return_value = False

        from ib_iam.exceptions.custom_exceptions import InvalidUserId
        with pytest.raises(InvalidUserId):
            interactor.get_user_status_for_given_projects(
                user_id=user_id, project_ids=project_ids)

        user_storage_mock.is_user_exist.assert_called_once_with(
            user_id=user_id)

    def test_given_invalid_project_ids_then_raise_exception(
            self, init_interactor, project_storage_mock, user_storage_mock,
            team_storage_mock
    ):
        user_id = "1"
        project_ids = ["1", "2"]
        project_ids = list(set(project_ids))
        valid_project_ids = ["1"]
        invalid_project_ids = ["2"]
        interactor = init_interactor
        user_storage_mock.is_user_exist.return_value = True
        project_storage_mock.get_valid_project_ids_from_given_project_ids. \
            return_value = valid_project_ids

        from ib_iam.exceptions.custom_exceptions import InvalidProjectIds
        with pytest.raises(InvalidProjectIds) as err:
            interactor.get_user_status_for_given_projects(
                user_id=user_id, project_ids=project_ids)

        user_storage_mock.is_user_exist.assert_called_once_with(
            user_id=user_id)
        project_storage_mock.get_valid_project_ids_from_given_project_ids. \
            assert_called_once_with(project_ids=project_ids)
        assert err.value.project_ids == invalid_project_ids
