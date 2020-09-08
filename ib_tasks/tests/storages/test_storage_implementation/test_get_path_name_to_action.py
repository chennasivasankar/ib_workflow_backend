import pytest


@pytest.mark.django_db
class TestGetPathNameToAction:

    def test_get_path_name_to_action(self):
        # Arrange
        action_id = 1
        from ib_tasks.storages.storage_implementation \
            import StorageImplementation
        from ib_tasks.tests.factories.models \
            import StageActionFactory
        StageActionFactory.reset_sequence(1)
        StageActionFactory()
        storage = StorageImplementation()
        expected_path = "path"

        # Act
        response = storage.get_path_name_to_action(action_id=action_id)

        # Assert
        assert response == expected_path
