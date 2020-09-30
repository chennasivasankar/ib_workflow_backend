import pytest


class TestGetUserIdForGivenToken:

    @pytest.fixture()
    def user_storage(self):
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        user_storage = UserStorageImplementation()
        return user_storage

    @pytest.mark.django_db
    def test_with_token_does_not_exist_return_none(self, user_storage):
        # Arrange
        token = "token_1"

        # Act
        response = user_storage.get_user_id_for_given_token(token=token)

        # Assert
        assert response is None

    @pytest.mark.django_db
    def test_with_token_exist_return_response(self, user_storage):
        # Arrange
        token = "token_1"
        user_id = "user_id_1"
        from ib_iam.tests.factories.models import UserAuthTokenFactory
        UserAuthTokenFactory.reset_sequence(1)
        UserAuthTokenFactory(token=token)

        # Act
        response = user_storage.get_user_id_for_given_token(token=token)

        # Assert
        assert response == user_id
