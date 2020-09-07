import pytest

from ib_tasks.interactors.storage_interfaces.status_dtos import \
    TaskTemplateStatusDTO
from ib_tasks.models import TaskTemplateStatusVariable
from ib_tasks.storages.tasks_storage_implementation import \
    TasksStorageImplementation
from ib_tasks.tests.factories.storage_dtos import TaskTemplateStatusDTOFactory


@pytest.mark.django_db
class TestTaskStatusVariable:

    @pytest.fixture()
    def get_task_status_dtos(self):
        TaskTemplateStatusDTOFactory.reset_sequence()
        return TaskTemplateStatusDTOFactory.create_batch(size=3)

    def test_create_task_status_variable(self, get_task_status_dtos):
        # Arrange
        task_status_dtos = get_task_status_dtos
        status_ids = ["status_id_0", "status_id_1", "status_id_2"]
        storage = TasksStorageImplementation()

        # Act
        storage.create_status_for_tasks(get_task_status_dtos)

        # Assert
        tasks_status = TaskTemplateStatusVariable.objects.filter(
            variable__in=status_ids)
        self._validate_tasks_status(tasks_status, task_status_dtos)

    @staticmethod
    def _validate_tasks_status(returned_objects, expected_dtos):
        returned_dtos = [TaskTemplateStatusDTO(
            task_template_id=obj.task_template_id,
            status_variable_id=obj.variable
        ) for obj in returned_objects]
        for returned in returned_dtos:
            for expected in expected_dtos:
                if expected.status_variable_id == returned.status_variable_id:
                    assert returned.task_template_id == \
                           expected.task_template_id
                    assert returned.status_variable_id == \
                           expected.status_variable_id