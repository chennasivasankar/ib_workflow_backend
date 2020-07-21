def get_valid_role_ids_in_given_role_ids(mocker):
    mock = mocker.patch("ib_tasks.adapters.roles_service.RolesService.get_valid_role_ids_in_given_role_ids")
    valid_role_ids = [
        "ALL_ROLES", "FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"
    ]
    mock.return_value = valid_role_ids
    return mock


def get_user_role_ids(mocker):
     mock = mocker.patch(
         "ib_tasks.adapters.roles_service.RolesService.get_user_role_ids")
     user_role_ids = [
         "FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"
     ]
     mock.return_value = user_role_ids

