import pytest


class TestGetParentCommentId:

    @pytest.mark.django_db
    def test_with_valid_details_return_response(self, create_comments,
                                                comment_storage):
        # Arrange
        comment_id = "13be920b-7b4c-49e7-8adb-41a0c18da848"
        expected_parent_comment_id = '11be920b-7b4c-49e7-8adb-41a0c18da848'

        # Act
        response = comment_storage.get_parent_comment_id(
            comment_id=comment_id
        )

        # Assert
        assert response == expected_parent_comment_id
