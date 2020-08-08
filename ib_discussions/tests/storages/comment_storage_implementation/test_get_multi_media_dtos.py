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
        comment_id_with_multi_media_list = [{
            'comment_id': '11be920b-7b4c-49e7-8adb-41a0c18da848',
            'multi_media_id': '92be920b-7b4c-49e7-8adb-41a0c18da848',
            'format_type': 'VIDEO',
            'url': 'https://picsum.photos/200'
        }, {
            'comment_id': '91be920b-7b4c-49e7-8adb-41a0c18da848',
            'multi_media_id': '97be920b-7b4c-49e7-8adb-41a0c18da848',
            'format_type': 'IMAGE',
            'url': 'https://picsum.photos/200'
        }, {
            'comment_id': '91be920b-7b4c-49e7-8adb-41a0c18da848',
            'multi_media_id': '92be920b-7b4c-49e7-8adb-41a0c18da848',
            'format_type': 'VIDEO',
            'url': 'https://picsum.photos/200'
        }]
        from ib_discussions.tests.factories.storage_dtos import \
            CommentIdWithMultiMediaDTOFactory
        expected_comment_id_with_multi_media_dtos = [
            CommentIdWithMultiMediaDTOFactory(
                comment_id=comment_id_with_multi_media_dict["comment_id"],
                multi_media_id=comment_id_with_multi_media_dict["multi_media_id"],
                format_type=comment_id_with_multi_media_dict["format_type"],
                url=comment_id_with_multi_media_dict["url"]
            )
            for comment_id_with_multi_media_dict in
            comment_id_with_multi_media_list
        ]

        # Act
        response = comment_storage.get_multi_media_dtos(comment_ids=comment_ids)

        # Assert
        assert response == expected_comment_id_with_multi_media_dtos
