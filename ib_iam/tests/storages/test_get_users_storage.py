import pytest

from ib_iam.storages.user_storage_implementation \
    import UserStorageImplementation

from ib_iam.tests.common_fixtures.storages import \
    user_not_admin, users_company, users_team, users_role


class TestGetUsers:
    @pytest.fixture()
    def user_dtos(self):
        from ib_iam.interactors.storage_interfaces.dtos import UserDTO
        user_dtos = [
            UserDTO(user_id='user0', is_admin=False,
                    company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331'),
            UserDTO(user_id='user1', is_admin=False,
                    company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331'),
            UserDTO(user_id='user2', is_admin=False,
                    company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331'),
            UserDTO(user_id='user3', is_admin=False,
                    company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332'),
            UserDTO(user_id='user4', is_admin=False,
                    company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332'),
            UserDTO(user_id='user5', is_admin=False,
                    company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8332')]
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
                role_id='ROLE_0',
                name='role 0',
                description='payment_description0'),
            UserRoleDTO(
                user_id='user2',
                role_id='ROLE_0',
                name='role 0',
                description='payment_description0'),
            UserRoleDTO(
                user_id='user1',
                role_id='ROLE_1',
                name='role 1',
                description='payment_description1'),
            UserRoleDTO(
                user_id='user2',
                role_id='ROLE_1',
                name='role 1',
                description='payment_description1')]
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
    @pytest.mark.parametrize("expected_output, is_admin",
                             [(False, False), (True, True)])
    def test_validate_is_user_admin(self, expected_output, is_admin):
        # Arrange
        user_id = "user0"
        from ib_iam.tests.factories.models import UserDetailsFactory
        UserDetailsFactory.create(user_id=user_id, is_admin=is_admin)
        storage = UserStorageImplementation()

        # Act
        output = storage.is_user_admin(user_id=user_id)

        # Assert
        assert output == expected_output

    @pytest.fixture()
    def prepare_create_users_setup(self):
        company_id = "ef6d1fc6-ac3f-4d2d-a983-752c992e8331"
        from ib_iam.tests.factories.models import CompanyFactory
        company_object = CompanyFactory(
            company_id=company_id,
            name="name", description="description",
            logo_url="www.google.com"
        )
        users = [
            {
                "user_id": "1",
                "name": "sham",
                "company": company_object
            },
            {
                "user_id": "2",
                "name": "harry",
                "company": company_object
            },
            {
                "user_id": "3",
                "name": "noah",
                "company": company_object
            },
            {
                "user_id": "4",
                "name": "ava",
                "company": company_object
            }
        ]
        from ib_iam.tests.factories.models import UserDetailsFactory
        for user in users:
            UserDetailsFactory(
                user_id=user["user_id"], name=user["name"],
                company=user["company"]
            )

    @pytest.mark.django_db
    def test_get_users(self, prepare_create_users_setup):
        # Arrange
        users_list = [{
            'user_id': '1',
            'is_admin': False,
            'company_id': 'ef6d1fc6-ac3f-4d2d-a983-752c992e8331'
        }]
        from ib_iam.tests.factories.storage_dtos import UserDTOFactory
        expected_output = [
            UserDTOFactory(
                user_id=user_dict["user_id"],
                is_admin=user_dict["is_admin"],
                company_id=user_dict["company_id"]
            )
            for user_dict in users_list
        ]
        name_search_query = "s"
        storage = UserStorageImplementation()

        # Act
        output = storage.get_users_who_are_not_admins(
            offset=0, limit=10, name_search_query=name_search_query)
        assert output == expected_output

    @pytest.mark.django_db
    def test_get_users_with_empty_search_query(
            self, prepare_create_users_setup):
        # Arrange
        name_search_query = ""
        users_list = [{
            'user_id': '1',
            'is_admin': False,
            'company_id': 'ef6d1fc6-ac3f-4d2d-a983-752c992e8331'
        }, {
            'user_id': '2',
            'is_admin': False,
            'company_id': 'ef6d1fc6-ac3f-4d2d-a983-752c992e8331'
        }, {
            'user_id': '3',
            'is_admin': False,
            'company_id': 'ef6d1fc6-ac3f-4d2d-a983-752c992e8331'
        }, {
            'user_id': '4',
            'is_admin': False,
            'company_id': 'ef6d1fc6-ac3f-4d2d-a983-752c992e8331'
        }]
        from ib_iam.tests.factories.storage_dtos import UserDTOFactory
        expected_output = [
            UserDTOFactory(
                user_id=user_dict["user_id"],
                is_admin=user_dict["is_admin"],
                company_id=user_dict["company_id"]
            )
            for user_dict in users_list
        ]
        storage = UserStorageImplementation()

        # Act
        output = storage.get_users_who_are_not_admins(
            offset=0, limit=10, name_search_query=name_search_query)
        assert output == expected_output

    @pytest.mark.django_db
    def test_get_users_count_for_query(self, users_company, user_dtos):
        # Arrange
        expected_output = 6
        storage = UserStorageImplementation()

        # Act
        output = storage.get_total_count_of_users_for_query()
        assert output == expected_output

    @pytest.mark.django_db
    def test_get_team_details_of_users_bulk(self, users_team, user_team_dtos):
        # Arrange
        user_ids = ['user1', 'user2']
        expected_output = user_team_dtos
        storage = UserStorageImplementation()

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
        storage = UserStorageImplementation()

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
        storage = UserStorageImplementation()

        # Act
        output = storage.get_company_details_of_users_bulk(user_ids=user_ids)

        # Assert
        assert output == expected_output

    @pytest.mark.django_db
    @pytest.mark.parametrize("given_user_ids, expected_user_ids", [
        (["user1", "user2", "user3"], ["user1", "user2"]),
        (["user_id-3", "user_id-4"], [])
    ])
    def test_given_some_valid_members_it_returns_member_ids(
            self, create_users, given_user_ids, expected_user_ids):
        storage = UserStorageImplementation()

        actual_user_ids = \
            storage.get_valid_user_ids_among_the_given_user_ids(
                user_ids=given_user_ids)

        assert actual_user_ids == expected_user_ids

    @pytest.mark.django_db
    def test_update_user_name(self):
        from ib_iam.tests.factories.models import UserDetailsFactory
        user_id = "6ce31e92-f188-4019-b295-2e5ddc9c7a11"
        UserDetailsFactory(user_id=user_id)
        expected_name = "testusername"
        storage = UserStorageImplementation()

        storage.update_user_name(user_id=user_id, name=expected_name)

        from ib_iam.models import UserDetails
        user_object = UserDetails.objects.get(user_id=user_id)
        assert user_object.name == expected_name

    @pytest.mark.django_db
    def test_get_user_related_team_dtos(self):
        from ib_iam.tests.factories.models import TeamFactory, UserTeamFactory
        from ib_iam.tests.factories.storage_dtos import TeamDTOFactory
        TeamFactory.reset_sequence(1)
        TeamDTOFactory.reset_sequence(1)
        user_id = "6ce31e92-f188-4019-b295-2e5ddc9c7a11"
        team_ids = ["ec0be686-1c8f-4da6-afbe-3553f3e22104",
                    "8c944891-c90f-47b0-beb0-efd167c9e36e"]
        team_objects = [TeamFactory.create(team_id=team_id)
                        for team_id in team_ids]
        for team_object in team_objects:
            UserTeamFactory.create(team=team_object, user_id=user_id)
        expected_team_dtos = [TeamDTOFactory.create(team_id=team_id)
                              for team_id in team_ids]
        storage = UserStorageImplementation()

        actual_team_dtos = storage.get_user_related_team_dtos(user_id=user_id)

        assert actual_team_dtos == expected_team_dtos

    @pytest.mark.django_db
    def test_get_user_related_company_dto_as_user_company_exists_returns_company_dto(self):
        from ib_iam.tests.factories.models import \
            CompanyFactory, UserDetailsFactory
        from ib_iam.tests.factories.storage_dtos import CompanyDTOFactory
        CompanyFactory.reset_sequence(1, force=True)
        CompanyDTOFactory.reset_sequence(1, force=True)
        user_id = "6ce31e92-f188-4019-b295-2e5ddc9c7a11"
        company_id = "ec0be686-1c8f-4da6-afbe-3553f3e22104"
        company_object = CompanyFactory.create(company_id=company_id)
        UserDetailsFactory.create(company=company_object, user_id=user_id)
        from ib_iam.interactors.storage_interfaces.dtos import CompanyDTO
        expected_company_dto = CompanyDTO(company_id=company_id,
                                          name='company 1',
                                          description='description 1',
                                          logo_url='url 1')
        storage = UserStorageImplementation()

        actual_company_dto = storage.get_user_related_company_dto(
            user_id=user_id)

        assert actual_company_dto == expected_company_dto

    @pytest.mark.django_db
    def test_get_user_related_company_dto_as_user_company_not_exists_returns_none(
            self):
        from ib_iam.tests.factories.models import \
            CompanyFactory, UserDetailsFactory
        from ib_iam.tests.factories.storage_dtos import CompanyDTOFactory
        CompanyFactory.reset_sequence(1, force=True)
        CompanyDTOFactory.reset_sequence(1, force=True)
        user_id = "6ce31e92-f188-4019-b295-2e5ddc9c7a11"
        UserDetailsFactory.create(user_id=user_id, company=None)
        expected_response = None
        storage = UserStorageImplementation()

        actual_response = storage.get_user_related_company_dto(
            user_id=user_id)

        assert actual_response == expected_response

    @pytest.mark.django_db
    def test_get_team_user_ids_dtos_returns_team_users_dtos(self):
        storage = UserStorageImplementation()
        from ib_iam.tests.factories.storage_dtos import TeamUserIdsDTOFactory
        team_id = 'f2c02d98-f311-4ab2-8673-3daa00757002'
        user_ids = ['2bdb417e-4632-419a-8ddd-085ea272c6eb',
                    '4b8fb6eb-fa7d-47c1-8726-cd917901104e']
        from ib_iam.tests.factories.models import TeamFactory
        from ib_iam.tests.factories.models import UserTeamFactory
        team_object = TeamFactory.create(team_id=team_id)
        for user_id in user_ids:
            UserTeamFactory.create(team=team_object, user_id=user_id)
        expected_dto = [TeamUserIdsDTOFactory(team_id=team_id,
                                              user_ids=user_ids)]

        actual_dto = storage.get_team_user_ids_dtos(team_ids=[team_id])

        assert actual_dto == expected_dto

    @pytest.mark.django_db
    def test_get_company_employee_ids_dtos_returns_company_employee_ids_dtos(
            self):
        from ib_iam.tests.factories.models import \
            UserDetailsFactory, CompanyFactory
        storage = UserStorageImplementation()
        company_id = 'f2c02d98-f311-4ab2-8673-3daa00757002'
        user_ids = ['2bdb417e-4632-419a-8ddd-085ea272c6eb',
                    '4b8fb6eb-fa7d-47c1-8726-cd917901104e']
        company_object = CompanyFactory.create(company_id=company_id)
        for user_id in user_ids:
            UserDetailsFactory.create(company=company_object, user_id=user_id)
        from ib_iam.tests.factories.storage_dtos import \
            CompanyIdWithEmployeeIdsDTOFactory
        expected_dto = [CompanyIdWithEmployeeIdsDTOFactory(
            company_id=company_id, employee_ids=user_ids)]

        actual_dto = storage.get_company_employee_ids_dtos(
            company_ids=[company_id])

        assert actual_dto == expected_dto


