import pytest


class TestAddMentionUsersToComment:

    @pytest.mark.django_db
    def test_with_valid_comment_id(self, create_comments, comment_storage):
        # Arrange
        mention_user_ids = [
            "31be920b-7b4c-49e7-8adb-41a0c18da848",
            "01be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        comment_id = "21be920b-7b4c-49e7-8adb-41a0c18da848"

        # Act
        comment_storage.add_mention_users_to_comment(
            comment_id=comment_id, mention_user_ids=mention_user_ids)

        # Assert
        from ib_discussions.models.comment import CommentWithMentionUserId
        response_mention_user_ids = CommentWithMentionUserId.objects.filter(
            comment_id=comment_id
        ).values_list("mention_user_id", flat=True)

        assert list(response_mention_user_ids) == mention_user_ids
