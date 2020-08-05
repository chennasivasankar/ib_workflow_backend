import factory
import pytest

from ib_tasks.tests.factories.models import GoFFactory, TaskTemplateFactory, \
    GoFRoleFactory, FieldFactory
from ib_tasks.tests.factories.storage_dtos import (
    GoFDTOFactory,
    GoFRolesDTOFactory,
    CompleteGoFDetailsDTOFactory,
    FieldCompleteDetailsDTOFactory
)
from ib_tasks.tests.factories.storage_dtos \
    import GoFRoleDTOFactory


@pytest.mark.django_db
class TestTasksStorageImplementation:

    @pytest.fixture
    def storage(self):
        from ib_tasks.storages.tasks_storage_implementation import \
            TasksStorageImplementation
        return TasksStorageImplementation()

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        GoFFactory.reset_sequence(1)
        TaskTemplateFactory.reset_sequence(1)
        FieldFactory.reset_sequence(1)
        GoFRoleFactory.reset_sequence(1)
        GoFDTOFactory.reset_sequence(1)
        GoFRolesDTOFactory.reset_sequence(1)
        CompleteGoFDetailsDTOFactory.reset_sequence(1)
        GoFRoleDTOFactory.reset_sequence(1)
        FieldCompleteDetailsDTOFactory.reset_sequence(1)

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

    def test_get_actions_for_given_stage_ids(self, storage):
        # Arrange
        from ib_tasks.interactors.storage_interfaces.actions_dtos \
            import ActionsOfTemplateDTO
        from ib_tasks.tests.factories.models import \
            StageModelFactory, StageActionFactory
        expected_stage_ids = [1, 2]
        expected_output = [
            ActionsOfTemplateDTO(
                template_id='task_template_id_0',
                action_id=1, button_text='hey',
                button_color='#fafafa'
            ),
            ActionsOfTemplateDTO(
                template_id='task_template_id_1',
                action_id=2, button_text='hey',
                button_color='#fafafa'
            )
        ]
        import factory
        StageModelFactory.create_batch(
            size=2, stage_id=factory.Iterator(expected_stage_ids)
        )
        StageActionFactory.create_batch(
            size=2, stage_id=factory.Iterator(expected_stage_ids)
        )

        # Act
        result = storage.get_actions_for_given_stage_ids(
            stage_ids=expected_stage_ids
        )

        # Assert
        assert result == expected_output
