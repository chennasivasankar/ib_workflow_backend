import pytest


@pytest.mark.django_db
class TestGetStageDisplayNameValueDtosForStageIds:

    def test_given_stage_ids_returns_stage_display_name_value_dtos(
            self, snapshot
    ):
        # Arrange
        from ib_tasks.tests.factories.models import StageFactory
        StageFactory.reset_sequence()
        stage_objects = StageFactory.create_batch(size=5)
        stage_ids = [
            stage_obj.stage_id
            for stage_obj in stage_objects
        ]
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        stage_storage = StagesStorageImplementation()

        # Act
        stage_display_name_value_dtos = \
            stage_storage.get_stage_display_name_value_dtos_for_stage_ids(
                stage_ids
            )

        # Assert
        snapshot.assert_match(
            name="stage_display_name_value_dtos",
            value=stage_display_name_value_dtos
        )
