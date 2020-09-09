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
        from ib_discussions.interactors.create_comment_interactor import \
            CreateCommentInteractor
        interactor = CreateCommentInteractor(storage=storage_mock)
        return interactor

    def test_discussion_id_not_found_return_response(
            self, storage_mock, presenter_mock, interactor, mocker
    ):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_content = "content"
        mention_user_ids = [
            "10be920b-7b4c-49e7-8adb-41a0c18da848",
            "20be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_validate_user_ids_mock
        prepare_validate_user_ids_mock(mocker=mocker)

        from ib_discussions.tests.factories.interactor_dtos import \
            MultimediaDTOFactory
        MultimediaDTOFactory.format_type.reset()
        multimedia_dtos = MultimediaDTOFactory.create_batch(2)

        from ib_discussions.tests.factories.interactor_dtos import \
            CreateCompleteCommentDTOFactory
        create_complete_comment_dto = CreateCompleteCommentDTOFactory(
            discussion_id=discussion_id,
            user_id=user_id,
            comment_content=comment_content,
            mention_user_ids=mention_user_ids,
            multimedia_dtos=multimedia_dtos
        )

        expected_presenter_response_for_discussion_id_not_found_mock = Mock()

        storage_mock.is_discussion_id_exists.return_value = False

        presenter_mock.response_for_discussion_id_not_found.return_value \
            = expected_presenter_response_for_discussion_id_not_found_mock

        # Act
        response = interactor.create_comment_for_discussion_wrapper(
            create_complete_comment_dto=create_complete_comment_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_response_for_discussion_id_not_found_mock
        presenter_mock.response_for_discussion_id_not_found.assert_called_once()
        storage_mock.is_discussion_id_exists.assert_called_once_with(
            discussion_id=discussion_id
        )

    def test_empty_comment_content_and_multimedia_return_response(
            self, storage_mock, presenter_mock, interactor, mocker
    ):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_content = ""
        mention_user_ids = [
            "10be920b-7b4c-49e7-8adb-41a0c18da848",
            "20be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_validate_user_ids_mock
        prepare_validate_user_ids_mock(mocker=mocker)

        multimedia_dtos = []

        from ib_discussions.tests.factories.interactor_dtos import \
            CreateCompleteCommentDTOFactory
        create_complete_comment_dto = CreateCompleteCommentDTOFactory(
            discussion_id=discussion_id,
            user_id=user_id,
            comment_content=comment_content,
            mention_user_ids=mention_user_ids,
            multimedia_dtos=multimedia_dtos
        )

        expected_presenter_response_for_comment_or_multimedia_should_be_provided_mock = Mock()

        presenter_mock.response_for_comment_or_multimedia_should_be_provided.return_value \
            = expected_presenter_response_for_comment_or_multimedia_should_be_provided_mock

        # Act
        response = interactor.create_comment_for_discussion_wrapper(
            create_complete_comment_dto=create_complete_comment_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_response_for_comment_or_multimedia_should_be_provided_mock
        presenter_mock.response_for_comment_or_multimedia_should_be_provided.assert_called_once()

    def test_invalid_user_ids_return_response(
            self, storage_mock, presenter_mock, interactor, mocker
    ):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_content = "content"
        mention_user_ids = [
            "10be920b-7b4c-49e7-8adb-41a0c18da848",
            "20be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        invalid_user_ids = [
            "10be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_validate_user_ids_mock
        validate_user_ids_mock = prepare_validate_user_ids_mock(mocker=mocker)
        from ib_discussions.adapters.auth_service import InvalidUserIds
        validate_user_ids_mock.side_effect = InvalidUserIds(
            user_ids=invalid_user_ids)

        from ib_discussions.tests.factories.interactor_dtos import \
            MultimediaDTOFactory
        MultimediaDTOFactory.format_type.reset()
        multimedia_dtos = MultimediaDTOFactory.create_batch(2)

        from ib_discussions.tests.factories.interactor_dtos import \
            CreateCompleteCommentDTOFactory
        create_complete_comment_dto = CreateCompleteCommentDTOFactory(
            discussion_id=discussion_id,
            user_id=user_id,
            comment_content=comment_content,
            mention_user_ids=mention_user_ids,
            multimedia_dtos=multimedia_dtos
        )

        expected_presenter_response_for_invalid_user_ids_mock = Mock()

        storage_mock.is_discussion_id_exists.return_value = False

        presenter_mock.response_for_invalid_user_ids.return_value \
            = expected_presenter_response_for_invalid_user_ids_mock

        # Act
        response = interactor.create_comment_for_discussion_wrapper(
            create_complete_comment_dto=create_complete_comment_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_response_for_invalid_user_ids_mock
        presenter_mock.response_for_invalid_user_ids.assert_called_once()

    def test_with_valid_details_return_response(
            self, storage_mock, presenter_mock, interactor, mocker
    ):
        # Arrange
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        discussion_id = "71be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        comment_ids = [comment_id]
        comment_content = "content"
        mention_user_ids = [
            "10be920b-7b4c-49e7-8adb-41a0c18da848",
            "20be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_validate_user_ids_mock
        prepare_validate_user_ids_mock(mocker=mocker)
        from ib_discussions.tests.factories.interactor_dtos import \
            MultimediaDTOFactory
        MultimediaDTOFactory.format_type.reset()
        multimedia_dtos = MultimediaDTOFactory.create_batch(2)

        from ib_discussions.tests.factories.interactor_dtos import \
            CreateCompleteCommentDTOFactory
        create_complete_comment_dto = CreateCompleteCommentDTOFactory(
            discussion_id=discussion_id,
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

        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_get_user_profile_dtos_mock
        get_user_profile_dtos_mock = prepare_get_user_profile_dtos_mock(mocker)
        user_profile_dtos = self._get_user_profile_dtos()
        get_user_profile_dtos_mock.return_value \
            = user_profile_dtos

        expected_presenter_prepare_response_for_create_comment_mock = Mock()

        storage_mock.is_discussion_id_exists.return_value = True
        storage_mock.create_comment_for_discussion.return_value = comment_id
        storage_mock.get_comment_details_dto.return_value = comment_dto
        storage_mock.get_replies_count_for_comments.return_value \
            = comment_id_with_replies_count_dtos

        presenter_mock.prepare_response_for_comment.return_value \
            = expected_presenter_prepare_response_for_create_comment_mock

        # Act
        response = interactor.create_comment_for_discussion_wrapper(
            create_complete_comment_dto=create_complete_comment_dto,
            presenter=presenter_mock
        )

        # Assert
        assert response \
               == expected_presenter_prepare_response_for_create_comment_mock
        presenter_mock.prepare_response_for_comment.assert_called_once()
        storage_mock.create_comment_for_discussion.assert_called_once_with(
            user_id=user_id, discussion_id=discussion_id,
            comment_content=comment_content
        )
        storage_mock.get_comment_details_dto.assert_called_once_with(
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
