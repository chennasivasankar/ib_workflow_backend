import pytest

from ib_tasks.models import Task
from ib_tasks.tests.factories.interactor_dtos import BasicTaskDetailsDTOFactory


@pytest.mark.django_db
class TestCreateTaskWithGivenDetails:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        BasicTaskDetailsDTOFactory.reset_sequence()

    def test_create_task_with_template_id(self, storage):
        # Arrange
        from ib_tasks.constants.constants import TASK_DISPLAY_ID
        basic_task_details_dto = BasicTaskDetailsDTOFactory()
        expected_task_display_id = TASK_DISPLAY_ID.format(1)

        # Act
        created_task_id = storage.create_task(basic_task_details_dto)

        # Assert
        due_datetime = basic_task_details_dto.due_datetime
        task = Task.objects.get(id=created_task_id)
        assert task.template_id == basic_task_details_dto.task_template_id
        assert task.created_by == basic_task_details_dto.created_by_id
        assert task.title == basic_task_details_dto.title
        assert task.description == basic_task_details_dto.description
        assert task.start_date == basic_task_details_dto.start_datetime
        assert task.due_date == due_datetime
        assert task.priority == basic_task_details_dto.priority
        assert task.task_display_id == expected_task_display_id
