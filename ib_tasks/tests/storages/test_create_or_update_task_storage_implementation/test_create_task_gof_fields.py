import factory
import pytest

from ib_tasks.models import TaskGoFField
from ib_tasks.tests.factories.models import FieldFactory, TaskGoFFactory
from ib_tasks.tests.factories.storage_dtos import TaskGoFFieldDTOFactory


@pytest.mark.django_db
class TestCreateTaskGoFFields:

    def test_create_task_gof_fields(self, storage):
        # Arrange
        task_gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(size=1)
        field_ids = [
            task_gof_field_dto.field_id
            for task_gof_field_dto in task_gof_field_dtos
        ]
        task_gof_ids = [
            task_gof_field_dto.task_gof_id
            for task_gof_field_dto in task_gof_field_dtos
        ]
        FieldFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids)
        )
        TaskGoFFactory.create_batch(
            size=1, id=factory.Iterator(task_gof_ids)
        )

        # Act
        storage.create_task_gof_fields(task_gof_field_dtos)

        # Assert
        for task_gof_field_dto in task_gof_field_dtos:
            TaskGoFField.objects.get(
                field_id=task_gof_field_dto.field_id,
                field_response=task_gof_field_dto.field_response,
                task_gof_id=task_gof_field_dto.task_gof_id
            )
