from unittest import mock

import pytest

from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory


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

    @pytest.mark.parametrize("name", [("user"), ("u")])
    def test_validate_name_minimum_name_length_exception(
            self, presenter_mock, interactor, name):
        # Arrange
        role_ids = ["1"]
        user_profile_dto = UserProfileDTOFactory(name=name)
        presenter_mock.raise_invalid_name_length_exception_for_update_user_profile \
            .return_value = mock.Mock()

        # Act
        interactor.update_user_profile_wrapper(
            user_profile_dto=user_profile_dto,
            role_ids=role_ids,
            presenter=presenter_mock)

        # Assert
        presenter_mock.raise_invalid_name_length_exception_for_update_user_profile \
            .assert_called_once()

    @pytest.mark.parametrize("name", [("user@"), ("_user"), ("user_name"),
                                      ("user0"), ("0user"), ("user0name")])
    def test_validate_name_when_contains_special_characters_and_numbers_throw_exception(
            self, presenter_mock, interactor, name):
        # Arrange
        role_ids = ["1"]
        user_profile_dto = UserProfileDTOFactory(name=name)
        presenter_mock \
            .raise_name_should_not_contain_special_chars_and_numbers_exception_for_update_user_profile \
            .return_value = mock.Mock()

        # Act
        interactor.update_user_profile_wrapper(
            user_profile_dto=user_profile_dto,
            role_ids=role_ids,
            presenter=presenter_mock)

        # Assert
        presenter_mock \
            .raise_name_should_not_contain_special_chars_and_numbers_exception_for_update_user_profile \
            .assert_called_once()

    def test_given_admin_and_duplicate_role_ids_returns_duplicate_role_ids_response(
            self, storage_mock, presenter_mock, interactor):
        # Arrange
        role_ids = ["1", "1"]
        user_id = "user_1"
        user_profile_dto = UserProfileDTOFactory(user_id=user_id,
                                                 name="username")
        storage_mock.is_user_admin.return_value = True
        presenter_mock.raise_duplicate_role_ids_exception.return_value = mock.Mock()

        # Act
        interactor.update_user_profile_wrapper(
            user_profile_dto=user_profile_dto,
            role_ids=role_ids,
            presenter=presenter_mock)

        # Assert
        storage_mock.is_user_admin.assert_called_once_with(user_id=user_id)
        presenter_mock.raise_duplicate_role_ids_exception.assert_called_once()

    def test_given_admin_and_invalid_role_ids_returns_invalid_role_ids_response(
            self, storage_mock, presenter_mock, interactor):
        # Arrange
        role_ids = ["1"]
        user_id = "user_1"
        user_profile_dto = UserProfileDTOFactory(user_id=user_id,
                                                 name="username")
        storage_mock.is_user_admin.return_value = True
        storage_mock.check_are_valid_role_ids.return_value = False
        presenter_mock.raise_invalid_role_ids_exception.return_value = mock.Mock()

        # Act
        interactor.update_user_profile_wrapper(
            user_profile_dto=user_profile_dto,
            role_ids=role_ids,
            presenter=presenter_mock)

        # Assert
        storage_mock.is_user_admin.assert_called_once_with(user_id=user_id)
        storage_mock.check_are_valid_role_ids.assert_called_once_with(
            role_ids=role_ids)
        presenter_mock.raise_invalid_role_ids_exception.assert_called_once()

    def test_given_invalid_email_returns_invalid_email_exception_response(
            self, mocker, presenter_mock, interactor):
        # Arrange
        role_ids = ["1"]
        user_profile_dto = UserProfileDTOFactory(name="username")
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import prepare_update_user_profile_adapter_mock
        adapter_mock = prepare_update_user_profile_adapter_mock(mocker=mocker)
        from ib_iam.exceptions.custom_exceptions import InvalidEmail
        adapter_mock.side_effect = InvalidEmail
        presenter_mock.raise_invalid_email_exception_for_update_user_profile \
            .return_value = mock.Mock()

        # Act
        interactor.update_user_profile_wrapper(
            user_profile_dto=user_profile_dto,
            role_ids=role_ids,
            presenter=presenter_mock)

        # Assert
        presenter_mock.raise_invalid_email_exception_for_update_user_profile \
            .assert_called_once()

    def test_given_email_already_in_use_returns_email_already_in_use_response(
            self, mocker, presenter_mock, interactor):
        # Arrange
        role_ids = ["1"]
        user_profile_dto = UserProfileDTOFactory(name="username")
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import prepare_update_user_profile_adapter_mock
        adapter_mock = prepare_update_user_profile_adapter_mock(mocker=mocker)
        from ib_iam.exceptions.custom_exceptions import \
            UserAccountAlreadyExistWithThisEmail
        adapter_mock.side_effect = UserAccountAlreadyExistWithThisEmail
        presenter_mock.raise_email_already_in_use_exception_for_update_user_profile \
            .return_value = mock.Mock()

        # Act
        interactor.update_user_profile_wrapper(
            user_profile_dto=user_profile_dto,
            role_ids=role_ids,
            presenter=presenter_mock)

        # Assert
        presenter_mock.raise_email_already_in_use_exception_for_update_user_profile \
            .assert_called_once()

    def test_given_valid_details_returns_success_response_for_user(
            self, mocker, storage_mock, presenter_mock, interactor):
        # Arrange
        name = "username"
        user_id = "user_id1"
        role_ids = ["1"]
        user_profile_dto = UserProfileDTOFactory(user_id=user_id, name=name)
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import prepare_update_user_profile_adapter_mock
        adapter_mock = prepare_update_user_profile_adapter_mock(mocker=mocker)
        presenter_mock.get_success_response_for_update_user_profile \
            .return_value = mock.Mock()

        # Act
        interactor.update_user_profile_wrapper(
            user_profile_dto=user_profile_dto,
            role_ids=role_ids,
            presenter=presenter_mock)

        # Assert
        adapter_mock.assert_called_once()
        storage_mock.is_user_admin.assert_called_once_with(user_id=user_id)
        storage_mock.update_user_name_and_cover_page_url \
            .assert_called_once_with(user_profile_dto=user_profile_dto)
        presenter_mock.get_success_response_for_update_user_profile \
            .assert_called_once()

    def test_given_valid_details_returns_success_response_for_admin(
            self, mocker, storage_mock, presenter_mock, interactor):
        # Arrange
        name = "username"
        user_id = "user_id1"
        role_ids = ["1"]
        ids_of_role_objects = ["role_1"]
        user_profile_dto = UserProfileDTOFactory(user_id=user_id, name=name)
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import prepare_update_user_profile_adapter_mock
        adapter_mock = prepare_update_user_profile_adapter_mock(mocker=mocker)
        storage_mock.is_user_admin.return_value = True
        storage_mock.get_role_objs_ids.return_value = ids_of_role_objects
        presenter_mock.get_success_response_for_update_user_profile \
            .return_value = mock.Mock()

        # Act
        interactor.update_user_profile_wrapper(
            user_profile_dto=user_profile_dto,
            role_ids=role_ids,
            presenter=presenter_mock)

        # Assert
        adapter_mock.assert_called_once()
        storage_mock.is_user_admin.assert_called_once_with(user_id=user_id)
        storage_mock.check_are_valid_role_ids.assert_called_once_with(role_ids)
        storage_mock.remove_roles_for_user.assert_called_once_with(user_id)
        storage_mock.get_role_objs_ids.assert_called_once_with(role_ids)
        storage_mock.add_roles_to_the_user.assert_called_once_with(
            user_id=user_id, role_ids=ids_of_role_objects)
        storage_mock.update_user_name_and_cover_page_url \
            .assert_called_once_with(user_profile_dto=user_profile_dto)
        presenter_mock.get_success_response_for_update_user_profile \
            .assert_called_once()
