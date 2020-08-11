"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""

import factory

from ib_boards.interactors.dtos import BoardDTO, ColumnDTO, \
    TaskTemplateStagesDTO, TaskSummaryFieldsDTO, \
    TaskStatusDTO, FieldDetailsDTO, ActionDetailsDTO, TaskIdStageDTO, \
    ColumnTaskIdsDTO
from ib_boards.interactors.dtos import ColumnTasksDTO
from ib_boards.interactors.storage_interfaces.dtos import ColumnStageIdsDTO
from ib_tasks.interactors.task_dtos import TaskDetailsConfigDTO, \
    GetTaskDetailsDTO


class TaskColumnDTOFactory(factory.Factory):
    class Meta:
        model = ColumnTasksDTO

    column_id = factory.Sequence(lambda n: f"COLUMN_ID_{n + 1}")
    task_id = factory.Sequence(lambda n: "task_id_%d" % n)
    stage_id = factory.Sequence(lambda n: f'stage_id_{n}')


class ColumnStageIdsDTOFactory(factory.Factory):
    class Meta:
        model = ColumnStageIdsDTO

    column_id = factory.Sequence(lambda n: f"COLUMN_ID_{n + 1}")
    stage_ids = factory.Iterator(
        [
            ['STAGE_ID_1', 'STAGE_ID_2'],
            ['STAGE_ID_3', 'STAGE_ID_4'],
            ['STAGE_ID_5', 'STAGE_ID_6'],
        ]
    )


class TaskTemplateStagesDTOFactory(factory.Factory):
    class Meta:
        model = TaskTemplateStagesDTO

    task_template_id = factory.Sequence(lambda n: f'TASK_TEMPLATE_ID_{n + 1}')
    stages = ['PR_PAYMENT_REQUEST_DRAFTS', 'PR_PENDING_RP_APPROVAL']


class TaskSummaryFieldsDTOFactory(factory.Factory):
    class Meta:
        model = TaskSummaryFieldsDTO

    task_id = factory.Sequence(lambda n: f'TASK_TEMPLATE_ID_{n + 1}')
    summary_fields = ['Price', 'task_name']


class BoardDTOFactory(factory.Factory):
    class Meta:
        model = BoardDTO

    board_id = factory.Sequence(lambda n: f'BOARD_ID_{n + 1}')
    name = factory.Sequence(lambda n: f'BOARD_DISPLAY_NAME')


class ColumnDTOFactory(factory.Factory):
    class Meta:
        model = ColumnDTO

    column_id = factory.Sequence(lambda n: f'COLUMN_ID_{n + 1}')
    name = factory.Sequence(lambda n: f'COLUMN_DISPLAY_NAME_{n + 1}')
    display_order = factory.Sequence(lambda n: n + 1)
    task_template_stages = TaskTemplateStagesDTOFactory.create_batch(5)
    user_role_ids = ['ALL_ROLES']
    column_summary = 'COLUMN_SUMMARY'
    column_actions = 'COLUMN_ACTIONS'
    list_view_fields = TaskSummaryFieldsDTOFactory.create_batch(5)
    kanban_view_fields = TaskSummaryFieldsDTOFactory.create_batch(5)
    board_id = "BOARD_ID_0"


class FieldDetailsDTOFactory(factory.Factory):
    class Meta:
        model = FieldDetailsDTO

    field_id = factory.Sequence(lambda n: f'FIELD_ID_{n + 1}')
    field_type = factory.Sequence(lambda n: f'FIELD_TYPE_ID_{n + 1}')
    key = factory.Sequence(lambda n: f'KEY_{n + 1}')
    value = factory.Sequence(lambda n: f'VALUE_{n + 1}')
    stage_id = factory.Sequence(lambda n: f'STAGE_ID_{n + 1}')


class ActionDTOFactory(factory.Factory):
    class Meta:
        model = ActionDetailsDTO

    action_id = factory.Sequence(lambda n: f'ACTION_ID_{n + 1}')
    name = factory.Sequence(lambda n: f'NAME_{n + 1}')
    button_text = factory.Sequence(lambda n: f'BUTTON_TEXT_{n + 1}')
    button_color = factory.Sequence(lambda n: f'BUTTON_COLOR_{n + 1}')
    stage_id = factory.Sequence(lambda n: f'STAGE_ID_{n + 1}')


class TaskStatusDTOFactory(factory.Factory):
    class Meta:
        model = TaskStatusDTO

    stage = factory.Sequence(lambda n: f'STAGE_ID_{n + 1}')
    status = factory.Sequence(lambda n: f'STATUS_ID_{n + 1}')


class TaskStageIdDTOFactory(factory.Factory):
    class Meta:
        model = TaskIdStageDTO

    stage_id = factory.Sequence(lambda n: f'STAGE_ID_{n + 1}')
    task_id = factory.Sequence(lambda n: f'TASK_ID_{n + 1}')


class ColumnTaskIdsDTOFactory(factory.Factory):
    class Meta:
        model = ColumnTaskIdsDTO

    unique_key = factory.Sequence(lambda n: f'COLUMN_ID_{n + 1}')
    task_stage_ids = TaskStageIdDTOFactory.create_batch(3)
    total_tasks = 10


class TaskDetailsConfigDTOFactory(factory.Factory):
    class Meta:
        model = TaskDetailsConfigDTO

    unique_key = factory.Sequence(lambda n: f'COLUMN_ID_{n + 1}')
    stage_ids = factory.Iterator(
        [
            ['STAGE_ID_1', 'STAGE_ID_2'],
            ['STAGE_ID_3', 'STAGE_ID_4'],
            ['STAGE_ID_5', 'STAGE_ID_6'],
        ]
    )
    offset = 0
    limit = 10
    user_id = 'user_id_1'


class GetTaskDetailsDTOFactory(factory.Factory):
    class Meta:
        model = GetTaskDetailsDTO

    stage_id = factory.Sequence(lambda n: f'STAGE_ID_{n + 1}')
    task_id = factory.Sequence(lambda n: f'TASK_ID_{n + 1}')
