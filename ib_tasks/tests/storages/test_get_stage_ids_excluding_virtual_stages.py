import factory
import pytest


@pytest.mark.django_db
class TestGetStageIdsWithoutVirtualStages:

    def test_given_stage_ids_returns_stage_ids_with_out_virtual_stages(
            self, snapshot
    ):
        # Arrange
        from ib_tasks.tests.factories.models import StageFactory
        values = [1, -1, 2]
        stage_objs = StageFactory.create_batch(size=10, value=factory.Iterator(values))
        stage_ids = [
            stage_obj.stage_id
            for stage_obj in stage_objs
        ]
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        stage_storage = StagesStorageImplementation()

        # Act
        stage_ids_without_virtual_stages = \
            stage_storage.get_stage_ids_excluding_virtual_stages(
            stage_ids)

        # Assert
        snapshot.assert_match(
            name="stage_ids_without_virtual_stages",
            value=stage_ids_without_virtual_stages
        )

