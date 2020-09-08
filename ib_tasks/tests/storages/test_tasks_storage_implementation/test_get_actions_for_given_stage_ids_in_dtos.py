import factory
import pytest


@pytest.mark.django_db
class TestGetActionsForGivenStageIds:

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
