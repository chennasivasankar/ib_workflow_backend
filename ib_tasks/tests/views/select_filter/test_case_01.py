"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01SelectFilterAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def setup(self):
        from ib_tasks.tests.factories.models \
            import FilterConditionFactory, FieldFactory
        FilterConditionFactory.reset_sequence(1)
        FieldFactory.reset_sequence(1)
        FilterConditionFactory()

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {'filter_id': 1, 'action': 'ENABLED'}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )