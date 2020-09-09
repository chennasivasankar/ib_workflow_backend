import pytest

from ib_tasks.tests.factories.models import TaskFactory


@pytest.mark.django_db
class TestValidateTaskId:

    def test_given_invalid_task_id_raise_exception(self, task_storage):
        # Arrange
        task_id = 2
        from ib_tasks.exceptions.task_custom_exceptions import \
            InvalidTaskIdException
        exception_obj = InvalidTaskIdException(task_id=task_id)

        # Act
        with pytest.raises(InvalidTaskIdException) as err:
            task_storage.validate_task_id(task_id=task_id)

        # Assert
        error_obj = err.value
        assert error_obj.task_id == exception_obj.task_id

    def test_given_valid_task_id_returns_task_display_id(self, task_storage):
        # Arrange
        task_id = 1
        task_obj = TaskFactory(task_display_id="IBWF-1")

        # Act
        task_display_id = task_storage.validate_task_id(task_id=task_id)

        # Assert
        assert task_display_id == task_obj.task_display_id
