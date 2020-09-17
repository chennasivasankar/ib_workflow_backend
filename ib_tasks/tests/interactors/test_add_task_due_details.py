from datetime import datetime
from unittest.mock import create_autospec

import pytest

from ib_tasks.interactors.add_task_due_details_interactor import \
    AddTaskDueDetailsInteractor
from ib_tasks.interactors.presenter_interfaces \
    .task_due_missing_details_presenter import \
    TaskDueDetailsPresenterInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import TaskDelayParametersDTO
from ib_tasks.tests.factories.interactor_dtos import \
    (TaskDueParametersDTOFactory,
     TaskDelayParametersDTOFactory)


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

    @pytest.fixture
    def storage_mock(self):
        return create_autospec(StorageInterface)

    @pytest.fixture
    def presenter_mock(self):
        return create_autospec(TaskDueDetailsPresenterInterface)

    @pytest.fixture
    def interactor(self, storage_mock, task_storage_mock):
        interactor = AddTaskDueDetailsInteractor(storage=storage_mock,
                                                 task_storage=task_storage_mock)
        return interactor

    @pytest.fixture
    def task_storage_mock(self):
        return create_autospec(TaskStorageInterface)

    def test_given_invalid_task_id(self, due_details, storage_mock,
                                   presenter_mock, interactor,
                                   task_storage_mock):
        # Arrange
        task_display_id = "iBWF-1"
        task_storage_mock.check_is_valid_task_display_id.return_value = False

        # Act
        interactor.add_task_due_details_wrapper(
                presenter=presenter_mock,
                due_details=due_details,
                task_display_id=task_display_id)

        # Assert
        task_storage_mock.check_is_valid_task_display_id \
            .assert_called_once_with(
                task_display_id)
        presenter_mock.response_for_invalid_task_id.assert_called_once()

    def test_given_invalid_stage_id(self, due_details, storage_mock,
                                    presenter_mock, interactor,
                                    task_storage_mock):
        # Arrange
        task_display_id = "iBWF-1"
        stage_id = due_details.stage_id
        task_storage_mock.check_is_valid_task_display_id.return_value = True
        storage_mock.validate_stage_id.return_value = False

        # Act
        interactor.add_task_due_details_wrapper(
                presenter=presenter_mock,
                due_details=due_details,
                task_display_id=task_display_id)

        # Assert
        storage_mock.validate_stage_id.assert_called_once_with(
                stage_id)
        presenter_mock.response_for_invalid_stage_id.assert_called_once()

    def test_given_updated_due_date_time_is_invalid_raises_exception(
            self,
            due_details, interactor,
            storage_mock,
            presenter_mock,
            task_storage_mock
    ):
        # Arrange
        task_display_id = "iBWF-1"
        task_id = 1
        due_details.due_date_time = datetime(2020, 8, 10)
        task_storage_mock.get_task_id_for_task_display_id.return_value = 1
        task_storage_mock.get_task_due_datetime.return_value = datetime.now()

        storage_mock.validate_task_id.return_value = True

        # Act
        interactor.add_task_due_details_wrapper(
                presenter=presenter_mock,
                due_details=due_details,
                task_display_id=task_display_id)

        # Assert
        task_storage_mock.get_task_due_datetime.assert_called_once_with(
                task_id)
        presenter_mock.response_for_invalid_due_datetime.assert_called_once()

    def test_given_invalid_reason_id_raises_exception(
            self, due_details, storage_mock, presenter_mock,
            task_storage_mock, interactor):
        # Arrange
        task_display_id = "iBWF-1"
        due_details.reason_id = 6
        task_storage_mock.get_task_id_for_task_display_id.return_value = 1
        task_storage_mock.get_task_due_datetime.return_value = datetime.now()
        storage_mock.validate_if_task_is_assigned_to_user_in_given_stage \
            .return_value = True

        # Act
        interactor.add_task_due_details_wrapper(
                presenter=presenter_mock,
                due_details=due_details,
                task_display_id=task_display_id)

        # Assert
        task_storage_mock.get_task_id_for_task_display_id \
            .assert_called_once_with(
                task_display_id)
        presenter_mock.response_for_invalid_reason_id.assert_called_once()

    def test_given_valid_details_adds_due_delay_reasons(self, due_details,
                                                        storage_mock,
                                                        interactor,
                                                        presenter_mock,
                                                        task_storage_mock):
        # Arrange
        task_display_id = "iBWF-1"
        task_id = 1
        stage_id = due_details.stage_id
        storage_due_details = TaskDelayParametersDTO(
                task_id=1,
                user_id=due_details.user_id,
                reason_id=due_details.reason_id,
                reason="reason",
                stage_id=stage_id,
                due_date_time=due_details.due_date_time
        )
        task_storage_mock.get_task_id_for_task_display_id.return_value = 1
        task_storage_mock.get_task_due_datetime.return_value = datetime.now()
        storage_mock.validate_if_task_is_assigned_to_user_in_given_stage \
            .return_value = True

        # Act
        interactor.add_task_due_details_wrapper(
                presenter=presenter_mock,
                due_details=due_details,
                task_display_id=task_display_id)

        # Assert
        task_storage_mock.get_task_due_datetime.assert_called_once_with(
                task_id)
        storage_mock.add_due_delay_details.assert_called_once_with(
                storage_due_details)
        storage_mock.update_task_due_datetime.assert_called_once_with(
                storage_due_details)
