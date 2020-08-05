from unittest.mock import Mock

import pytest


class TestCreateCommentInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from unittest.mock import create_autospec
        from ib_discussions.interactors.storage_interfaces.comment_storage_interface import \
            CommentStorageInterface
        storage = create_autospec(CommentStorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from ib_discussions.interactors.presenter_interfaces.presenter_interface \
            import CreateCommentPresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(CreateCommentPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_discussions.interactors.comment_interactor import \
            CommentInteractor
        interactor = CommentInteractor(storage=storage_mock)
        return interactor

    def test_discussion_id_not_found_return_response(
            self, storage_mock, presenter_mock, interactor
    ):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_content = "content"

        expected_presenter_response_for_discussion_id_not_found_mock = Mock()

        storage_mock.is_discussion_id_exists.return_value = False

        presenter_mock.response_for_discussion_id_not_found.return_value \
            = expected_presenter_response_for_discussion_id_not_found_mock

        # Act
        response = interactor.create_comment_for_discussion_wrapper(
            discussion_id=discussion_id, comment_content=comment_content,
            user_id=user_id, presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_response_for_discussion_id_not_found_mock
        presenter_mock.response_for_discussion_id_not_found.assert_called_once()
        storage_mock.is_discussion_id_exists.assert_called_once()
