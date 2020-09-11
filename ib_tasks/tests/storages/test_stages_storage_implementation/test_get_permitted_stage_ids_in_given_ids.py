import pytest

from ib_tasks.tests.factories.models import (StageModelFactory,
                                             StagePermittedRolesFactory)


@pytest.mark.django_db
class TestGetPermittedStageIds:

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        StageModelFactory.reset_sequence()
        StagePermittedRolesFactory.reset_sequence(1)

    @pytest.fixture
    def populate_data(self):
        StagePermittedRolesFactory.create_batch(size=10)

    def test_get_permitted_stage_ids(self, populate_data):
        # Arrange
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()

        user_roles = ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_APPROVER"]
        stage_ids = ["stage_id_0", "stage_id_1", "stage_id_2"]
        expected_output = stage_ids

        # Act
        output = storage.get_permitted_stage_ids_given_stage_ids(user_roles,
                                                                 stage_ids)

        # Assert
        assert output == expected_output

    def test_get_permitted_stage_ids_for_only_some_permissions(self,
                                                               populate_data):
        # Arrange
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()
        expected_output = ["stage_id_0", "stage_id_2"]
        user_roles = ["FIN_PAYMENT_REQUESTER"]
        stage_ids = ["stage_id_0", "stage_id_1", "stage_id_2"]

        # Act
        output = storage.get_permitted_stage_ids_given_stage_ids(user_roles,
                                                                 stage_ids)

        # Assert
        assert output == expected_output

    def test_when_user_has_no_permitted_stages(self, populate_data):
        # Arrange
        from ib_tasks.storages.storage_implementation import \
            StagesStorageImplementation
        storage = StagesStorageImplementation()
        expected_output = []
        user_roles = ["user_role_1", "user_role_2"]
        stage_ids = ["stage_id_0", "stage_id_1", "stage_id_2"]

        # Act
        output = storage.get_permitted_stage_ids_given_stage_ids(user_roles,
                                                                 stage_ids)

        # Assert
        assert output == expected_output
