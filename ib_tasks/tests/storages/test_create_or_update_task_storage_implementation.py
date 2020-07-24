import pytest
import factory

from ib_tasks.models import Task, TaskGoF, TaskGoFField
from ib_tasks.tests.factories.models import TaskFactory, FieldFactory, \
    TaskGoFFactory
from ib_tasks.tests.factories.storage_dtos import TaskGoFDTOFactory, \
    TaskGoFFieldDTOFactory


@pytest.mark.django_db
class TestCreateOrUpdateTaskStorageImplementation:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskGoFDTOFactory.reset_sequence()
        TaskFactory.reset_sequence()
        TaskGoFFieldDTOFactory.reset_sequence()
        FieldFactory.reset_sequence()
        TaskGoFFactory.reset_sequence()

    @pytest.fixture
    def storage(self):
        from ib_tasks.storages.create_or_update_task_storage_implementation \
            import CreateOrUpdateTaskStorageImplementation
        return CreateOrUpdateTaskStorageImplementation()

    def test_create_task_with_template_id(self, storage):
        # Arrange
        template_id = "TEMPLATE_ID-1"
        created_by_id = "123e4567-e89b-12d3-a456-426614174000"

        # Act
        created_task_id = \
            storage.create_task_with_template_id(template_id, created_by_id)

        # Assert
        task = Task.objects.get(id=created_task_id)
        assert task.template_id == template_id
        assert task.created_by_id == created_by_id

    def test_create_task_gofs(self, storage):
        # Arrange
        task = TaskFactory()
        task_gof_dtos = TaskGoFDTOFactory.create_batch(
            size=1, task_id=task.id
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
            assert task_gof_object.same_gof_order == \
                   task_gof_details_dto.same_gof_order

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
