from ib_tasks.tests.factories.interactor_dtos import UserDTOFactory


def get_user_dtos_based_on_limit_and_offset_mock(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.auth_service.AuthService.get_user_dtos_based_on_limit_and_offset")
    user_dtos = UserDTOFactory.create_batch(2)
    mock.return_value = user_dtos
    return mock


def get_all_user_dtos_based_on_query_mock(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.auth_service.AuthService.get_all_user_dtos_based_on_query")
    user_dtos = UserDTOFactory.create_batch(2)
    mock.return_value = user_dtos
    return mock
