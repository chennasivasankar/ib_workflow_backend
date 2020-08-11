import pytest


class TestIsCommentIdExists:

    @pytest.mark.django_db
    def test_comment_id_not_exists_return_false(self, comment_storage,
                                                create_comments):
        # Arrange
        comment_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        expected_response = False

        # Act
        response = comment_storage.is_comment_id_exists(
            comment_id=comment_id
        )

        # Assert
        assert response == expected_response

    @pytest.mark.django_db
    def test_comment_id_exists_return_true(self, comment_storage,
                                           create_comments):
        # Arrange
        comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        expected_response = True

        # Act
        response = comment_storage.is_comment_id_exists(
            comment_id=comment_id
        )

        # Assert
        assert response == expected_response
