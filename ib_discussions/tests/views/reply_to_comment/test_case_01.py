"""
Create reply to comments
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01ReplyToCommentAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    def _get_or_create_user(self):
        user_id = "c8939223-79a0-4566-ba13-b4fbf7db6f93"
        from ib_users.models import UserAccount
        user = UserAccount.objects.create(user_id=user_id)
        return user

    @pytest.mark.django_db
    def test_case(self, snapshot, mocker):
        user_id = "c8939223-79a0-4566-ba13-b4fbf7db6f93"
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"

        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_get_user_profile_dtos_mock
        get_user_profile_dtos_mock = prepare_get_user_profile_dtos_mock(mocker)
        from ib_discussions.tests.factories.adapter_dtos import \
            UserProfileDTOFactory
        user_profile_dtos = [
            UserProfileDTOFactory(user_id=user_id)
        ]
        get_user_profile_dtos_mock.return_value = user_profile_dtos

        from ib_discussions.tests.factories.models import DiscussionFactory
        DiscussionFactory(id=discussion_id)

        from ib_discussions.tests.factories.models import CommentFactory
        CommentFactory.created_at.reset()
        comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        CommentFactory(
            id=comment_id,
            discussion_id=discussion_id,
            user_id=user_id
        )

        comment_reply_id = "01be920b-7b4c-49e7-8adb-41a0c18da848"

        from ib_discussions.tests.common_fixtures.storages import \
            prepare_create_reply_to_comment_mock
        create_reply_to_comment_mock = \
            prepare_create_reply_to_comment_mock(mocker)
        create_reply_to_comment_mock.return_value = comment_reply_id
        CommentFactory(
            id=comment_reply_id,
            parent_comment_id=comment_id,
            discussion_id=discussion_id,
            user_id=user_id
        )

        body = {'comment_content': 'string'}
        path_params = {"comment_id": comment_id}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
