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
    from ib_iam.exceptions.custom_exceptions \
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


def update_user_profile_user_already_exist_adapter_mock(mocker):
    mock = mocker.patch(
        'ib_iam.adapters.user_service.UserService.update_user_profile'
    )
    from ib_iam.exceptions.custom_exceptions import UserDoesNotExist
    mock.side_effect = UserDoesNotExist
    return mock


def update_user_profile_success_adapter_mock(mocker):
    mock = mocker.patch(
        'ib_iam.adapters.user_service.UserService.update_user_profile'
    )
    mock.return_value = None
    return mock


def prepare_get_user_profile_dto_mock(mocker):
    mock = mocker.patch(
        "ib_iam.adapters.user_service.UserService.get_user_profile_dto"
    )
    return mock

def update_user_profile_adapter_mock(mocker):
    mock = mocker.patch(
        'ib_iam.adapters.user_service.UserService.update_user_profile'
    )
    return mock


def deactivate_user_in_ib_users_mock(mocker):
    mock = mocker.patch(
        "ib_users.interfaces.service_interface.ServiceInterface.deactivate_user"
    )
    return mock
