
def get_valid_role_ids_in_given_role_ids(mocker):
    mock = mocker.patch("ib_tasks.adapters.roles_service.RolesService.get_valid_role_ids_in_given_role_ids")
    valid_roles = [
        "ALL_ROLES", "FIN_PAYMENT_REQUESTER",
        "FIN_PAYMENT_POC", "FIN_FINANCE_RP",
        "FIN_PAYMENTS_RP"
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
    user_role_ids = [
     "FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"
    ]
    mock.return_value = user_role_ids
    return mock
