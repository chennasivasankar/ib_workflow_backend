import pytest


@pytest.mark.django_db
class TestGetStageRoleDTOsGivenDBStageIds:

    def test_given_db_stage_ids_returns_stage_role_dtos(
            self, snapshot
    ):
        # Arrange
        from ib_tasks.tests.factories.models import StageFactory
        StageFactory.reset_sequence()
        stage_objects = StageFactory.create_batch(size=5)
        stage_ids = [
            stage_obj.id
            for stage_obj in stage_objects
        ]
        from ib_tasks.tests.factories.models import StagePermittedRolesFactory
        StagePermittedRolesFactory.reset_sequence()
        import factory
        StagePermittedRolesFactory.create_batch(
            size=5, stage=factory.Iterator(stage_objects))
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        stage_storage = StagesStorageImplementation()

        # Act
        stage_role_dtos = \
            stage_storage.get_stage_role_dtos_given_db_stage_ids(
                stage_ids)

        # Assert
        snapshot.assert_match(
            name="stage_role_dtos",
            value=stage_role_dtos
        )
