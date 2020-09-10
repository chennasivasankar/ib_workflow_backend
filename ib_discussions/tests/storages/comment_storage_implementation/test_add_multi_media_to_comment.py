import pytest


class TestAddMultiMediaToComment:

    @pytest.mark.django_db
    def test_with_valid_details(self, comment_storage, create_comments):
        # Arrange
        comment_id = "21be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_discussions.tests.factories.interactor_dtos import \
            MultimediaDTOFactory
        MultimediaDTOFactory.format_type.reset()
        multimedia_dtos = MultimediaDTOFactory.create_batch(2)

        # Act
        comment_storage.add_multimedia_to_comment(
            comment_id=comment_id, multimedia_dtos=multimedia_dtos
        )

        # Assert
        from ib_discussions.models.comment import CommentWithMultiMedia
        multimedia_objects_count = CommentWithMultiMedia.objects.filter(
            comment_id=comment_id
        ).count()

        assert multimedia_objects_count == 2
