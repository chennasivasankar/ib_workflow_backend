import factory
import pytest


class TestGetUserAndTokenDTOS:

    @pytest.fixture()
    def user_storage(self):
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        user_storage = UserStorageImplementation()
        return user_storage

    @pytest.mark.django_db
    def test_with_valid_tokens_return_response(self, user_storage):
        # Arrange
        tokens = ["user_token_3", "user_token_1", "user_token_2"]
        from ib_iam.tests.factories.models import UserAuthTokenFactory
        UserAuthTokenFactory.reset_sequence(1)
        UserAuthTokenFactory.create_batch(
            size=3, token=factory.Iterator(tokens)
        )

        from ib_iam.tests.factories.storage_dtos import \
            UserIdWithTokenDTOFactory
        UserIdWithTokenDTOFactory.reset_sequence(1)
        expected_user_auth_dtos = UserIdWithTokenDTOFactory.create_batch(
            size=3, token=factory.Iterator(tokens)
        )

        # Act
        response = user_storage.get_user_and_token_dtos(tokens=tokens)

        # Assert
        assert response == expected_user_auth_dtos

    @pytest.mark.django_db
    def test_with_invalid_tokens_return_empty_list(self, user_storage):
        # Arrange
        tokens = ["user_token_3", "user_token_1", "user_token_2"]
        expected_user_auth_dtos = []

        # Act
        response = user_storage.get_user_and_token_dtos(tokens=tokens)

        # Assert
        assert response == expected_user_auth_dtos
