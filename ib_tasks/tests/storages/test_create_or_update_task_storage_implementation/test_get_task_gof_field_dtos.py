import pytest

from ib_tasks.tests.factories.models import TaskGoFFieldFactory, \
    TaskGoFFactory, TaskFactory, GoFFactory


@pytest.mark.django_db
class TestGetTaskGoFFieldDTOS:
    def test_given_task_gof_ids_returns_task_gof_field_dtos(
            self, storage, snapshot
    ):
        # Arrange
        gof_objects = GoFFactory.create_batch(size=3)
        task_obj = TaskFactory()
        task_id = task_obj.id
        task_gof_objects = [
            TaskGoFFactory(task_id=task_id, gof=gof_objects[0]),
            TaskGoFFactory(task_id=task_id, gof=gof_objects[1]),
            TaskGoFFactory(task_id=task_id, gof=gof_objects[2])
        ]
        TaskGoFFieldFactory(task_gof=task_gof_objects[0])
        TaskGoFFieldFactory(task_gof=task_gof_objects[1])
        TaskGoFFieldFactory(task_gof=task_gof_objects[2])
        TaskGoFFieldFactory(task_gof=task_gof_objects[1])
        TaskGoFFieldFactory(task_gof=task_gof_objects[0])
        task_gof_ids = [
            task_gof_obj.id
            for task_gof_obj in task_gof_objects
        ]

        # Act
        task_gof_field_dtos = storage.get_task_gof_field_dtos(task_gof_ids)

        # Assert
        snapshot.assert_match(name="task_gof_field_dtos",
                              value=task_gof_field_dtos)
