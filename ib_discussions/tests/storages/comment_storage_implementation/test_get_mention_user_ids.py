import pytest


class TestGetMentionUserIds:

    @pytest.mark.django_db
    def test_with_valid_comment_ids_return_response(self, create_comments,
                                                    comment_storage):
        # Arrange
        comment_ids = [
            "91be920b-7b4c-49e7-8adb-41a0c18da848",
            "11be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        expected_mention_user_ids = [
            '31be920b-7b4c-49e7-8adb-41a0c18da848',
            '01be920b-7b4c-49e7-8adb-41a0c18da848'
        ]

        # Act
        mention_user_ids = comment_storage.get_mention_user_ids(
            comment_ids=comment_ids)

        # Assert
        assert sorted(mention_user_ids) == sorted(expected_mention_user_ids)
