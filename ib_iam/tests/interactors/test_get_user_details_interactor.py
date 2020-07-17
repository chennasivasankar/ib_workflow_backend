from unittest.mock import create_autospec, Mock, patch
from uuid import uuid4

import pytest
from ib_iam.interactors.get_users_details_inteactor import GetUsersDetailsInteractor
from ib_iam.interactors.presenter_interfaces.presenter_interface \
    import PresenterInterface
from ib_iam.interactors.storage_interfaces.storage_interface \
    import StorageInterface
from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
from ib_iam.tests.factories.storage_dtos import UserDTOFactory

USER_ID = "dd67ab82-ab8a-4253-98ae-bef82b8013a8"


@pytest.fixture()
def user_team_dtos():
    user_ids = ["user1", "user2", "user3"]
    user_teams = []
    from ib_iam.tests.factories.storage_dtos \
        import UserTeamDTOFactory
    for user_id in user_ids:
        user_teams.extend(UserTeamDTOFactory.create_batch(4, user_id=user_id))
    return user_teams


@pytest.fixture()
def user_company_dtos():
    user_ids = ["user1", "user2", "user3"]
    company_ids = ["company1", "company2", "company3"]
    from ib_iam.tests.factories.storage_dtos \
        import UserCompanyDTOFactory
    user_company_dtos = [
        UserCompanyDTOFactory.create(company_id=company_id, user_id=user_id) \
        for company_id, user_id in zip(company_ids, user_ids)
    ]
    return user_company_dtos


@pytest.fixture()
def user_role_dtos():
    user_ids = ["user1", "user2", "user3"]
    user_roles = []
    from ib_iam.tests.factories.storage_dtos \
        import UserRoleDTOFactory
    for user_id in user_ids:
        user_roles.extend(UserRoleDTOFactory.create_batch(
            4, user_id=user_id))
    return user_roles


@pytest.fixture()
def user_dtos():
    user_ids = ["user1", "user2", "user3"]
    from ib_iam.tests.factories.storage_dtos \
        import UserDTOFactory
    user_dtos = [UserDTOFactory.create(user_id=user_id)
                 for user_id in user_ids]
    return user_dtos


@pytest.fixture()
def user_profile_dtos():
    user_ids = ["user1", "user2", "user3"]
    user_profile_dtos = [UserDTOFactory.create(user_id=user_id) \
                         for user_id in user_ids]
    return user_profile_dtos


