from datetime import datetime
from unittest.mock import create_autospec

import pytest

from ib_tasks.interactors.add_task_due_details_interactor import AddTaskDueDetailsInteractor
from ib_tasks.interactors.presenter_interfaces.task_due_missing_details_presenter import \
    TaskDueDetailsPresenterInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import StorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import TaskStorageInterface
from ib_tasks.interactors.task_dtos import TaskDelayParametersDTO
from ib_tasks.tests.factories.interactor_dtos import TaskDueParametersDTOFactory, \
    TaskDelayParametersDTOFactory


class TestAddTaskDueDetails:
    @classmethod
    def setup_class(cls):
        TaskDueParametersDTOFactory.reset_sequence()
        TaskDelayParametersDTOFactory.reset_sequence()

    @classmethod
    def teardown_class(cls):
        pass

    @pytest.fixture()
    def due_details(self):
        return TaskDueParametersDTOFactory()

    def test_given_invalid_task_id(self, due_details):
        # Arrange
        task_display_id = "iBWF-1"
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(TaskDueDetailsPresenterInterface)
        task_storage = create_autospec(TaskStorageInterface)
        interactor = AddTaskDueDetailsInteractor(storage=storage,
                                                 task_storage=task_storage)
        task_storage.check_is_valid_task_display_id.return_value = False

        # Act
        response = interactor.add_task_due_details_wrapper(
            presenter=presenter,
            due_details=due_details,
            task_display_id=task_display_id)

        # Assert
        task_storage.check_is_valid_task_display_id.assert_called_once_with(
            task_display_id)
        presenter.response_for_invalid_task_id.assert_called_once()

    def test_given_updated_due_date_time_is_invalid_raises_exception(self, due_details):
        # Arrange
        task_display_id = "iBWF-1"
        due_details.due_date_time = datetime(2020, 8, 10)
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(TaskDueDetailsPresenterInterface)
        task_storage = create_autospec(TaskStorageInterface)
        interactor = AddTaskDueDetailsInteractor(storage=storage,
                                                 task_storage=task_storage)
        storage.validate_task_id.return_value = True

        # Act
        response = interactor.add_task_due_details_wrapper(
            presenter=presenter,
            due_details=due_details,
            task_display_id=task_display_id)

        # Assert
        presenter.response_for_invalid_due_datetime.assert_called_once()

    # def test_given_user_is_not_assigned_to_given_task_raises_exception(
    #         self, due_details):
    #     # Arrange
    #     task_display_id = "iBWF-1"
    #     task_id = 1
    #     user_id = due_details.user_id
    #     stage_id = due_details.stage_id
    #     due_details.due_date_time = datetime(2020, 8, 10)
    #     storage = create_autospec(StorageInterface)
    #     presenter = create_autospec(TaskDueDetailsPresenterInterface)
    #     task_storage = create_autospec(TaskStorageInterface)
    #     interactor = AddTaskDueDetailsInteractor(storage=storage,
    #                                              task_storage=task_storage)
    #     task_storage.get_task_id_for_task_display_id.return_value = 1
    #     storage.validate_if_task_is_assigned_to_user_in_given_stage.return_value = False
    #
    #     # Act
    #     response = interactor.add_task_due_details_wrapper(
    #         presenter=presenter,
    #         due_details=due_details,
    #         task_display_id=task_display_id)
    #
    #     # Assert
    #     storage.validate_if_task_is_assigned_to_user_in_given_stage.\
    #         assert_called_once_with(task_id, user_id, stage_id)
    #     presenter.response_for_user_is_not_assignee_for_task.assert_called_once()

    def test_given_invalid_reason_id_raises_exception(
            self, due_details):
        # Arrange
        task_display_id = "iBWF-1"
        due_details.reason_id = 6
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(TaskDueDetailsPresenterInterface)
        task_storage = create_autospec(TaskStorageInterface)
        interactor = AddTaskDueDetailsInteractor(storage=storage,
                                                 task_storage=task_storage)
        task_storage.get_task_id_for_task_display_id.return_value = 1
        storage.validate_if_task_is_assigned_to_user_in_given_stage.return_value = True

        # Act
        response = interactor.add_task_due_details_wrapper(
            presenter=presenter,
            due_details=due_details,
            task_display_id=task_display_id)

        # Assert
        task_storage.get_task_id_for_task_display_id.assert_called_once_with(task_display_id)
        presenter.response_for_invalid_reason_id.assert_called_once()

    def test_given_valid_details_adds_due_delay_reasons(self, due_details):
        # Arrange
        task_display_id = "iBWF-1"
        storage = create_autospec(StorageInterface)
        presenter = create_autospec(TaskDueDetailsPresenterInterface)
        task_storage = create_autospec(TaskStorageInterface)
        storage_due_details = TaskDelayParametersDTO(
            task_id=1,
            user_id=due_details.user_id,
            reason_id=due_details.reason_id,
            reason="Doesn't follow Instructions",
            stage_id=due_details.stage_id,
            due_date_time=due_details.due_date_time
        )
        interactor = AddTaskDueDetailsInteractor(storage=storage,
                                                 task_storage=task_storage)
        task_storage.get_task_id_for_task_display_id.return_value = 1
        storage.validate_if_task_is_assigned_to_user_in_given_stage.return_value = True

        # Act
        response = interactor.add_task_due_details_wrapper(
            presenter=presenter,
            due_details=due_details,
            task_display_id=task_display_id)

        # Assert
        storage.add_due_delay_details.assert_called_once_with(storage_due_details)
        storage.update_task_due_datetime.assert_called_once_with(storage_due_details)
