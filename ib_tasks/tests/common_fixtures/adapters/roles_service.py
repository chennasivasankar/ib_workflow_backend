from typing import List

from ib_tasks.adapters.dtos import AssigneeDetailsDTO, ProjectRolesDTO
from ib_tasks.exceptions.permission_custom_exceptions import \
    InvalidUserIdException


def get_valid_role_ids_in_given_role_ids(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.roles_service.RolesService"
        ".get_valid_role_ids_in_given_role_ids")
    valid_roles = [
        "ALL_ROLES", "FIN_PAYMENT_REQUESTER",
        "FIN_PAYMENT_POC", "FIN_FINANCE_RP",
        "FIN_PAYMENTS_RP", "role_id_1",
        "role_id_2", "role_id_3", "role_id_0"
    ]
    mock.return_value = valid_roles
    return mock


def get_user_details_for_given_role_ids_mock(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.auth_service.AuthService"
        ".get_permitted_user_details"
    )
    assignees_details_dtos = [AssigneeDetailsDTO(
        assignee_id='assignee_id_1',
        name='assignee_1',
        profile_pic_url='https://google.com'
    )]
    mock.return_value = assignees_details_dtos
    return assignees_details_dtos


def prepare_get_roles_for_invalid_mock(mocker):
    mock = mocker.patch(
        'ib_tasks.adapters.roles_service.RolesService.get_valid_role_ids_in_given_role_ids'
    )
    roles = ["ROLE_3"]
    mock.return_value = roles
    return mock


def prepare_get_roles_for_valid_mock(mocker):
    mock = mocker.patch(
        'ib_tasks.adapters.roles_service.RolesService.get_valid_role_ids_in_given_role_ids'
    )
    roles = ["ROLE_1", "ROLE_2", "ROLE_3", "ROLE_4", "ROLE_5"]
    mock.return_value = roles
    return mock


def get_user_role_ids_exception(mocker, user_id):
    mock = mocker.patch(
        "ib_tasks.adapters.roles_service.RolesService.get_user_role_ids")
    mock.side_effect = InvalidUserIdException(user_id)
    return mock


def get_user_role_ids(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.roles_service.RolesService.get_user_role_ids")
    user_role_ids = ['FIN_PAYMENT_REQUESTER', 'FIN_PAYMENT_POC',
                     'FIN_PAYMENT_APPROVER', 'FIN_COMPLIANCE_VERIFIER',
                     'FIN_COMPLIANCE_APPROVER', 'FIN_PAYMENTS_LEVEL1_VERIFIER',
                     'FIN_PAYMENTS_LEVEL2_VERIFIER',
                     'FIN_PAYMENTS_LEVEL3_VERIFIER',
                     'FIN_PAYMENTS_RP', 'FIN_FINANCE_RP',
                     'FIN_ACCOUNTS_LEVEL1_VERIFIER',
                     'FIN_ACCOUNTS_LEVEL2_VERIFIER']
    mock.return_value = user_role_ids
    return mock


def get_required_user_role_ids(mocker, user_role_ids: List[str]):
    mock = mocker.patch(
        "ib_tasks.adapters.roles_service.RolesService.get_user_role_ids")
    mock.return_value = user_role_ids
    return mock


def get_assignees_details_dtos(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.assignees_details_service"
        ".AssigneeDetailsService"
        ".get_assignees_details_dtos"
    )
    assignees_details_dtos = [AssigneeDetailsDTO(
        assignee_id='assignee_id_1',
        name='assignee_1',
        profile_pic_url='https://google.com'
    )]
    mock.return_value = assignees_details_dtos
    return assignees_details_dtos


def get_some_user_role_ids(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.roles_service.RolesService.get_user_role_ids"
    )
    user_role_ids = [
        'FIN_PAYMENT_REQUESTER', 'FIN_PAYMENT_POC'
    ]

    mock.return_value = user_role_ids
    return mock


def get_user_role_ids_based_on_project_mock(mocker):
    mock = mocker.patch("ib_tasks.adapters.roles_service.RolesService."
                        "get_user_role_ids_based_on_project")
    user_role_ids = ['FIN_PAYMENT_REQUESTER', 'FIN_PAYMENT_POC',
                     'FIN_PAYMENT_APPROVER', 'FIN_COMPLIANCE_VERIFIER',
                     'FIN_COMPLIANCE_APPROVER', 'FIN_PAYMENTS_LEVEL1_VERIFIER',
                     'FIN_PAYMENTS_LEVEL2_VERIFIER',
                     'FIN_PAYMENTS_LEVEL3_VERIFIER',
                     'FIN_PAYMENTS_RP', 'FIN_FINANCE_RP',
                     'FIN_ACCOUNTS_LEVEL1_VERIFIER',
                     'FIN_ACCOUNTS_LEVEL2_VERIFIER']
    mock.return_value = user_role_ids
    return mock


def get_user_role_ids_based_on_project_mock_given_user_role_ids(
        mocker, user_role_ids: List[str]):
    mock = mocker.patch("ib_tasks.adapters.roles_service.RolesService."
                        "get_user_role_ids_based_on_project")

    mock.return_value = user_role_ids
    return mock


def get_user_role_ids_based_on_project_mock_exception(mocker):
    from ib_tasks.adapters.roles_service import \
        UserNotAMemberOfAProjectException
    mock = mocker.patch(
        "ib_tasks.adapters.roles_service.RolesService"
        ".get_user_role_ids_based_on_project")
    mock.side_effect = UserNotAMemberOfAProjectException()
    return mock


def get_user_role_ids_based_on_projects_mock(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.roles_service.RolesService"
        ".get_user_role_ids_based_on_given_project_ids")
    project_roles = [ProjectRolesDTO(
        project_id="project_id_1",
        roles=['FIN_PAYMENT_REQUESTER', 'FIN_PAYMENT_POC',
               'FIN_PAYMENT_APPROVER', 'FIN_COMPLIANCE_VERIFIER',
               'FIN_COMPLIANCE_APPROVER', 'FIN_PAYMENTS_LEVEL1_VERIFIER',
               'FIN_PAYMENTS_LEVEL2_VERIFIER']),
        ProjectRolesDTO(
            project_id="project_id_1",
            roles=['FIN_PAYMENTS_LEVEL3_VERIFIER',
                   'FIN_PAYMENTS_RP', 'FIN_FINANCE_RP',
                   'FIN_ACCOUNTS_LEVEL1_VERIFIER',
                   'FIN_ACCOUNTS_LEVEL2_VERIFIER'])]
    mock.return_value = project_roles
    return mock
