import pytest


class TestGetCommentsCountForDiscussions:

    @pytest.fixture()
    def create_discussion_with_comments(self):
        from ib_discussions.constants.enum import EntityType
        from ib_discussions.tests.factories.models import DiscussionSetFactory

        entity_id = "00ce920b-7b4c-49e7-8adb-41a0c18da848"
        entity_type = EntityType.TASK.value
        discussion_set_id = "11ce920b-7b4c-49e7-8adb-41a0c18da848"
        discussion_set = DiscussionSetFactory(
            entity_id=entity_id, entity_type=entity_type, id=discussion_set_id)

        discussion_ids = [
            "09be920b-7b4c-49e7-8adb-41a0c18da848",
            "04be920b-7b4c-49e7-8adb-41a0c18da848",
            "10be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_discussions.tests.factories.models import DiscussionFactory
        discussion_objects = [
            DiscussionFactory(id=discussion_id, discussion_set=discussion_set)
            for discussion_id in discussion_ids
        ]

        user_ids = [
            "31be920b-7b4c-49e7-8adb-41a0c18da848",
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "77be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        comments_list = [
            {
                "id": "91be920b-7b4c-49e7-8adb-41a0c18da848",
                "discussion": discussion_objects[0],
                "user_id": user_ids[0]
            },
            {
                "id": "11be920b-7b4c-49e7-8adb-41a0c18da848",
                "discussion": discussion_objects[1],
                "user_id": user_ids[1]
            },
            {
                "id": "21be920b-7b4c-49e7-8adb-41a0c18da848",
                "discussion": discussion_objects[0],
                "user_id": user_ids[2]
            }
        ]
        from ib_discussions.tests.factories.models import CommentFactory
        CommentFactory.created_at.reset()
        comment_objects = [
            CommentFactory(
                id=comment_dict["id"],
                discussion=comment_dict["discussion"],
                user_id=comment_dict["user_id"]
            )
            for comment_dict in comments_list
        ]

    @pytest.mark.django_db
    def test_with_valid_details(self, storage, create_discussion_with_comments):
        # Arrange
        discussion_set_id = "11ce920b-7b4c-49e7-8adb-41a0c18da848"
        discussion_id_with_comments_count_list = [
            {
                "discussion_id": '09be920b-7b4c-49e7-8adb-41a0c18da848',
                "comments_count": 2
            },
            {
                "discussion_id": '04be920b-7b4c-49e7-8adb-41a0c18da848',
                "comments_count": 1
            },
            {
                "discussion_id": '10be920b-7b4c-49e7-8adb-41a0c18da848',
                "comments_count": 0
            }
        ]
        from ib_discussions.tests.factories.storage_dtos import \
            DiscussionIdWithCommentsCountDTOFactory
        expected_discussion_with_comments_count_dtos = [
            DiscussionIdWithCommentsCountDTOFactory(
                discussion_id=discussion_id_with_comments_count_dict["discussion_id"],
                comments_count=discussion_id_with_comments_count_dict["comments_count"]
            )
            for discussion_id_with_comments_count_dict in
            discussion_id_with_comments_count_list
        ]

        # Act
        response = storage.get_comments_count_for_discussions(
            discussion_set_id=discussion_set_id
        )

        # Assert
        assert response == expected_discussion_with_comments_count_dtos
