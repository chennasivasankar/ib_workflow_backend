from unittest import mock

import pytest

from ib_iam.tests.factories.storage_dtos import \
    UserIdNameEmailAndProfilePicUrlDTOFactory


class TestUpdateUserProfileInteractor:

    @pytest.fixture
    def storage_mock(self):
        from ib_iam.interactors.storage_interfaces.user_storage_interface \
            import UserStorageInterface
        storage = mock.create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from unittest import mock
        from ib_iam.interactors.presenter_interfaces \
            .update_user_profile_presenter_interface import \
            UpdateUserProfilePresenterInterface
        storage = mock.create_autospec(UpdateUserProfilePresenterInterface)
        return storage

    @pytest.fixture
    def interactor(self, storage_mock):
        from ib_iam.interactors.update_user_profile_interactor import \
            UpdateUserProfileInteractor
        interactor = UpdateUserProfileInteractor(user_storage=storage_mock)
        return interactor

    @pytest.mark.parametrize("name", [(""), ("  ")])
    def test_validate_name_when_empty_throw_exception(
            self, presenter_mock, interactor, name):
        # Arrange
        user_id_name_email_and_profile_pic_url_dto = \
            UserIdNameEmailAndProfilePicUrlDTOFactory(name=name)
        presenter_mock.get_response_for_empty_name_exception \
            .return_value = mock.Mock()

        # Act
        interactor.update_user_profile_wrapper(
            user_id_name_email_and_profile_pic_url_dto=
            user_id_name_email_and_profile_pic_url_dto,
            presenter=presenter_mock)

        # Assert
        presenter_mock.get_response_for_empty_name_exception \
            .assert_called_once()

    @pytest.mark.parametrize("name", [("user"), ("u")])
    def test_validate_name_minimum_name_length_exception(
            self, presenter_mock, interactor, name):
        # Arrange
        user_id_name_email_and_profile_pic_url_dto = \
            UserIdNameEmailAndProfilePicUrlDTOFactory(name=name)
        presenter_mock.get_response_for_minimum_name_length \
            .return_value = mock.Mock()

        # Act
        interactor.update_user_profile_wrapper(
            user_id_name_email_and_profile_pic_url_dto=
            user_id_name_email_and_profile_pic_url_dto,
            presenter=presenter_mock)

        # Assert
        presenter_mock.get_response_for_minimum_name_length \
            .assert_called_once()

    @pytest.mark.parametrize("name", [("user@"), ("_user"), ("user_name"),
                                      ("user0"), ("0user"), ("user0name")])
    def test_validate_name_when_contains_special_characters_and_numbers_throw_exception(
            self, presenter_mock, interactor, name):
        # Arrange
        user_id_name_email_and_profile_pic_url_dto = \
            UserIdNameEmailAndProfilePicUrlDTOFactory(name=name)
        presenter_mock \
            .get_response_for_name_contains_special_chars_and_numbers_exception \
            .return_value = mock.Mock()

        # Act
        interactor.update_user_profile_wrapper(
            user_id_name_email_and_profile_pic_url_dto=
            user_id_name_email_and_profile_pic_url_dto,
            presenter=presenter_mock)

        # Assert
        presenter_mock \
            .get_response_for_name_contains_special_chars_and_numbers_exception \
            .assert_called_once()

    def test_given_valid_details_returns_success_response(
            self, mocker, storage_mock, presenter_mock, interactor):
        # Arrange
        name = "username"
        user_id = "user_id1"
        user_id_name_email_and_profile_pic_url_dto = \
            UserIdNameEmailAndProfilePicUrlDTOFactory(user_id=user_id,
                                                      name=name)
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import update_user_profile_adapter_mock
        adapter_mock = update_user_profile_adapter_mock(mocker=mocker)
        presenter_mock.get_success_response_for_update_user_profile \
            .return_value = mock.Mock()

        # Act
        interactor.update_user_profile_wrapper(
            user_id_name_email_and_profile_pic_url_dto=
            user_id_name_email_and_profile_pic_url_dto,
            presenter=presenter_mock)

        # Assert
        adapter_mock.assert_called_once()
        storage_mock.update_user_name.assert_called_once_with(user_id=user_id,
                                                              name=name)
        presenter_mock.get_success_response_for_update_user_profile \
            .assert_called_once()
