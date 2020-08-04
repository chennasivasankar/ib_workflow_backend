'''
TODO:

4. Success for Update

completed
1. Title is empty
3. Discussion Id not found
2. user cannot update the


'''
from unittest.mock import Mock

import pytest


class TestUpdateDiscussionInteractor:

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
            import UpdateDiscussionPresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(UpdateDiscussionPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_discussions.interactors.discussion_interactor import \
            DiscussionInteractor
        interactor = DiscussionInteractor(storage=storage_mock)
        return interactor

    @pytest.fixture()
    def get_discussion_id_with_title_and_description_dto(self):
        from ib_discussions.tests.factories.interactor_dtos import \
            DiscussionIdWithTitleAndDescriptionDTOFactory

        title = "title"
        description = "description"
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        return DiscussionIdWithTitleAndDescriptionDTOFactory(
            title=title,
            description=description,
            discussion_id=discussion_id
        )

    def test_title_is_empty_return_response(
            self, storage_mock, presenter_mock, interactor,
            get_discussion_id_with_title_and_description_dto

    ):
        # Arrange
        get_discussion_id_with_title_and_description_dto.title = ""
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"

        expected_presenter_response_for_empty_title_mock = Mock()

        presenter_mock.response_for_empty_title.return_value \
            = expected_presenter_response_for_empty_title_mock

        # Act
        response = interactor.update_discussion_wrapper(
            discussion_id_with_title_and_description_dto\
                =get_discussion_id_with_title_and_description_dto,
            user_id=user_id, presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_response_for_empty_title_mock
        presenter_mock.response_for_empty_title.assert_called_once()

    def test_discussion_id_not_found_return_response(
            self, storage_mock, presenter_mock, interactor,
            get_discussion_id_with_title_and_description_dto

    ):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"

        expected_presenter_response_for_discussion_id_not_found_mock = Mock()

        storage_mock.is_discussion_id_exists.return_value = False

        presenter_mock.response_for_discussion_id_not_found.return_value \
            = expected_presenter_response_for_discussion_id_not_found_mock

        # Act
        response = interactor.update_discussion_wrapper(
            discussion_id_with_title_and_description_dto \
                =get_discussion_id_with_title_and_description_dto,
            user_id=user_id, presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_response_for_discussion_id_not_found_mock
        presenter_mock.response_for_discussion_id_not_found.assert_called_once()
        storage_mock.is_discussion_id_exists.assert_called_once()

    def test_user_cannot_update_return_response(
            self, storage_mock, presenter_mock, interactor,
            get_discussion_id_with_title_and_description_dto

    ):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"

        expected_presenter_response_for_user_cannot_update_discussion_mock = Mock()

        storage_mock.is_discussion_id_exists.return_value = True
        storage_mock.is_user_can_update_discussion.return_value = False

        presenter_mock.response_for_user_cannot_update_discussion.return_value \
            = expected_presenter_response_for_user_cannot_update_discussion_mock

        # Act
        response = interactor.update_discussion_wrapper(
            discussion_id_with_title_and_description_dto \
                =get_discussion_id_with_title_and_description_dto,
            user_id=user_id, presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_response_for_user_cannot_update_discussion_mock
        presenter_mock.response_for_user_cannot_update_discussion.assert_called_once()
        storage_mock.is_user_can_update_discussion.assert_called_once()

    def test_with_valid_details_return_response(
            self, storage_mock, presenter_mock, interactor,
            get_discussion_id_with_title_and_description_dto
    ):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"

        expected_presenter_response_for_user_cannot_update_discussion_mock = Mock()

        storage_mock.is_discussion_id_exists.return_value = True
        storage_mock.is_user_can_update_discussion.return_value = True

        presenter_mock.response_for_user_cannot_update_discussion.return_value \
            = expected_presenter_response_for_user_cannot_update_discussion_mock

        # Act
        response = interactor.update_discussion_wrapper(
            discussion_id_with_title_and_description_dto \
                =get_discussion_id_with_title_and_description_dto,
            user_id=user_id, presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_response_for_user_cannot_update_discussion_mock
        presenter_mock.response_for_user_cannot_update_discussion.assert_called_once()