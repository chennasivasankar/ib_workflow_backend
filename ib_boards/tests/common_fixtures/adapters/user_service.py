"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""
from typing import List


def adapter_mock(mocker, user_roles: List[str]):
    mock = mocker.patch(
        'ib_boards.adapters.user_service.UserService.validate_user_role_ids'
    )
    from ib_boards.exceptions.custom_exceptions import InvalidUserRoles
    mock.side_effect = InvalidUserRoles(user_role_ids=user_roles)
    return mock