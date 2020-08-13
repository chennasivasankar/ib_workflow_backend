import pytest


class TestGetCommentIdWithMentionUserIdDTOS:

    @pytest.mark.django_db
    def test_with_valid_comment_ids_return_response(self, create_comments,
                                                    comment_storage):
        # Arrange
        comment_ids = [
            "91be920b-7b4c-49e7-8adb-41a0c18da848",
            "11be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        comment_id_and_mention_user_id_list = [
            {
                "comment_id": '11be920b-7b4c-49e7-8adb-41a0c18da848',
                "mention_user_id": '01be920b-7b4c-49e7-8adb-41a0c18da848'
            },
            {
                "comment_id": '91be920b-7b4c-49e7-8adb-41a0c18da848',
                "mention_user_id": '31be920b-7b4c-49e7-8adb-41a0c18da848'
            },
            {
                "comment_id": '91be920b-7b4c-49e7-8adb-41a0c18da848',
                "mention_user_id": '01be920b-7b4c-49e7-8adb-41a0c18da848'
            }
        ]
        from ib_discussions.tests.factories.storage_dtos import \
            CommentIdWithMentionUserIdDTOFactory
        expected_comment_id_and_mention_user_id_dtos = [
            CommentIdWithMentionUserIdDTOFactory(
                comment_id=comment_id_and_mention_user_id_dict["comment_id"],
                mention_user_id=comment_id_and_mention_user_id_dict[
                    "mention_user_id"]
            )
            for comment_id_and_mention_user_id_dict in
            comment_id_and_mention_user_id_list
        ]

        # Act
        response = comment_storage.get_comment_id_with_mention_user_id_dtos(
            comment_ids=comment_ids
        )

        # Assert
        assert response == expected_comment_id_and_mention_user_id_dtos
