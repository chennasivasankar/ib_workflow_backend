import pytest

from ib_tasks.tests.factories.models import TaskFactory, SubTaskFactory


@pytest.mark.django_db
class TestGetSubTaskDetails:

    @pytest.fixture()
    def populate_data(self):
        TaskFactory.reset_sequence()
        SubTaskFactory.reset_sequence()
        task = TaskFactory()
        SubTaskFactory.create_batch(2, task=task)

    def sub_tasks_count_response(self):
        from ib_tasks.tests.factories.storage_dtos import SubTasksCountDTOFactory
        SubTasksCountDTOFactory.reset_sequence(1)
        return SubTasksCountDTOFactory.create_batch(1, sub_tasks_count=2)

    def test_get_sub_tasks_count_to_tasks(self, populate_data, storage):
        # Arrange
        task_ids = [1]
        expected = self.sub_tasks_count_response()

        # Act
        response = storage.get_sub_tasks_count_to_tasks(task_ids=task_ids)

        # Assert
        assert response == expected

    def sub_tasks_response(self):
        from ib_tasks.tests.factories.storage_dtos import SubTasksIdsDTOFactory
        SubTasksIdsDTOFactory.reset_sequence(1)
        return SubTasksIdsDTOFactory.create_batch(1, sub_task_ids=[2, 3])

    def test_get_sub_task_ids_to_tasks(self, populate_data, storage):
        # Arrange
        task_ids = [1]
        expected = self.sub_tasks_response()

        # Act
        response = storage.get_sub_task_ids_to_tasks(task_ids=task_ids)

        # Assert
        assert response == expected
