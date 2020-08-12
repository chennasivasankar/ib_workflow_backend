from unittest.mock import create_autospec, Mock

import pytest

from ib_tasks.interactors.get_task_due_missing_reasons import \
    GetTaskDueMissingReasonsInteractor
from ib_tasks.interactors.presenter_interfaces.get_task_presenter_interface import \
    GetTaskPresenterInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import StorageInterface
from ib_tasks.tests.common_fixtures.adapters.auth_service import get_user_dtos_given_user_ids
from ib_tasks.tests.factories.storage_dtos import TaskDueMissingDTOFactory


class TestGetTaskReasons:

    @pytest.fixture()
    def get_due_missing_details(self):
        TaskDueMissingDTOFactory.reset_sequence()
        tasks = TaskDueMissingDTOFactory.create_batch(size=2)
        return tasks

    def test_given_invalid_task_id_raises_exception(self):
        # Arrange
        task_id = 1
        user_id = "user_id_1"
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(GetTaskPresenterInterface)
        interactor = GetTaskDueMissingReasonsInteractor(
            task_storage=storage
        )
        storage.validate_task_id.return_value = False

        # Act
        interactor.get_task_due_missing_reasons_wrapper(
            presenter=presenter, task_id=task_id, user_id=user_id
        )

        # Assert
        storage.validate_task_id.assert_called_once_with(task_id)
        presenter.response_for_invalid_task_id.assert_called_once()

    def test_given_task_is_not_assigned_to_user_raises_exception(self):
        # Arrange
        task_id = 1
        user_id = "user_id_1"
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(GetTaskPresenterInterface)
        interactor = GetTaskDueMissingReasonsInteractor(
            task_storage=storage
        )
        storage.validate_task_id.return_value = True
        storage.validate_if_task_is_assigned_to_user.return_value = False

        # Act
        interactor.get_task_due_missing_reasons_wrapper(
            presenter=presenter, task_id=task_id, user_id=user_id
        )

        # Assert
        storage.validate_if_task_is_assigned_to_user.assert_called_once_with(
            task_id, user_id)
        presenter.response_for_user_is_not_assignee_for_task.assert_called_once()

    def test_given_task_due_missing_details(self, mocker, get_due_missing_details):
        # Arrange
        task_id = 1
        user_id = "user_id_1"
        expected_response = Mock()
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(GetTaskPresenterInterface)
        interactor = GetTaskDueMissingReasonsInteractor(
            task_storage=storage
        )
        storage.validate_task_id.return_value = True
        storage.validate_if_task_is_assigned_to_user.return_value = True
        storage.get_task_due_missing_reasons_details.return_value = \
            get_due_missing_details
        presenter.get_response_for_get_task_due_details.return_value = expected_response
        user_service = get_user_dtos_given_user_ids(mocker)
        user_dtos = user_service.get_user_dtos_given_user_ids()

        # Act
        interactor.get_task_due_missing_reasons_wrapper(
            presenter=presenter, task_id=task_id, user_id=user_id
        )

        # Assert
        storage.get_task_due_missing_reasons_details.assert_called_once_with(
            task_id)
        presenter.get_response_for_get_task_due_details.assert_called_once()
