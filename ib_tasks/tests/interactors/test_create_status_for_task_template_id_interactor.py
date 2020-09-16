import pytest

from ib_tasks.exceptions.task_custom_exceptions import \
    (InvalidTaskTemplateIds,
     DuplicateTaskStatusVariableIds)
from ib_tasks.interactors.create_task_status_interactor import \
    CreateTaskStatusInteractor
from ib_tasks.tests.factories.storage_dtos import TaskTemplateStatusDTOFactory
from ib_tasks.tests.interactors.storage_method_mocks import StorageMethodsMock


class TestCreateStatusInteractor(StorageMethodsMock):
    @pytest.fixture
    def task_status_dtos(self):
        TaskTemplateStatusDTOFactory.reset_sequence(1)
        return TaskTemplateStatusDTOFactory.create_batch(size=2)

    @pytest.fixture
    def duplicate_status_dtos(self):
        task_status_dto = TaskTemplateStatusDTOFactory.create_batch(
                task_template_id="task_template_id_1",
                status_variable_id="status_variable_id_1", size=2)
        return task_status_dto

    @pytest.fixture
    def interactor(self, task_storage, task_template_storage):
        storage = task_storage
        interactor = CreateTaskStatusInteractor(
                status_storage=storage, template_storage=task_template_storage
        )
        return interactor

    def test_validate_task_template_id_invalid_task_template_id_raises_exception(
            self, task_status_dtos, task_storage, task_template_storage,
            interactor):
        # Arrange
        task_template_storage \
            .get_valid_task_template_ids_in_given_task_template_ids \
            .return_value = []

        # Act
        with pytest.raises(InvalidTaskTemplateIds) as err:
            interactor.create_task_status(task_status_dtos)

        # Assert
        task_template_storage \
            .get_valid_task_template_ids_in_given_task_template_ids \
            .assert_called_once()

    def test_create_status_for_task_given_valid_details(
            self, task_status_dtos, task_storage, task_template_storage,
            interactor):
        # Arrange
        storage = task_storage
        task_template_storage \
            .get_valid_task_template_ids_in_given_task_template_ids \
            .return_value = \
            ["task_template_id_1", "task_template_id_2"]

        # Act
        interactor.create_task_status(task_status_dtos)

        # Assert
        storage.create_status_for_tasks.assert_called_once_with(
                task_status_dtos)

    def test_duplicate_status_ids_for_task_template_id_raises_exception(
            self, duplicate_status_dtos, task_storage, task_template_storage,
            interactor):
        # Arrange
        task_template_storage \
            .get_valid_task_template_ids_in_given_task_template_ids \
            .return_value = \
            ["task_template_id_1"]

        # Act
        with pytest.raises(DuplicateTaskStatusVariableIds) as err:
            interactor.create_task_status(duplicate_status_dtos)

        # Assert
        task_template_storage \
            .get_valid_task_template_ids_in_given_task_template_ids \
            .assert_called_once()
