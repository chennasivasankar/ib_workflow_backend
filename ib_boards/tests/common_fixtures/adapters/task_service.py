"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""
from typing import List


def adapter_mock(mocker, task_template_ids: List[str]):

    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService.validate_task_template_ids'
    )
    from ib_boards.exceptions.custom_exceptions import \
        InvalidTaskTemplateIdInStages
    mock.side_effect = InvalidTaskTemplateIdInStages(
        task_template_ids=task_template_ids
    )
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
