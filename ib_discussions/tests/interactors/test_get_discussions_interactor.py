from unittest.mock import Mock

import pytest


class TestGetDiscussionsInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from ib_discussions.interactors.storage_interfaces.storage_interface \
            import StorageInterface
        from unittest.mock import create_autospec
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from ib_discussions.interactors.presenter_interfaces. \
            presenter_interface import GetDiscussionsPresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(GetDiscussionsPresenterInterface)
        return presenter

    @pytest.fixture()
    def entity_id_and_entity_type_dto(self):
        from ib_discussions.constants.enum import EntityType
        from ib_discussions.interactors.dtos.dtos import \
            EntityIdAndEntityTypeDTO
        entity_id_and_entity_type_dto = EntityIdAndEntityTypeDTO(
            entity_id="6a76277b-fb73-4920-a79d-4c65814f9de5",
            entity_type=EntityType.TASK.value
        )
        return entity_id_and_entity_type_dto

    @pytest.fixture()
    def offset_and_limit_dto(self):
        from ib_discussions.interactors.dtos.dtos import \
            OffsetAndLimitDTO
        offset_and_limit_dto = OffsetAndLimitDTO(
            offset=0,
            limit=3
        )
        return offset_and_limit_dto

    @pytest.fixture()
    def initialise_discussions_interactor(self, storage_mock):
        from ib_discussions.interactors.get_discussions_interactor import \
            GetDiscussionInteractor
        interactor = GetDiscussionInteractor(storage=storage_mock)
        return interactor

    @pytest.fixture()
    def filter_by_dto(self):
        from ib_discussions.interactors.dtos.dtos import FilterByDTO
        from ib_discussions.constants.enum import FilterByEnum
        filter_by_dto = FilterByDTO(
            filter_by=FilterByEnum.CLARIFIED.value,
            value=True
        )
        return filter_by_dto

    @pytest.fixture()
    def sort_by_dto(self):
        from ib_discussions.interactors.dtos.dtos import SortByDTO
        from ib_discussions.constants.enum import SortByEnum
        from ib_discussions.constants.enum import OrderByEnum
        sort_by_dto = SortByDTO(
            sort_by=SortByEnum.LATEST.value,
            order=OrderByEnum.ASC.value
        )
        return sort_by_dto

    @staticmethod
    def _get_discussion_dtos(discussion_set_id):
        total_count = 3
        from ib_discussions.tests.factories.storage_dtos import \
            DiscussionDTOFactory
        complete_discussion_dtos = [
            DiscussionDTOFactory(discussion_set_id=discussion_set_id)
            for _ in range(1, total_count)
        ]
        return complete_discussion_dtos

    @staticmethod
    def _get_user_profile_dtos():
        from ib_discussions.tests.factories.adapter_dtos import \
            UserProfileDTOFactory
        user_profile_factory = UserProfileDTOFactory.create_batch(size=3)
        return user_profile_factory

    def test_validate_offset_value_raise_exception(
            self, presenter_mock, entity_id_and_entity_type_dto,
            offset_and_limit_dto, initialise_discussions_interactor,
            filter_by_dto, sort_by_dto
    ):
        # Arrange
        offset_and_limit_dto.offset = -1
        user_id = "c8939223-79a0-4566-ba13-b4fbf7db6f93"

        expected_presenter_raise_exception_for_invalid_offset_mock = Mock()

        presenter_mock.response_for_invalid_offset.return_value \
            = expected_presenter_raise_exception_for_invalid_offset_mock

        interactor = initialise_discussions_interactor

        # Act
        response = interactor.get_discussions_wrapper(
            entity_id_and_entity_type_dto=entity_id_and_entity_type_dto,
            offset_and_limit_dto=offset_and_limit_dto, presenter=presenter_mock,
            sort_by_dto=sort_by_dto, filter_by_dto=filter_by_dto,
            user_id=user_id
        )

        # Assert
        assert response \
               == expected_presenter_raise_exception_for_invalid_offset_mock

    def test_validate_limit_value_raise_exception(
            self, presenter_mock, entity_id_and_entity_type_dto,
            offset_and_limit_dto, initialise_discussions_interactor,
            filter_by_dto, sort_by_dto
    ):
        # Arrange
        offset_and_limit_dto.limit = -1
        user_id = "c8939223-79a0-4566-ba13-b4fbf7db6f93"
        expected_presenter_raise_exception_for_invalid_limit_mock = Mock()

        presenter_mock.response_for_invalid_limit.return_value \
            = expected_presenter_raise_exception_for_invalid_limit_mock

        interactor = initialise_discussions_interactor

        # Act
        response = interactor.get_discussions_wrapper(
            entity_id_and_entity_type_dto=entity_id_and_entity_type_dto,
            offset_and_limit_dto=offset_and_limit_dto, presenter=presenter_mock,
            sort_by_dto=sort_by_dto, filter_by_dto=filter_by_dto,
            user_id=user_id
        )

        # Assert
        assert response == \
               expected_presenter_raise_exception_for_invalid_limit_mock

    def test_get_discussions_details_return_response(
            self, presenter_mock, entity_id_and_entity_type_dto, storage_mock,
            offset_and_limit_dto, initialise_discussions_interactor,
            mocker, filter_by_dto, sort_by_dto
    ):
        discussion_set_id = "e892e8db-6064-4d8f-9ce2-7c9032dbd8a5"
        discussions_count = 3
        user_id = "c8939223-79a0-4566-ba13-b4fbf7db6f93"
        expected_presenter_response_for_discussions = Mock()

        discussion_dtos = self._get_discussion_dtos(
            discussion_set_id
        )

        storage_mock.get_discussion_set_id_if_exists.return_value \
            = discussion_set_id
        storage_mock.get_discussion_dtos.return_value \
            = discussion_dtos
        storage_mock.get_total_discussion_count.return_value \
            = discussions_count

        presenter_mock.prepare_response_for_discussions_details_dto. \
            return_value = expected_presenter_response_for_discussions

        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_get_user_profile_dtos_mock
        get_user_profile_dtos_mock = prepare_get_user_profile_dtos_mock(mocker)
        user_profile_dtos = self._get_user_profile_dtos()
        get_user_profile_dtos_mock.return_value \
            = user_profile_dtos

        from ib_discussions.interactors.presenter_interfaces.dtos import \
            DiscussionsWithUsersAndDiscussionCountDTO
        discussions_details_dto = DiscussionsWithUsersAndDiscussionCountDTO(
            discussion_dtos=discussion_dtos,
            user_profile_dtos=user_profile_dtos,
            total_count=discussions_count
        )

        interactor = initialise_discussions_interactor

        # Act
        response = interactor.get_discussions_wrapper(
            entity_id_and_entity_type_dto=entity_id_and_entity_type_dto,
            offset_and_limit_dto=offset_and_limit_dto, presenter=presenter_mock,
            sort_by_dto=sort_by_dto, filter_by_dto=filter_by_dto,
            user_id=user_id
        )

        # Assert
        assert response == expected_presenter_response_for_discussions

        storage_mock.get_discussion_set_id_if_exists.assert_called_once()
        storage_mock.get_discussion_dtos.assert_called_once_with(
            discussion_set_id=discussion_set_id,
            offset_and_limit_dto=offset_and_limit_dto,
            sort_by_dto=sort_by_dto,
            filter_by_dto=filter_by_dto
        )
        storage_mock.get_total_discussion_count.assert_called_once_with(
            discussion_set_id=discussion_set_id, filter_by_dto=filter_by_dto
        )
        presenter_mock.prepare_response_for_discussions_details_dto. \
            assert_called_once()
