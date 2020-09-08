import pytest

from ib_tasks.models import Task
from ib_tasks.tests.factories.interactor_dtos import CreateTaskDTOFactory


@pytest.mark.django_db
class TestCreateTaskWithGivenDetails:

    def test_create_task_with_template_id(self, storage):
        # Arrange
        from ib_tasks.constants.constants import TASK_DISPLAY_ID
        create_task_dto = CreateTaskDTOFactory()
        expected_task_display_id = TASK_DISPLAY_ID.format(1)

        # Act
        created_task_id = \
            storage.create_task_with_given_task_details(create_task_dto)

        # Assert
        due_datetime = create_task_dto.due_datetime
        task = Task.objects.get(id=created_task_id)
        assert task.template_id == create_task_dto.task_template_id
        assert task.created_by == create_task_dto.created_by_id
        assert task.title == create_task_dto.title
        assert task.description == create_task_dto.description
        assert task.start_date == create_task_dto.start_datetime
        assert task.due_date == due_datetime
        assert task.priority == create_task_dto.priority
        assert task.task_display_id == expected_task_display_id
