"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""
from typing import List


def adapter_mock(mocker, user_roles: List[str]):
    mock = mocker.patch(
        'ib_boards.adapters.iam_service.IAMService.get_valid_user_role_ids'
    )
    mock.return_value = user_roles
    return mock


def adapter_mock_to_get_user_role(mocker, user_role: str):
    mock = mocker.patch(
        'ib_boards.adapters.iam_service.IAMService.get_user_role'
    )
    mock.return_value = user_role
    return mock