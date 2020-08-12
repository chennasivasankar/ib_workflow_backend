"""
# Given invalid limit value raise exception
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetAllTasksOverviewAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        from ib_tasks.tests.common_fixtures.storages import mock_filter_tasks
        mock_filter_tasks(mocker)

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {}
        path_params = {}
        query_params = {'limit': 0, 'offset': 18}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
