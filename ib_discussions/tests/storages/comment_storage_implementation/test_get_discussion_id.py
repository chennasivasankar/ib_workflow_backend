import pytest


class TestGetDiscussionId:

    @pytest.mark.django_db
    def test_with_valid_detail_return_response(self, create_comments,
                                               comment_storage):
        # Arrange
        comment_id = "19be920b-7b4c-49e7-8adb-41a0c18da848"
        expected_discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"

        # Act
        response = comment_storage.get_discussion_id(comment_id=comment_id)

        # Assert
        assert response == expected_discussion_id
