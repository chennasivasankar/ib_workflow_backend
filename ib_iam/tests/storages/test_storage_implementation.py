import pytest


class TestStorageImplementation:

    @pytest.mark.django_db
    def test_get_is_admin_of_given_user_id(self):
        # Arrange
        user_id = 1
        from ib_iam.tests.factories.models import UserFactory
        UserFactory.reset_sequence(1)
        user_object = UserFactory(is_admin=True)

        from ib_iam.storages.user_storage_implementation import UserStorageImplementation
        storage = UserStorageImplementation()

        # Act
        is_admin = storage.check_is_admin_user(
            user_id=user_id
        )

        # Assert
        assert is_admin == user_object.is_admin