"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.interactors.dtos import StageAssigneesDTO


def adapter_mock(mocker, user_roles: List[str]):
    mock = mocker.patch(
        'ib_boards.adapters.iam_service.IamService.get_valid_user_role_ids'
    )
    mock.return_value = user_roles
    return mock


def get_tasks_assignees_details_mock(mocker, assignee_details_dtos: List[
    StageAssigneesDTO]):
    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService'
        '.get_tasks_assignees_details'
    )
    mock.return_value = assignee_details_dtos
    return mock


def adapter_mock_to_get_user_role(mocker, user_role: str):
    mock = mocker.patch(
        'ib_boards.adapters.iam_service.IamService'
        '.get_user_role_ids_based_on_project'
    )
    mock.return_value = user_role
    return mock


def mock_get_user_roles(mocker, roles: List[str]):
    mock = mocker.patch(
        'ib_boards.adapters.iam_service.IamService.get_user_roles'
    )
    mock.return_value = roles
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
