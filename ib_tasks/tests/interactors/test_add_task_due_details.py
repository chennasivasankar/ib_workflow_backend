from datetime import datetime
from unittest.mock import create_autospec
from freezegun import freeze_time
import pytest

from ib_tasks.interactors.add_task_due_details_interactor import AddTaskDueDetailsInteractor
from ib_tasks.interactors.presenter_interfaces.task_due_missing_details_presenter import \
    TaskDueDetailsPresenterInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import StorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.tests.factories.interactor_dtos import TaskDueParametersDTOFactory


class TestAddTaskDueDetails:
    @classmethod
    def setup_class(cls):
        TaskDueParametersDTOFactory.reset_sequence()

    @classmethod
    def teardown_class(cls):
        pass

    @pytest.fixture()
    def due_details(self):
        return TaskDueParametersDTOFactory()

    def test_given_invalid_task_id(self, due_details):
        # Arrange
        task_id = due_details.task_id
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(TaskDueDetailsPresenterInterface)
        interactor = AddTaskDueDetailsInteractor(storage=storage)
        storage.validate_task_id.return_value = False

        # Act
        response = interactor.add_task_due_details_wrapper(presenter=presenter,
                                                           due_details=due_details)

        # Assert
        storage.validate_task_id.assert_called_once_with(task_id)
        presenter.response_for_invalid_task_id.assert_called_once()

    def test_given_updated_due_date_time_is_invalid_raises_exception(self, due_details):
        # Arrange
        due_details.due_date_time = datetime(2020, 8, 10)
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(TaskDueDetailsPresenterInterface)
        interactor = AddTaskDueDetailsInteractor(storage=storage)
        storage.validate_task_id.return_value = True

        # Act
        response = interactor.add_task_due_details_wrapper(presenter=presenter,
                                                           due_details=due_details)

        # Assert
        presenter.response_for_invalid_due_datetime.assert_called_once()

    def test_given_user_is_not_assigned_to_given_task_raises_exception(
            self, due_details):
        # Arrange
        due_details.due_date_time = datetime(2020, 8, 10)
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(TaskDueDetailsPresenterInterface)
        interactor = AddTaskDueDetailsInteractor(storage=storage)
        storage.validate_task_id.return_value = True
        storage.validate_if_task_is_assigned_to_user.return_value = False

        # Act
        response = interactor.add_task_due_details_wrapper(presenter=presenter,
                                                           due_details=due_details)

        # Assert
        storage.validate_if_task_is_assigned_to_user.assert_called_once()
        presenter.response_for_user_is_not_assignee_for_task.assert_called_once()

    def test_given_invalid_reason_id_raises_exception(
            self, due_details):
        # Arrange
        due_details.reason_id = 6
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(TaskDueDetailsPresenterInterface)
        interactor = AddTaskDueDetailsInteractor(storage=storage)
        storage.validate_task_id.return_value = True
        storage.validate_if_task_is_assigned_to_user.return_value = True

        # Act
        response = interactor.add_task_due_details_wrapper(presenter=presenter,
                                                           due_details=due_details)

        # Assert
        presenter.response_for_invalid_reason_id.assert_called_once()
