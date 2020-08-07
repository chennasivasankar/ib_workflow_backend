import pytest


@pytest.mark.django_db
class TestGetGlobalConstantsToTask:

    def test_get_global_constants_to_task(self):
        # Arrange
        task_id = 1
        from ib_tasks.storages.storage_implementation \
            import StorageImplementation

        from ib_tasks.tests.factories.models import (
            TaskTemplateWithTransitionFactory, GlobalConstantFactory,
            TaskModelFactory
        )
        TaskTemplateWithTransitionFactory.reset_sequence(0)
        TaskModelFactory.reset_sequence(0)
        GlobalConstantFactory.reset_sequence(0)
        TaskModelFactory()
        task_template = TaskTemplateWithTransitionFactory()
        GlobalConstantFactory.create_batch(size=3, task_template=task_template)
        from ib_tasks.tests.factories.storage_dtos \
            import GlobalConstantDTOFactory
        GlobalConstantDTOFactory.reset_sequence(0)
        storage = StorageImplementation()
        expected = GlobalConstantDTOFactory.create_batch(size=3)

        # Act
        response = storage.get_global_constants_to_task(task_id=task_id)

        # Assert
        assert response == expected
