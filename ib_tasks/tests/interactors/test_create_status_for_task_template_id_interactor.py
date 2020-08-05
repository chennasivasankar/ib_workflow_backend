from unittest.mock import create_autospec

import pytest

from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskTemplateIds, DuplicateTaskStatusVariableIds
from ib_tasks.interactors.create_task_status_interactor import \
    CreateTaskStatusInteractor
from ib_tasks.interactors.storage_interfaces.status_dtos import TaskTemplateStatusDTO
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.tests.factories.storage_dtos import TaskTemplateStatusDTOFactory


class TestCreateStatusInteractor:
    @pytest.fixture
    def task_status_dtos(self):
        TaskTemplateStatusDTOFactory.reset_sequence(1)
        return TaskTemplateStatusDTOFactory.create_batch(size=2)

    @pytest.fixture
    def duplicate_status_dtos(self):
        task_status_dto = TaskTemplateStatusDTOFactory.create_batch(
            task_template_id="task_template_id_1", status_variable_id="status_variable_id_1", size=2)
        return task_status_dto

    def test_validate_task_template_id_invalid_task_template_id_raises_exception(
            self, task_status_dtos):
        # Arrange

        storage = create_autospec(TaskStorageInterface)
        storage.get_valid_template_ids_in_given_template_ids.return_value = []
        interactor = CreateTaskStatusInteractor(
            status_storage=storage
        )

        # Act
        with pytest.raises(InvalidTaskTemplateIds) as err:
            interactor.create_task_status(task_status_dtos)

        # Assert
        storage.get_valid_template_ids_in_given_template_ids.assert_called_once()

    def test_create_status_for_task_given_valid_details(
            self, task_status_dtos):
        # Arrange
        storage = create_autospec(TaskStorageInterface)
        storage.get_valid_template_ids_in_given_template_ids.return_value = \
            ["task_template_id_1", "task_template_id_2"]
        interactor = CreateTaskStatusInteractor(
            status_storage=storage
        )

        # Act
        interactor.create_task_status(task_status_dtos)

        # Assert
        storage.create_status_for_tasks.assert_called_once_with(
            task_status_dtos)

    def test_duplicate_status_ids_for_task_template_id_raises_exception(
            self, duplicate_status_dtos):
        # Arrange
        storage = create_autospec(TaskStorageInterface)
        storage.get_valid_template_ids_in_given_template_ids.return_value = \
            ["task_template_id_1"]
        interactor = CreateTaskStatusInteractor(
            status_storage=storage
        )

        # Act
        with pytest.raises(DuplicateTaskStatusVariableIds) as err:
            interactor.create_task_status(duplicate_status_dtos)

        # Assert
        storage.get_valid_template_ids_in_given_template_ids.assert_called_once()
