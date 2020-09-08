import pytest


@pytest.mark.django_db
class TestUpdateStatusVariablesToTask:

    def test_update_status_variables_to_task(self):
        # Arrange
        task_id = 1
        from ib_tasks.storages.storage_implementation \
            import StorageImplementation
        from ib_tasks.tests.factories.models \
            import TaskStatusVariableFactory
        TaskStatusVariableFactory.reset_sequence(1)
        TaskStatusVariableFactory(task_id="1")
        TaskStatusVariableFactory(task_id="1")
        storage = StorageImplementation()
        from ib_tasks.models import TaskStatusVariable
        expected_status_variable = "status_variable_1"
        expected_value = "value_1"

        # Act
        storage.get_status_variables_to_task(task_id=task_id)

        # Assert
        status_obj = TaskStatusVariable.objects.get(id=1)
        assert status_obj.variable == expected_status_variable
        assert status_obj.value == expected_value
