"""
Check whether it updates the checklist item with given details
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01UpdateChecklistItemAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture()
    def setup(self, api_user):
        checklist_item_id = "413642ff-1272-4990-b878-6607a5e02bc1"
        from ib_utility_tools.tests.factories.models import (
            ChecklistItemFactory
        )
        ChecklistItemFactory.reset_sequence(1)
        ChecklistItemFactory.create(checklist_item_id=checklist_item_id)
        return checklist_item_id

    @pytest.mark.django_db
    def test_case(self, setup, snapshot):
        body = {
            'text': 'As a developer I should be able to update checklist item',
            'is_checked': True
        }
        checklist_item_id = setup
        path_params = {
            "checklist_item_id": checklist_item_id
        }
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
