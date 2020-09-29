import pytest

from ib_tasks.storages.storage_implementation import \
    StagesStorageImplementation


@pytest.mark.django_db
class TestGetExistingGoFIdsWithStageIdOfStages:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.models import StageFactory, GoFFactory
        StageFactory.reset_sequence(1)
        GoFFactory.reset_sequence()

    def test_when_stage_gofs_exists_for_given_stages_returns_db_stage_id_with_gof_id_dtos(
            self, snapshot):
        # Arrange
        import factory
        from ib_tasks.tests.factories.models import StageFactory, GoFFactory, \
            StageGoFFactory

        stage_objs = StageFactory.create_batch(size=2)
        gof_objs = GoFFactory.create_batch(size=4)
        stage_gof_objs = StageGoFFactory.create_batch(
            size=4, gof=factory.Iterator(gof_objs),
            stage=factory.Iterator(stage_objs)
        )

        stage_ids = \
            [stage_gof_obj.stage_id for stage_gof_obj in stage_gof_objs]

        storage = StagesStorageImplementation()

        # Act
        response = storage.get_existing_gof_ids_with_stage_id_of_stages(
            stage_ids=stage_ids)

        # Assert
        snapshot.assert_match(
            response, "db_stage_id_with_gof_id_dtos")

    def test_when_stage_gofs_not_exists_for_given_stages_returns_empty_list(
            self, snapshot):
        # Arrange
        stage_ids = [1, 2]

        storage = StagesStorageImplementation()

        # Act
        response = storage.get_existing_gof_ids_with_stage_id_of_stages(
            stage_ids=stage_ids)

        # Assert
        snapshot.assert_match(
            response, "db_stage_id_with_gof_id_dtos")
