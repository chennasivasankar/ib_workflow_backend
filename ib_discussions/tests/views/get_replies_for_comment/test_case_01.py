"""
get replies for comments
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetRepliesForCommentAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    def _get_or_create_user(self):
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_users.models import UserAccount
        user = UserAccount.objects.create(user_id=user_id)
        return user

    @pytest.mark.django_db
    def test_case(self, snapshot, mocker):
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_discussions.tests.factories.models import DiscussionFactory
        DiscussionFactory(id=discussion_id)

        user_ids = [
            "31be920b-7b4c-49e7-8adb-41a0c18da848",
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "77be920b-7b4c-49e7-8adb-41a0c18da848"
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

        comments_list = [
            {
                "id": "91be920b-7b4c-49e7-8adb-41a0c18da848",
                "discussion_id": discussion_id,
                "user_id": user_ids[0]
            },
            {
                "id": "11be920b-7b4c-49e7-8adb-41a0c18da848",
                "discussion_id": discussion_id,
                "user_id": user_ids[1]
            },
            {
                "id": "21be920b-7b4c-49e7-8adb-41a0c18da848",
                "discussion_id": discussion_id,
                "user_id": user_ids[2]
            }
        ]
        from ib_discussions.tests.factories.models import CommentFactory
        CommentFactory.created_at.reset()
        comment_objects = [
            CommentFactory(
                id=comment_dict["id"],
                discussion_id=comment_dict["discussion_id"],
                user_id=comment_dict["user_id"]
            )
            for comment_dict in comments_list
        ]

        replies_list = [
            {
                "id": "19be920b-7b4c-49e7-8adb-41a0c18da848",
                "discussion_id": discussion_id,
                "user_id": user_ids[1]
            },
            {
                "id": "12be920b-7b4c-49e7-8adb-41a0c18da848",
                "discussion_id": discussion_id,
                "user_id": user_ids[2]
            },
            {
                "id": "13be920b-7b4c-49e7-8adb-41a0c18da848",
                "discussion_id": discussion_id,
                "user_id": user_ids[0]
            }
        ]
        from ib_discussions.tests.factories.models import ReplyToCommentFactory
        ReplyToCommentFactory.created_at.reset()
        reply_to_comment_objects = [
            ReplyToCommentFactory(
                id=replies_list[0]["id"],
                parent_comment=comment_objects[0],
                discussion_id=replies_list[0]["discussion_id"],
                user_id=replies_list[0]["user_id"]
            ),
            ReplyToCommentFactory(
                id=replies_list[1]["id"],
                parent_comment=comment_objects[0],
                discussion_id=replies_list[1]["discussion_id"],
                user_id=replies_list[1]["user_id"]
            ),
            ReplyToCommentFactory(
                id=replies_list[2]["id"],
                parent_comment=comment_objects[1],
                discussion_id=replies_list[2]["discussion_id"],
                user_id=replies_list[2]["user_id"]
            )
        ]

        multimedia_ids = [
            "97be920b-7b4c-49e7-8adb-41a0c18da848",
            "92be920b-7b4c-49e7-8adb-41a0c18da848",
            "93be920b-7b4c-49e7-8adb-41a0c18da848"
        ]

        from ib_discussions.tests.factories.models import MultiMediaFactory
        MultiMediaFactory.format_type.reset()
        multimedia_objects = [
            MultiMediaFactory(id=multimedia_id)
            for multimedia_id in multimedia_ids
        ]

        from ib_discussions.tests.factories.models import \
            CommentWithMultiMediaFactory
        CommentWithMultiMediaFactory(comment=reply_to_comment_objects[0],
                                     multimedia=multimedia_objects[0])
        CommentWithMultiMediaFactory(comment=reply_to_comment_objects[0],
                                     multimedia=multimedia_objects[1])
        CommentWithMultiMediaFactory(comment=reply_to_comment_objects[1],
                                     multimedia=multimedia_objects[1])

        from ib_discussions.tests.factories.models import \
            CommentWithMentionUserIdFactory
        CommentWithMentionUserIdFactory(comment=reply_to_comment_objects[0],
                                        mention_user_id=user_ids[0])
        CommentWithMentionUserIdFactory(comment=reply_to_comment_objects[0],
                                        mention_user_id=user_ids[1])
        CommentWithMentionUserIdFactory(comment=reply_to_comment_objects[1],
                                        mention_user_id=user_ids[1])

        body = {}
        path_params = {"comment_id": "91be920b-7b4c-49e7-8adb-41a0c18da848"}
        query_params = {}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
