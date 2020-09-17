from unittest import mock

import pytest

from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
from ib_iam.tests.factories.interactor_dtos import \
    CompleteUserProfileDTOFactory


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
            .auth_presenter_interface import \
            UpdateUserProfilePresenterInterface
        storage = mock.create_autospec(UpdateUserProfilePresenterInterface)
        return storage

    @pytest.fixture
    def interactor(self, storage_mock):
        from ib_iam.interactors.update_user_profile_interactor import \
            UpdateUserProfileInteractor
        interactor = UpdateUserProfileInteractor(user_storage=storage_mock)
        return interactor

    @pytest.mark.parametrize("name", ["user", "u"])
    def test_with_name_and_name_length_is_less_than_five_then_raise_exception(
            self, presenter_mock, interactor, name
    ):
        # Arrange
        role_ids = []
        user_profile_dto = CompleteUserProfileDTOFactory(name=name)
        presenter_mock.response_for_invalid_name_length_exception \
            .return_value = mock.Mock()

        # Act
        interactor.update_user_profile_wrapper(
            user_profile_dto=user_profile_dto, role_ids=role_ids,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.response_for_invalid_name_length_exception \
            .assert_called_once()

    @pytest.mark.parametrize(
        "name", ["user@", "_user", "user_name", "user0", "0user", "user0name"]
    )
    def test_validate_name_when_contains_special_characters_and_numbers_throw_exception(
            self, presenter_mock, interactor, name
    ):
        # Arrange
        role_ids = ["1"]
        user_profile_dto = CompleteUserProfileDTOFactory(name=name)
        presenter_mock \
            .response_for_name_contains_special_character_exception \
            .return_value = mock.Mock()

        # Act
        interactor.update_user_profile_wrapper(
            user_profile_dto=user_profile_dto, role_ids=role_ids,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.response_for_name_contains_special_character_exception \
            .assert_called_once()

    def test_given_admin_and_duplicate_role_ids_then_raise_duplicate_role_ids_exception(
            self, storage_mock, presenter_mock, interactor
    ):
        # Arrange
        role_ids = ["1", "1"]
        user_id = "user_1"
        user_profile_dto = CompleteUserProfileDTOFactory(
            user_id=user_id, name="username"
        )
        storage_mock.is_user_admin.return_value = True
        presenter_mock.response_for_duplicate_role_ids_exception.return_value = \
            mock.Mock()

        # Act
        interactor.update_user_profile_wrapper(
            user_profile_dto=user_profile_dto, role_ids=role_ids,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.is_user_admin.assert_called_once_with(user_id=user_id)
        presenter_mock.response_for_duplicate_role_ids_exception.assert_called_once()

    def test_given_admin_and_invalid_role_ids_returns_invalid_role_ids_response(
            self, storage_mock, presenter_mock, interactor):
        # Arrange
        role_ids = ["1"]
        user_id = "user_1"
        user_profile_dto = CompleteUserProfileDTOFactory(
            user_id=user_id, name="username"
        )
        storage_mock.is_user_admin.return_value = True
        storage_mock.check_are_valid_role_ids.return_value = False
        presenter_mock.response_for_invalid_role_ids_exception.return_value = \
            mock.Mock()

        # Act
        interactor.update_user_profile_wrapper(
            user_profile_dto=user_profile_dto, role_ids=role_ids,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.is_user_admin.assert_called_once_with(user_id=user_id)
        storage_mock.check_are_valid_role_ids.assert_called_once_with(
            role_ids=role_ids
        )
        presenter_mock.response_for_invalid_role_ids_exception.assert_called_once()

    def test_given_invalid_email_returns_invalid_email_exception_response(
            self, mocker, presenter_mock, interactor
    ):
        # Arrange
        role_ids = ["1"]
        user_profile_dto = CompleteUserProfileDTOFactory(name="username")
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import update_user_profile_adapter_mock
        adapter_mock = update_user_profile_adapter_mock(mocker=mocker)
        from ib_iam.exceptions.custom_exceptions import InvalidEmail
        adapter_mock.side_effect = InvalidEmail
        presenter_mock.response_for_invalid_email_exception \
            .return_value = mock.Mock()

        # Act
        interactor.update_user_profile_wrapper(
            user_profile_dto=user_profile_dto, role_ids=role_ids,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.response_for_invalid_email_exception \
            .assert_called_once()

    def test_given_email_already_in_use_returns_email_already_in_use_response(
            self, mocker, presenter_mock, interactor
    ):
        # Arrange
        role_ids = ["1"]
        user_profile_dto = CompleteUserProfileDTOFactory(name="username")
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import update_user_profile_adapter_mock
        adapter_mock = update_user_profile_adapter_mock(mocker=mocker)
        from ib_iam.exceptions.custom_exceptions import \
            UserAccountAlreadyExistWithThisEmail
        adapter_mock.side_effect = UserAccountAlreadyExistWithThisEmail
        presenter_mock.response_for_email_already_exists_exception \
            .return_value = mock.Mock()

        # Act
        interactor.update_user_profile_wrapper(
            user_profile_dto=user_profile_dto, role_ids=role_ids,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.response_for_email_already_exists_exception \
            .assert_called_once()

    def test_given_valid_details_returns_success_response_for_user(
            self, mocker, storage_mock, presenter_mock, interactor
    ):
        # Arrange
        name = "username"
        user_id = "user_id1"
        role_ids = ["1"]
        CompleteUserProfileDTOFactory.reset_sequence(1)
        user_profile_dto = CompleteUserProfileDTOFactory(
            user_id=user_id, name=name
        )
        storage_mock.is_user_admin.return_value = False
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import update_user_profile_adapter_mock
        adapter_mock = update_user_profile_adapter_mock(mocker=mocker)
        presenter_mock.get_response_for_update_user_profile \
            .return_value = mock.Mock()
        UserProfileDTOFactory.reset_sequence(1)
        user_profile_dto_of_ib_user = UserProfileDTOFactory(
            user_id=user_id, name=name, is_email_verified=None
        )

        # Act
        interactor.update_user_profile_wrapper(
            user_profile_dto=user_profile_dto, role_ids=role_ids,
            presenter=presenter_mock
        )

        # Assert
        adapter_mock.assert_called_once_with(
            user_id=user_id, user_profile_dto=user_profile_dto_of_ib_user
        )
        storage_mock.is_user_admin.assert_called_once_with(user_id=user_id)
        storage_mock.update_user_name_and_cover_page_url.assert_called_once_with(
            name=name, user_id=user_id,
            cover_page_url=user_profile_dto.cover_page_url
        )
        presenter_mock.get_response_for_update_user_profile \
            .assert_called_once()

    def test_given_valid_details_returns_success_response_for_admin(
            self, mocker, storage_mock, presenter_mock, interactor
    ):
        # Arrange
        name = "username"
        user_id = "user_id1"
        role_ids = ["1"]
        ids_of_role_objects = ["role_1"]
        UserProfileDTOFactory.reset_sequence(1)
        CompleteUserProfileDTOFactory.reset_sequence(1)
        user_profile_dto = CompleteUserProfileDTOFactory(
            user_id=user_id, name=name
        )
        user_profile_dto_of_ib_user = UserProfileDTOFactory(
            user_id=user_id, name=name, is_email_verified=None
        )
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import update_user_profile_adapter_mock
        adapter_mock = update_user_profile_adapter_mock(mocker=mocker)
        storage_mock.is_user_admin.return_value = True
        storage_mock.get_role_objs_ids.return_value = ids_of_role_objects
        presenter_mock.get_response_for_update_user_profile \
            .return_value = mock.Mock()

        # Act
        interactor.update_user_profile_wrapper(
            user_profile_dto=user_profile_dto,
            role_ids=role_ids,
            presenter=presenter_mock)

        # Assert
        adapter_mock.assert_called_once_with(
            user_id=user_id, user_profile_dto=user_profile_dto_of_ib_user)
        storage_mock.is_user_admin.assert_called_once_with(user_id=user_id)
        storage_mock.check_are_valid_role_ids.assert_called_once_with(role_ids)
        storage_mock.update_user_name_and_cover_page_url.assert_called_once_with(
            name=name, user_id=user_id,
            cover_page_url=user_profile_dto.cover_page_url)
        presenter_mock.get_response_for_update_user_profile \
            .assert_called_once()

    # def test_given_valid_details_returns_success_response_for_admin(
    #         self, mocker, storage_mock, presenter_mock, interactor):
    #     # Arrange
    #     name = "username"
    #     user_id = "user_id1"
    #     role_ids = ["1"]
    #     ids_of_role_objects = ["role_1"]
    #     UserProfileDTOFactory.reset_sequence(1)
    #     CompleteUserProfileDTOFactory.reset_sequence(1)
    #     user_profile_dto = CompleteUserProfileDTOFactory(
    #         user_id=user_id, name=name)
    #     user_profile_dto_of_ib_user = UserProfileDTOFactory(
    #         user_id=user_id, name=name, is_email_verified=None)
    #     from ib_iam.tests.common_fixtures.adapters.user_service \
    #         import update_user_profile_adapter_mock
    #     adapter_mock = update_user_profile_adapter_mock(mocker=mocker)
    #     storage_mock.is_user_admin.return_value = True
    #     storage_mock.get_role_objs_ids.return_value = ids_of_role_objects
    #     presenter_mock.get_response_for_update_user_profile \
    #         .return_value = mock.Mock()
    #
    #     # Act
    #     interactor.update_user_profile_wrapper(
    #         user_profile_dto=user_profile_dto,
    #         role_ids=role_ids,
    #         presenter=presenter_mock)
    #
    #     # Assert
    #     adapter_mock.assert_called_once_with(
    #         user_id=user_id, user_profile_dto=user_profile_dto_of_ib_user)
    #     storage_mock.is_user_admin.assert_called_once_with(user_id=user_id)
    #     storage_mock.check_are_valid_role_ids.assert_called_once_with(role_ids)
    #     storage_mock.remove_roles_for_user.assert_called_once_with(user_id)
    #     storage_mock.get_role_objs_ids.assert_called_once_with(role_ids)
    #     # storage_mock.add_roles_to_the_user.assert_called_once_with(
    #     #     user_id=user_id, role_ids=ids_of_role_objects)
    #     storage_mock.update_user_name_and_cover_page_url.assert_called_once_with(
    #         name=name, user_id=user_id,
    #         cover_page_url=user_profile_dto.cover_page_url)
    #     presenter_mock.get_response_for_update_user_profile \
    #         .assert_called_once()
