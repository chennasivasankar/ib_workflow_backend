import factory
import pytest

from ib_tasks.tests.factories.models import StagePermittedRolesFactory
from ib_tasks.tests.factories.storage_dtos import StageRoleDTOFactory


@pytest.mark.django_db
class TestGetStageRoles:
    @pytest.fixture()
    def stage_role_objects(self):
        StagePermittedRolesFactory.reset_sequence()
        stage_role_objects = StagePermittedRolesFactory.create_batch(2)
        return stage_role_objects

    @pytest.fixture()
    def stage_role_dtos(self, stage_role_objects):
        db_stage_ids = [stage_role_object.id for stage_role_object in
                        stage_role_objects]
        stage_roles = [
            stage_role_object.role_id for stage_role_object in
            stage_role_objects
        ]
        StageRoleDTOFactory.reset_sequence()
        stage_role_dtos = StageRoleDTOFactory.create_batch(
            size=2, db_stage_id=factory.Iterator(db_stage_ids),
            role_id=factory.Iterator(stage_roles)
        )
        return stage_role_dtos

    def test_get_stage_role_dtos_given_stage_ids(self, stage_role_objects,
                                                 stage_role_dtos):
        # Arrange

        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        db_stage_ids = [
            stage_role_dto.db_stage_id for stage_role_dto in stage_role_dtos
        ]
        storage = StagesStorageImplementation()
        # Act
        actual_result = storage.get_stage_role_dtos_given_db_stage_ids(
            db_stage_ids=db_stage_ids)
        # Assert
        assert stage_role_dtos == actual_result
