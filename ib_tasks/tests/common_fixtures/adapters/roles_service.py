

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
def get_all_valid_read_permission_roles(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.roles_service.RolesService.get_all_valid_read_permission_roles")
    valid_read_permission_roles = [
        "ALL_ROLES", "FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"
    ]
    mock.return_value = valid_read_permission_roles
    return mock


def get_all_valid_write_permission_roles(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.roles_service.RolesService.get_all_valid_write_permission_roles")
    valid_write_permission_roles = [
        "ALL_ROLES", "FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"
    ]
    mock.return_value = valid_write_permission_roles
    return mock


def get_user_role_ids(mocker):
    mock = mocker.patch(
        "ib_tasks.adapters.roles_service.RolesService.get_user_role_ids")
    user_role_ids = [
        "FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"
    ]
    mock.return_value = user_role_ids
    return mock
