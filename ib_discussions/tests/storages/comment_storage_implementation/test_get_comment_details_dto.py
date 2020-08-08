import datetime
from uuid import UUID

import pytest


class TestGetCommentDetailsDTO:

    @pytest.mark.django_db
    def test_with_valid_comment_id_return_response(self, comment_storage,
                                                   mocker):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"

        from ib_discussions.tests.factories.storage_dtos import \
            CommentDTOFactory
        expected_comment_dto = CommentDTOFactory(
            comment_id=UUID('91be920b-7b4c-49e7-8adb-41a0c18da848'),
            comment_content='content',
            user_id='31be920b-7b4c-49e7-8adb-41a0c18da848',
            created_at=datetime.datetime(2008, 1, 1, 0, 0),
            parent_comment_id=None
        )

        from ib_discussions.tests.factories.models import DiscussionFactory
        discussion_object = DiscussionFactory(
            id=discussion_id
        )

        from ib_discussions.tests.factories.models import ReplyToCommentFactory
        ReplyToCommentFactory.created_at.reset()
        ReplyToCommentFactory(
            id=comment_id, user_id=user_id, discussion=discussion_object,
            parent_comment_id=None
        )

        # Act
        response = comment_storage.get_comment_details_dto(
            comment_id=comment_id
        )

        # Assert
        assert response == expected_comment_dto
