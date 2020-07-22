import pytest


def get_users_adapter_mock(mocker, user_profile_dtos):
    mock = mocker.patch(
        'ib_iam.adapters.user_service.UserService.get_user_profile_bulk'
    )
    mock.return_value = user_profile_dtos
    return mock


def email_exist_adapter_mock(mocker):
    mock = mocker.patch(
        'ib_iam.adapters.user_service.UserService.create_user_account_with_email'
    )
    from ib_iam.exceptions.exceptions \
        import UserAccountAlreadyExistWithThisEmail
    mock.side_effect = UserAccountAlreadyExistWithThisEmail
    return mock


def create_user_account_adapter_mock(mocker):
    mock = mocker.patch(
        'ib_iam.adapters.user_service.UserService.create_user_account_with_email'
    )
    mock.return_value = "user2"
    return mock


def create_user_profile_adapter_mock(mocker):
    mock = mocker.patch(
        'ib_iam.adapters.user_service.UserService.create_user_profile'
    )
    return mock
