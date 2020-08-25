from unittest.mock import create_autospec, Mock

import pytest

from ib_tasks.interactors.get_task_due_missing_reasons import \
    GetTaskDueMissingReasonsInteractor
from ib_tasks.interactors.presenter_interfaces.task_due_missing_details_presenter \
    import TaskDueDetailsPresenterInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.tests.common_fixtures.adapters.assignees_details_service import \
    assignee_details_dtos_mock
from ib_tasks.tests.factories.storage_dtos import TaskDueMissingDTOFactory


class TestGetTaskReasons:

    @pytest.fixture()
    def get_due_missing_details(self):
        TaskDueMissingDTOFactory.reset_sequence(1)
        tasks = TaskDueMissingDTOFactory.create_batch(size=2)
        return tasks

    def test_given_invalid_task_id_raises_exception(self):
        # Arrange
        task_id = "iBWF-1"
        user_id = "user_id_1"
        stage_id = "stage_id_1"
        storage = create_autospec(StorageInterface)
        task_storage = create_autospec(TaskStorageInterface)
        presenter = create_autospec(TaskDueDetailsPresenterInterface)
        interactor = GetTaskDueMissingReasonsInteractor(
            storage=storage, task_storage=task_storage
        )
        task_storage.check_is_valid_task_display_id.return_value = False

        # Act
        interactor.get_task_due_missing_reasons_wrapper(
            presenter=presenter, task_display_id=task_id, user_id=user_id,
            stage_id=stage_id
        )

        # Assert
        presenter.response_for_invalid_task_id.assert_called_once()
        call_args = presenter.response_for_invalid_task_id.call_args
        error_object = call_args[0][0]
        invalid_task_id = error_object.task_display_id
        assert invalid_task_id == task_id

    def test_given_task_is_not_assigned_to_user_raises_exception(self):
        # Arrange
        task_display_id = "iBWF-1"
        task_id = 1
        user_id = "user_id_1"
        stage_id = "stage_id_1"
        storage = create_autospec(StorageInterface)
        task_storage = create_autospec(TaskStorageInterface)
        presenter = create_autospec(TaskDueDetailsPresenterInterface)
        interactor = GetTaskDueMissingReasonsInteractor(
            storage=storage, task_storage=task_storage
        )
        task_storage.check_is_valid_task_display_id.return_value = True
        task_storage.get_task_id_for_task_display_id.return_value = 1
        storage.validate_if_task_is_assigned_to_user_in_given_stage.return_value = False

        # Act
        interactor.get_task_due_missing_reasons_wrapper(
            presenter=presenter, task_display_id=task_display_id, user_id=user_id,
            stage_id=stage_id
        )

        # Assert
        storage.validate_if_task_is_assigned_to_user_in_given_stage.assert_called_once_with(
            task_id, user_id, stage_id)
        presenter.response_for_user_is_not_assignee_for_task.assert_called_once()

    def test_given_invalid_stage_id_raises_exception(self):
        # Arrange
        task_display_id = "iBWF-1"
        task_id = 1
        user_id = "user_id_1"
        stage_id = "stage_id_1"
        storage = create_autospec(StorageInterface)
        task_storage = create_autospec(TaskStorageInterface)
        presenter = create_autospec(TaskDueDetailsPresenterInterface)
        interactor = GetTaskDueMissingReasonsInteractor(
            storage=storage, task_storage=task_storage
        )
        task_storage.check_is_valid_task_display_id.return_value = True
        task_storage.get_task_id_for_task_display_id.return_value = 1
        storage.validate_stage_id.return_value = False

        # Act
        interactor.get_task_due_missing_reasons_wrapper(
            presenter=presenter, task_display_id=task_display_id, user_id=user_id,
            stage_id=stage_id
        )

        # Assert
        storage.validate_stage_id.assert_called_once_with(
            stage_id)
        presenter.response_for_invalid_stage_id.assert_called_once()

    def test_given_task_due_missing_details(self, mocker, get_due_missing_details):
        # Arrange
        task_display_id = "iBWF-1"
        task_id = 1
        user_id = "user_id_1"
        stage_id = "stage_id_1"
        user_ids = ['123e4567-e89b-12d3-a456-426614174001', '123e4567-e89b-12d3-a456-426614174002']
        expected_response = Mock()
        storage = create_autospec(StorageInterface)
        task_storage = create_autospec(TaskStorageInterface)
        presenter = create_autospec(TaskDueDetailsPresenterInterface)
        interactor = GetTaskDueMissingReasonsInteractor(
            storage=storage, task_storage=task_storage
        )
        task_storage.check_is_valid_task_display_id.return_value = True
        task_storage.get_task_id_for_task_display_id.return_value = 1
        storage.validate_if_task_is_assigned_to_user_in_given_stage.return_value = True
        storage.get_task_due_details.return_value = \
            get_due_missing_details
        presenter.get_response_for_get_task_due_details.return_value = expected_response
        assignee_details_dtos = assignee_details_dtos_mock(mocker)

        # Act
        result = interactor.get_task_due_missing_reasons_wrapper(
            presenter=presenter, task_display_id=task_display_id, user_id=user_id,
            stage_id=stage_id
        )

        # Assert
        assert result == expected_response
        storage.get_task_due_details.assert_called_once_with(
            task_id, stage_id)
        assignee_details_dtos.assert_called_once_with(user_ids)
        presenter.get_response_for_get_task_due_details.assert_called_once()

    def test_given_valid_details_get_task_due_missing_details(self, mocker, get_due_missing_details):
        # Arrange
        task_display_id = "iBWF-1"
        task_id = 1
        user_id = "user_id_1"
        stage_id = "stage_id_1"
        user_ids = ['123e4567-e89b-12d3-a456-426614174001', '123e4567-e89b-12d3-a456-426614174002']
        expected_response = Mock()
        storage = create_autospec(StorageInterface)
        task_storage = create_autospec(TaskStorageInterface)
        presenter = create_autospec(TaskDueDetailsPresenterInterface)
        interactor = GetTaskDueMissingReasonsInteractor(
            storage=storage, task_storage=task_storage
        )
        storage.validate_stage_id.return_value = True
        task_storage.check_is_valid_task_display_id.return_value = True
        task_storage.get_task_id_for_task_display_id.return_value = 1
        storage.validate_if_task_is_assigned_to_user_in_given_stage.return_value = True
        storage.get_task_due_details.return_value = \
            get_due_missing_details
        presenter.get_response_for_get_task_due_details.return_value = expected_response
        assignee_details_dtos = assignee_details_dtos_mock(mocker)

        # Act
        result = interactor.get_task_due_missing_reasons_wrapper(
            presenter=presenter, task_display_id=task_display_id, user_id=user_id,
            stage_id=stage_id
        )

        # Assert
        assert result == expected_response
        storage.get_task_due_details.assert_called_once_with(
            task_id, stage_id)
        assignee_details_dtos.assert_called_once_with(user_ids)
        presenter.get_response_for_get_task_due_details.assert_called_once()
