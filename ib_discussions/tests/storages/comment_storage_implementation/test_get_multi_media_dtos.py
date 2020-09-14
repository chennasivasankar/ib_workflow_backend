import pytest


class TestGetMultiMediaDTOS:

    @pytest.mark.django_db
    def test_with_valid_comment_ids_return_response(self, create_comments,
                                                    comment_storage):
        # Arrange
        comment_ids = [
            "91be920b-7b4c-49e7-8adb-41a0c18da848",
            "11be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        comment_id_with_multimedia_list = [{
            'comment_id': '11be920b-7b4c-49e7-8adb-41a0c18da848',
            'multimedia_id': '92be920b-7b4c-49e7-8adb-41a0c18da848',
            'format_type': 'VIDEO'
        }, {
            'comment_id': '91be920b-7b4c-49e7-8adb-41a0c18da848',
            'multimedia_id': '97be920b-7b4c-49e7-8adb-41a0c18da848',
            'format_type': 'IMAGE'
        }, {
            'comment_id': '91be920b-7b4c-49e7-8adb-41a0c18da848',
            'multimedia_id': '92be920b-7b4c-49e7-8adb-41a0c18da848',
            'format_type': 'VIDEO'
        }]
        from ib_discussions.tests.factories.storage_dtos import \
            CommentIdWithMultiMediaDTOFactory
        expected_comment_id_with_multimedia_dtos = [
            CommentIdWithMultiMediaDTOFactory(
                comment_id=comment_id_with_multimedia_dict["comment_id"],
                multimedia_id=comment_id_with_multimedia_dict["multimedia_id"],
                format_type=comment_id_with_multimedia_dict["format_type"]
            )
            for comment_id_with_multimedia_dict in
            comment_id_with_multimedia_list
        ]

        # Act
        response = comment_storage.get_multimedia_dtos(comment_ids=comment_ids)

        # Assert
        assert response == expected_comment_id_with_multimedia_dtos
