import pytest


class TestValidateUserIds:

    def test_with_invalid_user_ids_raise_exception(self, mocker):
        # Arrange
        user_ids = [
            "9cc22e39-2390-4d96-b7ac-6bb27816461f",
            "cd4eb7da-6a5f-4f82-82ba-12e40ab7bf5a"
        ]
        invalid_user_ids = [
            "1cc22e39-2390-4d96-b7ac-6bb27816461f"
        ]

        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_validate_user_ids_mock
        validate_user_ids_mock = prepare_validate_user_ids_mock(mocker=mocker)
        from ib_discussions.adapters.auth_service import InvalidUserIds
        validate_user_ids_mock.side_effect = InvalidUserIds(
            user_ids=invalid_user_ids)

        from ib_discussions.adapters.auth_service import AuthService
        auth_service = AuthService()

        # Assert
        with pytest.raises(InvalidUserIds) as err:
            auth_service.validate_user_ids(user_ids=user_ids)

        assert err.value.user_ids == invalid_user_ids

    def test_with_valid_user_ids(self, mocker):
        # Arrange
        user_ids = [
            "9cc22e39-2390-4d96-b7ac-6bb27816461f",
            "cd4eb7da-6a5f-4f82-82ba-12e40ab7bf5a"
        ]

        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_validate_user_ids_mock
        validate_user_ids_mock = prepare_validate_user_ids_mock(
            mocker=mocker)

        from ib_discussions.adapters.auth_service import AuthService
        auth_service = AuthService()

        # Act
        auth_service.validate_user_ids(user_ids=user_ids)

        # Assert
        validate_user_ids_mock.assert_called_once()
