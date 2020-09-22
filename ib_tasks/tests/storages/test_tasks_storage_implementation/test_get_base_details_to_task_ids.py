import pytest

from ib_tasks.tests.factories.models import TaskModelFactory


@pytest.mark.django_db
class TestAddDueDelayDetails:

    def expected_response(self):
        TaskModelFactory.reset_sequence(1)
        task_obj = TaskModelFactory()
        from ib_tasks.tests.factories.storage_dtos import TaskBaseDetailsDTOFactory
        TaskBaseDetailsDTOFactory.reset_sequence(1)
        response = TaskBaseDetailsDTOFactory.create_batch(
            1, task_id=1, task_display_id='iB_1',
            template_id='template_2', start_date=task_obj.start_date,
            due_date=task_obj.due_date
        )
        return response

    def test_get_base_details_to_tasks(self, storage):
        # Arrange
        task_ids = [1]
        expected = self.expected_response()

        # Act
        response = storage.get_base_details_to_task_ids(task_ids=task_ids)

        # Assert
        assert expected == response
