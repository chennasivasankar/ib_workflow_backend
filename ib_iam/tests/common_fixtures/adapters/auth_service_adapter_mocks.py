def prepare_get_reset_password_token_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.auth_service.AuthService.get_reset_password_token"
    )
    return mock


def prepare_user_log_out_from_a_device_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.auth_service.AuthService.user_log_out_from_a_device"
    )
    return mock


def prepare_get_user_tokens_dto_for_given_email_and_password_dto_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.auth_service.AuthService.get_user_tokens_dto_for_given_email_and_password_dto"
    )
    return mock


def prepare_update_user_password_with_reset_password_token_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.auth_service.AuthService.update_user_password_with_reset_password_token"
    )
    return mock


def prepare_update_user_password(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.auth_service.AuthService.update_user_password")
    return mock
