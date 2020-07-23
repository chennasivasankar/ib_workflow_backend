import uuid
from unittest.mock import patch

import pytest

from ib_iam.storages.get_users_list_storage_implementation \
    import GetUsersListStorageImplementation

from ib_iam.tests.common_fixtures.storages import \
    user_not_admin, users_company, users_team, users_role


class TestGetUsers:
    @pytest.fixture()
    def user_dtos(self):
        from ib_iam.interactors.storage_interfaces.dtos import UserDTO
        user_dtos = [
            UserDTO(user_id='user0', is_admin=False, company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331'),
            UserDTO(user_id='user1', is_admin=False, company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331'),
            UserDTO(user_id='user2', is_admin=False, company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331'),
            UserDTO(user_id='user3', is_admin=False, company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332'),
            UserDTO(user_id='user4', is_admin=False, company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332'),
            UserDTO(user_id='user5', is_admin=False, company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332')]
        return user_dtos
    @pytest.fixture()
    def users_company_dtos(self):
        from ib_iam.interactors.storage_interfaces.dtos import UserCompanyDTO
        users_company_dtos = [
            UserCompanyDTO(
                user_id='user0',
                company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331',
                company_name='company 0'
            ),
            UserCompanyDTO(
                user_id='user1',
                company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331',
                company_name='company 0'
            )
        ]
        return users_company_dtos

    @pytest.fixture()
    def user_role_dtos(self):
        from ib_iam.interactors.storage_interfaces.dtos import UserRoleDTO
        users_role_dtos = [
            UserRoleDTO(
                user_id='user1',
                role_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331',
                name='role 0',
                description='payment_description0'
            ),
            UserRoleDTO(
                user_id='user2',
                role_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331',
                name='role 0',
                description='payment_description0'
            ), UserRoleDTO(
                user_id='user1',
                role_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332',
                name='role 1',
                description='payment_description1'
            ),
            UserRoleDTO(
                user_id='user2',
                role_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332',
                name='role 1',
                description='payment_description1'
            )
        ]
        return users_role_dtos

    @pytest.fixture()
    def user_team_dtos(self):
        from ib_iam.interactors.storage_interfaces.dtos import UserTeamDTO
        user_team_dtos = [
            UserTeamDTO(
                user_id='user1',
                team_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331',
                team_name='team 0'
            ), UserTeamDTO(
                user_id='user2',
                team_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331',
                team_name='team 0'
            ),
            UserTeamDTO(
                user_id='user1',
                team_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332',
                team_name='team 1'
            ),
            UserTeamDTO(
                user_id='user2',
                team_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332',
                team_name='team 1'
            )
        ]
        return user_team_dtos
    @pytest.mark.django_db
    def test_validate_user_is_admin(self, user_not_admin):
        # Arrange
        user_id = "user0"
        expected_output = False
        storage = GetUsersListStorageImplementation()

        # Act
        output = storage.check_is_admin_user(user_id=user_id)

        # Assert
        assert output == expected_output

    @pytest.mark.django_db
    def test_get_users(self, users_company, user_dtos):
        # Arrange
        offset = 0
        limit = 10
        expected_output = user_dtos
        storage = GetUsersListStorageImplementation()


        # Act
        output = storage.get_users_who_are_not_admins()

        assert output == expected_output

    @pytest.mark.django_db
    def test_get_team_details_of_users_bulk(self, users_team, user_team_dtos):
        # Arrange
        user_ids = ['user1', 'user2']
        expected_output = user_team_dtos
        storage = GetUsersListStorageImplementation()

        # Act
        output = storage.get_team_details_of_users_bulk(user_ids=user_ids)

        # Assert
        assert output == expected_output

    @pytest.mark.django_db
    def test_get_role_details_of_users_bulk(
            self, users_role, user_role_dtos):
        # Arrange
        user_ids = ['user1', 'user2']
        expected_output = user_role_dtos
        storage = GetUsersListStorageImplementation()

        # Act
        output = storage.get_role_details_of_users_bulk(user_ids=user_ids)

        # Assert
        assert output == expected_output

    @pytest.mark.django_db
    def test_get_company_details_of_users_bulk(
            self, users_company, users_company_dtos):
        # Arrange
        user_ids = ['user0', 'user1']
        expected_output = users_company_dtos
        storage = GetUsersListStorageImplementation()

        # Act
        output = storage.get_company_details_of_users_bulk(user_ids=user_ids)

        # Assert
        assert output == expected_output
