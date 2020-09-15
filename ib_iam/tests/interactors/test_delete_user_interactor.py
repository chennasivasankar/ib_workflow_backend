from unittest.mock import Mock

import pytest

from ib_iam.exceptions.custom_exceptions import UserNotFound
from ib_iam.interactors.delete_user_interactor import DeleteUserInteractor


class TestDeleteUserInteractor:
    @pytest.fixture
    def storage_mock(self):
        from unittest import mock
        from ib_iam.interactors.storage_interfaces.delete_user_storage_interface import \
            DeleteUserStorageInterface
        storage = mock.create_autospec(DeleteUserStorageInterface)
        return storage

    @pytest.fixture
    def user_storage_mock(self):
        from unittest import mock
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        storage = mock.create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture()
    def elastic_storage(self):
        from unittest import mock
        from ib_iam.interactors.storage_interfaces.elastic_storage_interface \
            import ElasticSearchStorageInterface
        storage = mock.create_autospec(ElasticSearchStorageInterface)
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from unittest import mock
        from ib_iam.interactors.presenter_interfaces.delete_user_presenter_interface import \
            DeleteUserPresenterInterface
        presenter = mock.create_autospec(DeleteUserPresenterInterface)
        return presenter

    @staticmethod
    def deactivate_delete_user_id_in_ib_users(mocker):
        mock = mocker.patch(
            "ib_iam.adapters.user_service.UserService.deactivate_delete_user_id_in_ib_users"
        )
        return mock

    def test_delete_user_given_valid_details_then_delete_user_from_user_details_db(
            self, storage_mock, user_storage_mock, presenter_mock, mocker,
            elastic_storage
    ):
        # Arrange
        admin_user_id = "1"
        delete_user_id = "2"
        interactor = DeleteUserInteractor(
            storage=storage_mock, user_storage=user_storage_mock,
            elastic_storage=elastic_storage
        )
        from ib_iam.tests.factories.storage_dtos import UserDTOFactory
        user_details_dto = UserDTOFactory.create(
            user_id=delete_user_id, is_admin=False
        )
        deactivate_delete_user_mocker = self. \
            deactivate_delete_user_id_in_ib_users(mocker=mocker)

        storage_mock.get_user_details.return_value = user_details_dto
        deactivate_delete_user_mocker.return_value = None
        presenter_mock.get_delete_user_response.return_value = Mock()

        # Act
        interactor.delete_user_wrapper(
            user_id=admin_user_id, delete_user_id=delete_user_id,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.delete_user.assert_called_once_with(
            user_id=delete_user_id
        )
        presenter_mock.get_delete_user_response.assert_called_once()

    # def test_delete_user_given_valid_details_then_delete_user_roles_from_user_roles_db(
    #         self, storage_mock, user_storage_mock, presenter_mock, mocker,
    #         elastic_storage
    # ):
    #     # Arrange
    #     admin_user_id = "1"
    #     delete_user_id = "2"
    #     interactor = DeleteUserInteractor(
    #         storage=storage_mock, user_storage=user_storage_mock,
    #         elastic_storage=elastic_storage
    #     )
    #     from ib_iam.tests.factories.storage_dtos import UserDTOFactory
    #     user_details_dto = UserDTOFactory.create(
    #         user_id=delete_user_id, is_admin=False
    #     )
    #     deactivate_delete_user_mocker = self. \
    #         deactivate_delete_user_id_in_ib_users(mocker=mocker)
    #
    #     storage_mock.get_user_details.return_value = user_details_dto
    #     deactivate_delete_user_mocker.return_value = None
    #     presenter_mock.get_delete_user_response.return_value = Mock()
    #
    #     # Act
    #     interactor.delete_user_wrapper(
    #         user_id=admin_user_id, delete_user_id=delete_user_id,
    #         presenter=presenter_mock
    #     )
    #
    #     # Assert
    #     storage_mock.delete_user.assert_called_once_with(
    #         user_id=delete_user_id
    #     )
    #     storage_mock.delete_user_roles.assert_called_once_with(
    #         user_id=delete_user_id
    #     )
    #     presenter_mock.get_delete_user_response.assert_called_once()

    def test_delete_user_given_valid_user_id_then_delete_user_teams_from_user_team_db(
            self, storage_mock, user_storage_mock, presenter_mock, mocker,
            elastic_storage
    ):
        # Arrange
        admin_user_id = "1"
        delete_user_id = "2"
        interactor = DeleteUserInteractor(
            storage=storage_mock, user_storage=user_storage_mock,
            elastic_storage=elastic_storage
        )
        from ib_iam.tests.factories.storage_dtos import UserDTOFactory
        user_details_dto = UserDTOFactory.create(
            user_id=delete_user_id, is_admin=False
        )
        deactivate_delete_user_mocker = self. \
            deactivate_delete_user_id_in_ib_users(mocker=mocker)

        storage_mock.get_user_details.return_value = user_details_dto
        deactivate_delete_user_mocker.return_value = None
        presenter_mock.get_delete_user_response.return_value = Mock()

        # Act
        interactor.delete_user_wrapper(
            user_id=admin_user_id, delete_user_id=delete_user_id,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.delete_user.assert_called_once_with(
            user_id=delete_user_id
        )
        storage_mock.delete_user_teams.assert_called_once_with(
            user_id=delete_user_id
        )
        presenter_mock.get_delete_user_response.assert_called_once()

    def test_delete_user_given_valid_delete_user_id_and_invalid_admin_user_id_then_raise_exception(
            self, storage_mock, user_storage_mock, presenter_mock,
            elastic_storage
    ):
        # Arrange
        invalid_admin_user_id = "1"
        delete_user_id = "2"
        interactor = DeleteUserInteractor(
            storage=storage_mock, user_storage=user_storage_mock,
            elastic_storage=elastic_storage
        )

        user_storage_mock.is_user_admin.return_value = False
        presenter_mock.get_delete_user_response.return_value = Mock()

        # Act
        interactor.delete_user_wrapper(
            user_id=invalid_admin_user_id, delete_user_id=delete_user_id,
            presenter=presenter_mock
        )

        # Assert
        user_storage_mock.is_user_admin.assert_called_once_with(
            user_id=invalid_admin_user_id
        )
        presenter_mock.response_for_user_is_not_admin_exception.assert_called_once()

    def test_delete_user_given_invalid_delete_user_id_then_raise_exception(
            self, storage_mock, user_storage_mock, presenter_mock,
            elastic_storage
    ):
        # Arrange
        admin_user_id = "1"
        invalid_delete_user_id = "2"
        interactor = DeleteUserInteractor(
            storage=storage_mock, user_storage=user_storage_mock,
            elastic_storage=elastic_storage
        )

        storage_mock.get_user_details.side_effect = UserNotFound
        presenter_mock.get_delete_user_response.return_value = Mock()

        # Act
        interactor.delete_user_wrapper(
            user_id=admin_user_id, delete_user_id=invalid_delete_user_id,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.get_user_details.assert_called_once_with(
            user_id=invalid_delete_user_id
        )
        presenter_mock.raise_user_is_not_found_exception.assert_called_once()

    def test_delete_user_given_valid_details_and_delete_user_id_is_admin_then_raise_exception(
            self, storage_mock, user_storage_mock, presenter_mock,
            elastic_storage
    ):
        # Arrange
        admin_user_id = "1"
        delete_user_id = "2"
        interactor = DeleteUserInteractor(
            storage=storage_mock, user_storage=user_storage_mock,
            elastic_storage=elastic_storage
        )
        from ib_iam.tests.factories.storage_dtos import UserDTOFactory
        user_details_dto = UserDTOFactory.create(
            user_id=delete_user_id, is_admin=True
        )

        storage_mock.get_user_details.return_value = user_details_dto
        presenter_mock.get_delete_user_response.return_value = Mock()

        # Act
        interactor.delete_user_wrapper(
            user_id=admin_user_id, delete_user_id=delete_user_id,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.get_user_details.assert_called_once_with(
            user_id=delete_user_id)
        presenter_mock.raise_user_does_not_have_delete_permission_exception. \
            assert_called_once()

    def test_delete_user_given_valid_details_then_deactivate_delete_user_in_ib_users(
            self, storage_mock, user_storage_mock, presenter_mock, mocker,
            elastic_storage
    ):
        # Arrange
        admin_user_id = "1"
        delete_user_id = "2"
        interactor = DeleteUserInteractor(
            storage=storage_mock, user_storage=user_storage_mock,
            elastic_storage=elastic_storage
        )
        from ib_iam.tests.factories.storage_dtos import UserDTOFactory
        user_details_dto = UserDTOFactory.create(
            user_id=delete_user_id, is_admin=False
        )
        deactivate_delete_user_mocker = self. \
            deactivate_delete_user_id_in_ib_users(mocker=mocker)

        storage_mock.get_user_details.return_value = user_details_dto
        presenter_mock.get_delete_user_response.return_value = Mock()

        # Act
        interactor.delete_user_wrapper(
            user_id=admin_user_id, delete_user_id=delete_user_id,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.delete_user.assert_called_once_with(
            user_id=delete_user_id
        )
        deactivate_delete_user_mocker.assert_called_once_with(
            user_id=delete_user_id
        )
        presenter_mock.get_delete_user_response.assert_called_once()
        elastic_storage.delete_elastic_user.assert_called_once_with(
            user_id=delete_user_id
        )
