import pytest


class TestDeleteComment:

    @pytest.mark.django_db
    def test_with_valid_comment_id(
            self, create_comments, comment_storage):
        # Arrange
        comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"

        # Act
        comment_storage.delete_comment(comment_id=comment_id)

        # Assert
        from ib_discussions.models import Comment
        comment_objects = Comment.objects.filter(id=comment_id)
        reply_objects = Comment.objects.filter(parent_comment_id=comment_id)

        assert comment_objects.exists() is False
        assert reply_objects.exists() is False
