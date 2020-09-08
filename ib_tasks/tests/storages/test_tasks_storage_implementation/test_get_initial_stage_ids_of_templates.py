import pytest


@pytest.mark.django_db
class TestGetInitialStageIdsOfTemplates:

    def test_get_initial_stage_ids_of_templates(self, storage):
        # Arrange
        from ib_tasks.tests.factories.models import StageModelFactory, \
            TaskTemplateInitialStageFactory, TaskTemplateFactory
        expected_stage_ids = [1, 2]
        import factory
        stages = StageModelFactory.create_batch(size=2)
        task_templates = TaskTemplateFactory.create_batch(size=2)
        TaskTemplateInitialStageFactory.create_batch(
            size=2, stage=factory.Iterator(stages),
            task_template=factory.Iterator(task_templates)
        )

        # Act
        result = storage.get_initial_stage_ids_of_templates()

        # Assert
        assert result == expected_stage_ids
