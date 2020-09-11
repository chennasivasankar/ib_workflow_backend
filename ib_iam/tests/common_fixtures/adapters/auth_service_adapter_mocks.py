def get_basic_user_profile_dtos_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.user_service.UserService.get_basic_user_dtos"
    )
    return mock


def get_user_profile_bulk_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.user_service.UserService.get_user_profile_bulk"
    )
    return mock


def get_reset_password_token_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.auth_service.AuthService.get_reset_password_token"
    )
    return mock


def user_log_out_from_a_device_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.auth_service.AuthService.user_log_out_from_a_device"
    )
    return mock


def get_user_tokens_dto_for_given_email_and_password_dto_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.auth_service.AuthService.get_user_tokens_dto_for_given_email_and_password_dto"
    )
    return mock


def update_user_password_with_reset_password_token_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.auth_service.AuthService.update_user_password_with_reset_password_token"
    )
    return mock


def update_user_password_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.auth_service.AuthService.update_user_password")
    return mock


def get_refresh_auth_tokens_dto_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.auth_service.AuthService.get_refresh_auth_tokens_dto"
    )
    return mock


def create_auth_tokens_for_user_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.auth_service.AuthService.create_auth_tokens_for_user"
    )
    return mock


def update_is_email_verified_value_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.auth_service.AuthService.update_is_email_verified_value_in_ib_user"
    )
    return mock
