"""
add comment
"""
from unittest.mock import patch

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01AddCommentAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(self, mocker, snapshot):
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_content = "content"

        from ib_discussions.tests.common_fixtures.storages import \
            prepare_create_comment_for_discussion_mock
        create_comment_for_discussion_mock = \
            prepare_create_comment_for_discussion_mock(mocker)
        create_comment_for_discussion_mock.return_value = comment_id

        from ib_discussions.tests.factories.models import CommentFactory
        CommentFactory.created_at.reset()
        CommentFactory(
            id=comment_id,
            discussion_id=discussion_id,
            user_id="31be920b-7b4c-49e7-8adb-41a0c18da848"
        )

        from ib_discussions.tests.factories.models import DiscussionFactory
        DiscussionFactory(id=discussion_id)

        user_ids = [
            "31be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_get_user_profile_dtos_mock
        get_user_profile_dtos_mock = prepare_get_user_profile_dtos_mock(mocker)
        from ib_discussions.tests.factories.adapter_dtos import \
            UserProfileDTOFactory
        user_profile_dtos = [
            UserProfileDTOFactory(user_id=user_id)
            for user_id in user_ids
        ]
        get_user_profile_dtos_mock.return_value = user_profile_dtos

        body = {'comment_content': comment_content}
        path_params = {"discussion_id": discussion_id}
        query_params = {}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
