"""
check the exception cases
"""
from uuid import UUID

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02CreateDiscussionAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    # @pytest.mark.django_db
    # def test_invalid_entity_id_raise_exception(self, snapshot):
    #     from ib_discussions.constants.enum import EntityType
    #     from ib_discussions.tests.factories.models import EntityFactory
    #
    #     entity_ids = [
    #         UUID('31be920b-7b4c-49e7-8adb-41a0c18da848'),
    #         UUID('4c28801f-7084-4b93-a938-f261aedf8f29'),
    #         UUID('64eade81-86d0-43d4-9575-d3482aaa30e5'),
    #     ]
    #     for entity_id in entity_ids:
    #         EntityFactory(id=entity_id)
    #
    #     entity_id = "41be920b-7b4c-49e7-8adb-41a0c18da848"
    #     entity_type = EntityType.TASK.value
    #     title = "Interactor"
    #     description = "test for interactor"
    #     body = {
    #         'entity_id': entity_id,
    #         'entity_type': entity_type,
    #         'title': title,
    #         'description': description}
    #     path_params = {}
    #     query_params = {}
    #     headers = {}
    #     response = self.make_api_call(
    #         body=body, path_params=path_params,
    #         query_params=query_params, headers=headers, snapshot=snapshot
    #     )
    #
    # @pytest.mark.django_db
    # def test_invalid_entity_type_for_entity_id_raise_exception(self, snapshot):
    #     from ib_discussions.constants.enum import EntityType
    #     from ib_discussions.tests.factories.models import EntityFactory
    #
    #     entity_ids = [
    #         UUID('31be920b-7b4c-49e7-8adb-41a0c18da848'),
    #         UUID('4c28801f-7084-4b93-a938-f261aedf8f29'),
    #         UUID('64eade81-86d0-43d4-9575-d3482aaa30e5'),
    #     ]
    #     for entity_id in entity_ids:
    #         EntityFactory(id=entity_id)
    #
    #     entity_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
    #     entity_type = EntityType.COLUMN.value
    #     title = "Interactor"
    #     description = "test for interactor"
    #     body = {
    #         'entity_id': entity_id,
    #         'entity_type': entity_type,
    #         'title': title,
    #         'description': description}
    #     path_params = {}
    #     query_params = {}
    #     headers = {}
    #     response = self.make_api_call(
    #         body=body, path_params=path_params,
    #         query_params=query_params, headers=headers, snapshot=snapshot
    #     )
