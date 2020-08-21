"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetFiltersAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture(autouse=True)
    def setup(self, api_user):
        from ib_tasks.tests.factories.models import (
            FilterConditionFactory, FieldFactory,
            FilterFactory, TaskTemplateFactory
        )
        TaskTemplateFactory.reset_sequence()
        FilterConditionFactory.reset_sequence(1)
        FieldFactory.reset_sequence(1)
        FilterFactory.reset_sequence(1)
        filters = FilterFactory(created_by=api_user.user_id)
        FilterConditionFactory(filter=filters)


    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )