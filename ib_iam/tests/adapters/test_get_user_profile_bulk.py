from unittest.mock import patch

import pytest


class TestGetUserProfileBulk:

    @staticmethod
    def get_user_profile_bulk_mock(mocker):
        mock = mocker.patch(
            "ib_users.interfaces.service_interface.ServiceInterface.get_user_profile_bulk"
        )
        return mock

    def test_get_user_profile_bulk_returns_user_profile_dtos(
            self, mocker):
        # Arrange
        user_ids = ['e06b8a3b-94af-4d2e-ba14-bcec11140277']
        from ib_users.interactors.user_profile_interactor import \
            GetUserProfileDTO
        user_profile_dtos = [GetUserProfileDTO(
            user_id='e06b8a3b-94af-4d2e-ba14-bcec11140277',
            name="parker"
        )]
        get_user_profile_bulk_mock = self.get_user_profile_bulk_mock(
            mocker=mocker)

        get_user_profile_bulk_mock.return_value = user_profile_dtos
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()

        # Act
        service_adapter.user_service.get_user_profile_bulk(
            user_ids=user_ids)
        get_user_profile_bulk_mock.assert_called_once_with(user_ids=user_ids)

    def test_get_user_profile_bulk_raise_invalid_user_when_a_user_does_not_exist(
            self, mocker):
        # Arrange
        user_ids = ['e06b8a3b-94af-4d2e-ba14-bcec11140277',
                    'e06b8a3b-94af-4d2e-ba14-bcec11140288']
        from ib_users.interactors.exceptions.user_profile \
            import InvalidUserException
        get_user_profile_bulk_mock = self.get_user_profile_bulk_mock(
            mocker=mocker)

        get_user_profile_bulk_mock.side_effect = InvalidUserException(
            message=None, exception_type=None
        )
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()

        # Act
        from ib_iam.exceptions.custom_exceptions import InvalidUser
        with pytest.raises(InvalidUser):
            service_adapter.user_service.get_user_profile_bulk(
                user_ids=user_ids)
        get_user_profile_bulk_mock.assert_called_once_with(user_ids=user_ids)
