import factory
import pytest

from ib_tasks.tests.factories.interactor_dtos import \
    StageIdWithGoFIdsDTOFactory
from ib_tasks.tests.factories.models import StageModelFactory, \
    GoFFactory, StageGoFFactory


class TestPopulateStageGoFs:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        GoFFactory.reset_sequence()
        StageGoFFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        StageIdWithGoFIdsDTOFactory.reset_sequence(1)

    @pytest.fixture
    def create_stage_gofs_interactor(self):
        from ib_tasks.interactors.create_stage_gofs_interactor \
            import CreateStageGoFsInteractor
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation

        stage_storage = StagesStorageImplementation()

        from ib_tasks.storages.gof_storage_implementation import \
            GoFStorageImplementation

        gof_storage = GoFStorageImplementation()

        create_stage_gofs_interactor = CreateStageGoFsInteractor(
            stage_storage=stage_storage, gof_storage=gof_storage)
        return create_stage_gofs_interactor

    @pytest.mark.django_db
    def test_with_duplicate_stage_ids_raises_exception(
            self, create_stage_gofs_interactor, snapshot):
        # Arrange
        stage_id = "stage_1"
        stage_id_with_gof_ids_dtos = StageIdWithGoFIdsDTOFactory.create_batch(
            size=4, stage_id=stage_id
        )

        from ib_tasks.exceptions.stage_custom_exceptions import \
            DuplicateStageIds

        # Assert
        with pytest.raises(DuplicateStageIds) as err:
            create_stage_gofs_interactor.create_stage_gofs(
                stage_id_with_gof_ids_dtos=stage_id_with_gof_ids_dtos)

        snapshot.assert_match(err.value.args[0], 'message')

    @pytest.mark.django_db
    def test_with_duplicate_gof_ids_for_same_stage_raises_exception(
            self, create_stage_gofs_interactor, snapshot):
        # Arrange
        duplicate_gof_ids = ["gof_1", "gof_1"]
        stage_id_with_gof_ids_dtos = StageIdWithGoFIdsDTOFactory.create_batch(
            size=4, gof_ids=duplicate_gof_ids
        )

        from ib_tasks.exceptions.gofs_custom_exceptions import \
            DuplicateGoFIds

        # Assert
        with pytest.raises(DuplicateGoFIds) as err:
            create_stage_gofs_interactor.create_stage_gofs(
                stage_id_with_gof_ids_dtos=stage_id_with_gof_ids_dtos)

        snapshot.assert_match(err.value.args[0], 'message')

    @pytest.mark.django_db
    def test_with_invalid_stage_ids_raises_exception(
            self, create_stage_gofs_interactor, snapshot):
        # Arrange
        stage_id_with_gof_ids_dtos = StageIdWithGoFIdsDTOFactory.create_batch(
            size=4
        )

        from ib_tasks.exceptions.stage_custom_exceptions import \
            InvalidStageIdsListException

        # Assert
        with pytest.raises(InvalidStageIdsListException) as err:
            create_stage_gofs_interactor.create_stage_gofs(
                stage_id_with_gof_ids_dtos=stage_id_with_gof_ids_dtos)

        snapshot.assert_match(err.value.args[0], 'message')

    @pytest.mark.django_db
    def test_with_invalid_gof_ids_raises_exception(
            self, create_stage_gofs_interactor, snapshot):
        # Arrange
        stage_objs = StageModelFactory.create_batch(size=4)
        stage_ids = [stage_obj.stage_id for stage_obj in stage_objs]
        stage_id_with_gof_ids_dtos = StageIdWithGoFIdsDTOFactory.create_batch(
            size=4, stage_id=factory.Iterator(stage_ids)
        )

        from ib_tasks.exceptions.gofs_custom_exceptions import \
            InvalidGoFIds

        # Assert
        with pytest.raises(InvalidGoFIds) as err:
            create_stage_gofs_interactor.create_stage_gofs(
                stage_id_with_gof_ids_dtos=stage_id_with_gof_ids_dtos)

        snapshot.assert_match(err.value.args[0], 'message')

    @pytest.mark.django_db
    def test_with_valid_details_create_stage_gofs(
            self, create_stage_gofs_interactor, snapshot):
        # Arrange
        stage_objs = StageModelFactory.create_batch(size=2)
        gof_objs = GoFFactory.create_batch(size=2)
        stage_ids = [stage_obj.stage_id for stage_obj in stage_objs]
        gof_ids = [gof_obj.gof_id for gof_obj in gof_objs]

        stage_id_with_gof_ids_dtos = StageIdWithGoFIdsDTOFactory.create_batch(
            size=2, stage_id=factory.Iterator(stage_ids),
            gof_ids=gof_ids
        )

        # Act
        create_stage_gofs_interactor.create_stage_gofs(
            stage_id_with_gof_ids_dtos=stage_id_with_gof_ids_dtos)

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

    @pytest.mark.django_db
    def test_with_existing_stage_gofs_skips_those_stage_gofs_to_create(
            self, create_stage_gofs_interactor, snapshot):
        # Arrange
        stage_objs = StageModelFactory.create_batch(size=2)
        gof_objs = GoFFactory.create_batch(size=2)

        StageGoFFactory.create(stage=stage_objs[0], gof=gof_objs[0])
        stage_ids = [stage_obj.stage_id for stage_obj in stage_objs]
        gof_ids = [gof_obj.gof_id for gof_obj in gof_objs]

        stage_id_with_gof_ids_dtos = StageIdWithGoFIdsDTOFactory.create_batch(
            size=2, stage_id=factory.Iterator(stage_ids),
            gof_ids=gof_ids
        )

        # Act
        create_stage_gofs_interactor.create_stage_gofs(
            stage_id_with_gof_ids_dtos=stage_id_with_gof_ids_dtos)

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
