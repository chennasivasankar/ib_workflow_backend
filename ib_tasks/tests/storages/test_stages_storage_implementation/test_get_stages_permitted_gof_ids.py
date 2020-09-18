import factory
import pytest


@pytest.mark.django_db
class TestGetStagesPermissionGoFIds:

    def test_given_stage_ids_and_gof_ids_returns_gof_ids_having_permission_for_stages(
            self, snapshot
    ):
        # Arrange
        from ib_tasks.tests.factories.models import StageGoFFactory
        from ib_tasks.tests.factories.models import StageFactory
        from ib_tasks.tests.factories.models import GoFFactory
        stage_objs = StageFactory.create_batch(size=3)
        stage_ids = [
            stage_obj.id
            for stage_obj in stage_objs
        ]
        gof_objs = GoFFactory.create_batch(size=15)
        gof_ids = [
            gof_obj.gof_id
            for gof_obj in gof_objs
        ]
        StageGoFFactory.create_batch(
            size=12,
            stage=factory.Iterator(stage_objs),
            gof=factory.Iterator(gof_objs)
        )
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()

        # Act
        stages_permission_gof_ids = storage.get_stages_permitted_gof_ids(
            stage_ids, gof_ids
        )

        # Assert
        snapshot.assert_match(
            name="stages_permission_gof_ids",
            value=stages_permission_gof_ids
        )
