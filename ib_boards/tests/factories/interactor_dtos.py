"""
Created on: 14/07/20
Author: Pavankumar Pamuru

"""
import json

import factory

from ib_boards.interactors.dtos import BoardDTO, ColumnDTO


class BoardDTOFactory(factory.Factory):
    class Meta:
        model = BoardDTO

    board_id = factory.Sequence(lambda n: f'BOARD_ID_{n + 1}')
    display_name = factory.Sequence(lambda n: f'BOARD_DISPLAY_NAME')


class ColumnDTOFactory(factory.Factory):
    class Meta:
        model = ColumnDTO

    column_id = factory.Sequence(lambda n: f'COLUMN_ID_{n + 1}')
    display_name = factory.Sequence(lambda n: f'COLUMN_DISPLAY_NAME_{n + 1}')
    task_template_stages = json.dumps({
        "FIN_PR": ["PR_PAYMENT_REQUEST_DRAFTS"]
    })
    user_role_ids = ['ALL_ROLES']
    column_summary = 'COLUMN_SUMMARY'
    task_summary_fields = json.dumps(
        {
            "CardInfo_Requester": "Field Description"
        }
    )
    board_id = "BOARD_ID_0"
