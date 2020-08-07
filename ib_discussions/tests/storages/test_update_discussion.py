import pytest


class TestUpdateDiscussion:

    @pytest.fixture()
    def storage(self):
        from ib_discussions.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()
        return storage

    @pytest.mark.django_db
    def test_with_valid_details_update_discussion(self, storage):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        title = "Cyber EYE"
        description = "Provide security"
        from ib_discussions.tests.factories.interactor_dtos import \
            DiscussionIdWithTitleAndDescriptionDTOFactory
        discussion_id_with_title_and_description_dto = DiscussionIdWithTitleAndDescriptionDTOFactory(
            discussion_id=discussion_id, title=title, description=description
        )

        from ib_discussions.tests.factories.models import DiscussionFactory
        DiscussionFactory(id=discussion_id, user_id=user_id)

        # Act
        storage.update_discussion(
            discussion_id_with_title_and_description_dto
        )

        # Assert
        from ib_discussions.models import Discussion
        discussion_object = Discussion.objects.get(id=discussion_id)

        assert discussion_object.title == title
        assert discussion_object.description == description