class TestGetUsersDetailsInteractor:
    def test_get_users_when_user_is_not_admin_then_throw_exception(self):
        # Arrange
        user_id = USER_ID
        limit = 10
        offset = 0
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = GetUsersDetailsInteractor(storage=storage)
        storage.validate_user_is_admin.return_value = False
        presenter.raise_user_is_not_admin_exception.return_value = Mock()
        # Act
        response = interactor.get_users_details_wrapper(
            user_id=user_id, offset=offset, limit=limit,
            presenter=presenter
        )

        # Assert
        storage.validate_user_is_admin.assert_called_once_with(
            user_id=user_id)
        presenter.raise_user_is_not_admin_exception.assert_called_once()

    def test_get_users_when_offset_value_is_less_than_0_then_throw_exception(self):
        # Arrange
        user_id = USER_ID
        limit = 10
        offset = -1
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = GetUsersDetailsInteractor(storage=storage)
        storage.validate_user_is_admin.return_value = True

        # Act
        response = interactor.get_users_details_wrapper(
            user_id=user_id, offset=offset, limit=limit,
            presenter=presenter
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
        interactor = GetUsersDetailsInteractor(storage=storage)
        storage.validate_user_is_admin.return_value = True

        # Act
        response = interactor.get_users_details_wrapper(
            user_id=user_id, offset=offset, limit=limit,
            presenter=presenter
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
        interactor = GetUsersDetailsInteractor(storage=storage)
        storage.validate_user_is_admin.return_value = True

        # Act
        response = interactor.get_users_details_wrapper(
            user_id=user_id, offset=offset, limit=limit,
            presenter=presenter
        )

        # Assert
        presenter.raise_offset_value_is_greater_than_limit_value_exception. \
            assert_called_once()

    def test_get_users_returns_user_dtos(self, user_dtos):
        # Arrange
        user_id = USER_ID
        limit = 10
        offset = 0
        user_ids = ["user1", "user2", "user3"]
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = GetUsersDetailsInteractor(storage=storage)
        storage.validate_user_is_admin.return_value = True
        storage.get_users_who_are_not_admins.return_value = user_dtos

        # Act
        response = interactor.get_users_details_wrapper(
            user_id=user_id, offset=offset, limit=limit, presenter=presenter
        )

        # Assert
        storage.get_users_who_are_not_admins.assert_called_once()

    def test_get_users_team_details_returns_team_details_of_users(
            self, user_dtos, user_team_dtos):
        user_id = USER_ID
        limit = 10
        offset = 0
        user_ids = ["user1", "user2", "user3"]
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = GetUsersDetailsInteractor(storage=storage)
        storage.validate_user_is_admin.return_value = True
        storage.get_users_who_are_not_admins.return_value = user_dtos
        storage.get_team_details_of_users_bulk.return_value = user_team_dtos

        # Act
        response = interactor.get_users_details_wrapper(
            user_id=user_id, offset=offset, limit=limit, presenter=presenter
        )

        # Assert
        storage.get_users_who_are_not_admins.assert_called_once()
        storage.get_team_details_of_users_bulk.assert_called_once_with(
            user_ids)

    def test_get_users_role_details_returns_team_details_of_users(
            self, user_dtos, user_role_dtos):
        user_id = USER_ID
        limit = 10
        offset = 0
        user_ids = ["user1", "user2", "user3"]
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = GetUsersDetailsInteractor(storage=storage)
        storage.validate_user_is_admin.return_value = True
        storage.get_users_who_are_not_admins.return_value = user_dtos
        storage.get_role_details_of_users_bulk.return_value = user_role_dtos
        # Act
        response = interactor.get_users_details_wrapper(
            user_id=user_id, offset=offset, limit=limit, presenter=presenter
        )

        # Assert
        storage.get_users_who_are_not_admins.assert_called_once()
        storage.get_role_details_of_users_bulk.assert_called_once_with(
            user_ids)

    def test_get_users_company_details_returns_team_details_of_users(
            self, user_dtos, user_company_dtos):
        user_id = USER_ID
        limit = 10
        offset = 0
        user_ids = ["user1", "user2", "user3"]
        company_ids = ["company1", "company2", "company3"]
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = GetUsersDetailsInteractor(storage=storage)
        storage.validate_user_is_admin.return_value = True

        storage.get_users_who_are_not_admins.return_value = user_dtos
        storage.get_company_details_of_users_bulk.return_value = user_company_dtos

        # Act
        response = interactor.get_users_details_wrapper(
            user_id=user_id, offset=offset, limit=limit, presenter=presenter
        )

        # Assert
        storage.get_users_who_are_not_admins.assert_called_once()
        storage.get_company_details_of_users_bulk.assert_called_once()

    @patch(
        "ib_iam.adapters.user_service.UserService.get_user_profile_bulk")
    def test_get_users_from_adapter_return_user_deails(
            self, get_user_profile_bulk, user_dtos, user_team_dtos,
            user_role_dtos, user_company_dtos, user_profile_dtos):
        user_id = USER_ID
        limit = 10
        offset = 0
        user_ids = ["user1", "user2", "user3"]
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = GetUsersDetailsInteractor(storage=storage)
        storage.validate_user_is_admin.return_value = True
        user_dtos = [UserDTOFactory.create(user_id=user_id)
                     for user_id in user_ids]
        storage.get_users_who_are_not_admins.return_value = user_dtos
        userprofile_dtos = [UserDTOFactory.create(user_id=user_id)
                            for user_id in user_ids]
        get_user_profile_bulk.return_value = user_profile_dtos

        # Act
        response = interactor.get_users_details_wrapper(
            user_id=user_id, offset=offset, limit=limit, presenter=presenter
        )

        # Assert
        get_user_profile_bulk.assert_called_once_with(user_ids=user_ids)

    @patch(
        "ib_iam.adapters.user_service.UserService.get_user_profile_bulk")
    def test_get_users_complete_details(
            self, get_user_profile_bulk, user_dtos, user_team_dtos,
            user_role_dtos, user_company_dtos, user_profile_dtos):
        user_id = USER_ID
        limit = 10
        offset = 0
        user_ids = ["user1", "user2", "user3"]
        presenter = create_autospec(PresenterInterface)
        storage = create_autospec(StorageInterface)
        interactor = GetUsersDetailsInteractor(storage=storage)
        storage.validate_user_is_admin.return_value = True
        storage.get_users_who_are_not_admins.return_value = user_dtos

        storage.get_team_details_of_users_bulk.return_value = user_team_dtos
        storage.get_company_details_of_users_bulk.return_value = \
            user_company_dtos
        storage.get_role_details_of_users_bulk.return_value = user_role_dtos

        get_user_profile_bulk.return_value = user_profile_dtos

        # Act
        response = interactor.get_users_details_wrapper(
            user_id=user_id, offset=offset, limit=limit, presenter=presenter
        )

        # Assert
        get_user_profile_bulk.assert_called_once_with(user_ids=user_ids)
        presenter.response_for_get_users.assert_called_once()
