"""
Check whether It creates a checklist item and returns checklist item id
"""
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
    def test_case(self, mocker, snapshot):
        from uuid import UUID
        from ib_utility_tools.constants.enum import EntityType
        from ib_utility_tools.tests.common_fixtures.uuid_mock import \
            prepare_uuid_mock
        mock = prepare_uuid_mock(mocker)
        mock.return_value = UUID("f2c02d98-f311-4ab2-8673-3daa00757002")
        body = {'entity_id': "09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a",
                'entity_type': EntityType.TASK.value,
                'text': 'As a developer I should create a checklist item',
                'is_checked': True}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
