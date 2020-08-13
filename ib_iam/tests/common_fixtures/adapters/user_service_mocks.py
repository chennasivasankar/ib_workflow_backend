def prepare_user_profile_dtos_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.user_service.UserService.get_basic_user_dtos"
    )
    return mock


def prepare_profile_bulk_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.user_service.UserService.get_user_profile_bulk"
    )
    return mock
