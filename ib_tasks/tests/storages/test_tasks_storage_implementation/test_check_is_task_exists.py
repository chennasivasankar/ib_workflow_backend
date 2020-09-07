import pytest

from ib_tasks.tests.factories.models import TaskFactory


@pytest.mark.django_db
class TestCheckIsTaskExists:

    def test_given_valid_task_id_returns_true(self, storage):
        # Arrange
        TaskFactory()
        task_id = 1

        # Act
        is_task_exists = storage.check_is_task_exists(task_id)

        # Assert
        assert is_task_exists == True

    def test_given_invalid_task_id_returns_false(self, storage):
        # Arrange
        TaskFactory()
        task_id = 2

        # Act
        is_task_exists = storage.check_is_task_exists(task_id)

        # Assert
        assert is_task_exists is False
