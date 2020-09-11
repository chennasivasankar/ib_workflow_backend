"""
Check whether It creates a checklist item and returns checklist item id
"""
import json

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01CreateChecklistItemAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_given_entity_details_not_exists_returns_checklist_item_id(
            self, mocker, snapshot
    ):
        from uuid import UUID
        from ib_utility_tools.constants.enum import EntityType
        from ib_utility_tools.tests.common_fixtures.uuid_mock import \
            prepare_uuid_mock
        mock = prepare_uuid_mock(mocker)
        mock.return_value = UUID("f2c02d98-f311-4ab2-8673-3daa00757002")
        body = {'entity_id': "09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a",
                'entity_type': EntityType.TASK.value,
                'text': 'As a developer I should create a checklist item1',
                'is_checked': True
                }
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
        self._check_created_checklist_item_text(response, snapshot)

    @pytest.mark.django_db
    def test_given_entity_details_exists_returns_checklist_item_id(
            self, mocker, snapshot
    ):
        from uuid import UUID
        from ib_utility_tools.constants.enum import EntityType
        from ib_utility_tools.tests.common_fixtures.uuid_mock import \
            prepare_uuid_mock
        mock = prepare_uuid_mock(mocker)
        mock.return_value = UUID("f2c02d98-f311-4ab2-8673-3daa00757003")
        entity_id = "09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a"
        entity_type = EntityType.TASK.value
        from ib_utility_tools.tests.factories.models import ChecklistFactory
        ChecklistFactory.create(entity_id=entity_id, entity_type=entity_type)
        body = {'entity_id': entity_id,
                'entity_type': entity_type,
                'text': 'As a developer I should create a checklist item2',
                'is_checked': True
                }
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
        self._check_created_checklist_item_text(response, snapshot)

    @staticmethod
    def _check_created_checklist_item_text(response, snapshot):
        checklist_item_id = json.loads(response.content)["checklist_item_id"]
        from ib_utility_tools.models import ChecklistItem
        checklist_item_object = ChecklistItem.objects.get(
            checklist_item_id=checklist_item_id)
        snapshot.assert_match(checklist_item_object.text,
                              "checklist_item_text")
