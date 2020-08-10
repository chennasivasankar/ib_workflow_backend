"""
get all discussions
"""
import datetime
from uuid import UUID

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetDiscussionsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    def _get_or_create_user(self):
        user_id = "e597ab2f-a10c-4164-930e-23af375741cb"
        from ib_users.models import UserAccount
        user = UserAccount.objects.create(user_id=user_id)
        return user

    @pytest.fixture()
    def prepare_get_discussions_mock_setup(self, mocker):
        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_get_user_profile_dtos_mock
        get_user_profile_dtos_mock = prepare_get_user_profile_dtos_mock(mocker)
        user_ids = [
            "9cc22e39-2390-4d96-b7ac-6bb27816461f",
            "cd4eb7da-6a5f-4f82-82ba-12e40ab7bf5a",
            "e597ab2f-a10c-4164-930e-23af375741cb"
        ]
        from ib_discussions.tests.factories.adapter_dtos import \
            UserProfileDTOFactory
        user_profile_dtos = [
            UserProfileDTOFactory(user_id=user_id)
            for user_id in user_ids
        ]
        get_user_profile_dtos_mock.return_value = user_profile_dtos

    @pytest.mark.django_db
    def test_case(self, snapshot, prepare_get_discussions_mock_setup,
                  prepare_discussion_setup):
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
