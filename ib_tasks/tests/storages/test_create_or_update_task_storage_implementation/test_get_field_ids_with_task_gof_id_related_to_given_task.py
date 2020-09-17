import factory
import pytest

from ib_tasks.tests.factories.models import TaskGoFFactory, TaskGoFFieldFactory


@pytest.mark.django_db
class TestGetFieldsOfATask:

    def test_get_field_ids_related_to_given_task(self, storage):

        # Arrange
        task_id = 1
        task_gofs = TaskGoFFactory.create_batch(
            size=2, task_id=task_id
        )
        task_gof_fields = TaskGoFFieldFactory.create_batch(
            size=2, task_gof=factory.Iterator(task_gofs)
        )
        from ib_tasks.interactors.field_dtos import FieldIdWithTaskGoFIdDTO
        expected_fields_dtos = [
            FieldIdWithTaskGoFIdDTO(
                field_id=task_gof_field.field_id,
                task_gof_id=task_gof_field.task_gof_id
            )
            for task_gof_field in task_gof_fields
        ]

        # Act
        actual_fields_dtos = \
            storage.get_field_id_with_task_gof_id_dtos(
                task_id)

        # Assert
        assert expected_fields_dtos == actual_fields_dtos
