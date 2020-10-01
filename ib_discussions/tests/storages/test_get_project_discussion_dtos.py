import factory
import pytest


class TestGetProjectDiscussionDTOs:

    @pytest.fixture()
    def storage_implementation(self):
        from ib_discussions.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()
        return storage

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
        user_ids = ["user_id_1", "user_id_2", "user_id_3"]
        from ib_discussions.tests.factories.models import DiscussionFactory
        DiscussionFactory.create_batch(
            size=3, discussion_set_id=discussion_set_id,
            user_id=factory.Iterator(user_ids)
        )
        DiscussionFactory.create_batch(
            size=3, discussion_set_id=discussion_set_id)
        return user_ids

    @pytest.fixture()
    def get_project_discussions_input_dto(self):
        from ib_discussions.tests.factories.interactor_dtos import \
            GetProjectDiscussionsInputDTOFactory
        GetProjectDiscussionsInputDTOFactory.reset_sequence(1)
        get_project_discussions_input_dto = GetProjectDiscussionsInputDTOFactory()
        return get_project_discussions_input_dto

    @pytest.mark.django_db
    def test_with_valid_details_return_response(
            self, storage_implementation, get_project_discussions_input_dto,
            create_discussions
    ):
        # Arrange
        from ib_discussions.constants.enum import FilterByEnum
        get_project_discussions_input_dto.filter_by_dto.filter_by = \
            FilterByEnum.POSTED_BY_ME.value
        get_project_discussions_input_dto.filter_by_dto.value = "user_id_1"

        discussion_set_id = 'f032383d-ea21-4da3-8194-a676be299987'
        user_ids = create_discussions
        from ib_discussions.tests.factories.storage_dtos import \
            DiscussionDTOFactory
        DiscussionDTOFactory.is_clarified.reset()
        expected_discussion_dtos = [DiscussionDTOFactory.create(
            user_id="user_id_1", discussion_set_id=discussion_set_id,
            is_clarified=True
        )]

        # Act
        response = storage_implementation.get_project_discussion_dtos(
            discussion_set_id=discussion_set_id, user_ids=user_ids,
            get_project_discussions_input_dto=get_project_discussions_input_dto
        )

        # Assert
        self._compare_two_complete_discussion_dtos(
            response, expected_discussion_dtos
        )

    def _compare_two_complete_discussion_dtos(
            self, discussion_dtos_list2,
            discussion_dtos_list1):
        for discussion_dto1, discussion_dto2 in list(
                zip(discussion_dtos_list2,
                    discussion_dtos_list1)):
            self._compare_two_complete_discussion_dto(
                discussion_dto1, discussion_dto2
            )

    @staticmethod
    def _compare_two_complete_discussion_dto(discussion_dto1,
                                             discussion_dto2):
        assert discussion_dto1.user_id == discussion_dto2.user_id
        assert discussion_dto1.discussion_set_id \
               == discussion_dto2.discussion_set_id
        assert discussion_dto1.title \
               == discussion_dto2.title
        assert discussion_dto1.description \
               == discussion_dto2.description
        assert discussion_dto1.is_clarified \
               == discussion_dto2.is_clarified
        assert discussion_dto1.created_at.replace(tzinfo=None) \
               == discussion_dto2.created_at.replace(tzinfo=None)
