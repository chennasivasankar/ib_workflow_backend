from unittest.mock import Mock

import pytest


class TestDeleteDiscussionInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from ib_discussions.interactors.storage_interfaces.storage_interface \
            import StorageInterface
        from unittest.mock import create_autospec
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from unittest.mock import create_autospec
        from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
            DeleteDiscussionPresenterInterface
        presenter = create_autospec(DeleteDiscussionPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_discussions.interactors.discussion_interactor import \
            DiscussionInteractor
        interactor = DiscussionInteractor(storage=storage_mock)
        return interactor

    def test_discussion_id_not_found_return_response(
            self, storage_mock, presenter_mock, interactor,

    ):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"

        expected_presenter_response_for_discussion_id_not_found_mock = Mock()

        storage_mock.is_discussion_id_exists.return_value = False

        presenter_mock.response_for_discussion_id_not_found.return_value \
            = expected_presenter_response_for_discussion_id_not_found_mock

        # Act
        response = interactor.delete_discussion_wrapper(
            discussion_id=discussion_id, user_id=user_id,
            presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_response_for_discussion_id_not_found_mock
        presenter_mock.response_for_discussion_id_not_found.assert_called_once()
        storage_mock.is_discussion_id_exists.assert_called_once_with(
            discussion_id=discussion_id
        )

    def test_user_cannot_update_return_response(
            self, storage_mock, presenter_mock, interactor,
    ):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"

        expected_presenter_response_for_user_cannot_delete_discussion_mock = Mock()

        storage_mock.is_discussion_id_exists.return_value = True
        storage_mock.is_user_can_edit_discussion.return_value = False

        presenter_mock.response_for_user_cannot_delete_discussion.return_value \
            = expected_presenter_response_for_user_cannot_delete_discussion_mock

        # Act
        response = interactor.delete_discussion_wrapper(
            discussion_id=discussion_id, user_id=user_id,
            presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_response_for_user_cannot_delete_discussion_mock
        presenter_mock.response_for_user_cannot_delete_discussion.assert_called_once()
        storage_mock.is_user_can_edit_discussion.assert_called_once_with(
            user_id=user_id, discussion_id=discussion_id
        )

    def test_with_valid_details_return_response(
            self, presenter_mock, storage_mock, interactor):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"

        expected_presenter_prepare_success_response_for_delete_discussion_mock = Mock()

        storage_mock.is_discussion_id_exists.return_value = True
        storage_mock.is_user_can_edit_discussion.return_value = True

        presenter_mock.prepare_success_response_for_delete_discussion.return_value \
            = expected_presenter_prepare_success_response_for_delete_discussion_mock

        # Act
        response = interactor.delete_discussion_wrapper(
            discussion_id=discussion_id, user_id=user_id,
            presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_prepare_success_response_for_delete_discussion_mock
        presenter_mock.prepare_success_response_for_delete_discussion.assert_called_once()
        storage_mock.delete_discussion.assert_called_once_with(
            discussion_id=discussion_id)
