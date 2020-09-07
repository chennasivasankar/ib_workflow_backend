import pytest

from ib_tasks.models import TaskGoF
from ib_tasks.tests.factories.models import GoFFactory, TaskFactory
from ib_tasks.tests.factories.storage_dtos import TaskGoFWithTaskIdDTOFactory


@pytest.mark.django_db
class TestCreateTaskGoFs:

    def test_create_task_gofs(self, storage):
        # Arrange
        gof_obj = GoFFactory()
        task = TaskFactory()

        task_gof_dtos = TaskGoFWithTaskIdDTOFactory.create_batch(
            size=1, task_id=task.id, gof_id=gof_obj.gof_id
        )

        # Act
        task_gof_details_dtos = storage.create_task_gofs(task_gof_dtos)

        # Assert
        for task_gof_dto in task_gof_dtos:
            TaskGoF.objects.get(
                task_id=task_gof_dto.task_id,
                gof_id=task_gof_dto.gof_id,
                same_gof_order=task_gof_dto.same_gof_order
            )
        for task_gof_details_dto in task_gof_details_dtos:
            task_gof_object = TaskGoF.objects.get(
                id=task_gof_details_dto.task_gof_id
            )
            assert task_gof_object.gof_id == task_gof_details_dto.gof_id
            assert (
                    task_gof_object.same_gof_order ==
                    task_gof_details_dto.same_gof_order
            )
