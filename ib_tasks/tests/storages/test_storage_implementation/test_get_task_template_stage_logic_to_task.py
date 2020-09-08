import pytest


@pytest.mark.django_db
class TestGetTaskTemplateStageLogicToTask:

    def test_given_task_id_returns_stage_display_value_dtos(self, snapshot):
        # Arrange
        from ib_tasks.tests.factories.models import TaskFactory, StageFactory
        TaskFactory.reset_sequence()
        task_obj = TaskFactory()
        task_id = task_obj.id
        template_id = task_obj.template_id
        template_ids = [template_id, "template_2", "template_3"]
        StageFactory.reset_sequence()
        import factory
        StageFactory.create_batch(size=10, task_template_id=factory.Iterator(
            template_ids))
        from ib_tasks.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()

        # Act
        stage_display_value_dtos = \
            storage.get_task_template_stage_logic_to_task(
                task_id)

        # Assert
        snapshot.assert_match(
            name="stage_display_value_dtos",
            value=stage_display_value_dtos
        )
