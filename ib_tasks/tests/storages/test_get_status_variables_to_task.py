
import pytest


@pytest.mark.django_db
class TestGetStatusVariablesToTask:

    def test_get_status_variables_to_task(self):
        # Arrange
        task_id = 1
        from ib_tasks.storages.storage_implementation \
            import StorageImplementation
        from ib_tasks.tests.factories.models \
            import TaskStatusVariableFactory
        TaskStatusVariableFactory.reset_sequence(1)
        TaskStatusVariableFactory(task_id=1, variable='variable_1', value='stage_1')
        TaskStatusVariableFactory(task_id=1, variable='variable_2', value='stage_2')
        storage = StorageImplementation()
        from ib_tasks.tests.factories.storage_dtos import StatusVariableDTOFactory
        StatusVariableDTOFactory.reset_sequence(0)
        expected_dto = StatusVariableDTOFactory.create_batch(size=2)

        # Act
        response = storage.get_status_variables_to_task(task_id=task_id)

        # Assert
        assert response == expected_dto
