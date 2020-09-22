import pytest

from ib_tasks.tests.factories.models import TaskGoFFactory, TaskFactory, \
    GoFFactory


@pytest.mark.django_db
class TestGetTaskGoFDTOS:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        GoFFactory.reset_sequence()
        TaskFactory.reset_sequence()
        TaskGoFFactory.reset_sequence()

    def test_given_task_id_returns_task_gof_dtos(self, storage, snapshot):
        # Arrange
        task_obj = TaskFactory()
        task_id = task_obj.id
        task_gofs = TaskGoFFactory.create_batch(size=3, task=task_obj)
        gof_ids = [task_gof.gof_id for task_gof in task_gofs]

        # Act
        task_gof_dtos = storage.get_task_gof_dtos(task_id, gof_ids)

        # Assert
        snapshot.assert_match(name="task_gof_dtos", value=task_gof_dtos)

    def test_given_task_id_with_no_gof_ids_returns_empty_list(
            self, storage, snapshot
    ):
        # Arrange
        task_obj = TaskFactory()
        task_id = task_obj.id
        gof_ids = []

        # Act
        task_gof_dtos = storage.get_task_gof_dtos(task_id, gof_ids)

        # Assert
        snapshot.assert_match(name="task_gof_dtos", value=task_gof_dtos)
