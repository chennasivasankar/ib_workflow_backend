import pytest

from ib_tasks.models import TaskGoF
from ib_tasks.tests.factories.models import TaskGoFFactory
from ib_tasks.tests.factories.storage_dtos import TaskGoFWithTaskIdDTOFactory


@pytest.mark.django_db
class TestUpdateTaskGoFs:

    def test_update_task_gofs(self, storage):

        # Arrange
        task_id = 1

        task_gofs = TaskGoFFactory.create_batch(
            size=2, task_id=task_id
        )
        task_gof_dtos = [
            TaskGoFWithTaskIdDTOFactory(
                task_id=task_gof.task_id,
                gof_id=task_gof.gof_id,
                same_gof_order=2
            )
            for task_gof in task_gofs
        ]

        # Act
        task_gof_details_dtos = storage.update_task_gofs(task_gof_dtos)

        # Arrange
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
