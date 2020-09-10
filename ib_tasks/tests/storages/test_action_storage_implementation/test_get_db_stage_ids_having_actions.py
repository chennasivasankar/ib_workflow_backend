import factory
import pytest

from ib_tasks.tests.factories.models import StageModelFactory, \
    StageActionFactory


@pytest.mark.django_db
class TestGetStageIdsHavingActions:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        StageModelFactory.reset_sequence()
        StageActionFactory.reset_sequence()

    def test_given_db_stage_ids_returns_db_stage_ids_having_actions(
            self, storage, snapshot
    ):
        # Arrange
        stage_objects = StageModelFactory.create_batch(size=5)
        db_stage_ids = [
            stage_obj.id
            for stage_obj in stage_objects
        ]
        StageActionFactory.create_batch(
            size=3, stage=factory.Iterator(stage_objects))

        # Act
        db_stage_ids_having_actions = storage.get_stage_ids_having_actions(
            db_stage_ids)

        # Assert
        snapshot.assert_match(
            name="db_stage_ids_having_actions",
            value=db_stage_ids_having_actions
        )
