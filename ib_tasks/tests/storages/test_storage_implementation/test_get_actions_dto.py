import pytest


@pytest.mark.django_db
class TestGetActionsDto:

    def test_get_actions_dto(self):
        # Arrange
        action_ids = [1]
        from ib_tasks.storages.storage_implementation \
            import StorageImplementation
        from ib_tasks.tests.factories.models \
            import StageActionFactory
        from ib_tasks.tests.factories.models \
            import StageModelFactory, TaskTemplateFactory
        StageModelFactory.reset_sequence(0)
        StageActionFactory.reset_sequence(1)
        TaskTemplateFactory.reset_sequence(0)
        StageActionFactory()
        storage = StorageImplementation()
        from ib_tasks.interactors.storage_interfaces.actions_dtos\
            import ActionDTO
        from ib_tasks.constants.enum import ActionTypes
        expected_dtos = [
            ActionDTO(
                action_id=1,
                name="action_name_1",
                stage_id="stage_id_0",
                button_text="hey",
                button_color="#fafafa",
                action_type=ActionTypes.NO_VALIDATIONS.value,
                transition_template_id='template_1'
            )
        ]
        StageActionFactory.reset_sequence(0)

        # Act
        response = storage.get_actions_dto(action_ids=action_ids)

        # Assert
        assert response == expected_dtos
