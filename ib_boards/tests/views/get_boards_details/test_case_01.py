"""
# get board details
"""

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_boards.tests.common_fixtures.adapters.iam_service import (
    adapter_mock_to_get_user_role, mock_validate_project_ids,
    mock_for_validate_if_user_is_in_project)
from ib_boards.tests.factories.models import UserStarredBoardFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


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

        project_id = "project_id_1"
        BoardFactory.reset_sequence()
        boards = BoardFactory.create_batch(size=10, project_id=project_id)
        UserStarredBoardFactory.reset_sequence()
        UserStarredBoardFactory(board=boards[1], user_id=api_user.user_id)
        UserStarredBoardFactory(board=boards[3], user_id=api_user.user_id)
        UserStarredBoardFactory(board=boards[7], user_id=api_user.user_id)
        roles = ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC", "FIN_PAYMENT_APPROVER",
                 "FIN_PAYMENTS_LEVEL1_VERIFIER", "FIN_PAYMENTS_LEVEL2_VERIFIER",
                 "FIN_PAYMENTS_LEVEL3_VERIFIER"]
        user_roles = adapter_mock_to_get_user_role(mocker, api_user.user_id)
        user_roles.return_value = roles

        project_ids = [project_id]
        mock_validate_project_ids(mocker, project_ids)
        user_in_project_mock = mock_for_validate_if_user_is_in_project(mocker)
        user_in_project_mock.return_value = True

        board = BoardFactory(project_id=project_id)
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
        query_params = {'limit': 11, 'offset': 0, "project_id": "project_id_1"}
        headers = {}

        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
