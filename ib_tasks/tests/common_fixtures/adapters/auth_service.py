from typing import List

from ib_tasks.tests.factories.adapter_dtos import UserDetailsDTOFactory, \
    TeamDetailsWithUserIdDTOFactory

from ib_tasks.tests.factories.interactor_dtos import \
    UserDetailsDTOFactory, \
    SearchableFieldUserDetailDTOFactory


def get_user_dtos_based_on_limit_and_offset_mock(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.auth_service.AuthService."
        "get_user_dtos_based_on_limit_and_offset")
    searchable_user_detail_dtos = SearchableFieldUserDetailDTOFactory. \
        create_batch(2)
    mock.return_value = searchable_user_detail_dtos
    return mock


def search_users_mock(mocker):
    path = 'ib_tasks.adapters.search_service.SearchService.get_search_user_ids'
    mock_obj = mocker.patch(path)

    return mock_obj


def assignees_details_mock(mocker):
    path = 'ib_tasks.adapters.assignees_details_service.AssigneeDetailsService.get_assignees_details_dtos'
    mock_obj = mocker.patch(path)
    return mock_obj


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


def get_user_dtos_given_user_ids_mock(mocker):
    from ib_tasks.tests.factories.storage_dtos import UserDetailsDTOFactory
    mock = mocker.patch(
        "ib_tasks.adapters.auth_service.AuthService."
        "get_user_details"
    )
    UserDetailsDTOFactory.reset_sequence(50)
    user_dtos = UserDetailsDTOFactory.create_batch(size=2)
    mock.return_value = user_dtos
    return mock


def get_user_details_for_the_given_role_ids_based_on_query(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.auth_service.AuthService.get_user_details_for_the_given_role_ids_based_on_query"
    )
    user_details_dtos = UserDetailsDTOFactory.create_batch(size=4)
    mock.return_value = user_details_dtos
    return mock


def get_projects_info_for_given_ids_mock(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.auth_service.AuthService.get_projects_info_for_given_ids"
    )
    from ib_tasks.tests.factories.adapter_dtos import \
        ProjectDetailsDTOFactory
    ProjectDetailsDTOFactory.reset_sequence()
    project_details_dtos = ProjectDetailsDTOFactory.create_batch(size=3)
    mock.return_value = project_details_dtos
    return mock


def get_user_id_team_details_dtos_mock(
        mocker
):
    mock = mocker.patch(
        "ib_tasks.adapters.auth_service.AuthService.get_user_id_team_details_dtos"
    )
    team_details_with_user_id_dtos = \
        TeamDetailsWithUserIdDTOFactory.create_batch(size=3)
    mock.return_value = team_details_with_user_id_dtos
    return mock


def get_immediate_superior_user_id_mock(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.auth_service.AuthService.get_immediate_superior_user_id"
    )
    return mock


def get_valid_project_ids_mock(mocker, project_ids: List[str]):
    mock = mocker.patch(
        "ib_tasks.adapters.auth_service.AuthService.validate_project_ids"
    )
    mock.return_value = project_ids
    return mock


def validate_if_user_is_in_project_mock(mocker, is_user_in_project: bool):
    mock = mocker.patch(
        "ib_tasks.adapters.auth_service.AuthService.validate_if_user_is_in_project"
    )
    mock.return_value = is_user_in_project
    return mock