import pytest


class TestCreateDiscussionInteractor:

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
            import CreateDiscussionPresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(CreateDiscussionPresenterInterface)
        return presenter

    @pytest.fixture()
    def discussion_dto(self):
        from ib_discussions.interactors.DTOs.common_dtos import DiscussionDTO
        from ib_discussions.constants.enum import EntityType
        discussion_dto = DiscussionDTO(
            user_id="1",
            entity_id="6a76277b-fb73-4920-a79d-4c65814f9de5",
            entity_type=EntityType.TASK.value,
            title="Interactor",
            description="test for interactor"
        )
        return discussion_dto

    # def test_validate_entity_id_raise_exception(
    #         self, storage_mock, presenter_mock, discussion_dto
    # ):
    #     # Arrange
    #     from unittest.mock import Mock
    #     expected_presenter_entity_id_not_found_mock = Mock()
    #
    #     from ib_discussions.exceptions.custom_exceptions import EntityIdNotFound
    #     storage_mock.validate_entity_id.side_effect \
    #         = EntityIdNotFound
    #
    #     presenter_mock.raise_exception_for_entity_id_not_found.return_value \
    #         = expected_presenter_entity_id_not_found_mock
    #
    #     from ib_discussions.interactors.discussion_interactor import \
    #         DiscussionInteractor
    #     interactor = DiscussionInteractor(storage=storage_mock)
    #
    #     # Act
    #     response = interactor.create_discussion_wrapper(
    #         discussion_dto=discussion_dto, presenter=presenter_mock
    #     )
    #
    #     # Assert
    #     assert response == expected_presenter_entity_id_not_found_mock
    #     presenter_mock.raise_exception_for_entity_id_not_found. \
    #         assert_called_once()
    #
    # def test_validate_entity_type_for_entity_id_raise_exception(
    #         self, storage_mock, presenter_mock, discussion_dto
    # ):
    #     # Arrange
    #     from unittest.mock import Mock
    #     expected_presenter_invalid_entity_type_mock = Mock()
    #
    #     from ib_discussions.exceptions.custom_exceptions import \
    #         InvalidEntityTypeForEntityId
    #     storage_mock.validate_entity_type_for_entity_id.side_effect \
    #         = InvalidEntityTypeForEntityId
    #
    #     presenter_mock.raise_exception_for_invalid_entity_type_for_entity_id \
    #         .return_value = expected_presenter_invalid_entity_type_mock
    #
    #     from ib_discussions.interactors.discussion_interactor import \
    #         DiscussionInteractor
    #     interactor = DiscussionInteractor(storage=storage_mock)
    #
    #     # Act
    #     response = interactor.create_discussion_wrapper(
    #         discussion_dto=discussion_dto, presenter=presenter_mock
    #     )
    #
    #     # Assert
    #     assert response == expected_presenter_invalid_entity_type_mock
    #     presenter_mock.raise_exception_for_invalid_entity_type_for_entity_id. \
    #         assert_called_once()

    def test_create_discussion_set_when_does_not_exists(
            self, storage_mock, presenter_mock, discussion_dto
    ):
        # Arrange
        from ib_discussions.interactors.discussion_interactor import \
            DiscussionSetNotFound
        storage_mock.get_discussion_set_id_if_exists.side_effect \
            = DiscussionSetNotFound

        from ib_discussions.interactors.discussion_interactor import \
            DiscussionInteractor
        interactor = DiscussionInteractor(storage=storage_mock)

        # Act
        response = interactor.create_discussion_wrapper(
            discussion_dto=discussion_dto, presenter=presenter_mock
        )

        # Assert
        storage_mock.get_discussion_set_id_if_exists.assert_called_once_with(
            entity_id=discussion_dto.entity_id,
            entity_type=discussion_dto.entity_type
        )
        storage_mock.create_discussion_set_return_id.assert_called_once_with(
            entity_id=discussion_dto.entity_id,
            entity_type=discussion_dto.entity_type
        )

    def test_create_discussion_when_discussion_set_exists(
            self, storage_mock, presenter_mock, discussion_dto
    ):
        # Arrange
        from unittest.mock import Mock
        expected_presenter_success_response_mock = Mock()
        presenter_mock.prepare_success_response_for_create_discussion.\
            return_value = expected_presenter_success_response_mock

        from ib_discussions.interactors.discussion_interactor import \
            DiscussionInteractor
        interactor = DiscussionInteractor(storage=storage_mock)

        # Act
        response = interactor.create_discussion_wrapper(
            discussion_dto=discussion_dto, presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_success_response_mock
        storage_mock.get_discussion_set_id_if_exists.assert_called_once_with(
            entity_id=discussion_dto.entity_id,
            entity_type=discussion_dto.entity_type
        )
        storage_mock.create_discussion_set_return_id.assert_not_called()
        storage_mock.create_discussion.assert_called_once()
