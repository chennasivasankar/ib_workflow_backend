from unittest.mock import create_autospec, Mock
from uuid import uuid4

from ib_iam.interactors.get_users_details_inteactor import GetUsersDetails
from ib_iam.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from ib_iam.interactors.storage_interfaces.storage_interface import StorageInterface

USER_ID = uuid4()
class TestGetUsersDetailsInteractor:
    def test_get_users_when_user_is_not_admin_then_throw_exception(self):
        # Arrange
        user_id = USER_ID
        limit = 10
        offset = 0
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = GetUsersDetails(storage=storage)
        storage.validate_user_is_admin.return_value = False
        presenter.raise_user_is_not_admin_exception.return_value = Mock()
        # Act
        response = interactor.get_users_details_wrapper(
            user_id=user_id, offset=offset, limit=limit, presenter=presenter
        )

        # Assert
        storage.validate_user_is_admin.assert_called_once_with(user_id=user_id)
        presenter.raise_user_is_not_admin_exception.assert_called_once()

    def test_get_users_when_offset_value_is_less_than_0_then_throw_exception(self):
        # Arrange
        user_id = USER_ID
        limit = 10
        offset = -1
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = GetUsersDetails(storage=storage)
        storage.validate_user_is_admin.return_value = True

        # Act
        response = interactor.get_users_details_wrapper(
            user_id=user_id, offset=offset, limit=limit, presenter=presenter
        )

        # Assert
        presenter.raise_invalid_offset_value_exception.assert_called_once()

    def test_get_users_when_limit_value_is_less_than_0_then_throw_exception(self):
        # Arrange
        user_id = USER_ID
        limit = -10
        offset = 0
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = GetUsersDetails(storage=storage)
        storage.validate_user_is_admin.return_value = True

        # Act
        response = interactor.get_users_details_wrapper(
            user_id=user_id, offset=offset, limit=limit, presenter=presenter
        )

        # Assert
        presenter.raise_invalid_limit_value_exception.assert_called_once()

    def test_get_users_when_offset_value_is_greater_than_limit_then_throw_exception(self):
        # Arrange
        user_id = USER_ID
        limit = 5
        offset = 10
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = GetUsersDetails(storage=storage)
        storage.validate_user_is_admin.return_value = True

        # Act
        response = interactor.get_users_details_wrapper(
            user_id=user_id, offset=offset, limit=limit, presenter=presenter
        )

        # Assert
        presenter.raise_offset_value_is_greater_than_limit_exception.assert_called_once()

    def test_get_user_ids_returns_user_ids(self):
        # Arrange
        user_id = USER_ID
        limit = 10
        offset = 0
        user_ids = ["dd67ab82-ab8a-4253-98ae-bef82b8013a8",
                    "dd67ab82-ab8a-4253-98ae-bef82b8013a9"
                    "dd67ab82-ab8a-4253-98ae-bef82b8013b8"]
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = GetUsersDetails(storage=storage)
        storage.validate_user_is_admin.return_value = True
        storage.get_user_ids.return_value = user_ids

        # Act
        response = interactor.get_users_details_wrapper(
            user_id=user_id, offset=offset, limit=limit, presenter=presenter
        )

        # Assert
        storage.get_user_ids.assert_called_once()

    def test_get_users_team_details_returns_team_details_of_users(self):
        user_id = USER_ID
        limit = 10
        offset = 0
        user_ids = ["dd67ab82-ab8a-4253-98ae-bef82b8013a8",
                    "dd67ab82-ab8a-4253-98ae-bef82b8013a9",
                    "dd67ab82-ab8a-4253-98ae-bef82b8013b8"]
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = GetUsersDetails(storage=storage)
        storage.validate_user_is_admin.return_value = True
        storage.get_user_ids.return_value = user_ids
        from ib_iam.tests.factories.storage_dtos import UserTeamDTOFactory
        user_team_dtos = UserTeamDTOFactory.create_batch(4)
        storage.get_team_details_of_users_bulk.return_value = user_team_dtos

        # Act
        response = interactor.get_users_details_wrapper(
            user_id=user_id, offset=offset, limit=limit, presenter=presenter
        )

        # Assert
        storage.get_user_ids.assert_called_once()
        storage.get_team_details_of_users_bulk.assert_called_once_with(user_ids)

    def test_get_users_role_details_returns_team_details_of_users(self):
        user_id = USER_ID
        limit = 10
        offset = 0
        user_ids = ["dd67ab82-ab8a-4253-98ae-bef82b8013a8",
                    "dd67ab82-ab8a-4253-98ae-bef82b8013a9",
                    "dd67ab82-ab8a-4253-98ae-bef82b8013b8"]
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = GetUsersDetails(storage=storage)
        storage.validate_user_is_admin.return_value = True
        storage.get_user_ids.return_value = user_ids
        from ib_iam.tests.factories.storage_dtos import UserRoleDTOFactory
        user_role_dtos = UserRoleDTOFactory.create_batch(4)
        storage.get_role_details_of_users_bulk.return_value = user_role_dtos

        # Act
        response = interactor.get_users_details_wrapper(
            user_id=user_id, offset=offset, limit=limit, presenter=presenter
        )

        # Assert
        storage.get_user_ids.assert_called_once()
        storage.get_role_details_of_users_bulk.assert_called_once_with(user_ids)

    # TODO: Incomplete
    def test_get_users_company_details_returns_team_details_of_users(self):
        user_id = USER_ID
        limit = 10
        offset = 0
        user_ids = ["dd67ab82-ab8a-4253-98ae-bef82b8013a8",
                    "dd67ab82-ab8a-4253-98ae-bef82b8013a9",
                    "dd67ab82-ab8a-4253-98ae-bef82b8013b8"]
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = GetUsersDetails(storage=storage)
        storage.validate_user_is_admin.return_value = True
        storage.get_user_ids.return_value = user_ids
        from ib_iam.tests.factories.storage_dtos import UserRoleDTOFactory
        user_role_dtos = UserRoleDTOFactory.create_batch(4)
        storage.get_role_details_of_users_bulk.return_value = user_role_dtos

        # Act
        response = interactor.get_users_details_wrapper(
            user_id=user_id, offset=offset, limit=limit, presenter=presenter
        )

        # Assert
        storage.get_user_ids.assert_called_once()
        storage.get_role_details_of_users_bulk.assert_called_once_with(user_ids)