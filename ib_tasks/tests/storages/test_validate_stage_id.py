import pytest


@pytest.mark.django_db
class TestValidateStageId:

    @pytest.fixture
    def populate_data(self):
        from ib_tasks.tests.factories.models import StageModelFactory
        StageModelFactory.reset_sequence()
        StageModelFactory.create_batch(size=3)

    def test_given_invalid_stage_id(self):
        # Arrange
        stage_id = 1
        expected_output = False
        from ib_tasks.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()

        # Act
        result = storage.validate_stage_id(stage_id)

        # Assert
        assert result == expected_output

    def test_given_valid_stage_id(self, populate_data):
        # Arrange
        stage_id = 1
        expected_output = True
        from ib_tasks.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()

        # Act
        result = storage.validate_stage_id(stage_id)

        # Assert
        assert result == expected_output
