import pytest

from ib_tasks.tests.factories.models import TaskFactory


@pytest.mark.django_db
class TestValidateTaskId:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskFactory.reset_sequence()

    def test_given_invalid_task_id_raise_exception(self, storage):
        # Arrange
        from ib_tasks.exceptions.task_custom_exceptions \
            import InvalidTaskIdException
        task_id = -1

        # Act
        with pytest.raises(InvalidTaskIdException) as err:
            storage.validate_task_id(task_id)

        # Assert
        exception_obj = err.value
        assert exception_obj.task_id == task_id

    def test_given_valid_task_id_returns_task_base_details_dto(self, storage):
        # Arrange
        task_id = 1
        task_obj = TaskFactory()
        from ib_tasks.interactors.storage_interfaces.get_task_dtos import \
            TaskBaseDetailsDTO
        excepted_task_base_details_dto = TaskBaseDetailsDTO(
            template_id=task_obj.template_id,
            task_display_id=task_obj.task_display_id,
            title=task_obj.title,
            description=task_obj.description,
            start_date=task_obj.start_date,
            due_date=task_obj.due_date,
            priority=task_obj.priority,
            project_id=task_obj.project_id
        )
        # Act
        actual_task_base_details_dto = storage.validate_task_id(task_id)

        # Assert
        assert actual_task_base_details_dto == excepted_task_base_details_dto
