from django_swagger_utils.utils.test import CustomAPITestCase

from ib_boards.tests.factories.models import (
    BoardFactory, ColumnFactory, ColumnPermissionFactory)


class CustomTestUtils(CustomAPITestCase):
    def create_boards(self):
        BoardFactory.reset_sequence()
        BoardFactory.create_batch(size=10)

    def create_columns(self):
        BoardFactory.reset_sequence()
        board = BoardFactory()
        ColumnFactory.reset_sequence()
        ColumnPermissionFactory.reset_sequence()
        columns = ColumnFactory.create_batch(size=4, board=board)
        ColumnPermissionFactory.create_batch(size=2, column=columns[0])
        ColumnPermissionFactory.create_batch(size=2, column=columns[1])
        ColumnPermissionFactory.create_batch(size=2, column=columns[2])
        ColumnPermissionFactory.create_batch(size=2, column=columns[3])
