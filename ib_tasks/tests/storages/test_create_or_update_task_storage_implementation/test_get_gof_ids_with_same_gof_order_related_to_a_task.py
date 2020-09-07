import pytest

from ib_tasks.interactors.gofs_dtos import GoFIdWithSameGoFOrderDTO
from ib_tasks.tests.factories.models import TaskGoFFactory


@pytest.mark.django_db
class TestGetGoFsOfATask:

    def test_get_gof_ids_related_to_a_task(self, storage):
        # Arrange
        task_id = 1
        task_gofs = TaskGoFFactory.create_batch(
            size=2, task_id=task_id)
        expected_task_gof_dtos = [
            GoFIdWithSameGoFOrderDTO(
                gof_id=task_gof.gof_id,
                same_gof_order=task_gof.same_gof_order
            )
            for task_gof in task_gofs
        ]

        # Act
        actual_task_gof_dtos = \
            storage.get_gof_ids_with_same_gof_order_related_to_a_task(
                task_id)

        # Assert
        assert expected_task_gof_dtos == actual_task_gof_dtos
