import factory
import pytest


@pytest.mark.django_db
class TestTasksStorageImplementation:

    @pytest.fixture
    def storage(self):
        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation
        return TasksStorageImplementation()

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.models import StageModelFactory, \
            TaskTemplateInitialStageFactory, TaskTemplateFactory, \
            StageActionFactory

        TaskTemplateFactory.reset_sequence(1)
        StageModelFactory.reset_sequence(1)
        TaskTemplateInitialStageFactory.reset_sequence(1)
        StageActionFactory.reset_sequence(1)

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

    def test_get_actions_for_given_stage_ids_in_dtos(self, storage):
        # Arrange
        from ib_tasks.interactors.storage_interfaces.actions_dtos \
            import ActionWithStageIdDTO
        from ib_tasks.tests.factories.models import \
            StageModelFactory, StageActionFactory
        expected_stage_ids = [1, 2]
        expected_output = [
            ActionWithStageIdDTO(
                stage_id=1,
                action_id=1, button_text='hey',
                button_color='#fafafa'
            ),
            ActionWithStageIdDTO(
                stage_id=2,
                action_id=2, button_text='hey',
                button_color='#fafafa'
            )
        ]
        StageModelFactory.create_batch(
            size=2, stage_id=factory.Iterator(expected_stage_ids)
        )
        StageActionFactory.create_batch(
            size=2, stage_id=factory.Iterator(expected_stage_ids)
        )

        # Act
        result = storage.get_actions_for_given_stage_ids_in_dtos(
            stage_ids=expected_stage_ids
        )

        # Assert
        assert result == expected_output
