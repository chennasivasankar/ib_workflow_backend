import pytest

from ib_tasks.models import Task
from ib_tasks.tests.factories.models import TaskFactory
from ib_tasks.tests.factories.storage_dtos import TaskGoFDTOFactory


@pytest.mark.django_db
class TestCreateOrUpdateTaskStorageImplementation:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskGoFDTOFactory.reset_sequence()
        TaskFactory.reset_sequence()

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
        task_gof_details_dto = storage.create_task_gofs(task_gof_dtos)

        # Assert
