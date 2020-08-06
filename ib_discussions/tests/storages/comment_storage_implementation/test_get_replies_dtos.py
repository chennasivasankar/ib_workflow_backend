import datetime
from uuid import UUID

import pytest


class TestGetRepliesDTOS:

    @pytest.mark.django_db
    def test_with_valid_details_return_response(self, comment_storage,
                                                create_comments):
        # Arrange
        comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        comments_list = [
            {
                "comment_id": UUID('19be920b-7b4c-49e7-8adb-41a0c18da848'),
                "comment_content": 'content',
                "user_id": '01be920b-7b4c-49e7-8adb-41a0c18da848',
                "created_at": datetime.datetime(2008, 1, 1, 0, 0),
                "parent_comment_id": UUID('91be920b-7b4c-49e7-8adb-41a0c18da848')
            },
            {
                "comment_id": UUID('12be920b-7b4c-49e7-8adb-41a0c18da848'),
                "comment_content": 'content',
                "user_id": '77be920b-7b4c-49e7-8adb-41a0c18da848',
                "created_at": datetime.datetime(2020, 5, 1, 0, 0),
                "parent_comment_id": UUID('91be920b-7b4c-49e7-8adb-41a0c18da848')
            }
        ]
        from ib_discussions.tests.factories.storage_dtos import \
            CommentDTOFactory
        expected_comment_dtos = [
            CommentDTOFactory(
                comment_id=comment_dict["comment_id"],
                comment_content=comment_dict["comment_content"],
                user_id=comment_dict["user_id"],
                created_at=comment_dict["created_at"],
                parent_comment_id=comment_dict["parent_comment_id"]
            )
            for comment_dict in comments_list
        ]

        # Act
        response = comment_storage.get_replies_dtos(comment_id=comment_id)

        # Assert
        assert response == expected_comment_dtos
