# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestGetBoardDetails.test_get_board_details_given_board_id_and_stages response'] = GenericRepr("TaskBoardsDetailsDTO(board_dto=BoardDTO(board_id='BOARD_ID_11', name='BOARD_DISPLAY_NAME'), column_stage_dtos=[ColumnStageDTO(column_id='COLUMN_ID_1', stage_id='stage_id_1'), ColumnStageDTO(column_id='COLUMN_ID_1', stage_id='stage_id_2'), ColumnStageDTO(column_id='COLUMN_ID_1', stage_id='stage_id_3'), ColumnStageDTO(column_id='COLUMN_ID_2', stage_id='stage_id_1'), ColumnStageDTO(column_id='COLUMN_ID_2', stage_id='stage_id_2'), ColumnStageDTO(column_id='COLUMN_ID_2', stage_id='stage_id_3'), ColumnStageDTO(column_id='COLUMN_ID_3', stage_id='stage_id_1'), ColumnStageDTO(column_id='COLUMN_ID_3', stage_id='stage_id_2'), ColumnStageDTO(column_id='COLUMN_ID_3', stage_id='stage_id_3'), ColumnStageDTO(column_id='COLUMN_ID_4', stage_id='stage_id_1'), ColumnStageDTO(column_id='COLUMN_ID_4', stage_id='stage_id_2'), ColumnStageDTO(column_id='COLUMN_ID_4', stage_id='stage_id_3')], columns_dtos=[ColumnBoardDTO(column_id='COLUMN_ID_1', board_id='BOARD_ID_11', name='COLUMN_DISPLAY_NAME_1'), ColumnBoardDTO(column_id='COLUMN_ID_2', board_id='BOARD_ID_11', name='COLUMN_DISPLAY_NAME_2'), ColumnBoardDTO(column_id='COLUMN_ID_3', board_id='BOARD_ID_11', name='COLUMN_DISPLAY_NAME_3'), ColumnBoardDTO(column_id='COLUMN_ID_4', board_id='BOARD_ID_11', name='COLUMN_DISPLAY_NAME_4')])")
