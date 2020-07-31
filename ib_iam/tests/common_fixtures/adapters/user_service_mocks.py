def prepare_user_profile_dtos_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.user_service.UserService.get_basic_user_dtos"
    )
    return mock
