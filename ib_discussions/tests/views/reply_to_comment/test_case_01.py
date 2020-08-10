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
        comment_reply_id = "01be920b-7b4c-49e7-8adb-41a0c18da848"

        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_validate_user_ids_mock
        prepare_validate_user_ids_mock(mocker=mocker)

        user_ids = [
            "c8939223-79a0-4566-ba13-b4fbf7db6f93"
        ]
        mention_user_ids = [
            "10be920b-7b4c-49e7-8adb-41a0c18da848",
            "20be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_get_user_profile_dtos_mock
        get_user_profile_dtos_mock = prepare_get_user_profile_dtos_mock(mocker)
        from ib_discussions.tests.factories.adapter_dtos import \
            UserProfileDTOFactory
        user_profile_dtos = [
            UserProfileDTOFactory(user_id=user_id)
            for user_id in (user_ids + mention_user_ids)
        ]
        get_user_profile_dtos_mock.return_value = user_profile_dtos

        from ib_discussions.constants.enum import MultiMediaFormatEnum
        multimedia = [
            {
                "format_type": MultiMediaFormatEnum.IMAGE.value,
                "url": "https://picsum.photos/200"
            },
            {
                "format_type": MultiMediaFormatEnum.VIDEO.value,
                "url": "https://picsum.photos/200"
            }
        ]

        multimedia_ids = [
            "97be920b-7b4c-49e7-8adb-41a0c18da848",
            "92be920b-7b4c-49e7-8adb-41a0c18da848",
        ]
        from ib_discussions.tests.factories.storage_dtos import \
            CommentIdWithMultiMediaDTOFactory
        multimedia_dtos = [
            CommentIdWithMultiMediaDTOFactory(
                comment_id=comment_reply_id,
                multimedia_id=multimedia_ids[0],
                format_type=multimedia[0]["format_type"],
                url=multimedia[0]["url"]
            ),
            CommentIdWithMultiMediaDTOFactory(
                comment_id=comment_reply_id,
                multimedia_id=multimedia_ids[1],
                format_type=multimedia[1]["format_type"],
                url=multimedia[1]["url"]
            )
        ]
        from ib_discussions.tests.common_fixtures.storages import \
            prepare_get_multimedia_dtos_mock
        multimedia_mock = prepare_get_multimedia_dtos_mock(mocker)
        multimedia_mock.return_value = multimedia_dtos

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

        body = {
            'comment_content': "string",
            'mention_user_ids': mention_user_ids,
            'multimedia': multimedia
        }
        path_params = {"comment_id": comment_id}
        query_params = {}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
