import pytest
from freezegun import freeze_time

from ib_tasks.tests.factories.models import TaskFactory


@pytest.mark.django_db
class TestGetTaskDueDatetime:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskFactory.reset_sequence()

    @freeze_time("2020-10-12 4:40")
    def test_get_task_due_date(self):
        # Arrange
        user_id = "123e4567-e89b-12d3-a456-426614174000"
        task_id = 1
        task = TaskFactory()
        expected_output = task.due_date
        stage_id = 1

        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation
        storage = TasksStorageImplementation()

        # Act
        result = storage.get_task_due_datetime(task_id)

        # Assert
        assert result == expected_output
