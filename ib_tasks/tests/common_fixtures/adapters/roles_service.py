

def prepare_get_roles_for_invalid_mock(mocker):
    mock = mocker.patch(
        'ib_tasks.adapters.roles_service.RolesService.get_db_roles'
    )
    roles = ["VALID_ROLE_3"]
    mock.return_value = roles
    return mock


def prepare_get_roles_for_valid_mock(mocker):
    mock = mocker.patch(
        'ib_tasks.adapters.roles_service.RolesService.get_db_roles'
    )
    roles = ["VALID_ROLE_1", "VALID_ROLE_2", "VALID_ROLE_3"]
    mock.return_value = roles
    return mock
