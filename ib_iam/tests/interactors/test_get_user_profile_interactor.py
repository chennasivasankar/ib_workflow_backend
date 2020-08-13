import pytest


class TestGetUserProfileInteractor:

    @pytest.fixture()
    def presenter_mock(self):
        from ib_iam.interactors.presenter_interfaces.auth_presenter_interface import \
            GetUserProfilePresenterInterface
        from unittest.mock import create_autospec
        presenter = create_autospec(GetUserProfilePresenterInterface)
        return presenter

    @pytest.fixture()
    def storage_mock(self):
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        from unittest.mock import create_autospec
        storage = create_autospec(UserStorageInterface)
        return storage

    def test_invalid_email_raise_exception(self, mocker, presenter_mock,
                                           storage_mock):
        # Arrange
        user_id = ""
        from unittest.mock import Mock
        expected_presenter_invalid_user_id_mock = Mock()

        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dto_mock
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(mocker)
        from ib_iam.exceptions.custom_exceptions import InvalidUserId
        get_user_profile_dto_mock.side_effect = InvalidUserId

        presenter_mock.raise_exception_for_invalid_user_id.return_value \
            = expected_presenter_invalid_user_id_mock

        from ib_iam.interactors.get_user_profile_interactor import \
            GetUserProfileInteractor
        interactor = GetUserProfileInteractor(
            storage=storage_mock
        )

        # Act
        response = interactor.get_user_profile_wrapper(
            user_id=user_id, presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_invalid_user_id_mock
        presenter_mock.raise_exception_for_invalid_user_id.assert_called_once()

    def test_with_user_id_which_is_does_not_exist_raise_exception(
            self, mocker, presenter_mock, storage_mock
    ):
        # Arrange
        user_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        from unittest.mock import Mock
        expected_presenter_user_account_does_not_exist_mock = Mock()

        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dto_mock
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(mocker)
        from ib_iam.adapters.user_service import UserAccountDoesNotExist
        get_user_profile_dto_mock.side_effect = UserAccountDoesNotExist

        presenter_mock.raise_exception_for_user_account_does_not_exist \
            .return_value = expected_presenter_user_account_does_not_exist_mock

        from ib_iam.interactors.get_user_profile_interactor import \
            GetUserProfileInteractor
        interactor = GetUserProfileInteractor(
            storage=storage_mock
        )

        # Act
        response = interactor.get_user_profile_wrapper(
            user_id=user_id, presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_user_account_does_not_exist_mock
        presenter_mock.raise_exception_for_user_account_does_not_exist. \
            assert_called_once()

    def test_with_valid_user_id_return_response(self, mocker, storage_mock,
                                                presenter_mock):
        # Arrange
        user_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        from unittest.mock import Mock
        expected_presenter_user_profile_response_mock = Mock()
        from ib_iam.adapters.dtos import UserProfileDTO
        expected_user_profile_dto = UserProfileDTO(
            user_id=user_id,
            email="test@gmail.com",
            profile_pic_url="test.com",
            is_admin=True,
            name="test"
        )

        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dto_mock
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(mocker)
        get_user_profile_dto_mock.return_value = UserProfileDTO(
            user_id=user_id,
            email="test@gmail.com",
            profile_pic_url="test.com",
            is_admin=False,
            name="test"
        )

        storage_mock.is_user_admin.return_value = True

        presenter_mock.prepare_response_for_user_profile_dto \
            .return_value = expected_presenter_user_profile_response_mock

        from ib_iam.interactors.get_user_profile_interactor import \
            GetUserProfileInteractor
        interactor = GetUserProfileInteractor(
            storage=storage_mock
        )

        # Act
        response = interactor.get_user_profile_wrapper(
            user_id=user_id, presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_user_profile_response_mock
        presenter_mock.prepare_response_for_user_profile_dto. \
            assert_called_once_with(expected_user_profile_dto)
