def get_all_valid_read_permission_roles(mocker):
    mock = mocker.patch("ib_tasks.adapters.roles_service.RolesService.get_all_valid_read_permission_roles")
    valid_read_permission_roles = [
        "ALL_ROLES", "FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"
    ]
    mock.return_value = valid_read_permission_roles
    return mock


def get_all_valid_write_permission_roles(mocker):
    mock = mocker.patch("ib_tasks.adapters.roles_service.RolesService.get_all_valid_write_permission_roles")
    valid_write_permission_roles = [
        "ALL_ROLES", "FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"
    ]
    mock.return_value = valid_write_permission_roles
    return mock
