import datetime
from uuid import UUID

import pytest


class TestGetCommentsForDiscussion:

    @pytest.mark.django_db
    def test_with_valid_details_return_response(self, comment_storage,
                                                create_comments):
        # Arrange
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"

        comment_list = [
            {
                "comment_id": '91be920b-7b4c-49e7-8adb-41a0c18da848',
                "user_id": '31be920b-7b4c-49e7-8adb-41a0c18da848',
                "created_at": datetime.datetime(2008, 1, 1, 0, 0),
                "parent_comment_id": None
            },
            {
                "comment_id": '11be920b-7b4c-49e7-8adb-41a0c18da848',
                "user_id": '01be920b-7b4c-49e7-8adb-41a0c18da848',
                "created_at": datetime.datetime(2020, 5, 1, 0, 0),
                "parent_comment_id": None
            },
            {
                "comment_id": '21be920b-7b4c-49e7-8adb-41a0c18da848',
                "user_id": '77be920b-7b4c-49e7-8adb-41a0c18da848',
                "created_at": datetime.datetime(2020, 1, 20, 0, 0),
                "parent_comment_id": None
            }
        ]

        from ib_discussions.tests.factories.storage_dtos import \
            CommentDTOFactory
        expected_comment_dtos = [
            CommentDTOFactory(
                comment_id=comment_dict["comment_id"],
                user_id=comment_dict["user_id"],
                created_at=comment_dict["created_at"],
                parent_comment_id=comment_dict["parent_comment_id"]
            )
            for comment_dict in comment_list
        ]
        # Act
        response = comment_storage.get_comments_for_discussion_dtos(
            discussion_id=discussion_id
        )

        # Assert
        assert response == expected_comment_dtos
