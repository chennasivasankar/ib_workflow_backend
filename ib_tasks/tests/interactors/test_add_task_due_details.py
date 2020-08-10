from unittest.mock import create_autospec

import pytest

from ib_tasks.interactors.add_task_due_details_interactor import AddTaskDueDetailsInteractor
from ib_tasks.interactors.presenter_interfaces.task_due_missing_details_presenter import \
    TaskDueDetailsPresenterInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.tests.factories.interactor_dtos import TaskDueParametersDTOFactory


class TestAddTaskDueDetails:

    @pytest.fixture()
    def due_details(self):
        TaskDueParametersDTOFactory.reset_sequence()
        return TaskDueParametersDTOFactory()

    def test_given_invalid_task_id(self, due_details):
        # Arrange
        task_id = due_details.task_id
        storage = create_autospec(TaskStorageInterface)
        presenter = create_autospec(TaskDueDetailsPresenterInterface)
        interactor = AddTaskDueDetailsInteractor(storage=storage)
        storage.validate_task_id.return_value = False

        # Act
        response = interactor.add_task_due_details_wrapper(presenter=presenter,
                                                           due_details=due_details)

        # Assert
        storage.validate_task_id.assert_called_once_with(task_id)
        presenter.response_for_invalid_task_id.assert_called_once()
