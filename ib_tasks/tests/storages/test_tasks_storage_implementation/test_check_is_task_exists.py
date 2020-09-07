import pytest


@pytest.mark.django_db
class TestCheckIsTaskExists:

    def test_check_is_task_exists_with_valid_task_id_returns_true(
            self, task_storage):
        # Arrange
        task_id = 1
        from ib_tasks.tests.factories.models import TaskFactory
        TaskFactory.create()

        # Act
        is_task_exists = task_storage.check_is_task_exists(task_id=task_id)

        # Assert
        assert is_task_exists is True

    def test_check_is_task_exists_with_invalid_task_id_returns_false(
            self, task_storage):
        # Arrange
        task_id = 1

        # Act
        is_task_exists = task_storage.check_is_task_exists(task_id=task_id)

        # Assert
        assert is_task_exists is False
