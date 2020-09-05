import pytest

from ib_tasks.tests.factories.models import TaskFactory


@pytest.mark.django_db
class TestIsValidTaskId:

    def test_is_valid_task_id_with_valid_task_id(self, storage):
        # Arrange
        task = TaskFactory.create()
        task_id = task.id
        expected_response = True

        # Act
        actual_response = storage.is_valid_task_id(task_id)

        # Assert
        assert actual_response == expected_response

    def test_is_valid_task_id_with_invalid_task_id(self, storage):
        # Arrange
        TaskFactory.create_batch(size=5)
        task_id = 100
        expected_response = False

        # Act
        actual_response = storage.is_valid_task_id(task_id)

        # Assert
        assert actual_response == expected_response
