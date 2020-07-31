from ib_tasks.tests.factories.interactor_dtos import \
    SearchableFieldUserDetailDTOFactory


def get_user_dtos_based_on_limit_and_offset_mock(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.auth_service.AuthService."
        "get_user_dtos_based_on_limit_and_offset")
    searchable_user_detail_dtos = SearchableFieldUserDetailDTOFactory. \
        create_batch(2)
    mock.return_value = searchable_user_detail_dtos
    return mock


def get_all_user_dtos_based_on_query_mock(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.auth_service.AuthService."
        "get_all_user_dtos_based_on_query")
    searchable_all_user_detail_dtos = SearchableFieldUserDetailDTOFactory. \
        create_batch(2)
    mock.return_value = searchable_all_user_detail_dtos
    return mock
