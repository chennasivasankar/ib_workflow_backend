import pytest


class TestGetRepliesForComments:

    @pytest.mark.django_db
    def test_get_replies_for_comments(self, comment_storage, create_comments):
        # Arrange
        comment_ids = [
            "91be920b-7b4c-49e7-8adb-41a0c18da848",
            "11be920b-7b4c-49e7-8adb-41a0c18da848",
            "21be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        expected_comment_replies_count_list = [
            {
                "comment_id": '91be920b-7b4c-49e7-8adb-41a0c18da848',
                "replies_count": 2
            },
            {
                "comment_id": '11be920b-7b4c-49e7-8adb-41a0c18da848',
                "replies_count": 1
            },
            {
                "comment_id": '21be920b-7b4c-49e7-8adb-41a0c18da848',
                "replies_count": 0
            }

        ]

        from ib_discussions.tests.factories.storage_dtos import \
            CommentIdWithRepliesCountDTOFactory
        expected_comment_replies_count_dtos = [
            CommentIdWithRepliesCountDTOFactory(
                comment_id=expected_comment_replies_count_dict["comment_id"],
                replies_count=expected_comment_replies_count_dict[
                    "replies_count"]
            )
            for expected_comment_replies_count_dict in
            expected_comment_replies_count_list
        ]

        # Act
        response = comment_storage.get_replies_count_for_comments(
            comment_ids=comment_ids
        )

        # Assert
        assert response == expected_comment_replies_count_dtos
