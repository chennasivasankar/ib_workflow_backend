import pytest

from ib_tasks.tests.factories.models import TaskFactory


@pytest.mark.django_db
class TestGetProjectIdOfTask:

    def test_given_task_id_returns_project_id(self, storage):
        # Arrange
        task_id = 1
        project_id_of_task = "project_id_1"
        TaskFactory.reset_sequence()
        TaskFactory()

        # Act
        project_id = storage.get_project_id_of_task(task_id)

        # Assert
        assert project_id == project_id_of_task
