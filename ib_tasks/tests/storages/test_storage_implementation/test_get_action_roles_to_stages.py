import pytest

from ib_tasks.interactors.storage_interfaces.actions_dtos import ActionRolesDTO


@pytest.mark.django_db
class TestActionRolesToStages:

    def test_get_action_roles_to_stages(self):
        # Arrange
        stage_ids = ["stage_id_0"]
        from ib_tasks.storages.storage_implementation \
            import StorageImplementation
        from ib_tasks.tests.factories.models \
            import ActionPermittedRolesFactory, StageActionFactory
        from ib_tasks.tests.factories.models import StageModelFactory
        StageModelFactory.reset_sequence(0)
        StageActionFactory.reset_sequence(0)
        ActionPermittedRolesFactory.reset_sequence(1)
        ActionPermittedRolesFactory()
        storage = StorageImplementation()
        expected = [ActionRolesDTO(
                action_id=1,
                roles=["role_1"]
            )
        ]
        ActionPermittedRolesFactory.reset_sequence(0)

        # Act
        response = storage.get_action_roles_to_stages(stage_ids=stage_ids)

        # Assert
        assert response == expected

