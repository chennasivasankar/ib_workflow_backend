import pytest

from ib_tasks.models import StageAction, ActionPermittedRoles
from ib_tasks.storages.action_storage_implementation import \
    ActionsStorageImplementation
from ib_tasks.tests.factories.interactor_dtos import StageActionDTOFactory
from ib_tasks.tests.factories.models import StageModelFactory, \
    TaskTemplateWithTransitionFactory, TaskTemplateFactory


@pytest.mark.django_db
class TestCreateStageActions:
    @pytest.fixture()
    def stage_actions_dtos(self):
        StageActionDTOFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        StageModelFactory.create_batch(size=5)
        TaskTemplateFactory.reset_sequence()
        TaskTemplateWithTransitionFactory.create_batch(size=4)
        return StageActionDTOFactory.create_batch(size=4)

    @staticmethod
    def _validate(expected, returned):
        for val in range(len(expected)):
            assert returned[val].name == expected[val].action_name
            assert returned[val].button_color == expected[val].button_color
            assert returned[val].logic == expected[val].logic
            assert returned[val].button_text == expected[val].button_text

    def test_with_action_details_creates_action(self, stage_actions_dtos,
                                                snapshot):
        # Arrange
        action_ids = [1, 2, 3, 4]
        storage = ActionsStorageImplementation()

        # Act
        storage.create_stage_actions(stage_actions_dtos)

        # Assert
        actions = StageAction.objects.filter(id__in=action_ids)
        roles = ActionPermittedRoles.objects.filter(
            action_id__in=action_ids).values()
        snapshot.assert_match(roles, "roles")
        self._validate(stage_actions_dtos, actions)
