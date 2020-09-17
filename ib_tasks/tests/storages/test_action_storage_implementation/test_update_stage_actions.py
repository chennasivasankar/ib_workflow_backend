import factory
import pytest

from ib_tasks.models import StageAction, ActionPermittedRoles
from ib_tasks.storages.action_storage_implementation import \
    ActionsStorageImplementation
from ib_tasks.tests.factories.interactor_dtos import ActionDTOFactory, \
    StageActionDTOFactory
from ib_tasks.tests.factories.models import (StageActionFactory,
                                             StageModelFactory,
                                             TaskTemplateWithTransitionFactory,
                                             TaskTemplateFactory,
                                             ActionPermittedRolesFactory)


@pytest.mark.django_db
class TestUpdateStageActions:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        ActionDTOFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        StageActionDTOFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        TaskTemplateFactory.reset_sequence()
        StageActionFactory.reset_sequence()

    @pytest.fixture()
    def stage_actions_dtos(self):
        TaskTemplateWithTransitionFactory.create_batch(size=4)
        return StageActionDTOFactory.create_batch(size=4)

    @pytest.fixture()
    def create_stage_actions(self):
        action_objs = StageActionFactory.create_batch(size=40)
        ActionPermittedRolesFactory.create_batch(
            size=40, action=factory.Iterator(action_objs))

    @staticmethod
    def _validate(expected, returned):
        for val in range(len(expected)):
            assert returned[val].name == expected[val].action_name
            assert returned[val].button_color == expected[val].button_color
            assert returned[val].logic == expected[val].logic
            assert returned[val].button_text == expected[val].button_text

    def test_with_action_details_updates_action(
            self, stage_actions_dtos, snapshot,
            create_stage_actions
    ):
        # Arrange
        action_ids = [5, 2, 3, 4]
        storage = ActionsStorageImplementation()

        # Act
        storage.update_stage_actions(stage_actions_dtos)

        # Assert
        returned = StageAction.objects.filter(id__in=action_ids)
        roles = ActionPermittedRoles.objects.filter(
            action_id__in=action_ids).values()
        self._validate(stage_actions_dtos, returned)
        snapshot.assert_match(roles, "roles")
