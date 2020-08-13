from ib_tasks.adapters.dtos import AssigneeDetailsDTO


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


def prepare_get_roles_for_invalid_mock(mocker):
    mock = mocker.patch(
        'ib_tasks.adapters.roles_service.RolesService.get_db_roles'
    )
    roles = ["ROLE_3"]
    mock.return_value = roles
    return mock


def prepare_get_roles_for_valid_mock(mocker):
    mock = mocker.patch(
        'ib_tasks.adapters.roles_service.RolesService.get_db_roles'
    )
    roles = ["ROLE_1", "ROLE_2", "ROLE_3", "ROLE_4", "ROLE_5"]
    mock.return_value = roles
    return mock


def get_user_role_ids(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.roles_service.RolesService.get_user_role_ids")
    user_role_ids = ['ALL_ROLES', 'FIN_PAYMENT_REQUESTER', 'FIN_PAYMENT_POC',
                     'FIN_PAYMENT_APPROVER', 'FIN_COMPLIANCE_VERIFIER',
                     'FIN_COMPLIANCE_APPROVER', 'FIN_PAYMENTS_LEVEL1_VERIFIER',
                     'FIN_PAYMENTS_LEVEL2_VERIFIER',
                     'FIN_PAYMENTS_LEVEL3_VERIFIER',
                     'FIN_PAYMENTS_RP', 'FIN_FINANCE_RP',
                     'FIN_ACCOUNTS_LEVEL1_VERIFIER',
                     'FIN_ACCOUNTS_LEVEL2_VERIFIER']
    mock.return_value = user_role_ids
    return mock


def get_assignees_details_dtos(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.assignees_details_service.AssigneeDetailsService.get_assignees_details_dtos"
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
