from typing import List

from ib_boards.interactors.dtos import TaskStageIdDTO
from ib_boards.tests.factories.storage_dtos import TaskActionsDTOFactory, TaskFieldsDTOFactory


def prepare_task_details_dtos(mocker, task_dtos: List[TaskStageIdDTO],
                              user_id: str):
    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService'
    )

    actions_dto = [
        TaskActionsDTOFactory.create(
            task_id=task_dto.task_id
        ) for _index, task_dto in enumerate(task_dtos)
    ]

    fields_dto = [
        TaskFieldsDTOFactory.create(
            task_id=task_dto.task_id
        ) for _index, task_dto in enumerate(task_dtos)
    ]

    mock.return_value = actions_dto, fields_dto
    return mock
"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_boards.interactors.dtos import TaskIdStageDTO


def get_valid_task_template_ids_mock(mocker, task_template_ids: List[str]):

    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService.get_valid_task_template_ids'
    )
    mock.return_value = task_template_ids
    return mock


def get_valid_task_ids_mock(
        mocker, task_template_ids: List[str], task_ids: List[str]):

    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService.get_valid_task_template_ids'
    )
    mock.side_effect = [task_template_ids, task_ids]
    return mock


def get_valid_task_ids_for_kanban_view_mock(
        mocker, task_template_ids_for_stages: List[str],
        task_template_ids_list_view: List[str], task_ids: List[str]):

    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService.get_valid_task_template_ids'
    )
    mock.side_effect = [
        task_template_ids_for_stages,
        task_template_ids_list_view,
        task_ids
    ]
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


def get_task_ids_mock(mocker, task_stage_dtos: List[TaskIdStageDTO]):
    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService.get_task_ids_with_respective_stages'
    )

    mock.return_value = task_stage_dtos
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
