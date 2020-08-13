"""
test with invalid limit value raises exception
"""

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase03GetStageSearchablePossibleAssigneesOfATaskAPITestCase(
        TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.parametrize('limit', [-1, 0, -5])
    @pytest.mark.django_db
    def test_case(self, snapshot, limit):
        body = {}
        path_params = {"stage_id": 1}
        query_params = {'limit': limit, 'offset': 0, 'search_query': 'string'}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
