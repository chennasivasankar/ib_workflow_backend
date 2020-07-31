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
        columns = ColumnFactory.create_batch(
            3, board=board
        )
        ColumnPermissionFactory.create_batch(
            3, column=factory.Iterator(columns)
        )
