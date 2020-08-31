"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01AddProjectAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            'name': 'string',
            'description': 'string',
            'logo_url': 'string',
            'team_ids': ['string']
        }
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body,
            path_params=path_params,
            query_params=query_params,
            headers=headers,
            snapshot=snapshot
        )
