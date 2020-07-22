from unittest.mock import Mock

import pytest

from ib_iam.interactors.delete_user_interactor import DeleteUserInteractor
from ib_iam.tests.common_fixtures.storages import reset_all_factories_sequence
from ib_iam.tests.factories.models import UserDetailsFactory, UserRoleFactory


class TestDeleteUserInteractor:
    @pytest.fixture
    def storage_mock(self):
        from unittest import mock
        from ib_iam.interactors.storage_interfaces.delete_user_storage_interface import \
            DeleteUserStorageInterface
        storage = mock.create_autospec(DeleteUserStorageInterface)
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from unittest import mock
        from ib_iam.interactors.presenter_interfaces.delete_user_presenter_interface import \
            DeleteUserPresenterInterface
        presenter = mock.create_autospec(DeleteUserPresenterInterface)
        return presenter

    def test_delete_user_given_valid_user_id_then_delete_user_from_user_details_db(
            self, storage_mock, presenter_mock):
        admin_user_id = "1"
        delete_user_id = "2"
        interactor = DeleteUserInteractor(storage=storage_mock)

        presenter_mock.get_delete_user_response.return_value = Mock()

        interactor.delete_user_wrapper(user_id=admin_user_id,
                                       delete_user_id=delete_user_id,
                                       presenter=presenter_mock)

        storage_mock.delete_user.assert_called_once_with(
            user_id=delete_user_id)
        presenter_mock.get_delete_user_response.assert_called_once()

    def test_delete_user_given_valid_user_id_then_delete_user_roles_from_user_roles_db(
            self, storage_mock, presenter_mock):
        admin_user_id = "1"
        delete_user_id = "2"
        interactor = DeleteUserInteractor(storage=storage_mock)

        presenter_mock.get_delete_user_response.return_value = Mock()

        interactor.delete_user_wrapper(user_id=admin_user_id,
                                       delete_user_id=delete_user_id,
                                       presenter=presenter_mock)

        storage_mock.delete_user.assert_called_once_with(
            user_id=delete_user_id)
        storage_mock.delete_user_roles.assert_called_once_with(
            user_id=delete_user_id)
        presenter_mock.get_delete_user_response.assert_called_once()

    def test_delete_user_given_valid_user_id_then_delete_user_teams_from_user_team_db(
            self, storage_mock, presenter_mock):
        admin_user_id = "1"
        delete_user_id = "2"
        interactor = DeleteUserInteractor(storage=storage_mock)

        presenter_mock.get_delete_user_response.return_value = Mock()

        interactor.delete_user_wrapper(user_id=admin_user_id,
                                       delete_user_id=delete_user_id,
                                       presenter=presenter_mock)

        storage_mock.delete_user.assert_called_once_with(
            user_id=delete_user_id)
        storage_mock.delete_user_roles.assert_called_once_with(
            user_id=delete_user_id)
        storage_mock.delete_user_teams.assert_called_once_with(
            user_id=delete_user_id)
        presenter_mock.get_delete_user_response.assert_called_once()
