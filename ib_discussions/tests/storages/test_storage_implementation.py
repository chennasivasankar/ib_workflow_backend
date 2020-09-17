import datetime

import pytest


class TestStorageImplementation:

    @pytest.fixture()
    def create_entity_objects(self):
        from ib_discussions.tests.factories.models import EntityFactory
        entity_ids = [
            '31be920b-7b4c-49e7-8adb-41a0c18da848',
            '4c28801f-7084-4b93-a938-f261aedf8f29',
            '64eade81-86d0-43d4-9575-d3482aaa30e5',
            '9cbbe720-9244-441e-b910-1c695b3a7cd1',
            'da145a02-e164-4203-9317-1d42bb68e3ce',
            '5c27801f-9084-7b93-a038-f261aedf8f29'
        ]
        for entity_id in entity_ids:
            EntityFactory(id=entity_id)

    @pytest.fixture()
    def create_discussion_set_objects(self):
        from ib_discussions.tests.factories.models import \
            DiscussionSetFactory
        entity_ids = [
            '31be920b-7b4c-49e7-8adb-41a0c18da848',
            '4c28801f-7084-4b93-a938-f261aedf8f29',
            '64eade81-86d0-43d4-9575-d3482aaa30e5',
            '9cbbe720-9244-441e-b910-1c695b3a7cd1',
            'da145a02-e164-4203-9317-1d42bb68e3ce'
        ]
        discussion_set_ids = [
            '641bfcc5-e1ea-4231-b482-f7f34fb5c7c4',
            '94557db1-c123-4e16-a69d-98a6a4850b84',
            '98ec9bf6-c83c-4f40-9f8c-bd1998b7e452',
            'e12c2408-fc30-4e55-8f9a-6847d915481e',
            'f032383d-ea21-4da3-8194-a676be299987'
        ]
        for entity_id, discussion_set_id in list(
                zip(entity_ids, discussion_set_ids)):
            DiscussionSetFactory(entity_id=entity_id, id=discussion_set_id)

    @staticmethod
    def create_discussion_objects(discussion_set_id, size):
        from ib_discussions.tests.factories.models import DiscussionFactory
        for i in range(size):
            DiscussionFactory(discussion_set_id=discussion_set_id)

    @pytest.fixture()
    def storage_implementation(self):
        from ib_discussions.storages.storage_implementation import \
            StorageImplementation
        storage = StorageImplementation()
        return storage

    @pytest.mark.django_db
    def test_get_discussion_set_id_if_exists_return_id(
            self, create_entity_objects, create_discussion_set_objects,
            storage_implementation):
        # Arrange
        entity_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        expected_discussion_set_id = '641bfcc5-e1ea-4231-b482-f7f34fb5c7c4'
        from ib_discussions.constants.enum import EntityType
        entity_type = EntityType.TASK.value

        # Act
        response = storage_implementation.get_discussion_set_id_if_exists(
            entity_id=entity_id, entity_type=entity_type
        )

        # Assert
        assert response == expected_discussion_set_id

    @pytest.mark.django_db
    def test_get_discussion_set_id_for_does_not_exist_raise_exception(
            self, create_entity_objects, create_discussion_set_objects,
            storage_implementation):
        # Arrange
        entity_id = '5c27801f-9084-7b93-a038-f261aedf8f29'
        from ib_discussions.constants.enum import EntityType
        entity_type = EntityType.TASK.value

        # Assert
        from ib_discussions.exceptions.custom_exceptions import \
            DiscussionSetNotFound
        with pytest.raises(DiscussionSetNotFound):
            storage_implementation.get_discussion_set_id_if_exists(
                entity_id=entity_id, entity_type=entity_type
            )

    @pytest.mark.django_db
    def test_create_discussion_set_return_id(self, create_entity_objects,
                                             create_discussion_set_objects,
                                             storage_implementation):
        # Arrange
        entity_id = '5c27801f-9084-7b93-a038-f261aedf8f29'
        from ib_discussions.constants.enum import EntityType
        entity_type = EntityType.TASK.value

        # Act
        response = storage_implementation.create_discussion_set_return_id(
            entity_id=entity_id, entity_type=entity_type
        )

        # Assert
        from ib_discussions.models import DiscussionSet
        discussion_set_object = DiscussionSet.objects.get(
            entity_id=entity_id, entity_type=entity_type
        )

        assert discussion_set_object.id == response

    @pytest.mark.django_db
    def test_create_discussion(self, create_entity_objects,
                               create_discussion_set_objects,
                               storage_implementation):
        # Arrange
        from ib_discussions.constants.enum import EntityType
        entity_id = '31be920b-7b4c-49e7-8adb-41a0c18da848'
        entity_type = EntityType.TASK.value
        user_id = "e1ed4b2d-f5d5-4b20-a5c4-8536130e704d"
        title = "interactor"
        description = "test for interactor"
        from ib_discussions.tests.factories.interactor_dtos import \
            DiscussionWithEntityDetailsDTOFactory
        discussion_with_entity_details_dto = DiscussionWithEntityDetailsDTOFactory(
            user_id=user_id,
            entity_id=entity_id,
            entity_type=entity_type,
            title=title,
            description=description
        )
        discussion_set_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"

        # Act
        storage_implementation.create_discussion(
            discussion_with_entity_details_dto\
                =discussion_with_entity_details_dto,
            discussion_set_id=discussion_set_id
        )

        # Assert
        from ib_discussions.models import Discussion
        discussion_obj = Discussion.objects.get(
            discussion_set_id=discussion_set_id)

        assert str(discussion_obj.user_id) == user_id
        assert discussion_obj.title == title
        assert discussion_obj.description == description
        assert str(discussion_obj.discussion_set_id) == discussion_set_id

    @pytest.mark.django_db
    def test_get_total_discussion_count(
            self, create_entity_objects, create_discussion_set_objects,
            storage_implementation):
        # Arrange
        from ib_discussions.interactors.dtos.dtos import FilterByDTO
        from ib_discussions.constants.enum import FilterByEnum
        filter_by_dto = FilterByDTO(
            filter_by=FilterByEnum.CLARIFIED.value,
            value=True
        )
        expected_discussion_count_after_filter = 3

        discussion_set_id1 = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        size_of_discussion_set_id1 = 3
        self.create_discussion_objects(
            discussion_set_id=discussion_set_id1,
            size=size_of_discussion_set_id1
        )
        size_of_discussion_set_id2 = 6
        discussion_set_id2 = '94557db1-c123-4e16-a69d-98a6a4850b84'
        self.create_discussion_objects(
            discussion_set_id=discussion_set_id2,
            size=size_of_discussion_set_id2
        )

        # Act
        response = storage_implementation.get_total_discussion_count(
            discussion_set_id=discussion_set_id2, filter_by_dto=filter_by_dto
        )

        # Assert
        assert response == expected_discussion_count_after_filter

    @pytest.mark.django_db
    def test_with_filter_by_CLARIFIED_return_response(
            self, create_entity_objects, create_discussion_set_objects,
            storage_implementation
    ):
        # Arrange
        discussion_set_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        from ib_discussions.tests.factories.storage_dtos import \
            DiscussionDTOFactory
        expected_complete_discussion_dtos = [
            DiscussionDTOFactory(
                user_id='9cc22e39-2390-4d96-b7ac-6bb27816461f',
                discussion_id='829db67d-0663-4e71-a103-826706ab5678',
                discussion_set_id='641bfcc5-e1ea-4231-b482-f7f34fb5c7c4',
                created_at=datetime.datetime(2020, 1, 20, 0, 0,
                                             tzinfo=datetime.timezone.utc),
                is_clarified=True
            ),
            DiscussionDTOFactory(
                user_id='9cc22e39-2390-4d96-b7ac-6bb27816461f',
                discussion_id='c0091084-1d34-4e8c-b813-464e14cb152c',
                discussion_set_id='641bfcc5-e1ea-4231-b482-f7f34fb5c7c4',
                created_at=datetime.datetime(2008, 1, 1, 0, 0,
                                             tzinfo=datetime.timezone.utc),
                is_clarified=True
            )
        ]

        size = 12
        from ib_discussions.tests.factories.models import DiscussionFactory
        for i in range(size):
            DiscussionFactory(discussion_set_id=discussion_set_id)

        from ib_discussions.interactors.dtos.dtos import FilterByDTO
        from ib_discussions.constants.enum import FilterByEnum
        filter_by_dto = FilterByDTO(
            filter_by=FilterByEnum.POSTED_BY_ME.value,
            value=True
        )

        from ib_discussions.interactors.dtos.dtos import \
            OffsetAndLimitDTO
        offset_and_limit_dto = OffsetAndLimitDTO(
            offset=1,
            limit=2
        )

        from ib_discussions.interactors.dtos.dtos import SortByDTO
        from ib_discussions.constants.enum import SortByEnum
        from ib_discussions.constants.enum import OrderByEnum
        sort_by_dto = SortByDTO(
            sort_by=SortByEnum.LATEST.value,
            order=OrderByEnum.ASC.value
        )
        # Act
        response = storage_implementation.get_discussion_dtos(
            discussion_set_id=discussion_set_id, filter_by_dto=filter_by_dto,
            sort_by_dto=sort_by_dto, offset_and_limit_dto=offset_and_limit_dto
        )

        # Assert
        self._compare_two_complete_discussion_dtos(
            response, expected_complete_discussion_dtos
        )

    @pytest.mark.django_db
    def test_with_filter_by_ALL_return_response(
            self, create_entity_objects, create_discussion_set_objects,
            storage_implementation
    ):
        # Arrange
        discussion_set_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        from ib_discussions.tests.factories.storage_dtos import \
            DiscussionDTOFactory
        expected_complete_discussion_dtos = [
            DiscussionDTOFactory(
                user_id='cd4eb7da-6a5f-4f82-82ba-12e40ab7bf5a',
                discussion_id='cc38d53c-679c-4924-b110-69b697a1b888',
                discussion_set_id='641bfcc5-e1ea-4231-b482-f7f34fb5c7c4',
                created_at=datetime.datetime(2020, 5, 1, 0, 0,
                                             tzinfo=datetime.timezone.utc),
                is_clarified=False
            ),
            DiscussionDTOFactory(
                user_id='e597ab2f-a10c-4164-930e-23af375741cb',
                discussion_id='85b72743-aeaf-4000-be5f-6764807b90a1',
                discussion_set_id='641bfcc5-e1ea-4231-b482-f7f34fb5c7c4',
                created_at=datetime.datetime(2020, 1, 20, 0, 0,
                                             tzinfo=datetime.timezone.utc),
                is_clarified=True
            )
        ]

        size = 4
        from ib_discussions.tests.factories.models import DiscussionFactory
        for i in range(size):
            DiscussionFactory(discussion_set_id=discussion_set_id)

        from ib_discussions.interactors.dtos.dtos import FilterByDTO
        from ib_discussions.constants.enum import FilterByEnum
        filter_by_dto = FilterByDTO(
            filter_by=FilterByEnum.ALL.value,
            value=FilterByEnum.ALL.value
        )

        from ib_discussions.interactors.dtos.dtos import \
            OffsetAndLimitDTO
        offset_and_limit_dto = OffsetAndLimitDTO(
            offset=0,
            limit=2
        )

        from ib_discussions.interactors.dtos.dtos import SortByDTO
        from ib_discussions.constants.enum import SortByEnum
        from ib_discussions.constants.enum import OrderByEnum
        sort_by_dto = SortByDTO(
            sort_by=SortByEnum.LATEST.value,
            order=OrderByEnum.ASC.value
        )
        # Act
        response = storage_implementation.get_discussion_dtos(
            discussion_set_id=discussion_set_id, filter_by_dto=filter_by_dto,
            sort_by_dto=sort_by_dto, offset_and_limit_dto=offset_and_limit_dto
        )

        # Assert
        self._compare_two_complete_discussion_dtos(
            response, expected_complete_discussion_dtos
        )

    @pytest.mark.django_db
    def test_with_filter_by_POSTED_BY_ME_return_response(
            self, create_entity_objects, create_discussion_set_objects,
            storage_implementation
    ):
        # Arrange
        discussion_set_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        from ib_discussions.tests.factories.storage_dtos import \
            DiscussionDTOFactory
        expected_complete_discussion_dtos = [
            DiscussionDTOFactory(
                user_id='cd4eb7da-6a5f-4f82-82ba-12e40ab7bf5a',
                discussion_id='b7c61479-d9c3-4fbe-b08b-c7069c72f5a7',
                discussion_set_id='641bfcc5-e1ea-4231-b482-f7f34fb5c7c4',
                created_at=datetime.datetime(2008, 1, 1, 0, 0,
                                             tzinfo=datetime.timezone.utc),
                is_clarified=True
            )
        ]

        size = 3
        from ib_discussions.tests.factories.models import DiscussionFactory
        for i in range(size):
            DiscussionFactory(discussion_set_id=discussion_set_id)

        from ib_discussions.interactors.dtos.dtos import FilterByDTO
        from ib_discussions.constants.enum import FilterByEnum
        filter_by_dto = FilterByDTO(
            filter_by=FilterByEnum.POSTED_BY_ME.value,
            value="cd4eb7da-6a5f-4f82-82ba-12e40ab7bf5a"
        )

        from ib_discussions.interactors.dtos.dtos import \
            OffsetAndLimitDTO
        offset_and_limit_dto = OffsetAndLimitDTO(
            offset=0,
            limit=2
        )

        from ib_discussions.interactors.dtos.dtos import SortByDTO
        from ib_discussions.constants.enum import SortByEnum
        from ib_discussions.constants.enum import OrderByEnum
        sort_by_dto = SortByDTO(
            sort_by=SortByEnum.TOP.value,
            order=OrderByEnum.ASC.value
        )
        # Act
        response = storage_implementation.get_discussion_dtos(
            discussion_set_id=discussion_set_id, filter_by_dto=filter_by_dto,
            sort_by_dto=sort_by_dto, offset_and_limit_dto=offset_and_limit_dto
        )

        # Assert
        self._compare_two_complete_discussion_dtos(
            response, expected_complete_discussion_dtos
        )

    @pytest.mark.django_db
    def test_validate_discussion_id(self, create_entity_objects,
                                    create_discussion_set_objects,
                                    storage_implementation):
        # Arrange
        discussion_id = "12357db1-c123-4e16-a69d-98a6a4850b84"
        from ib_discussions.tests.factories.models import DiscussionFactory
        DiscussionFactory.create_batch(3)

        # Assert
        from ib_discussions.exceptions.custom_exceptions import \
            DiscussionIdNotFound
        with pytest.raises(DiscussionIdNotFound):
            storage_implementation.validate_discussion_id(
                discussion_id=discussion_id
            )

    @pytest.mark.django_db
    def test_validate_is_user_can_mark_as_clarified(self, create_entity_objects,
                                                    create_discussion_set_objects,
                                                    storage_implementation):
        # Arrange
        discussion_id = "12357db1-c123-4e16-a69d-98a6a4850b84"
        user_id = "755bb3ac-09c6-46ac-82bb-f2e39cb8fb32"
        from ib_discussions.tests.factories.models import DiscussionFactory
        DiscussionFactory.create_batch(3)

        # Assert
        from ib_discussions.exceptions.custom_exceptions import \
            UserCannotMarkAsClarified
        with pytest.raises(UserCannotMarkAsClarified):
            storage_implementation.validate_is_user_can_mark_as_clarified(
                discussion_id=discussion_id, user_id=user_id
            )

    @pytest.mark.django_db
    def test_mark_discussion_clarified(self, create_entity_objects,
                                       create_discussion_set_objects,
                                       storage_implementation):
        # Arrange
        from ib_discussions.tests.factories.models import DiscussionFactory
        discussion_id = "12357db1-c123-4e16-a69d-98a6a4850b84"
        DiscussionFactory(id=discussion_id, is_clarified=False)
        clarified = True

        # Act
        storage_implementation.mark_discussion_clarified(
            discussion_id=discussion_id
        )

        # Assert
        from ib_discussions.models import Discussion
        discussion_object = Discussion.objects.get(id=discussion_id)

        assert discussion_object.is_clarified == clarified

    def _compare_two_complete_discussion_dtos(self,
                                              complete_discussion_dtos2,
                                              complete_discussion_dtos1):
        for complete_discussion_dtos1, complete_discussion_dtos2 in list(
                zip(complete_discussion_dtos1,
                    complete_discussion_dtos2)):
            self._compare_two_complete_discussion_dto(
                complete_discussion_dtos1, complete_discussion_dtos1
            )

    @staticmethod
    def _compare_two_complete_discussion_dto(complete_discussion_dto1,
                                             complete_discussion_dto2):
        assert complete_discussion_dto1.user_id == complete_discussion_dto2.user_id
        assert complete_discussion_dto1.discussion_set_id \
               == complete_discussion_dto2.discussion_set_id
        assert complete_discussion_dto1.title \
               == complete_discussion_dto2.title
        assert complete_discussion_dto1.description \
               == complete_discussion_dto2.description
        assert complete_discussion_dto1.is_clarified \
               == complete_discussion_dto2.is_clarified
        assert complete_discussion_dto1.created_at.replace(tzinfo=None) \
               == complete_discussion_dto2.created_at.replace(tzinfo=None)
