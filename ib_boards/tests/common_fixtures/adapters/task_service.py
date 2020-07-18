"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""
from typing import List


def get_valid_task_template_ids_mock(mocker, task_template_ids: List[str]):

    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService.get_valid_task_template_ids'
    )
    mock.return_value = task_template_ids[0:1]
    return mock


def get_valid_task_ids_mock(mocker, task_template_ids: List[str]):

    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService.get_valid_task_ids'
    )
    mock.return_value = task_template_ids[0:3]
    return mock


def adapter_mock_for_task_template_stages(mocker):
    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService.validate_task_template_stages_with_id'
    )

    from ib_boards.exceptions.custom_exceptions import \
        TaskTemplateStagesNotBelongsToTaskTemplateId
    mock.side_effect = TaskTemplateStagesNotBelongsToTaskTemplateId
    return mock


def adapter_mock_for_task_template_fields(mocker):
    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService.validate_task_task_summary_fields_with_id'
    )

    from ib_boards.exceptions.custom_exceptions import \
        TaskSummaryFieldsNotBelongsToTaskTemplateId
    mock.side_effect = TaskSummaryFieldsNotBelongsToTaskTemplateId
    return mock
