'''
request - user_id(str), entity_id(str), entity_type(str), title(str), description

todo

2. create the discussion if discussion set found
3. create the discussion and discussion set

in prgress
1. validate the entity id and entity type not found

completed
'''
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
            import PresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(PresenterInterface)
        return presenter

    @pytest.fixture()
    def discussion_dto(self):
        from ib_discussions.constants.enum import EntityType
        from ib_discussions.interactors.discussion_interactor import \
            DiscussionDTO
        discussion_dto = DiscussionDTO(
            user_id="1",
            entity_id="6a76277b-fb73-4920-a79d-4c65814f9de5",
            entity_type=EntityType.TASK.value,
            title="Interactor",
            description="test for interactor"
        )
        return discussion_dto

    def test_validate_for_discussions_not_found_for_entity_id_and_entity_type(
            self, storage_mock, presenter_mock, discussion_dto
    ):
        # Arrange
        from unittest.mock import Mock
        expected_presenter_discussions_not_found_mock = Mock()

        from ib_discussions.interactors.discussion_interactor import \
            NotFoundDiscussionSetForEntityIdAndEntityType
        storage_mock.validate_entity_id_and_entity_type.side_effect \
            = NotFoundDiscussionSetForEntityIdAndEntityType

        presenter_mock.raise_exception_for_discussions_not_found.return_value \
            = expected_presenter_discussions_not_found_mock

        from ib_discussions.interactors.discussion_interactor import \
            DiscussionInteractor
        interactor = DiscussionInteractor(storage=storage_mock)

        # Act
        response = interactor.create_discussion_wrapper(
            discussion_dto=discussion_dto, presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_discussions_not_found_mock
        presenter_mock.raise_exception_for_discussions_not_found. \
            assert_called_once()

    def test_create_discussion_if_discussion_set_found(self, presenter_mock,
                                                       storage_mock
                                                       ):
        # Arrange
        from unittest.mock import Mock
        expected_presenter_discussions_not_found_mock = Mock()

        from ib_discussions.interactors.discussion_interactor import \
            NotFoundDiscussionSetForEntityIdAndEntityType
        storage_mock.validate_entity_id_and_entity_type.side_effect \
            = NotFoundDiscussionSetForEntityIdAndEntityType

        presenter_mock.raise_exception_for_discussions_not_found.return_value \
            = expected_presenter_discussions_not_found_mock

        from ib_discussions.interactors.discussion_interactor import \
            DiscussionInteractor
        interactor = DiscussionInteractor(storage=storage_mock)

        # Act
        response = interactor.create_discussion_wrapper(
            discussion_dto=discussion_dto, presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_discussions_not_found_mock
        presenter_mock.raise_exception_for_discussions_not_found. \
            assert_called_once()

