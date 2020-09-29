import pytest

from ib_tasks.storages.tasks_storage_implementation import \
    TasksStorageImplementation
from ib_tasks.tests.factories.models import TaskFactory
from ib_tasks.tests.factories.storage_dtos import TaskDisplayIdDTOFactory


@pytest.mark.django_db
class TestGetTaskIds:
    @pytest.fixture
    def storage(self):
        return TasksStorageImplementation()

    @pytest.fixture
    def populate_data(self):
        TaskFactory.reset_sequence()
        TaskFactory.create_batch(3)

    @pytest.fixture
    def expected_output(self):
        TaskDisplayIdDTOFactory.reset_sequence()
        return TaskDisplayIdDTOFactory.create_batch(3)

    def test_get_task_ids_given_task_display_ids(self, storage,
                                                 populate_data,
                                                 expected_output):
        # Arrange
        task_display_ids = ["IBWF-1", "IBWF-2", "IBWF-3"]

        # Act
        task_display_dtos = storage.get_task_ids_given_task_display_ids(
            task_display_ids)

        # Assert
        self._validate_output(expected_output, task_display_dtos)

    @staticmethod
    def _validate_output(expected_dtos, returned_dtos):
        for returned_dto, expected_dto in zip(returned_dtos, expected_dtos):
            assert returned_dto.task_id == expected_dto.task_id
            assert returned_dto.display_id == expected_dto.display_id
