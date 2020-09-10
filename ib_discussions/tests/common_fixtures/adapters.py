def prepare_get_user_profile_dtos_mock(mocker):
    mock = mocker.patch(
        "ib_discussions.adapters.auth_service.AuthService.get_user_profile_dtos"
    )
    return mock


def prepare_validate_user_ids_mock(mocker):
    mock = mocker.patch(
        "ib_discussions.adapters.auth_service.AuthService.validate_user_ids"
    )
    return mock
