import datetime
from unittest.mock import create_autospec, Mock, call

import pytest

from ib_tasks.interactors.get_task_related_rps_in_given_stage import GetTaskRPsInteractor


class TestGetTaskRelatedRps:

    @pytest.fixture
    def storage(self):
        from ib_tasks.interactors.storage_interfaces.storage_interface import \
            StorageInterface
        return create_autospec(StorageInterface)

    @pytest.fixture
    def task_storage(self):
        from ib_tasks.interactors.storage_interfaces.task_storage_interface \
            import TaskStorageInterface
        return create_autospec(TaskStorageInterface)

    @pytest.fixture
    def parameters(self):
        from ib_tasks.interactors.task_dtos import GetTaskRPsParametersDTO
        return GetTaskRPsParametersDTO(
            task_id="IBWF-1",
            stage_id=1,
            user_id="123e4567-e89b-12d3-a456-426614174001"
        )

    @pytest.fixture
    def presenter_mock(self):
        from ib_tasks.interactors.presenter_interfaces.get_task_rps_presenter_interface \
            import GetTaskRpsPresenterInterface
        return create_autospec(GetTaskRpsPresenterInterface)

    def test_given_invalid_task_id_raises_exception(self, storage, task_storage,
                                                    parameters, presenter_mock):
        # Arrange
        task_display_id = parameters.task_id
        task_storage.check_is_valid_task_display_id.return_value = False

        interactor = GetTaskRPsInteractor(storage=storage, task_storage=task_storage)

        # Act
        response = interactor.get_task_rps_wrapper(presenter_mock, parameters)

        # Assert
        task_storage.check_is_valid_task_display_id.assert_called_once_with(
            task_display_id)
        presenter_mock.response_for_invalid_task_id.assert_called_once()

    def test_given_user_is_not_assigned_to_task_raises_exception(
            self, storage, task_storage,
            parameters, presenter_mock):
        # Arrange
        task_display_id = parameters.task_id
        task_id = 1
        stage_id = parameters.stage_id
        user_id = parameters.user_id
        storage.validate_stage_id.return_value = True
        task_storage.check_is_valid_task_display_id.return_value = True
        task_storage.get_task_id_for_task_display_id.return_value = 1
        storage.validate_if_task_is_assigned_to_user_in_given_stage. \
            return_value = False

        interactor = GetTaskRPsInteractor(storage=storage, task_storage=task_storage)

        # Act
        response = interactor.get_task_rps_wrapper(presenter_mock, parameters)

        # Assert
        task_storage.check_is_valid_task_display_id.assert_called_once_with(
            task_display_id)
        storage.validate_if_task_is_assigned_to_user_in_given_stage.assert_called_once_with(
            task_id, user_id, stage_id
        )
        presenter_mock.response_for_user_is_not_assignee_for_task.assert_called_once()

    def test_given_invalid_stage_id_raises_exception(self, storage, task_storage,
                                                     parameters, presenter_mock):
        # Arrange
        task_display_id = parameters.task_id
        task_storage.get_task_id_for_task_display_id.return_value = 1
        task_storage.check_is_valid_task_display_id.return_value = True
        storage.validate_stage_id.return_value = False

        interactor = GetTaskRPsInteractor(storage=storage, task_storage=task_storage)

        # Act
        response = interactor.get_task_rps_wrapper(presenter_mock, parameters)

        # Assert
        task_storage.check_is_valid_task_display_id.assert_called_once_with(
            task_display_id)
        presenter_mock.response_for_invalid_stage_id.assert_called_once()

    def test_when_due_datetime_is_not_changed_and_rp_is_already_added(
            self, storage, task_storage, mocker,
            parameters, presenter_mock):
        # Arrange
        task_display_id = parameters.task_id
        task_id = 1
        team_id = "TEAM_ID_1"
        superior_id = "123e4567-e89b-12d3-a456-426614174002"
        user_ids = [superior_id]
        stage_id = parameters.stage_id
        user_id = parameters.user_id
        expected_response = Mock()
        storage.validate_stage_id.return_value = True
        task_storage.check_is_valid_task_display_id.return_value = True
        task_storage.get_user_team_id.return_value = team_id
        task_storage.get_task_id_for_task_display_id.return_value = 1
        storage.validate_if_task_is_assigned_to_user_in_given_stage. \
            return_value = True
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_immediate_superior_user_id_mock
        superior_mock = get_immediate_superior_user_id_mock(mocker)
        superior_mock.return_value = superior_id
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_user_dtos_given_user_ids
        user_details_mock = get_user_dtos_given_user_ids(mocker)
        storage.get_rp_ids.return_value = user_ids
        storage.get_latest_rp_id_if_exists.return_value = None
        task_storage.get_user_missed_the_task_due_time.return_value = datetime.datetime.now() - datetime.timedelta(days=2)
        storage.get_latest_rp_added_datetime.return_value = datetime.datetime.now()
        presenter_mock.response_for_get_rps_details.return_value = expected_response

        interactor = GetTaskRPsInteractor(storage=storage, task_storage=task_storage)

        # Act
        response = interactor.get_task_rps_wrapper(presenter_mock, parameters)

        # Assert
        assert response == expected_response
        task_storage.check_is_valid_task_display_id.assert_called_once_with(
            task_display_id)
        storage.validate_if_task_is_assigned_to_user_in_given_stage.assert_called_once_with(
            task_id, user_id, stage_id
        )
        storage.get_latest_rp_added_datetime.assert_called_once_with(task_id, stage_id)
        presenter_mock.response_for_get_rps_details.assert_called_once()

    def test_given_valid_details_get_rps_details_when_already_rp_in_db(
            self, storage, task_storage, mocker,
            parameters, presenter_mock):
        # Arrange
        task_display_id = parameters.task_id
        task_id = 1
        team_id = "TEAM_ID_1"
        superior_id = "123e4567-e89b-12d3-a456-426614174002"
        user_ids = [superior_id, "123e4567-e89b-12d3-a456-426614174003"]
        stage_id = parameters.stage_id
        user_id = parameters.user_id
        expected_response = Mock()
        storage.validate_stage_id.return_value = True
        task_storage.check_is_valid_task_display_id.return_value = True
        task_storage.get_user_team_id.return_value = team_id
        task_storage.get_task_id_for_task_display_id.return_value = 1
        storage.validate_if_task_is_assigned_to_user_in_given_stage. \
            return_value = True
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_immediate_superior_user_id_mock
        superior_mock = get_immediate_superior_user_id_mock(mocker)
        superior_mock.return_value = superior_id
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_user_dtos_given_user_ids
        user_details_mock = get_user_dtos_given_user_ids(mocker)
        storage.get_rp_ids.return_value = user_ids
        storage.get_latest_rp_id_if_exists.return_value = superior_id
        storage.get_latest_rp_added_datetime.return_value = datetime.datetime.now() - datetime.timedelta(days=3)
        task_storage.get_user_missed_the_task_due_time.return_value = datetime.datetime.now()
        presenter_mock.response_for_get_rps_details.return_value = expected_response

        interactor = GetTaskRPsInteractor(storage=storage, task_storage=task_storage)

        # Act
        response = interactor.get_task_rps_wrapper(presenter_mock, parameters)

        # Assert
        assert response == expected_response
        task_storage.check_is_valid_task_display_id.assert_called_once_with(
            task_display_id)
        storage.validate_if_task_is_assigned_to_user_in_given_stage.assert_called_once_with(
            task_id, user_id, stage_id
        )

        user_details_mock.assert_called_once_with(user_ids)
        superior_mock.assert_called_once_with(user_id=superior_id, team_id=team_id)
        presenter_mock.response_for_get_rps_details.assert_called_once()

    def test_when_due_datetime_is_not_missed_rp_ids_is_empty(
            self, storage, task_storage, mocker,
            parameters, presenter_mock):
        # Arrange
        task_display_id = parameters.task_id
        task_id = 1
        team_id = "TEAM_ID_1"
        superior_id = "123e4567-e89b-12d3-a456-426614174002"
        user_ids = [superior_id]
        stage_id = parameters.stage_id
        user_id = parameters.user_id
        expected_response = Mock()
        storage.validate_stage_id.return_value = True
        task_storage.check_is_valid_task_display_id.return_value = True
        task_storage.get_user_team_id.return_value = team_id
        task_storage.get_task_id_for_task_display_id.return_value = 1
        storage.validate_if_task_is_assigned_to_user_in_given_stage. \
            return_value = True
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_immediate_superior_user_id_mock
        superior_mock = get_immediate_superior_user_id_mock(mocker)
        superior_mock.return_value = superior_id
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_user_dtos_given_user_ids
        user_details_mock = get_user_dtos_given_user_ids(mocker)
        storage.get_rp_ids.return_value = []
        storage.get_latest_rp_id_if_exists.return_value = None
        task_storage.get_user_missed_the_task_due_time.return_value = datetime.datetime.now() - datetime.timedelta(days=2)
        storage.get_latest_rp_added_datetime.return_value = datetime.datetime.now()
        presenter_mock.response_for_get_rps_details.return_value = expected_response

        interactor = GetTaskRPsInteractor(storage=storage, task_storage=task_storage)

        # Act
        response = interactor.get_task_rps_wrapper(presenter_mock, parameters)

        # Assert
        assert response == expected_response
        task_storage.check_is_valid_task_display_id.assert_called_once_with(
            task_display_id)
        storage.validate_if_task_is_assigned_to_user_in_given_stage.assert_called_once_with(
            task_id, user_id, stage_id
        )
        storage.get_latest_rp_added_datetime.assert_called_once_with(task_id, stage_id)
        presenter_mock.response_for_get_rps_details.assert_called_once()
