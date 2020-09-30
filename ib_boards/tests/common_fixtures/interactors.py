"""
Created on: 16/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.tests.factories.interactor_dtos import TaskStatusDTOFactory


def get_board_details_mock(mocker):
    mock = mocker.patch(
        'ib_boards.interactors.get_board_details_interactor'
        '.GetBoardsDetailsInteractor.get_boards_details'
    )
    from ib_boards.tests.factories.storage_dtos import BoardDTOFactory
    mock.return_value = BoardDTOFactory.create_batch(3)
    return mock


def get_stage_display_logic_mock(mocker,
                                 task_status_dtos: List[TaskStatusDTOFactory]):
    mock = mocker.patch(
        'ib_boards.interactors.get_stage_display_logic_interactor'
        '.StageDisplayLogicInteractor.get_stage_display_logic_condition'
    )

    mock.return_value = task_status_dtos
    return mock


def get_task_details_mock(mocker, task_dtos, action_dtos):
    mock = mocker.patch(
        'ib_boards.interactors.get_tasks_details_interactor'
        '.GetTasksDetailsInteractor.get_task_details'
    )
    mock.return_value = task_dtos, action_dtos
    return mock


def get_assignee_details_mock(mocker):
    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService'
        '.get_tasks_assignees_details'
    )
    return mock


def column_tasks_interactor_mock(mocker, value):
    mock = mocker.patch(
        'ib_boards.interactors.get_column_tasks_interactor'
        '.GetColumnTasksInteractor.get_column_tasks')
    mock.return_value = value
    return mock


def get_column_tasks_with_column_ids_mock(mocker, task_field_dtos,
                                          task_action_dtos,
                                          task_stage_color_dtos,
                                          task_ids_stages_dtos,
                                          assignees_dtos):
    mock = mocker.patch(
        'ib_boards.interactors.get_tasks_details_for_the_column_ids'
        '.GetColumnsTasksDetailsInteractor.get_column_tasks_with_column_ids')
    mock.return_value = task_field_dtos, task_action_dtos, \
                        task_stage_color_dtos, task_ids_stages_dtos, \
                        assignees_dtos
    return mock
