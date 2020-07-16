"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""
import json

import factory

from ib_boards.interactors.dtos import CreateBoardDTO, ColumnDTO, \
    TaskTemplateStagesDTO, TaskSummaryFieldsDTO


class TaskTemplateStagesDTOFactory(factory.Factory):
    class Meta:
        model = TaskTemplateStagesDTO

    task_template_id = factory.Sequence(lambda n: f'TASK_TEMPLATE_ID_{n + 1}')
    stages = ['PR_PAYMENT_REQUEST_DRAFTS', 'PR_PENDING_RP_APPROVAL']


class TaskSummaryFieldsDTOFactory(factory.Factory):
    class Meta:
        model = TaskSummaryFieldsDTO

    task_id = factory.Sequence(lambda n: f'TASK_ID_{n + 1}')
    summary_fields = ['Price', 'task_name']


class CreateBoardDTOFactory(factory.Factory):
    class Meta:
        model = CreateBoardDTO

    board_id = factory.Sequence(lambda n: f'BOARD_ID_{n + 1}')
    display_name = factory.Sequence(lambda n: f'BOARD_DISPLAY_NAME')


class ColumnDTOFactory(factory.Factory):
    class Meta:
        model = ColumnDTO

    column_id = factory.Sequence(lambda n: f'COLUMN_ID_{n + 1}')
    display_name = factory.Sequence(lambda n: f'COLUMN_DISPLAY_NAME_{n + 1}')
    task_template_stages = TaskTemplateStagesDTOFactory.create_batch(2)
    user_role_ids = ['ALL_ROLES']
    column_summary = 'COLUMN_SUMMARY'
    task_summary_fields = TaskSummaryFieldsDTOFactory.create_batch(2)
    board_id = "BOARD_ID_0"
