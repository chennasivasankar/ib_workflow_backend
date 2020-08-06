from unittest.mock import Mock

import pytest


class TestGetRepliesForCommentInteractor:

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
            GetRepliesForCommentPresenterInterface
        presenter = create_autospec(GetRepliesForCommentPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_discussions.interactors.get_replies_for_comment_interactor import \
            GetRepliesForCommentInteractor
        interactor = GetRepliesForCommentInteractor(storage=storage_mock)
        return interactor

    def test_comment_id_not_found_return_response(
            self, storage_mock, presenter_mock, interactor
    ):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"

        expected_presenter_response_for_comment_id_not_found_mock = Mock()

        storage_mock.is_comment_id_exists.return_value = False

        presenter_mock.response_for_comment_id_not_found.return_value \
            = expected_presenter_response_for_comment_id_not_found_mock

        # Act
        response = interactor.get_replies_for_comment_wrapper(
            comment_id=comment_id, user_id=user_id, presenter=presenter_mock
        )

        # Assert
        assert response == \
               expected_presenter_response_for_comment_id_not_found_mock
        presenter_mock.response_for_comment_id_not_found.assert_called_once()
        storage_mock.is_comment_id_exists.assert_called_once()

    def test_with_valid_details_return_response(
            self, storage_mock, presenter_mock, interactor, mocker
    ):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        replies_ids = [
            "11be920b-7b4c-49e7-8adb-41a0c18da848",
            "21be920b-7b4c-49e7-8adb-41a0c18da848",
            "71be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        user_ids = [
            "31be920b-7b4c-49e7-8adb-41a0c18da848",
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "77be920b-7b4c-49e7-8adb-41a0c18da848"
        ]

        from ib_discussions.tests.factories.storage_dtos import \
            CommentDTOFactory
        reply_dtos = [
            CommentDTOFactory(comment_id=reply_id, user_id=user_id)
            for reply_id, user_id in zip(replies_ids, user_ids)
        ]

        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_get_user_profile_dtos_mock
        get_user_profile_dtos_mock = prepare_get_user_profile_dtos_mock(mocker)
        user_profile_dtos = self._get_user_profile_dtos()
        get_user_profile_dtos_mock.return_value \
            = user_profile_dtos

        expected_presenter_prepare_response_for_replies_with_users_dtos_mock = \
            Mock()

        storage_mock.is_comment_id_exists.return_value = True
        storage_mock.get_comment_dtos.return_value = reply_dtos

        presenter_mock.prepare_response_for_replies_with_users_dtos. \
            return_value = expected_presenter_prepare_response_for_replies_with_users_dtos_mock

        # Act
        response = interactor.get_replies_for_comment_wrapper(
            comment_id=comment_id, user_id=user_id, presenter=presenter_mock
        )

        # Assert
        assert response \
               == expected_presenter_prepare_response_for_replies_with_users_dtos_mock
        storage_mock.is_comment_id_exists.assert_called_once_with(
            comment_id=comment_id
        )
        storage_mock.get_comment_dtos.assert_called_once_with(
            comment_id=comment_id
        )
        presenter_mock.prepare_response_for_replies_with_users_dtos. \
            assert_called_once()

    @staticmethod
    def _get_user_profile_dtos():
        from ib_discussions.tests.factories.adapter_dtos import \
            UserProfileDTOFactory
        user_ids = [
            "31be920b-7b4c-49e7-8adb-41a0c18da848",
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "77be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        user_profile_dtos = [
            UserProfileDTOFactory(user_id=user_id)
            for user_id in user_ids
        ]
        return user_profile_dtos
