import pytest


class TestCreateCommentForDiscussion:

    @pytest.mark.django_db
    def test_with_valid_details_create_comment(self, comment_storage):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_content = "content"

        from ib_discussions.tests.factories.models import DiscussionFactory
        discussion_object = DiscussionFactory(
            id=discussion_id
        )

        from ib_discussions.tests.factories.models import ReplyToCommentFactory
        ReplyToCommentFactory(
            id=comment_id, user_id=user_id, discussion=discussion_object,
            parent_comment_id=None
        )

        # Act
        created_comment_id = comment_storage.create_comment_for_discussion(
            user_id=user_id, discussion_id=discussion_id,
            comment_content=comment_content
        )

        # Assert
        from ib_discussions.models.comment import Comment
        comment_object = Comment.objects.get(id=created_comment_id)

        assert str(comment_object.id) == created_comment_id
        assert comment_object.content == comment_content
        assert comment_object.parent_comment_id is None
        assert str(comment_object.discussion_id) == discussion_id
