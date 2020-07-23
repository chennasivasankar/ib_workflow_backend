import pytest


class TestStorageImplementation:

    @pytest.mark.django_db
    def test_get_is_admin_of_given_user_id(self):
        # Arrange
        user_id = 1
        from ib_iam.tests.factories.models import UserFactory
        UserFactory.reset_sequence(1)
        user_object = UserFactory(is_admin=True)

        from ib_iam.storages.storage_implementation import StorageImplementation
        storage = StorageImplementation()

        # Act
        is_admin = storage.get_is_admin_of_given_user_id(
            user_id=user_id
        )

        # Assert
        assert is_admin == user_object.is_admin