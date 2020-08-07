import pytest


class TestIsDiscussionIdExists:

    @pytest.fixture()
    def storage(self):
        from ib_discussions.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()
        return storage

    @pytest.mark.django_db
    def test_discussion_id_not_exists_return_false(self, storage):
        # Arrange
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        expected_response = False

        # Act
        response = storage.is_discussion_id_exists(
            discussion_id=discussion_id
        )

        # Assert
        assert response == expected_response

    @pytest.mark.django_db
    def test_discussion_id_exists_return_true(self, storage):
        # Arrange
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_discussions.tests.factories.models import DiscussionFactory
        DiscussionFactory(id=discussion_id)
        expected_response = True

        # Act
        response = storage.is_discussion_id_exists(
            discussion_id=discussion_id
        )

        # Assert
        assert response == expected_response
