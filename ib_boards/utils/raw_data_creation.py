"""
Created on: 31/07/20
Author: Pavankumar Pamuru

"""
import factory

from ib_boards.tests.factories.models import BoardFactory, ColumnFactory, \
    ColumnPermissionFactory


class DataCreation:

    @staticmethod
    def create_data():
        board = BoardFactory()
        BoardFactory.create_batch(19)
        columns = ColumnFactory.create_batch(
            4, board=board,
            task_selection_config="""{
                "template_1": ["stage_id_0", "stage_id_3"],
                "template_2": ["stage_id_1", "stage_id_4"],
                "template_3": ["stage_id_2", "stage_id_5"]
            }"""
        )
        ColumnPermissionFactory.create_batch(
            4, column=factory.Iterator(columns)
        )
