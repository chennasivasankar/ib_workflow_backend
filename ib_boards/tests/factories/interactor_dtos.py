"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""

import factory

from ib_boards.interactors.dtos import BoardDTO, ColumnDTO, \
    TaskTemplateStagesDTO, TaskSummaryFieldsDTO, ActionDTO, \
    TaskStatusDTO, TaskDTO
from ib_boards.interactors.dtos import TaskColumnDTO


class TaskColumnDTOFactory(factory.Factory):
    class Meta:
        model = TaskColumnDTO

    column_id = factory.Sequence(lambda n: "column_id_%d" % n)
    task_id = factory.Sequence(lambda n: "task_id_%d" % n)


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


class TaskDTOFactory(factory.Factory):
    class Meta:
        model = TaskDTO

    task_id = factory.Sequence(lambda n: f'TASK_ID_{n + 1}')
    field_type = factory.Sequence(lambda n: f'FIELD_TYPE_ID_{n + 1}')
    key = factory.Sequence(lambda n: f'KEY_{n + 1}')
    value = factory.Sequence(lambda n: f'VALUE_{n + 1}')


class ActionDTOFactory(factory.Factory):
    class Meta:
        model = ActionDTO

    action_id = factory.Sequence(lambda n: f'ACTION_ID_{n + 1}')
    name = factory.Sequence(lambda n: f'NAME_{n + 1}')
    button_text = factory.Sequence(lambda n: f'BUTTON_TEXT_{n + 1}')
    button_color = factory.Sequence(lambda n: f'BUTTON_COLOR_{n + 1}')
    task_id = factory.Sequence(lambda n: f'TASK_ID_{n + 1}')


class TaskStatusDTOFactory(factory.Factory):
    class Meta:
        model = TaskStatusDTO

    stage = factory.Sequence(lambda n: f'STAGE_ID_{n + 1}')
    status = factory.Sequence(lambda n: f'STATUS_ID_{n + 1}')
