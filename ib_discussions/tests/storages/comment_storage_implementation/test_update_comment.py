import pytest


class TestUpdateComment:

    @pytest.mark.django_db
    def test_with_valid_comment_id_update_comment(
            self, create_comments, comment_storage):
        # Arrange
        comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_content = "Hai, How are you"

        # Act
        comment_storage.update_comment(
            comment_id=comment_id, comment_content=comment_content)

        # Assert
        from ib_discussions.models import Comment
        comment_object = Comment.objects.get(id=comment_id)

        assert str(comment_object.id) == comment_id
        assert comment_object.content == comment_content
