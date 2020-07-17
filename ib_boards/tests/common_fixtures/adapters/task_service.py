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


def get_task_ids_mock(mocker, task_ids: List[str]):
    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService.get_task_ids'
    )

    mock.return_value = task_ids
    return mock


def validate_stage_ids_mock(mocker, stage_ids: List[str]):
    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService.validate_stage_ids'
    )

    from ib_boards.exceptions.custom_exceptions import InvalidStageIds
    mock.side_effect = InvalidStageIds(stage_ids=stage_ids)
    return mock


def get_stage_display_logics_mock(mocker):
    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService.get_stage_display_logics'
    )
    stage_display_logics = [
        "STATUS_ID_3 == STAGE_ID_3",
        "STATUS_ID_4 == STAGE_ID_4"
    ]
    mock.return_value = stage_display_logics
    return mock