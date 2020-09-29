import pytest

from ib_tasks.storages.storage_implementation import \
    StagesStorageImplementation


@pytest.mark.django_db
class TestCreateStageGoFs:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        from ib_tasks.tests.factories.models import StageFactory, GoFFactory
        from ib_tasks.tests.factories.interactor_dtos import \
            DBStageIdWithGoFIdsDTOFactory
        StageFactory.reset_sequence(1)
        GoFFactory.reset_sequence(1)
        DBStageIdWithGoFIdsDTOFactory.reset_sequence(1)

    def test_with_valid_stage_gofs(self, snapshot):
        # Arrange
        import factory
        from ib_tasks.tests.factories.models import StageFactory, GoFFactory
        from ib_tasks.tests.factories.interactor_dtos import \
            DBStageIdWithGoFIdsDTOFactory
        stage_objs = StageFactory.create_batch(size=2)
        gof_objs = GoFFactory.create_batch(size=2)

        db_stage_ids = [stage_obj.id for stage_obj in stage_objs]
        gof_ids = [gof_obj.gof_id for gof_obj in gof_objs]

        db_stage_id_with_gof_ids_dtos = \
            DBStageIdWithGoFIdsDTOFactory.create_batch(
                size=2, gof_ids=gof_ids,
                db_stage_id=factory.Iterator(db_stage_ids)
            )

        storage = StagesStorageImplementation()

        # Act
        storage.create_stage_gofs(
            stage_id_with_gof_ids_dtos=db_stage_id_with_gof_ids_dtos)

        # Assert
        from ib_tasks.models.stage_gof import StageGoF
        stage_gofs = StageGoF.objects.all()

        counter = 1
        for stage_gof in stage_gofs:
            snapshot.assert_match(
                stage_gof.stage_id,
                "stage_id_for_stage_gof_obj_{}".format(counter))
            snapshot.assert_match(
                stage_gof.gof_id,
                "gof_id_for_stage_gof_obj_{}".format(counter))
            counter = counter + 1
