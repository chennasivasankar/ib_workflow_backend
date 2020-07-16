import uuid
from unittest.mock import patch

import pytest

from ib_iam.storages.storage_implementation import StorageImplementation

from ib_iam.tests.common_fixtures.storages import \
    user_not_admin, users_company, users_team, users_role


class TestGetUsers:

    @pytest.mark.django_db
    def test_validate_user_is_admin(self, user_not_admin):
        # Arrange
        user_id = "user0"

        print(user_not_admin)
        expected_output = False
        storage = StorageImplementation()

        # Act
        output = storage.validate_user_is_admin(user_id=user_id)

        # Assert
        assert output == expected_output

    @pytest.mark.django_db
    def test_get_users(self, users_company):
        # Arrange
        offset = 0
        limit = 10
        storage = StorageImplementation()
        from ib_iam.interactors.storage_interfaces.dtos import UserDTO
        expected_output = [
            UserDTO(user_id='user0', is_admin=False, company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331'),
            UserDTO(user_id='user1', is_admin=False, company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331'),
            UserDTO(user_id='user2', is_admin=False, company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331'),
            UserDTO(user_id='user3', is_admin=False, company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332'),
            UserDTO(user_id='user4', is_admin=False, company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332'),
            UserDTO(user_id='user5', is_admin=False, company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332')]

        # Act
        output = storage.get_users_who_are_not_admins(offset=offset, limit=limit)

        assert output == expected_output

    @pytest.mark.django_db
    def test_get_team_details_of_users_bulk(self, users_team):
        # Arrange
        user_ids = ['user1', 'user2']
        from ib_iam.interactors.storage_interfaces.dtos import UserTeamDTO
        expected_output = [
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

        storage = StorageImplementation()

        # Act
        output = storage.get_team_details_of_users_bulk(user_ids=user_ids)

        # Assert
        assert output == expected_output

    @pytest.mark.django_db
    def test_get_role_details_of_users_bulk(self, users_role):
        # Arrange
        user_ids = ['user1', 'user2']
        from ib_iam.interactors.storage_interfaces.dtos import UserRoleDTO
        expected_output = [
            UserRoleDTO(
                user_id='user1',
                role_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331',
                role_name='role 0',
                role_description='payment_description0'
            ),
            UserRoleDTO(
                user_id='user2',
                role_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331',
                role_name='role 0',
                role_description='payment_description0'
            ), UserRoleDTO(
                user_id='user1',
                role_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332',
                role_name='role 1',
                role_description='payment_description1'
            ),
            UserRoleDTO(
                user_id='user2',
                role_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332',
                role_name='role 1',
                role_description='payment_description1'
            )
        ]

        storage = StorageImplementation()

        # Act
        output = storage.get_role_details_of_users_bulk(user_ids=user_ids)

        # Assert
        assert output == expected_output

    @pytest.mark.django_db
    def test_get_company_details_of_users_bulk(self, users_company):
        # Arrange
        user_ids = ['user0', 'user1']
        from ib_iam.interactors.storage_interfaces.dtos import UserCompanyDTO
        expected_output = [
            UserCompanyDTO(
                user_id='user0',
                company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331',
                company_name='company 3'
            ),
            UserCompanyDTO(
                user_id='user1',
                company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331',
                company_name='company 3'
            )
        ]
    
        storage = StorageImplementation()

        # Act
        output = storage.get_company_details_of_users_bulk(user_ids=user_ids)

        # Assert
        assert output == expected_output
