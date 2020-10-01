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


def get_subordinate_user_ids_mock(mocker):
    mock = mocker.patch(
        "ib_discussions.adapters.iam_service.IamService.get_subordinate_user_ids"
    )
    return mock


def validate_user_id_for_given_project(mocker, response=None, side_effect=None):
    mock = mocker.patch(
        "ib_discussions.adapters.iam_service.IamService.validate_user_id_for_given_project"
    )
    if response is not None:
        mock.return_value = response
    if side_effect is not None:
        mock.side_effect = side_effect
    return mock
