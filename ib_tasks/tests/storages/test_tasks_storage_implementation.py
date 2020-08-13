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
            StageActionFactory, TaskFactory

        TaskTemplateFactory.reset_sequence(1)
        StageModelFactory.reset_sequence(1)
        TaskTemplateInitialStageFactory.reset_sequence(1)
        StageActionFactory.reset_sequence(1)
        TaskFactory.reset_sequence()

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
        from ib_tasks.constants.enum import ValidationType
        from ib_tasks.tests.factories.models import \
            StageModelFactory, StageActionFactory
        expected_stage_ids = [1, 2]
        expected_output = [
            ActionWithStageIdDTO(
                stage_id=1,
                action_id=1, button_text='hey',
                button_color='#fafafa',
                action_type=ValidationType.NO_VALIDATIONS.value,
                transition_template_id='template_2'
            ),
            ActionWithStageIdDTO(
                stage_id=2,
                action_id=2, button_text='hey',
                button_color='#fafafa',
                action_type=ValidationType.NO_VALIDATIONS.value,
                transition_template_id='template_3'
            )
        ]
        StageModelFactory.create_batch(
            size=2, stage_id=factory.Iterator(expected_stage_ids)
        )
        StageActionFactory.create_batch(
            size=2, stage_id=factory.Iterator(expected_stage_ids),
            action_type=ValidationType.NO_VALIDATIONS.value,
        )

        # Act
        result = storage.get_actions_for_given_stage_ids_in_dtos(
            stage_ids=expected_stage_ids
        )

        # Assert
        assert result == expected_output

    def test_check_is_valid_task_display_id_with_invalid_task_display_id_returns_false(
            self, storage):
        # Arrange
        task_display_id = "iB_001"

        # Act
        result = storage.check_is_valid_task_display_id(
            task_display_id=task_display_id)

        # Assert
        assert result is False

    def test_check_is_valid_task_display_id_with_valid_task_display_id_returns_true(
            self, storage):
        # Arrange
        task_display_id = "iB_001"
        from ib_tasks.tests.factories.models import TaskFactory
        TaskFactory.create(task_display_id=task_display_id)

        # Act
        result = storage.check_is_valid_task_display_id(
            task_display_id=task_display_id)

        # Assert
        assert result is True

    def test_get_task_id_for_task_display_id_returns_task_id(self, storage):
        # Arrange
        expected_task_id = 1
        task_display_id = "iB_001"
        from ib_tasks.tests.factories.models import TaskFactory
        TaskFactory.create(task_display_id=task_display_id)

        # Act
        result = storage.check_is_valid_task_display_id(
            task_display_id=task_display_id)

        # Assert
        assert result == expected_task_id
