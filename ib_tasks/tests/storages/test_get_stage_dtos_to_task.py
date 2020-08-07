import pytest


@pytest.mark.django_db
class TestGetStageDTOsToTask:

    def test_get_stage_dtos_to_task(self):
        # Arrange
        task_id = 1
        from ib_tasks.storages.storage_implementation \
            import StorageImplementation

        from ib_tasks.tests.factories.models import (
            TaskTemplateWithTransitionFactory, TaskModelFactory, StageModelFactory
        )
        TaskTemplateWithTransitionFactory.reset_sequence(0)
        TaskModelFactory.reset_sequence(0)
        StageModelFactory.reset_sequence(1)
        TaskModelFactory()
        task_template = TaskTemplateWithTransitionFactory()
        StageModelFactory.create_batch(
            size=3, task_template_id=task_template.template_id)
        from ib_tasks.tests.factories.storage_dtos \
            import StageValueDTOFactory
        StageValueDTOFactory.reset_sequence(1)
        storage = StorageImplementation()
        expected = StageValueDTOFactory.create_batch(size=3)

        # Act
        response = storage.get_stage_dtos_to_task(task_id=task_id)

        # Assert
        assert response == expected
