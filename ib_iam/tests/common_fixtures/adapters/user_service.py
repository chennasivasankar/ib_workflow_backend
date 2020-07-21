def prepare_get_user_profile_dto_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.user_service.UserService.get_user_profile_dto"
    )
    return mock