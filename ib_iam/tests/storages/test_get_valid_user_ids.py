import pytest


class TestGetValidUserIds:

    @pytest.mark.django_db
    def test_get_valid_user_ids(self):
        # Arrange
        user_ids = [
            "eca1a0c1-b9ef-4e59-b415-60a28ef17b10",
            "abc1a0c1-b9ef-4e59-b415-60a28ef17b10",
            "1231a0c1-b9ef-4e59-b415-60a28ef17b10"
        ]
        valid_user_ids = ["eca1a0c1-b9ef-4e59-b415-60a28ef17b10"]
        from ib_iam.models import UserDetails
        UserDetails.objects.create(user_id=user_ids[0])

        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        storage = UserStorageImplementation()

        # Act
        response = storage.get_valid_user_ids(user_ids=user_ids)

        # Assert
        assert response == valid_user_ids
