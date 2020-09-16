import pytest

from ib_tasks.storages.tasks_storage_implementation import \
    TasksStorageImplementation
from ib_tasks.tests.factories.models import TaskFactory


@pytest.mark.django_db
class TestGetTaskProjectIds:
    @pytest.fixture
    def populate_data(self):
        TaskFactory.reset_sequence()
        TaskFactory.create_batch(4)

    def test_get_task_projects_given_task_ids(self, populate_data, snapshot):
        # Arrange
        task_ids = [1, 2, 3, 4]
        storage = TasksStorageImplementation()

        # Act
        response = storage.get_task_project_ids(task_ids)

        # Assert
        snapshot.assert_match(response, "task_project_dtos")
