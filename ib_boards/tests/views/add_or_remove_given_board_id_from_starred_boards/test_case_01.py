"""
# given action UNSTAR removes board from starred board
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils

from ib_boards.models import UserStarredBoard
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...common_fixtures.adapters.iam_service import adapter_mock_to_get_user_role
from ...factories.models import UserStarredBoardFactory, BoardFactory


class TestCase01AddOrRemoveGivenBoardIdFromStarredBoardsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read', 'write']}}

    @pytest.fixture()
    def setup(self, mocker):
        roles = ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC", "FIN_PAYMENT_APPROVER",
                 "FIN_PAYMENTS_LEVEL1_VERIFIER", "FIN_PAYMENTS_LEVEL2_VERIFIER", "FIN_PAYMENTS_LEVEL3_VERIFIER"]
        user_roles = adapter_mock_to_get_user_role(mocker, "user_id_0")
        user_roles.return_value = roles
        BoardFactory.reset_sequence()
        board = BoardFactory()
        UserStarredBoardFactory.reset_sequence()
        UserStarredBoardFactory(board=board)

    @pytest.mark.django_db
    def test_case(self, snapshot, setup):
        body = {'action': 'UNSTAR'}
        path_params = {"board_id": "BOARD_ID_1"}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
