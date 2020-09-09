"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01ActOnTaskAndUpdateTaskStageAssigneesAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            'board_id':
            'string',
            'task_id':
            'string',
            'action_id':
            'string',
            'stage_assignees': [{
                'stage_id': 1,
                'assignee_id': 'string',
                'team_id': 'string'
            }]
        }
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
