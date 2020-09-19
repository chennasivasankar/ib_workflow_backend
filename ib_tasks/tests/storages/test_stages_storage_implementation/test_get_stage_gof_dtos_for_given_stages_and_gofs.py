import pytest

from ib_tasks.storages.storage_implementation import \
    StagesStorageImplementation


@pytest.mark.django_db
class TestGetStageGoFDTOsForGivenStagesAndGoFs:

    def test_when_stage_gofs_exists_returns_stage_gof_dtos(self, snapshot):
        # Arrange
        stage_ids = [1, 2]
        gof_ids = ["gof_1", "gof_2", "gof_3"]
        import factory
        from ib_tasks.tests.factories.models import StageGoFFactory, \
            GoFFactory, StageModelFactory
        StageGoFFactory.reset_sequence()
        GoFFactory.reset_sequence()
        StageModelFactory.reset_sequence()

        gofs = GoFFactory.create_batch(
            size=3, gof_id=factory.Iterator(gof_ids))
        stages = StageModelFactory.create_batch(size=2)
        StageGoFFactory.create_batch(
            size=3, gof=factory.Iterator(gofs), stage=factory.Iterator(stages)
        )

        storage = StagesStorageImplementation()

        # Act
        response = storage.get_stage_gof_dtos_for_given_stages_and_gofs(
            stage_ids=stage_ids, gof_ids=gof_ids)

        # Assert
        snapshot.assert_match(response, "stage_gofs")

    def test_when_stage_gofs_not_exists_returns_empty_list(self, snapshot):
        # Arrange
        stage_ids = [1, 2]
        gof_ids = ["gof_1", "gof_2", "gof_3"]

        storage = StagesStorageImplementation()

        # Act
        response = storage.get_stage_gof_dtos_for_given_stages_and_gofs(
            stage_ids=stage_ids, gof_ids=gof_ids)

        # Assert
        snapshot.assert_match(response, "stage_gofs")
