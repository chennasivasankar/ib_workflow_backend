import pytest


class TestCreateReplyToComment:

    @pytest.mark.django_db
    def test_create_reply_to_comment_return_response(self, create_comments,
                                                     comment_storage):
        # Arrange
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_id = "13be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_content = "It is correct"
        user_id = "77be920b-7b4c-49e7-8adb-41a0c18da848"

        # Act
        comment_reply_id = comment_storage.create_reply_to_comment(
            discussion_id=discussion_id, user_id=user_id,
            comment_content=comment_content, parent_comment_id=comment_id
        )

        # Assert
        from ib_discussions.models import Comment
        comment_object = Comment.objects.get(id=comment_reply_id)

        assert str(comment_object.parent_comment_id) == comment_id
        assert comment_object.content == comment_content
        assert comment_object.user_id == user_id
        assert str(comment_object.discussion_id) == discussion_id
