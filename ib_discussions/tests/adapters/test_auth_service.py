from unittest.mock import patch

import pytest


class TestAuthService:

    def prepare_get_user_profile_bulk_mock(self, mocker):
        mock = mocker.patch(
            "ib_users.interfaces.service_interface.ServiceInterface.get_user_profile_bulk"
        )
        return mock

    def test_with_empty_user_id_raise_exception(
            self, mocker
    ):
        # Arrange
        user_ids = [
            "9cc22e39-2390-4d96-b7ac-6bb27816461f",
            "cd4eb7da-6a5f-4f82-82ba-12e40ab7bf5a"
        ]
        from ib_users.interactors.exceptions.user_profile import \
            InvalidUserException
        from ib_users.constants.user_profile.error_types import \
            EMPTY_USER_ID_ERROR_TYPE
        from ib_users.constants.user_profile.error_messages import EMPTY_USER_ID
        get_user_profile_dtos_mock = self.prepare_get_user_profile_bulk_mock(
            mocker=mocker)
        get_user_profile_dtos_mock.side_effect = InvalidUserException(
            message=EMPTY_USER_ID, exception_type=EMPTY_USER_ID_ERROR_TYPE
        )

        from ib_discussions.adapters.service_adapter import ServiceAdapter
        serice_adapter = ServiceAdapter()
        auth_service = serice_adapter.auth_service

        # Assert
        from ib_discussions.exceptions.custom_exceptions import InvalidUserId

        with pytest.raises(InvalidUserId):
            auth_service.get_user_profile_dtos(user_ids=user_ids)

    def test_with_invalid_user_id_raise_exception(self, mocker):
        # Arrange
        user_ids = [
            "9cc22e39-2390-4d96-b7ac-6bb27816461f",
            "cd4eb7da-6a5f-4f82-82ba-12e40ab7bf5a"
        ]
        from ib_users.interactors.exceptions.user_profile import \
            InvalidUserException

        from ib_users.constants.user_profile.error_messages import \
            INVALID_USER_ID
        from ib_users.constants.user_profile.error_types import \
            INVALID_USER_ID_ERROR_TYPE
        get_user_profile_dtos_mock = self.prepare_get_user_profile_bulk_mock(
            mocker=mocker)
        get_user_profile_dtos_mock.side_effect = InvalidUserException(
            message=INVALID_USER_ID, exception_type=INVALID_USER_ID_ERROR_TYPE
        )

        from ib_discussions.adapters.service_adapter import ServiceAdapter
        serice_adapter = ServiceAdapter()
        auth_service = serice_adapter.auth_service

        # Assert
        from ib_discussions.exceptions.custom_exceptions import InvalidUserId

        with pytest.raises(InvalidUserId):
            auth_service.get_user_profile_dtos(user_ids=user_ids)

    def test_with_valid_user_ids(self, mocker):
        # Arrange
        user_ids = [
            "9cc22e39-2390-4d96-b7ac-6bb27816461f",
            "cd4eb7da-6a5f-4f82-82ba-12e40ab7bf5a"
        ]
        from ib_discussions.adapters.auth_service import UserProfileDTO
        expected_user_profile_dtos = [
            UserProfileDTO(
                user_id='9cc22e39-2390-4d96-b7ac-6bb27816461f',
                name='test1',
                profile_pic_url='test1.com'
            ),
            UserProfileDTO(
                user_id='cd4eb7da-6a5f-4f82-82ba-12e40ab7bf5a',
                name='test2',
                profile_pic_url='test2.com'
            )
        ]

        from ib_users.interactors.user_profile_interactor import \
            GetUserProfileDTO
        get_user_profile_dtos_mock = self.prepare_get_user_profile_bulk_mock(
            mocker=mocker)
        get_user_profile_dtos_mock.return_value = [
            GetUserProfileDTO(
                user_id=user_ids[0],
                name="test1",
                profile_pic_url="test1.com"
            ),
            GetUserProfileDTO(
                user_id=user_ids[1],
                name="test2",
                profile_pic_url="test2.com"
            )
        ]

        from ib_discussions.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        auth_service = service_adapter.auth_service

        # Act
        user_profile_dtos = auth_service.get_user_profile_dtos(
            user_ids=user_ids)

        # Assert
        assert user_profile_dtos == expected_user_profile_dtos
