import pytest


@pytest.mark.django_db
class TestGetStageDetailsDTOsGivenStageIds:

    def test_given_stage_ids_returns_stage_details_dtos(
            self, snapshot
    ):
        # Arrange
        from ib_tasks.tests.factories.models import StageFactory
        StageFactory.reset_sequence()
        stage_objs = StageFactory.create_batch(size=5)
        stage_ids = [
            stage_obj.stage_id
            for stage_obj in stage_objs
        ]
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        stage_storage = StagesStorageImplementation()

        # Act
        stage_details_dtos = \
            stage_storage.get_stage_detail_dtos_given_stage_ids(
                stage_ids)

        # Assert
        snapshot.assert_match(
            name="stage_details_dtos",
            value=stage_details_dtos
        )
