import pytest


class TestStorageImplementation:

    @pytest.mark.django_db
    def test_given_user_id_returns_group_by_details_dtos(self, snapshot):
        # Arrange
        user_id = "user1"
        from ib_adhoc_tasks.tests.factories.models import GroupByInfoFactory
        GroupByInfoFactory.create_batch(size=2, user_id=user_id)
        from ib_adhoc_tasks.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()

        # Act
        group_by_details_dtos = storage.get_group_by_details_dtos(user_id)

        # Assert
        snapshot.assert_match(
            name="group_by_details_dtos",
            value=group_by_details_dtos
        )
