

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
