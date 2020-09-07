import pytest


@pytest.mark.django_db
class TestGetStageIdsHavingActions:

    def test_given_db_stage_ids_returns_db_stage_ids_having_actions(
            self, snapshot
    ):
        # Arrange
        from ib_tasks.tests.factories.models import StageModelFactory
        StageModelFactory.reset_sequence()
        stage_objs = StageModelFactory.create_batch(size=5)
        db_stage_ids = [
            stage_obj.id
            for stage_obj in stage_objs
        ]
        from ib_tasks.tests.factories.models import StageActionFactory
        import factory
        StageActionFactory.create_batch(size=3,
                                        stage=factory.Iterator(stage_objs))
        from ib_tasks.storages.action_storage_implementation import \
            ActionsStorageImplementation
        storage = ActionsStorageImplementation()

        # Act
        db_stage_ids_having_actions = storage.get_stage_ids_having_actions(
            db_stage_ids)

        # Assert
        snapshot.assert_match(
            name="db_stage_ids_having_actions",
            value=db_stage_ids_having_actions
        )
