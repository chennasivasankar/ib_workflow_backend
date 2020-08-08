"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01UpdateTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {'task_id': 1, 'title': 'string', 'description': 'string', 'start_date': '2099-12-31', 'due_date': '2099-12-31', 'priority': 'HIGH', 'stage_assignee': {'stage_id': 1, 'assignee_id': 'string'}, 'task_gofs': [{'gof_id': 'string', 'same_gof_order': 1.1, 'gof_fields': [{'field_id': 'string', 'field_response': 'string'}]}]}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )