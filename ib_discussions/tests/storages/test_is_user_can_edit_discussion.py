import pytest


class TestIsUserCanEditDiscussion:

    @pytest.fixture()
    def storage(self):
        from ib_discussions.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()
        return storage

    @pytest.mark.django_db
    def test_is_user_cannot_edit_return_false(self, storage):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        expected_response = False

        # Act
        response = storage.is_user_can_edit_discussion(
            user_id=user_id, discussion_id=discussion_id
        )

        # Assert
        assert response == expected_response

    @pytest.mark.django_db
    def test_is_user_can_edit_return_true(self, storage):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_discussions.tests.factories.models import DiscussionFactory
        DiscussionFactory(user_id=user_id, id=discussion_id)
        expected_response = True

        # Act
        response = storage.is_user_can_edit_discussion(
            user_id=user_id, discussion_id=discussion_id
        )

        # Assert
        assert response == expected_response
