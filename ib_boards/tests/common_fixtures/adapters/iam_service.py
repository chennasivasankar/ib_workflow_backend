"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""
from typing import List


def adapter_mock(mocker, user_roles: List[str]):
    mock = mocker.patch(
        'ib_boards.adapters.iam_service.IamService.get_valid_user_role_ids'
    )
    mock.return_value = user_roles
    return mock


def adapter_mock_to_get_user_role(mocker, user_role: str):
    mock = mocker.patch(
        'ib_boards.adapters.iam_service.IamService.get_user_role_ids_based_on_project'
    )
    mock.return_value = user_role
    return mock


def mock_get_user_roles(mocker, user_id: str):
    mock = mocker.patch(
        'ib_boards.adapters.iam_service.IamService.get_user_roles'
    )

    return mock


def mock_validate_project_ids(mocker, project_ids: List[str]):
    mock = mocker.patch(
        'ib_boards.adapters.iam_service.IamService.validate_project_ids'
    )
    mock.return_value = project_ids
    return mock


def mock_for_validate_if_user_is_in_project(mocker):
    mock = mocker.patch(
        'ib_boards.adapters.iam_service.IamService.validate_if_user_is_in_project'
    )
    return mock
