from unittest.mock import Mock

import pytest


class TestMarkDiscussionClarifiedInteractor:

    @pytest.fixture()
    def storage_mock(self):
        from ib_discussions.interactors.storage_interfaces.storage_interface \
            import StorageInterface
        from unittest.mock import create_autospec
        storage = create_autospec(StorageInterface)
        return storage

    @pytest.fixture()
    def presenter_mock(self):
        from ib_discussions.interactors.presenter_interfaces. \
            presenter_interface import MarkDiscussionClarifiedPresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(MarkDiscussionClarifiedPresenterInterface)
        return presenter

    def test_with_discussion_id_which_does_not_exist_raise_exception(
            self, storage_mock, presenter_mock
    ):
        # Arrange
        discussion_id = "6a76277b-fb73-4920-a79d-4c65814f9de5"
        user_id = "3216277b-fb73-4920-a79d-4c65814f9de5"
        expected_presenter_raise_exception_for_discussion_id_not_found_mock \
            = Mock()

        from ib_discussions.exceptions.custom_exceptions import \
            DiscussionIdNotFound
        storage_mock.validate_discussion_id.side_effect \
            = DiscussionIdNotFound

        presenter_mock.response_for_discussion_id_not_found.return_value \
            = expected_presenter_raise_exception_for_discussion_id_not_found_mock

        from ib_discussions.interactors.mark_discussion_clarified_interactor import \
            MarkDiscussionClarifiedInteractor
        interactor = MarkDiscussionClarifiedInteractor(storage=storage_mock)

        # Act
        response = interactor.mark_discussion_clarified_wrapper(
            user_id=user_id, discussion_id=discussion_id,
            presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_raise_exception_for_discussion_id_not_found_mock

        storage_mock.validate_discussion_id.assert_called_once_with(
            discussion_id=discussion_id
        )
        presenter_mock.response_for_discussion_id_not_found. \
            assert_called_once()

    def test_with_user_id_cannot_mark_as_clarified_raise_exception(
            self, storage_mock, presenter_mock
    ):
        # Arrange
        discussion_id = "6a76277b-fb73-4920-a79d-4c65814f9de5"
        user_id = "3216277b-fb73-4920-a79d-4c65814f9de5"
        expected_presenter_raise_exception_for_user_cannot_mark_as_clarified_mock \
            = Mock()

        from ib_discussions.exceptions.custom_exceptions import \
            UserCannotMarkAsClarified
        storage_mock.validate_is_user_can_mark_as_clarified.side_effect \
            = UserCannotMarkAsClarified

        presenter_mock.response_for_user_cannot_mark_as_clarified.return_value \
            = expected_presenter_raise_exception_for_user_cannot_mark_as_clarified_mock

        from ib_discussions.interactors.mark_discussion_clarified_interactor import \
            MarkDiscussionClarifiedInteractor
        interactor = MarkDiscussionClarifiedInteractor(storage=storage_mock)

        # Act
        response = interactor.mark_discussion_clarified_wrapper(
            user_id=user_id, discussion_id=discussion_id,
            presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_raise_exception_for_user_cannot_mark_as_clarified_mock

        storage_mock.validate_is_user_can_mark_as_clarified. \
            assert_called_once_with(user_id=user_id,
                                    discussion_id=discussion_id)
        presenter_mock.response_for_user_cannot_mark_as_clarified. \
            assert_called_once_with()

    def test_with_valid_details_return_response(
            self, storage_mock, presenter_mock
    ):
        # Arrange
        discussion_id = "6a76277b-fb73-4920-a79d-4c65814f9de5"
        user_id = "3216277b-fb73-4920-a79d-4c65814f9de5"
        expected_presenter_raise_success_response_for_mark_discussion_as_clarified_mock \
            = Mock()

        presenter_mock.prepare_success_response_for_mark_discussion_as_clarified.return_value \
            = expected_presenter_raise_success_response_for_mark_discussion_as_clarified_mock

        from ib_discussions.interactors.mark_discussion_clarified_interactor import \
            MarkDiscussionClarifiedInteractor
        interactor = MarkDiscussionClarifiedInteractor(storage=storage_mock)

        # Act
        response = interactor.mark_discussion_clarified_wrapper(
            user_id=user_id, discussion_id=discussion_id,
            presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_raise_success_response_for_mark_discussion_as_clarified_mock

        storage_mock.mark_discussion_clarified.assert_called_once_with(
            discussion_id=discussion_id
        )
        presenter_mock.prepare_success_response_for_mark_discussion_as_clarified. \
            assert_called_once_with()
