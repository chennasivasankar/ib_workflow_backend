from unittest.mock import patch

import pytest


class TestUserService:

    @staticmethod
    def get_user_profile_mock(mocker):
        mock = mocker.patch(
            "ib_users.interfaces.service_interface.ServiceInterface.get_user_profile"
        )
        return mock

    def test_user_account_does_not_exist_raise_excepiton(
            self, mocker
    ):
        # Arrange
        user_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        get_user_profile_mock = self.get_user_profile_mock(mocker=mocker)
        from ib_users.interactors.exceptions.user_profile import \
            InvalidUserException
        from ib_users.constants.user_profile.error_messages import \
            INVALID_USER_ID
        from ib_users.constants.user_profile.error_types import \
            INVALID_USER_ID_ERROR_TYPE
        get_user_profile_mock.side_effect = InvalidUserException(
            message=INVALID_USER_ID, exception_type=INVALID_USER_ID_ERROR_TYPE
        )

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()

        # Assert
        from ib_iam.adapters.user_service import UserAccountDoesNotExist
        with pytest.raises(UserAccountDoesNotExist):
            service_adapter.user_service.get_user_profile_dto(user_id=user_id)

    def test_with_invalid_user_id_raise_exception(
            self, mocker
    ):
        # Arrange
        user_id = ""
        get_user_profile_mock = self.get_user_profile_mock(mocker=mocker)
        from ib_users.interactors.exceptions.user_profile import \
            InvalidUserException
        from ib_users.constants.user_profile.error_messages import \
            EMPTY_USER_ID
        from ib_users.constants.user_profile.error_types import \
            EMPTY_USER_ID_ERROR_TYPE
        get_user_profile_mock.side_effect = InvalidUserException(
            message=EMPTY_USER_ID, exception_type=EMPTY_USER_ID_ERROR_TYPE
        )

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()

        # Assert
        from ib_iam.exceptions.custom_exceptions import InvalidUserId
        with pytest.raises(InvalidUserId):
            service_adapter.user_service.get_user_profile_dto(user_id=user_id)

    def test_with_valid_user_id_return_repsonse(
            self, mocker
    ):
        # Arrange
        user_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        get_user_profile_mock = self.get_user_profile_mock(mocker=mocker)
        from ib_iam.adapters.dtos import UserProfileDTO
        expected_user_profile_dto = UserProfileDTO(
            user_id='eca1a0c1-b9ef-4e59-b415-60a28ef17b10',
            name='test', email='test@gmail.com', profile_pic_url="test.com"
        )
        from ib_users.interactors.user_profile_interactor import \
            GetUserProfileDTO
        get_user_profile_mock.return_value = GetUserProfileDTO(
            user_id=user_id,
            profile_pic_url="test.com",
            email="test@gmail.com",
            name="test"
        )

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()

        # Act
        response = service_adapter.user_service.get_user_profile_dto(
            user_id=user_id)

        # Assert
        assert response == expected_user_profile_dto

    def test_deactivate_user_in_ib_users_given_valid_user_id(self, mocker):
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            deactivate_user_in_ib_users_mock
        mock = deactivate_user_in_ib_users_mock(mocker=mocker)
        mock.return_value = None
        user_id = "1234"

        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()

        service_adapter.user_service.deactivate_delete_user_id_in_ib_users(
            user_id=user_id)

        mock.assert_called_once_with(user_id=user_id)
