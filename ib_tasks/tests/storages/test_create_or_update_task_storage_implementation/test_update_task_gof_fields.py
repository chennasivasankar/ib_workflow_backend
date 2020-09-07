import factory
import pytest

from ib_tasks.models import TaskGoFField
from ib_tasks.tests.factories.models import TaskGoFFieldFactory, \
    FieldFactory, TaskGoFFactory
from ib_tasks.tests.factories.storage_dtos import TaskGoFFieldDTOFactory


@pytest.mark.django_db
class TestUpdateTaskGoFFields:

    def test_update_task_gof_fields(self, storage):
        # Arrange

        task_gof_field_dtos = TaskGoFFieldDTOFactory.create_batch(
            size=1, field_response=factory.Iterator(["field_response"])
        )
        field_ids = [
            task_gof_field_dto.field_id
            for task_gof_field_dto in task_gof_field_dtos
        ]
        task_gof_ids = [
            task_gof_field_dto.task_gof_id
            for task_gof_field_dto in task_gof_field_dtos
        ]
        fields = FieldFactory.create_batch(
            size=1, field_id=factory.Iterator(field_ids)
        )
        task_gofs = TaskGoFFactory.create_batch(
            size=1, id=factory.Iterator(task_gof_ids)
        )
        TaskGoFFieldFactory.create_batch(
            size=1, task_gof=factory.Iterator(task_gofs),
            field=factory.Iterator(fields)
        )
        # Act
        storage.update_task_gof_fields(task_gof_field_dtos)

        # Assert
        for task_gof_field_dto in task_gof_field_dtos:
            TaskGoFField.objects.get(
                field_id=task_gof_field_dto.field_id,
                field_response=task_gof_field_dto.field_response,
                task_gof_id=task_gof_field_dto.task_gof_id
            )
