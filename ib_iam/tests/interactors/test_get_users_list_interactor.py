from unittest.mock import Mock

import pytest

from ib_iam.interactors.get_users_list_interactor import \
    GetUsersDetailsInteractor
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
    from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
    user_profile_dtos = [UserProfileDTOFactory.create(user_id=user_id) \
                         for user_id in user_ids]
    return user_profile_dtos


class TestGetUsersDetailsInteractor:

    @pytest.fixture
    def storage_mock(self):
        from unittest import mock
        from ib_iam.interactors.storage_interfaces.user_storage_interface \
            import UserStorageInterface
        storage = mock.create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture
    def presenter_mock(self):
        from unittest import mock
        from ib_iam.interactors.presenter_interfaces. \
            get_users_list_presenter_interface import \
            GetUsersListPresenterInterface
        storage = mock.create_autospec(GetUsersListPresenterInterface)
        return storage

    def test_get_users_when_user_is_not_admin_then_throw_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        user_id = USER_ID
        limit = 10
        offset = 0
        from ib_iam.interactors.storage_interfaces.dtos import PaginationDTO
        pagination_dto = PaginationDTO(
            offset=offset,
            limit=limit
        )
        interactor = GetUsersDetailsInteractor(user_storage=storage_mock)
        storage_mock.is_user_admin.return_value = False
        presenter_mock.raise_user_is_not_admin_exception.return_value = Mock()
        # Act
        interactor.get_users_details_wrapper(
            user_id=user_id, pagination_dto=pagination_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.is_user_admin.assert_called_once_with(
            user_id=user_id)
        presenter_mock.raise_user_is_not_admin_exception.assert_called_once()

    def test_get_users_when_offset_value_is_less_than_0_then_throw_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        user_id = USER_ID
        limit = 10
        offset = -1
        from ib_iam.interactors.storage_interfaces.dtos import PaginationDTO
        pagination_dto = PaginationDTO(
            offset=offset,
            limit=limit
        )
        interactor = GetUsersDetailsInteractor(user_storage=storage_mock)
        storage_mock.is_user_admin.return_value = True

        # Act
        interactor.get_users_details_wrapper(
            user_id=user_id, pagination_dto=pagination_dto,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.raise_invalid_offset_value_exception.assert_called_once()

    def test_get_users_when_limit_value_is_less_than_0_then_throw_exception(
            self, storage_mock, presenter_mock):
        # Arrange
        user_id = USER_ID
        limit = -10
        offset = 0
        from ib_iam.interactors.storage_interfaces.dtos import PaginationDTO
        pagination_dto = PaginationDTO(
            offset=offset,
            limit=limit
        )
        interactor = GetUsersDetailsInteractor(user_storage=storage_mock)
        storage_mock.is_user_admin.return_value = True

        # Act
        interactor.get_users_details_wrapper(
            user_id=user_id, pagination_dto=pagination_dto,
            presenter=presenter_mock
        )

        # Assert
        presenter_mock.raise_invalid_limit_value_exception.assert_called_once()

    def test_get_users_returns_user_dtos(
            self, storage_mock, presenter_mock, user_dtos, mocker):
        # Arrange
        user_id = USER_ID
        limit = 10
        offset = 0
        from ib_iam.interactors.storage_interfaces.dtos import PaginationDTO
        pagination_dto = PaginationDTO(
            offset=offset,
            limit=limit
        )
        interactor = GetUsersDetailsInteractor(user_storage=storage_mock)
        storage_mock.is_user_admin.return_value = True
        storage_mock.get_users_who_are_not_admins.return_value = user_dtos
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import get_users_adapter_mock
        adapter_mock = get_users_adapter_mock(
            mocker=mocker,
            user_profile_dtos=user_profile_dtos
        )

        # Act
        interactor.get_users_details_wrapper(
            user_id=user_id, pagination_dto=pagination_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.get_users_who_are_not_admins.assert_called_once()
        adapter_mock.assert_called_once()

    def test_get_users_team_details_returns_team_details_of_users(
            self, user_dtos, user_team_dtos, storage_mock, presenter_mock,
            mocker):
        user_id = USER_ID
        limit = 10
        offset = 0
        from ib_iam.interactors.storage_interfaces.dtos import PaginationDTO
        pagination_dto = PaginationDTO(
            offset=offset,
            limit=limit
        )
        user_ids = ["user1", "user2", "user3"]
        interactor = GetUsersDetailsInteractor(user_storage=storage_mock)
        storage_mock.is_user_admin.return_value = True
        storage_mock.get_users_who_are_not_admins.return_value = user_dtos
        storage_mock.get_team_details_of_users_bulk.return_value = user_team_dtos
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import get_users_adapter_mock
        adapter_mock = get_users_adapter_mock(
            mocker=mocker,
            user_profile_dtos=user_profile_dtos
        )

        # Act
        interactor.get_users_details_wrapper(
            user_id=user_id, pagination_dto=pagination_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.get_users_who_are_not_admins.assert_called_once()
        storage_mock.get_team_details_of_users_bulk.assert_called_once_with(
            user_ids)
        adapter_mock.assert_called_once()

    def test_get_users_role_details_returns_team_details_of_users(
            self, user_dtos, user_role_dtos, storage_mock, presenter_mock,
            mocker):
        user_id = USER_ID
        limit = 10
        offset = 0
        from ib_iam.interactors.storage_interfaces.dtos import PaginationDTO
        pagination_dto = PaginationDTO(
            offset=offset,
            limit=limit
        )
        user_ids = ["user1", "user2", "user3"]
        interactor = GetUsersDetailsInteractor(user_storage=storage_mock)
        storage_mock.is_user_admin.return_value = True
        storage_mock.get_users_who_are_not_admins.return_value = user_dtos
        storage_mock.get_role_details_of_users_bulk.return_value = user_role_dtos
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import get_users_adapter_mock
        adapter_mock = get_users_adapter_mock(
            mocker=mocker,
            user_profile_dtos=user_profile_dtos
        )

        # Act
        interactor.get_users_details_wrapper(
            user_id=user_id, pagination_dto=pagination_dto,
            presenter=presenter_mock
        )
        adapter_mock.assert_called_once()

        # Assert
        storage_mock.get_users_who_are_not_admins.assert_called_once()
        storage_mock.get_role_details_of_users_bulk.assert_called_once_with(
            user_ids)

    def test_get_users_company_details_returns_team_details_of_users(
            self, user_dtos, user_company_dtos, storage_mock, presenter_mock,
            mocker):
        user_id = USER_ID
        limit = 10
        offset = 0
        from ib_iam.interactors.storage_interfaces.dtos import PaginationDTO
        pagination_dto = PaginationDTO(
            offset=offset,
            limit=limit
        )
        interactor = GetUsersDetailsInteractor(user_storage=storage_mock)
        storage_mock.is_user_admin.return_value = True

        storage_mock.get_users_who_are_not_admins.return_value = user_dtos
        storage_mock.get_company_details_of_users_bulk.return_value = user_company_dtos
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import get_users_adapter_mock
        adapter_mock = get_users_adapter_mock(
            mocker=mocker,
            user_profile_dtos=user_profile_dtos
        )

        # Act
        interactor.get_users_details_wrapper(
            user_id=user_id, pagination_dto=pagination_dto,
            presenter=presenter_mock
        )

        # Assert
        storage_mock.get_users_who_are_not_admins.assert_called_once()
        storage_mock.get_company_details_of_users_bulk.assert_called_once()
        adapter_mock.assert_called_once()

    def test_get_users_from_adapter_return_user_deails(
            self, user_profile_dtos, storage_mock, presenter_mock, mocker):
        user_id = USER_ID
        limit = 10
        offset = 0
        user_ids = ["user1", "user2", "user3"]
        from ib_iam.interactors.storage_interfaces.dtos import PaginationDTO
        pagination_dto = PaginationDTO(
            offset=offset,
            limit=limit
        )
        interactor = GetUsersDetailsInteractor(user_storage=storage_mock)
        storage_mock.is_user_admin.return_value = True
        user_dtos = [UserDTOFactory.create(user_id=user_id)
                     for user_id in user_ids]
        storage_mock.get_users_who_are_not_admins.return_value = user_dtos

        from ib_iam.tests.common_fixtures.adapters.user_service \
            import get_users_adapter_mock
        adapter_mock = get_users_adapter_mock(
            mocker=mocker,
            user_profile_dtos=user_profile_dtos
        )

        # Act
        interactor.get_users_details_wrapper(
            user_id=user_id, pagination_dto=pagination_dto,
            presenter=presenter_mock
        )

        # Assert
        adapter_mock.assert_called_once()

    def test_get_users_complete_details(
            self, user_dtos, user_team_dtos,
            user_role_dtos, user_company_dtos, user_profile_dtos,
            storage_mock, presenter_mock, mocker):
        user_id = USER_ID
        limit = 10
        offset = 0
        from ib_iam.interactors.storage_interfaces.dtos import PaginationDTO
        pagination_dto = PaginationDTO(
            offset=offset,
            limit=limit
        )
        interactor = GetUsersDetailsInteractor(user_storage=storage_mock)
        storage_mock.is_user_admin.return_value = True
        storage_mock.get_users_who_are_not_admins.return_value = user_dtos

        storage_mock.get_team_details_of_users_bulk.return_value = user_team_dtos
        storage_mock.get_company_details_of_users_bulk.return_value = \
            user_company_dtos
        storage_mock.get_role_details_of_users_bulk.return_value = user_role_dtos

        from ib_iam.tests.common_fixtures.adapters.user_service \
            import get_users_adapter_mock
        adapter_mock = get_users_adapter_mock(
            mocker=mocker,
            user_profile_dtos=user_profile_dtos
        )

        # Act
        interactor.get_users_details_wrapper(
            user_id=user_id, pagination_dto=pagination_dto,
            presenter=presenter_mock
        )

        # Assert
        adapter_mock.assert_called_once()
        storage_mock.get_total_count_of_users_for_query.assert_called_once()
        presenter_mock.response_for_get_users.assert_called_once()

    def test_get_user_dtos_return_response(self, mocker, storage_mock,
                                           user_profile_dtos):
        # Arrange
        user_ids = ["user1", "user2", "user3"]

        from ib_iam.tests.common_fixtures.adapters.user_service \
            import get_users_adapter_mock
        get_users_adapter_mock(
            mocker=mocker,
            user_profile_dtos=user_profile_dtos
        )

        interactor = GetUsersDetailsInteractor(user_storage=storage_mock)

        # Act
        response = interactor.get_user_dtos(user_ids=user_ids)

        # Assert
        assert response == user_profile_dtos

    def test_get_valid_user_ids_return_response(self, storage_mock):
        # Arrange
        user_ids = ["user1", "user2", "user3"]
        valid_user_ids = ["user1", "user2"]

        storage_mock.get_valid_user_ids.return_value = valid_user_ids

        interactor = GetUsersDetailsInteractor(user_storage=storage_mock)

        # Act
        response = interactor.get_valid_user_ids(user_ids=user_ids)

        # Assert
        assert response == valid_user_ids
