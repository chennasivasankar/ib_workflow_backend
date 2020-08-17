"""
test all cases of delete checklist items
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01DeleteChecklistItemsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['delete']}}

    @pytest.mark.django_db
    def test_success_case_for_delete_checklist_items(self, snapshot):
        checklist_item_id = '1c719377-105f-41a7-9d30-ad51d7beee2a'
        body = {'checklist_item_ids': [checklist_item_id]}
        path_params = {}
        query_params = {}
        headers = {}
        from ib_utility_tools.tests.factories.models import \
            ChecklistItemFactory
        ChecklistItemFactory.create(checklist_item_id=checklist_item_id)
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.mark.django_db
    def test_duplicate_items_response(self, snapshot):
        checklist_item_ids = ['1c719377-105f-41a7-9d30-ad51d7beee2a',
                              '1c719377-105f-41a7-9d30-ad51d7beee2a']
        body = {'checklist_item_ids': checklist_item_ids}
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.mark.django_db
    def test_invalid_checklist_item_ids_response(self, snapshot):
        checklist_item_ids = ['1c719377-105f-41a7-9d30-ad51d7beee2a']
        body = {'checklist_item_ids': checklist_item_ids}
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)
