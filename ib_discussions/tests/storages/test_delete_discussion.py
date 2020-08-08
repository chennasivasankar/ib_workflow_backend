import pytest


class TestDeleteDiscussion:

    @pytest.fixture()
    def storage(self):
        from ib_discussions.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()
        return storage

    @pytest.mark.django_db
    def test_with_valid_discussion_id_delete_discussion(self, storage):
        # Arrange
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_discussions.tests.factories.models import DiscussionFactory
        DiscussionFactory(id=discussion_id)
        is_discussion_objects_not_exists = False

        # Act
        storage.delete_discussion(discussion_id=discussion_id)

        # Assert
        from ib_discussions.models import Discussion
        discussion_objects = Discussion.objects.filter(id=discussion_id)

        assert discussion_objects.exists() == is_discussion_objects_not_exists
