"""
Check Whether it gets checklist items for given details
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
        entity_id, entity_type = setup
        body = {'entity_id': entity_id, 'entity_type': entity_type}
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
        from ib_utility_tools.tests.factories.models import \
            ChecklistFactory, ChecklistItemFactory
        entity_id = "09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a"
        entity_type = EntityType.TASK.value

        checklist_item_ids = ['7ee2c7b4-34c8-4d65-a83a-f87da75db24e',
                              '09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a']
        checklist_id = '2bdb417e-4632-419a-8ddd-085ea272c6eb'

        checklist_object = ChecklistFactory.create(checklist_id=checklist_id,
                                                   entity_id=entity_id,
                                                   entity_type=entity_type)
        ChecklistItemFactory.reset_sequence(1)
        for checklist_item_id in checklist_item_ids:
            ChecklistItemFactory.create(checklist_item_id=checklist_item_id,
                                        checklist=checklist_object)
        return entity_id, entity_type
