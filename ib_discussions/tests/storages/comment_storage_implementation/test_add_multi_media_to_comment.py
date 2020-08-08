import pytest


class TestAddMultiMediaToComment:

    @pytest.mark.django_db
    def test_with_valid_details(self, comment_storage, create_comments):
        # Arrange
        comment_id = "21be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_discussions.tests.factories.interactor_dtos import \
            MultiMediaDTOFactory
        MultiMediaDTOFactory.format_type.reset()
        multi_media_dtos = MultiMediaDTOFactory.create_batch(2)

        # Act
        comment_storage.add_multi_media_to_comment(
            comment_id=comment_id, multi_media_dtos=multi_media_dtos
        )

        # Assert
        from ib_discussions.models.comment import CommentWithMultiMedia
        multi_media_objects_count = CommentWithMultiMedia.objects.filter(
            comment_id=comment_id
        ).count()

        assert multi_media_objects_count == 2
