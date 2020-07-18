'''
request - entity-id, entity_type, offset, limit

# TODO

5. get discussion_set_id for entity id and entity type
6. get discussion_dto for discussion_set_id
7. get total discussions count
8. get user details

# Completed
1. validate offset
2. validate limit
3. validate the entity id
4. validate the entity type for entity id

'''
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
        from ib_discussions.interactors.presenter_interfaces.presenter_interface \
            import PresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(PresenterInterface)
        return presenter

    @pytest.fixture()
    def entity_id_and_entity_type_dto(self):
        from ib_discussions.interactors.discussion_interactor import \
            EntityIdAndEntityTypeDTO
        from ib_discussions.constants.enum import EntityType
        entity_id_and_entity_type_dto = EntityIdAndEntityTypeDTO(
            entity_id="6a76277b-fb73-4920-a79d-4c65814f9de5",
            entity_type=EntityType.TASK.value
        )
        return entity_id_and_entity_type_dto

    @pytest.fixture()
    def offset_and_limit_dto(self):
        from ib_discussions.interactors.discussion_interactor import \
            OffsetAndLimitDTO
        offset_and_limit_dto = OffsetAndLimitDTO(
            offset=0,
            limit=3
        )
        return offset_and_limit_dto

    @pytest.fixture()
    def initialise_discussions_interactor(self, storage_mock):
        from ib_discussions.interactors.discussion_interactor import \
            DiscussionInteractor
        interactor = DiscussionInteractor(storage=storage_mock)
        return interactor

    def test_validate_offset_value_raise_exception(
            self, presenter_mock, entity_id_and_entity_type_dto,
            offset_and_limit_dto, initialise_discussions_interactor
    ):
        # Arrange
        offset_and_limit_dto.offset = -1
        expected_presenter_raise_exception_for_invalid_offset_mock = Mock()

        presenter_mock.raise_exception_for_invalid_offset.return_value \
            = expected_presenter_raise_exception_for_invalid_offset_mock

        interactor = initialise_discussions_interactor

        # Act
        response = interactor.get_discussions_wrapper(
            entity_id_and_entity_type_dto=entity_id_and_entity_type_dto,
            offset_and_limit_dto=offset_and_limit_dto, presenter=presenter_mock
        )

        # Assert
        assert response \
               == expected_presenter_raise_exception_for_invalid_offset_mock

    def test_validate_limit_value_raise_exception(
            self, presenter_mock, entity_id_and_entity_type_dto,
            offset_and_limit_dto, initialise_discussions_interactor
    ):
        # Arrange
        offset_and_limit_dto.limit = -1
        expected_presenter_raise_exception_for_invalid_limit_mock = Mock()

        presenter_mock.raise_exception_for_invalid_limit.return_value \
            = expected_presenter_raise_exception_for_invalid_limit_mock

        interactor = initialise_discussions_interactor

        # Act
        response = interactor.get_discussions_wrapper(
            entity_id_and_entity_type_dto=entity_id_and_entity_type_dto,
            offset_and_limit_dto=offset_and_limit_dto, presenter=presenter_mock
        )

        # Assert
        assert response == \
               expected_presenter_raise_exception_for_invalid_limit_mock

    def test_validate_entity_id_raise_exception(
            self, presenter_mock, entity_id_and_entity_type_dto, storage_mock,
            offset_and_limit_dto, initialise_discussions_interactor
    ):
        # Arrange
        from unittest.mock import Mock
        expected_presenter_raise_exception_for_entity_id_not_found_mock = Mock()

        from ib_discussions.interactors.discussion_interactor import \
            EntityIdNotFound
        storage_mock.validate_entity_id.side_effect \
            = EntityIdNotFound

        presenter_mock.raise_exception_for_entity_id_not_found.return_value \
            = expected_presenter_raise_exception_for_entity_id_not_found_mock

        interactor = initialise_discussions_interactor

        # Act
        response = interactor.get_discussions_wrapper(
            entity_id_and_entity_type_dto=entity_id_and_entity_type_dto,
            offset_and_limit_dto=offset_and_limit_dto, presenter=presenter_mock
        )

        # Assert
        assert response \
               == expected_presenter_raise_exception_for_entity_id_not_found_mock
        presenter_mock.raise_exception_for_entity_id_not_found. \
            assert_called_once()

    def test_validate_entity_type_for_entity_id_raise_exception(
            self, presenter_mock, entity_id_and_entity_type_dto, storage_mock,
            offset_and_limit_dto, initialise_discussions_interactor
    ):
        # Arrange
        from unittest.mock import Mock
        expected_presenter_invalid_entity_type_mock = Mock()

        from ib_discussions.interactors.discussion_interactor import \
            InvalidEntityTypeForEntityId
        storage_mock.validate_entity_type_for_entity_id.side_effect \
            = InvalidEntityTypeForEntityId

        presenter_mock.raise_exception_for_invalid_entity_type_for_entity_id \
            .return_value = expected_presenter_invalid_entity_type_mock

        interactor = initialise_discussions_interactor

        # Act
        response = interactor.get_discussions_wrapper(
            entity_id_and_entity_type_dto=entity_id_and_entity_type_dto,
            offset_and_limit_dto=offset_and_limit_dto, presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_invalid_entity_type_mock
        presenter_mock.raise_exception_for_invalid_entity_type_for_entity_id. \
            assert_called_once()

    def test_get_discussions_details(
            self, presenter_mock, entity_id_and_entity_type_dto, storage_mock,
            offset_and_limit_dto, initialise_discussions_interactor
    ):

