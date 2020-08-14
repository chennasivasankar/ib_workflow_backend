from unittest.mock import Mock

import pytest


class TestUpdateCommentInteractor:

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
            UpdateCommentPresenterInterface
        presenter = create_autospec(UpdateCommentPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_discussions.interactors.update_comment_interactor import \
            UpdateCommentInteractor
        interactor = UpdateCommentInteractor(comment_storage=storage_mock)
        return interactor

    @pytest.fixture()
    def prepare_users_setup(self, mocker):
        user_ids = [
            "31be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        mention_user_ids = [
            "10be920b-7b4c-49e7-8adb-41a0c18da848",
            "20be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_get_user_profile_dtos_mock
        get_user_profile_dtos_mock = prepare_get_user_profile_dtos_mock(mocker)
        from ib_discussions.tests.factories.adapter_dtos import \
            UserProfileDTOFactory
        user_profile_dtos = [
            UserProfileDTOFactory(user_id=user_id)
            for user_id in (user_ids + mention_user_ids)
        ]
        get_user_profile_dtos_mock.return_value = user_profile_dtos
        return mention_user_ids

    @pytest.fixture()
    def prepare_multimedia_setup(self, mocker):
        comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_discussions.constants.enum import MultimediaFormat
        multimedia = [
            {
                "format_type": MultimediaFormat.IMAGE.value,
                "url": "https://picsum.photos/200",
                "thumbnail_url": "https://picsum.photos/200"
            },
            {
                "format_type": MultimediaFormat.VIDEO.value,
                "url": "https://picsum.photos/200",
                "thumbnail_url": "https://picsum.photos/200"
            }
        ]
        multimedia_ids = [
            "97be920b-7b4c-49e7-8adb-41a0c18da848",
            "92be920b-7b4c-49e7-8adb-41a0c18da848",
        ]
        from ib_discussions.tests.factories.storage_dtos import \
            CommentIdWithMultiMediaDTOFactory
        multimedia_dtos = [
            CommentIdWithMultiMediaDTOFactory(
                comment_id=comment_id,
                multimedia_id=multimedia_ids[0],
                format_type=multimedia[0]["format_type"],
                url=multimedia[0]["url"]
            ),
            CommentIdWithMultiMediaDTOFactory(
                comment_id=comment_id,
                multimedia_id=multimedia_ids[1],
                format_type=multimedia[1]["format_type"],
                url=multimedia[1]["url"]
            )
        ]
        return multimedia_dtos

    def test_with_comment_id_not_found_return_response(
            self, storage_mock, presenter_mock, interactor, prepare_users_setup,
            prepare_multimedia_setup
    ):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_id = "97be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_content = "content"
        mention_user_ids = prepare_users_setup
        multimedia_dtos = prepare_multimedia_setup

        from ib_discussions.tests.factories.interactor_dtos import \
            UpdateCompleteCommentDTOFactory
        update_complete_comment_dto = UpdateCompleteCommentDTOFactory(
            comment_id=comment_id,
            user_id=user_id,
            comment_content=comment_content,
            mention_user_ids=mention_user_ids,
            multimedia_dtos=multimedia_dtos
        )

        expected_presenter_prepare_response_for_comment_id_not_found_mock = \
            Mock()
        presenter_mock.prepare_response_for_comment_id_not_found. \
            return_value = expected_presenter_prepare_response_for_comment_id_not_found_mock

        storage_mock.is_comment_id_exists.return_value = False

        # Act
        response = interactor.update_comment_wrapper(
            presenter=presenter_mock,
            update_complete_comment_dto=update_complete_comment_dto
        )

        # Assert
        assert response == \
               expected_presenter_prepare_response_for_comment_id_not_found_mock
        presenter_mock.prepare_response_for_comment_id_not_found. \
            assert_called_once()
        storage_mock.is_comment_id_exists.assert_called_once_with(
            comment_id=comment_id)

    def test_with_user_cannot_edit_comment_return_response(
            self, storage_mock, presenter_mock, interactor, prepare_users_setup,
            prepare_multimedia_setup
    ):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_id = "97be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_content = "content"
        mention_user_ids = prepare_users_setup
        multimedia_dtos = prepare_multimedia_setup

        from ib_discussions.tests.factories.interactor_dtos import \
            UpdateCompleteCommentDTOFactory
        update_complete_comment_dto = UpdateCompleteCommentDTOFactory(
            comment_id=comment_id,
            user_id=user_id,
            comment_content=comment_content,
            mention_user_ids=mention_user_ids,
            multimedia_dtos=multimedia_dtos
        )

        expected_presenter_response_for_user_cannot_edit_comment_mock = \
            Mock()
        presenter_mock.response_for_user_cannot_edit_comment. \
            return_value = expected_presenter_response_for_user_cannot_edit_comment_mock

        storage_mock.is_comment_id_exists.return_value = True
        storage_mock.get_comment_creator_id.return_value = \
            "21be920b-7b4c-49e7-8adb-41a0c18da848"

        # Act
        response = interactor.update_comment_wrapper(
            presenter=presenter_mock,
            update_complete_comment_dto=update_complete_comment_dto
        )

        # Assert
        assert response == \
               expected_presenter_response_for_user_cannot_edit_comment_mock
        storage_mock.is_comment_id_exists.assert_called_once_with(
            comment_id=comment_id)
        storage_mock.get_comment_creator_id.assert_called_once_with(
            comment_id=comment_id)
        presenter_mock.response_for_user_cannot_edit_comment.assert_called_once()

    def test_invalid_user_ids_return_response(
            self, storage_mock, presenter_mock, interactor, mocker,
            prepare_users_setup, prepare_multimedia_setup
    ):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_id = "97be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_content = "content"
        mention_user_ids = prepare_users_setup
        invalid_user_ids = [
            "20be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_validate_user_ids_mock
        validate_user_ids_mock = prepare_validate_user_ids_mock(mocker=mocker)
        from ib_discussions.adapters.auth_service import InvalidUserIds
        validate_user_ids_mock.side_effect = InvalidUserIds(
            user_ids=invalid_user_ids)

        multimedia_dtos = prepare_multimedia_setup

        from ib_discussions.tests.factories.interactor_dtos import \
            UpdateCompleteCommentDTOFactory
        update_complete_comment_dto = UpdateCompleteCommentDTOFactory(
            comment_id=comment_id,
            user_id=user_id,
            comment_content=comment_content,
            mention_user_ids=mention_user_ids,
            multimedia_dtos=multimedia_dtos
        )

        expected_presenter_response_for_invalid_user_ids_mock = Mock()

        storage_mock.get_comment_creator_id.return_value = user_id
        storage_mock.is_comment_id_exists.return_value = True

        presenter_mock.response_for_invalid_user_ids.return_value \
            = expected_presenter_response_for_invalid_user_ids_mock

        # Act
        response = interactor.update_comment_wrapper(
            presenter=presenter_mock,
            update_complete_comment_dto=update_complete_comment_dto
        )

        # Assert
        assert response == expected_presenter_response_for_invalid_user_ids_mock
        presenter_mock.response_for_invalid_user_ids.assert_called_once()

    def test_with_valid_details_return_response(
            self, storage_mock, presenter_mock, interactor, mocker,
            prepare_users_setup, prepare_multimedia_setup
    ):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_id = "97be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_ids = [comment_id]
        comment_content = "content"
        mention_user_ids = prepare_users_setup
        multimedia_dtos = prepare_multimedia_setup

        from ib_discussions.tests.factories.interactor_dtos import \
            UpdateCompleteCommentDTOFactory
        update_complete_comment_dto = UpdateCompleteCommentDTOFactory(
            comment_id=comment_id,
            user_id=user_id,
            comment_content=comment_content,
            mention_user_ids=mention_user_ids,
            multimedia_dtos=multimedia_dtos
        )

        from ib_discussions.tests.factories.storage_dtos import \
            CommentDTOFactory
        comment_dto = CommentDTOFactory(
            comment_id=comment_id,
            user_id=user_id,
            comment_content=comment_content
        )

        from ib_discussions.tests.factories.storage_dtos import \
            CommentIdWithRepliesCountDTOFactory
        comment_id_with_replies_count_dtos = [
            CommentIdWithRepliesCountDTOFactory(
                comment_id=comment_id,
                replies_count=0
            )
        ]

        expected_presenter_prepare_response_for_comment_mock = Mock()

        storage_mock.is_comment_id_exists.return_value = True
        storage_mock.get_comment_creator_id.return_value = user_id
        storage_mock.get_comment_details_dto.return_value = comment_dto
        storage_mock.get_replies_count_for_comments.return_value \
            = comment_id_with_replies_count_dtos

        presenter_mock.prepare_response_for_comment.return_value = \
            expected_presenter_prepare_response_for_comment_mock

        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_validate_user_ids_mock
        prepare_validate_user_ids_mock(mocker=mocker)

        # Act
        response = interactor.update_comment_wrapper(
            presenter=presenter_mock,
            update_complete_comment_dto=update_complete_comment_dto
        )

        # Assert
        assert response == expected_presenter_prepare_response_for_comment_mock
        storage_mock.get_comment_details_dto.assert_called_once_with(
            comment_id=comment_id
        )
        storage_mock.is_comment_id_exists.assert_called_once_with(
            comment_id=comment_id
        )
        storage_mock.get_replies_count_for_comments.assert_called_once_with(
            comment_ids=comment_ids
        )
        storage_mock.get_mention_user_ids.assert_called_once_with(
            comment_ids=comment_ids
        )
        storage_mock.get_comment_id_with_mention_user_id_dtos.assert_called_once_with(
            comment_ids=comment_ids
        )
        storage_mock.get_multimedia_dtos.assert_called_once_with(
            comment_ids=comment_ids
        )