"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetBoardsDetailsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read', 'write']}}

    @pytest.fixture()
    def setup(self):
        from ib_boards.tests.factories.models import BoardFactory
        from ib_boards.tests.factories.models import ColumnFactory
        from ib_boards.tests.factories.models import ColumnPermissionFactory

        BoardFactory.reset_sequence()
        BoardFactory.create_batch(size=10)

        board = BoardFactory()
        ColumnFactory.reset_sequence()
        ColumnPermissionFactory.reset_sequence()
        columns = ColumnFactory.create_batch(size=4, board=board)
        ColumnPermissionFactory.create_batch(size=2, column=columns[0])
        ColumnPermissionFactory.create_batch(size=2, column=columns[1])
        ColumnPermissionFactory.create_batch(size=2, column=columns[2])
        ColumnPermissionFactory.create_batch(size=2, column=columns[3])

    @pytest.mark.django_db
    def test_case(self, snapshot, setup):
        body = {}
        path_params = {}
        query_params = {'limit': 10, 'offset': 0}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
