import pytest


def get_users_adapter_mock(mocker, user_profile_dtos):
    mock = mocker.patch(
        'ib_iam.adapters.user_service.UserService.get_user_profile_bulk'
    )
    mock.return_value = user_profile_dtos
    return mock
