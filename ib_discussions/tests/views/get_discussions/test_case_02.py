"""
test all exceptions
"""

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02GetDiscussionsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_invalid_offset_raise_exception(self, snapshot):
        entity_id = '31be920b-7b4c-49e7-8adb-41a0c18da848'
        from ib_discussions.constants.enum import EntityType
        from ib_discussions.constants.enum import SortByEnum
        from ib_discussions.constants.enum import FilterByEnum

        entity_type = EntityType.TASK.value
        offset = -1
        limit = 2
        filter_by = FilterByEnum.CLARIFIED.value
        sort_by = SortByEnum.LATEST.value
        body = {
            'entity_id': entity_id,
            'entity_type': entity_type,
            'filter_by': filter_by,
            'sort_by': sort_by
        }
        path_params = {}
        query_params = {'offset': offset, 'limit': limit}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    def test_invalid_limit_raise_exception(self, snapshot):
        from ib_discussions.constants.enum import EntityType
        from ib_discussions.constants.enum import SortByEnum
        from ib_discussions.constants.enum import FilterByEnum

        entity_id = '31be920b-7b4c-49e7-8adb-41a0c18da848'
        entity_type = EntityType.TASK.value
        offset = 1
        limit = -1
        filter_by = FilterByEnum.CLARIFIED.value
        sort_by = SortByEnum.LATEST.value
        body = {
            'entity_id': entity_id,
            'entity_type': entity_type,
            'filter_by': filter_by,
            'sort_by': sort_by
        }
        path_params = {}
        query_params = {'offset': offset, 'limit': limit}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.mark.django_db
    def test_user_profile_does_not_exist_raise_exception(
            self, snapshot, prepare_discussion_setup):

        from ib_discussions.constants.enum import EntityType
        from ib_discussions.constants.enum import SortByEnum
        from ib_discussions.constants.enum import FilterByEnum

        entity_id = '31be920b-7b4c-49e7-8adb-41a0c18da848'
        entity_type = EntityType.TASK.value
        offset = 1
        limit = 2
        filter_by = FilterByEnum.CLARIFIED.value
        sort_by = SortByEnum.LATEST.value
        body = {
            'entity_id': entity_id,
            'entity_type': entity_type,
            'filter_by': filter_by,
            'sort_by': sort_by
        }
        path_params = {}
        query_params = {'offset': offset, 'limit': limit}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
