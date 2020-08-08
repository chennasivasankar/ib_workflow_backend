from typing import List

from ib_boards.constants.enum import ViewType
from ib_boards.interactors.dtos import TaskStageIdDTO, TaskCompleteDetailsDTO, \
from ib_boards.constants.enum import VIEWTYPE
from ib_boards.interactors.dtos import TaskStageIdDTO, \
    TaskCompleteDetailsDTO, \
    ColumnTaskIdsDTO
from ib_boards.tests.factories.storage_dtos import TaskActionsDTOFactory, \
    TaskFieldsDTOFactory


def prepare_task_details_dtos(mocker, task_dtos: List[TaskStageIdDTO],
                              user_id: str, view_type: ViewType):
    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService.get_task_complete_details'
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

    mock.return_value = fields_dto, actions_dto
    return mock


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
        mocker, task_template_ids_for_stages: List[str]):
    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService.get_valid_task_template_ids'
    )
    mock.return_value = task_template_ids_for_stages,

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
        'ib_boards.adapters.task_service.TaskService.get_task_ids_for_stage_ids'
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


def task_details_mock(mocker, task_details: List[TaskCompleteDetailsDTO]):
    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService.get_task_complete_details'
    )
    mock.return_value = task_details[0].field_dtos, task_details[0].action_dtos
    return mock


def task_ids_mock(mocker, task_stage_ids: List[ColumnTaskIdsDTO]):
    mock = mocker.patch(
        'ib_boards.adapters.task_service.TaskService.get_task_ids_for_stage_ids'
    )
    mock.return_value = task_stage_ids
    return mock
