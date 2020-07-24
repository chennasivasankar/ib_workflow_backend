import pytest

from ib_tasks.storages.fields_storage_implementation import FieldsStorageImplementation
from ib_tasks.tests.factories.models import StageModelFactory, StageActionFactory


@pytest.mark.django_db
class TestGetActionDetails:

    @pytest.fixture()
    def populate_data(self):
        StageModelFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        StageActionFactory.create_batch(size=3)

    def test_get_action_details(self,
                                populate_data,
                                snapshot):
        # Arrange
        stage_ids = ["stage_id_1", "stage_id_2", "stage_id_3"]
        storage = FieldsStorageImplementation()

        # Act
        response = storage.get_actions_details(stage_ids=stage_ids)

        # Assert
        snapshot.assert_match(response, "response")
