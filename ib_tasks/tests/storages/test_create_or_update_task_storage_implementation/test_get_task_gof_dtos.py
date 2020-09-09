import pytest

from ib_tasks.tests.factories.models import TaskGoFFactory, TaskFactory


@pytest.mark.django_db
class TestGetTaskGoFDTOS:

    def test_given_task_id_returns_task_gof_dtos(self, storage, snapshot):
        # Arrange
        task_obj = TaskFactory()
        task_id = task_obj.id
        TaskGoFFactory(task_id=task_id)
        TaskGoFFactory(task_id=task_id)
        TaskGoFFactory(task_id=task_id)

        # Act
        task_gof_dtos = storage.get_task_gof_dtos(task_id)

        # Assert
        snapshot.assert_match(name="task_gof_dtos", value=task_gof_dtos)

    def test_given_task_id_with_no_gof_ids_returns_empty_list(
            self, storage, snapshot
    ):
        # Arrange
        task_obj = TaskFactory()
        task_id = task_obj.id

        # Act
        task_gof_dtos = storage.get_task_gof_dtos(task_id)

        # Assert
        snapshot.assert_match(name="task_gof_dtos", value=task_gof_dtos)
