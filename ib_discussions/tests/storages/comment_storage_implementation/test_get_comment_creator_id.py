import pytest


class TestGetCommentCreateId:

    @pytest.mark.django_db
    def test_valid_comment_id_return_user_id(
            self, create_comments, comment_storage):
        # Arrange
        comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"

        # Act
        response = comment_storage.get_comment_creator_id(comment_id=comment_id)

        # Assert
        assert response == user_id
