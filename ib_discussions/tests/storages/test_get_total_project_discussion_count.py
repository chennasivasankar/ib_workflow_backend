import factory
import pytest


class TestGetTotalProjectDiscussionCount:

    @pytest.fixture()
    def storage(self):
        from ib_discussions.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()
        return storage

    @pytest.fixture()
    def filter_by_dto(self):
        from ib_discussions.tests.factories.interactor_dtos import \
            FilterByDTOFactory
        from ib_discussions.constants.enum import FilterByEnum
        filter_by_dto = FilterByDTOFactory(
            filter_by=FilterByEnum.CLARIFIED.value,
            value=True
        )
        return filter_by_dto

    @pytest.fixture()
    def create_discussion_set(self):
        discussion_set_id = 'f032383d-ea21-4da3-8194-a676be299987'
        from ib_discussions.tests.factories.models import \
            DiscussionSetFactory
        DiscussionSetFactory(id=discussion_set_id)
        return discussion_set_id

    @pytest.fixture()
    def create_discussions(self, create_discussion_set):
        discussion_set_id = create_discussion_set
        user_ids = [
            "9cc22e39-2390-4d96-b7ac-6bb27816461f",
            "cd4eb7da-6a5f-4f82-82ba-12e40ab7bf5a",
            "e597ab2f-a10c-4164-930e-23af375741cb"
        ]
        from ib_discussions.tests.factories.models import DiscussionFactory
        DiscussionFactory.create_batch(
            size=3, discussion_set_id=discussion_set_id,
            user_id=factory.Iterator(user_ids)
        )
        DiscussionFactory.create_batch(
            size=3, discussion_set_id=discussion_set_id)
        return user_ids

    @pytest.mark.django_db
    def test_with_discussions_exists_for_given_details_return_response(
            self, storage, filter_by_dto, create_discussions):
        # Arrange
        expected_discussion_count = 3
        discussion_set_id = 'f032383d-ea21-4da3-8194-a676be299987'
        user_ids = create_discussions

        # Act
        response = storage.get_total_project_discussion_count(
            discussion_set_id=discussion_set_id, filter_by_dto=filter_by_dto,
            user_ids=user_ids
        )

        # Assert
        assert response == expected_discussion_count

    @pytest.mark.django_db
    def test_with_discussions_not_exists_for_given_details_return_response(
            self, storage, filter_by_dto, create_discussions):
        # Arrange
        expected_discussion_count = 0
        discussion_set_id = 'f032383d-ea21-4da3-8194-a676be299987'
        user_ids = [
            "1cc22e39-2390-4d96-b7ac-6bb27816461f",
            "ad4eb7da-6a5f-4f82-82ba-12e40ab7bf5a",
            "b597ab2f-a10c-4164-930e-23af375741cb"
        ]

        # Act
        response = storage.get_total_project_discussion_count(
            discussion_set_id=discussion_set_id, filter_by_dto=filter_by_dto,
            user_ids=user_ids
        )

        # Assert
        assert response == expected_discussion_count
