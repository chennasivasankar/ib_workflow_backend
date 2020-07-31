"""
# Given valid details
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase03GetSearchableValuesAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture()
    def setup(self, mocker):
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_user_dtos_based_on_limit_and_offset_mock
        get_user_dtos_based_on_limit_and_offset_mock_method = \
            get_user_dtos_based_on_limit_and_offset_mock(mocker)
        searchable_user_detail_dtos = get_user_dtos_based_on_limit_and_offset_mock_method(
        )
        return searchable_user_detail_dtos

    @pytest.mark.django_db
    def test_case(self, snapshot, setup):
        body = {}
        path_params = {}
        query_params = {'search_type': 'USER', 'limit': 2, 'offset': 0,
                        'search_query': 'string'}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
