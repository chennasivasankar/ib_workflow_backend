"""
# TODO: Update test case description
"""

import pytest
from django_swagger_utils.utils.test_v1 import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...common_fixtures.adapters.iam_service import \
    adapter_mock_to_get_user_role
from ...factories.models import UserStarredBoardFactory


class TestCase01GetBoardsDetailsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read', 'write']}}

    @pytest.fixture()
    def setup(self, mocker, api_user):
        from ib_boards.tests.factories.models import BoardFactory
        from ib_boards.tests.factories.models import ColumnFactory
        from ib_boards.tests.factories.models import ColumnPermissionFactory

        BoardFactory.reset_sequence()
        boards = BoardFactory.create_batch(size=10)
        UserStarredBoardFactory.reset_sequence()
        UserStarredBoardFactory(board=boards[1], user_id=api_user.user_id)
        UserStarredBoardFactory(board=boards[3], user_id=api_user.user_id)
        UserStarredBoardFactory(board=boards[7], user_id=api_user.user_id)
        roles = ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC", "FIN_PAYMENT_APPROVER",
                 "FIN_PAYMENTS_LEVEL1_VERIFIER", "FIN_PAYMENTS_LEVEL2_VERIFIER", "FIN_PAYMENTS_LEVEL3_VERIFIER"]
        user_roles = adapter_mock_to_get_user_role(mocker, api_user.user_id)
        user_roles.return_value = roles
        board = BoardFactory()
        ColumnFactory.reset_sequence()
        ColumnPermissionFactory.reset_sequence()
        columns = ColumnFactory.create_batch(size=4, board=board)
        ColumnPermissionFactory.create_batch(size=2, column=columns[0])
        ColumnPermissionFactory.create_batch(size=2, column=columns[1])
        ColumnPermissionFactory.create_batch(size=2, column=columns[2])
        ColumnPermissionFactory.create_batch(size=2, column=columns[3])

    @pytest.mark.django_db
    def test_case(self, mocker, snapshot, setup, api_user):
        body = {}
        path_params = {}
        query_params = {'limit': 11, 'offset': 0}
        headers = {}

        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
