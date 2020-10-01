from unittest.mock import Mock

import pytest


class TestGetDiscussionsInteractor:

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
            presenter_interface import GetDiscussionsPresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(GetDiscussionsPresenterInterface)
        return presenter

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_discussions.interactors.get_discussions_interactor import \
            GetDiscussionInteractor
        interactor = GetDiscussionInteractor(storage=storage_mock)
        return interactor

    @pytest.fixture()
    def get_discussion_dtos(self):
        discussion_set_id = "e892e8db-6064-4d8f-9ce2-7c9032dbd8a5"
        from ib_discussions.tests.factories.storage_dtos import \
            DiscussionDTOFactory
        DiscussionDTOFactory.is_clarified.reset()
        complete_discussion_dtos = DiscussionDTOFactory.create_batch(
            size=3, discussion_set_id=discussion_set_id
        )
        return complete_discussion_dtos

    @pytest.fixture()
    def get_discussions_input_dto(self):
        from ib_discussions.tests.factories.interactor_dtos import \
            GetDiscussionsInputDTOFactory
        get_discussions_input_dto = GetDiscussionsInputDTOFactory()
        return get_discussions_input_dto

    @pytest.fixture()
    def get_user_profile_dtos(self):
        from ib_discussions.tests.factories.adapter_dtos import \
            UserProfileDTOFactory
        user_profile_dtos = UserProfileDTOFactory.create_batch(size=3)
        return user_profile_dtos

    def test_validate_offset_value_raise_exception(
            self, presenter_mock, interactor, get_discussions_input_dto
    ):
        # Arrange
        get_discussions_input_dto.offset_and_limit_dto.offset = -1

        expected_presenter_raise_exception_for_invalid_offset_mock = Mock()

        presenter_mock.response_for_invalid_offset.return_value \
            = expected_presenter_raise_exception_for_invalid_offset_mock

        # Act
        response = interactor.get_discussions_wrapper(
            presenter=presenter_mock,
            get_discussions_input_dto=get_discussions_input_dto
        )

        # Assert
        assert response \
               == expected_presenter_raise_exception_for_invalid_offset_mock

    def test_validate_limit_value_raise_exception(
            self, presenter_mock, interactor,
            get_discussions_input_dto
    ):
        # Arrange
        get_discussions_input_dto.offset_and_limit_dto.limit = -1
        expected_presenter_raise_exception_for_invalid_limit_mock = Mock()

        presenter_mock.response_for_invalid_limit.return_value \
            = expected_presenter_raise_exception_for_invalid_limit_mock

        # Act
        response = interactor.get_discussions_wrapper(
            presenter=presenter_mock,
            get_discussions_input_dto=get_discussions_input_dto
        )

        # Assert
        assert response == \
               expected_presenter_raise_exception_for_invalid_limit_mock

    def test_get_discussions_details_return_response(
            self, presenter_mock, storage_mock, interactor,
            mocker, get_discussions_input_dto, get_discussion_dtos,
            get_user_profile_dtos
    ):
        discussion_set_id = "e892e8db-6064-4d8f-9ce2-7c9032dbd8a5"
        discussions_count = 3
        expected_presenter_response_for_discussions = Mock()

        storage_mock.get_discussion_set_id_if_exists.return_value \
            = discussion_set_id
        storage_mock.get_discussion_dtos.return_value \
            = get_discussion_dtos
        storage_mock.get_total_discussion_count.return_value \
            = discussions_count

        presenter_mock.prepare_response_for_discussions_details_dto. \
            return_value = expected_presenter_response_for_discussions

        from ib_discussions.tests.common_fixtures.adapters import \
            prepare_get_user_profile_dtos_mock
        get_user_profile_dtos_mock = prepare_get_user_profile_dtos_mock(mocker)
        get_user_profile_dtos_mock.return_value = get_user_profile_dtos

        # Act
        response = interactor.get_discussions_wrapper(
            presenter=presenter_mock,
            get_discussions_input_dto=get_discussions_input_dto
        )

        # Assert
        assert response == expected_presenter_response_for_discussions

        storage_mock.get_discussion_set_id_if_exists.assert_called_once()
        storage_mock.get_discussion_dtos.assert_called_once_with(
            discussion_set_id=discussion_set_id,
            get_discussions_input_dto=get_discussions_input_dto
        )
        storage_mock.get_total_discussion_count.assert_called_once_with(
            discussion_set_id=discussion_set_id,
            filter_by_dto=get_discussions_input_dto.filter_by_dto
        )
        presenter_mock.prepare_response_for_discussions_details_dto. \
            assert_called_once()
