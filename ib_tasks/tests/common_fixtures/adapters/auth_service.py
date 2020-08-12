from ib_tasks.tests.factories.adapter_dtos import UserDetailsDTOFactory

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


def prepare_permitted_user_details_mock(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.auth_service.AuthService.get_permitted_user_details"
    )
    user_details_dtos = [UserDetailsDTOFactory()]
    mock.return_value = user_details_dtos
    return mock


def prepare_empty_permitted_user_details_mock(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.auth_service.AuthService.get_permitted_user_details"
    )
    user_details_dtos = []
    mock.return_value = user_details_dtos
    return mock


def get_user_dtos_given_user_ids(mocker):
    from ib_tasks.tests.factories.adapter_dtos import UserDetailsDTOFactory
    mock = mocker.patch(
        "ib_tasks.adapters.auth_service.AuthService."
        "get_user_details"
    )
    UserDetailsDTOFactory.reset_sequence()
    user_dtos = UserDetailsDTOFactory.create_batch(size=2)
    mock.return_value = user_dtos
    return mock
