import pytest


@pytest.mark.django_db
class TestGetAllowedStageIdsOfUser:

    @pytest.fixture()
    def create_stages(self):
        from ib_tasks.tests.factories.models import StagePermittedRolesFactory
        StagePermittedRolesFactory.reset_sequence(1)
        StagePermittedRolesFactory.create_batch(size=3, role_id='ROLE_1')

    def test_get_stage_actions(self, create_stages):
        # Arrange
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()
        from ib_tasks.tests.factories.storage_dtos \
            import StageRolesDTOFactory
        expected = [
            StageRolesDTOFactory(stage_id='stage_id_0', role_ids=['ROLE_1']),
            StageRolesDTOFactory(stage_id='stage_id_1', role_ids=['ROLE_1']),
            StageRolesDTOFactory(stage_id='stage_id_2', role_ids=['ROLE_1'])
        ]
        # Act
        result = storage.get_stages_roles()

        # Assert
        assert result == expected

    def test_returns_empty_stage_roles(self):
        # Arrange
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()

        expected = []
        # Act
        result = storage.get_stages_roles()

        # Assert
        assert result == expected
