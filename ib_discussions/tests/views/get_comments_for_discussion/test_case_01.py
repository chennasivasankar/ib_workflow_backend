"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetCommentsForDiscussionAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

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
        CommentWithMultiMediaFactory(comment=comment_objects[0],
                                     multimedia=multimedia_objects[0])
        CommentWithMultiMediaFactory(comment=comment_objects[0],
                                     multimedia=multimedia_objects[1])
        CommentWithMultiMediaFactory(comment=comment_objects[1],
                                     multimedia=multimedia_objects[1])

        from ib_discussions.tests.factories.models import \
            CommentWithMentionUserIdFactory
        CommentWithMentionUserIdFactory(comment=comment_objects[0],
                                        mention_user_id=user_ids[0])
        CommentWithMentionUserIdFactory(comment=comment_objects[0],
                                        mention_user_id=user_ids[1])
        CommentWithMentionUserIdFactory(comment=comment_objects[1],
                                        mention_user_id=user_ids[1])

        body = {}
        path_params = {"discussion_id": discussion_id}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
