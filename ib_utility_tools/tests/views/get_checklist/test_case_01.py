"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetChecklistAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(self, setup, snapshot):
        body = {'entity_id': 'string', 'entity_type': 'TASK'}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.fixture
    def setup(self):
        from ib_utility_tools.constants.enum import EntityType
        entity_id = "09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a"
        entity_type = EntityType.TASK.vslue
        from ib_utility_tools.tests.factories.models import \
            ChecklistItemFactory
        def checklist_item_dtos(self):
            from ib_utility_tools.tests.factories.storage_dtos import \
                ChecklistItemWithIdDTOFactory
            checklist_item_dtos = ChecklistItemWithIdDTOFactory.create_batch(
                size=3)
            return checklist_item_dtos
