from unittest.mock import Mock

import pytest


class TestDeleteCommentInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from unittest.mock import create_autospec
        from ib_discussions.interactors.storage_interfaces.comment_storage_interface import \
            CommentStorageInterface
        storage = create_autospec(CommentStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from unittest.mock import create_autospec
        from ib_discussions.interactors.presenter_interfaces.presenter_interface import \
            DeleteCommentPresenterInterface
        presenter = create_autospec(DeleteCommentPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_discussions.interactors.delete_comment_interactor import \
            DeleteCommentInteractor
        interactor = DeleteCommentInteractor(comment_storage=storage_mock)
        return interactor

    def test_with_comment_id_not_found_return_response(
            self, storage_mock, presenter_mock, interactor):
        # Arrange
        comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"

        expected_presenter_prepare_response_for_comment_id_not_found_mock = \
            Mock()

        presenter_mock.prepare_response_for_comment_id_not_found. \
            return_value = expected_presenter_prepare_response_for_comment_id_not_found_mock

        storage_mock.is_comment_id_exists.return_value = False

        # Act
        response = interactor.delete_comment_wrapper(
            comment_id=comment_id, user_id=user_id, presenter=presenter_mock)

        # Assert
        assert response == \
               expected_presenter_prepare_response_for_comment_id_not_found_mock
        presenter_mock.prepare_response_for_comment_id_not_found. \
            assert_called_once()
        storage_mock.is_comment_id_exists.assert_called_once_with(
            comment_id=comment_id)

    def test_with_user_cannot_edit_comment_return_response(
            self, storage_mock, presenter_mock, interactor):
        comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"

        expected_presenter_response_for_user_cannot_edit_comment_mock = \
            Mock()
        presenter_mock.response_for_user_cannot_edit_comment. \
            return_value = expected_presenter_response_for_user_cannot_edit_comment_mock

        storage_mock.is_comment_id_exists.return_value = True
        storage_mock.get_comment_creator_id.return_value = \
            "21be920b-7b4c-49e7-8adb-41a0c18da848"

        # Act
        response = interactor.delete_comment_wrapper(
            comment_id=comment_id, user_id=user_id, presenter=presenter_mock)

        # Assert
        assert response == \
               expected_presenter_response_for_user_cannot_edit_comment_mock
        storage_mock.is_comment_id_exists.assert_called_once_with(
            comment_id=comment_id)
        storage_mock.get_comment_creator_id.assert_called_once_with(
            comment_id=comment_id)
        presenter_mock.response_for_user_cannot_edit_comment.assert_called_once()

    def test_with_valid_details_return_respones(
            self, storage_mock, presenter_mock, interactor):
        # Act
        comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"

        storage_mock.is_comment_id_exists.return_value = True
        storage_mock.get_comment_creator_id.return_value = user_id

        expected_presenter_prepare_response_for_delete_comment_mock = \
            Mock()
        presenter_mock.prepare_response_for_delete_comment. \
            return_value = expected_presenter_prepare_response_for_delete_comment_mock

        # Act
        response = interactor.delete_comment_wrapper(
            comment_id=comment_id, user_id=user_id, presenter=presenter_mock)

        # Assert
        assert response == \
               expected_presenter_prepare_response_for_delete_comment_mock

        storage_mock.delete_comment.assert_called_once_with(
            comment_id=comment_id)
        presenter_mock.prepare_response_for_delete_comment. \
            assert_called_once_with()
