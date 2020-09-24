import pytest

from ib_tasks.storages.tasks_storage_implementation import \
    TasksStorageImplementation
from ib_tasks.tests.factories.models import TaskFactory


@pytest.mark.django_db
class TestGetValidTaskDisplayIds:
    @pytest.fixture
    def storage(self):
        return TasksStorageImplementation()

    @pytest.fixture
    def populate_data(self):
        TaskFactory.reset_sequence()
        TaskFactory.create_batch(3)

    def test_get_task_ids_given_task_display_ids(self, storage,
                                                 populate_data):
        # Arrange
        task_display_ids = ["IBWF-1", "IBWF-2", "IBWF-3"]
        expected_display_ids = task_display_ids

        # Act
        task_display_ids = storage.get_valid_task_display_ids(
            task_display_ids)

        # Assert
        assert task_display_ids == expected_display_ids

    def test_get_task_ids_given_invalid_task_display_ids(self, storage,
                                                         populate_data):
        # Arrange
        task_display_ids = ["IBWF-11", "IBWF-21", "IBWF-10"]
        expected_display_ids = []

        # Act
        task_display_ids = storage.get_valid_task_display_ids(
            task_display_ids)

        # Assert
        assert task_display_ids == expected_display_ids
