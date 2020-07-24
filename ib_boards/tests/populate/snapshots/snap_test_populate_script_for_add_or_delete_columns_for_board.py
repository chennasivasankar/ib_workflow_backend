# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import GenericRepr, Snapshot

snapshots = Snapshot()

snapshots[
    'TestPopulateBoardsAndColumnsInteractor.test_with_valid_data_return_dtos boards'] = GenericRepr(
    "<QuerySet [<Board: Board object (BOARD_ID_1)>, <Board: Board object (BOARD_ID_2)>]>")

snapshots[
    'TestPopulateBoardsAndColumnsInteractor.test_with_valid_data_return_dtos columns'] = GenericRepr(
    "<QuerySet [<Column: Column object (COLUMN_ID_1)>, <Column: Column object (COLUMN_ID_2)>]>")

snapshots[
    'TestPopulateBoardsAndColumnsInteractor.test_with_valid_data_return_dtos column_permissions'] = GenericRepr(
    "<QuerySet [<ColumnPermission: ColumnPermission object (1)>, <ColumnPermission: ColumnPermission object (2)>, <ColumnPermission: ColumnPermission object (3)>, <ColumnPermission: ColumnPermission object (4)>]>")
