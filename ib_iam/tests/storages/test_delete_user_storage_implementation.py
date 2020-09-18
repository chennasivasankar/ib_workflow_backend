import pytest

from ib_iam.models import UserDetails, UserRole, TeamUser


class TestDeleteUSerStorageImplementation:

    @pytest.fixture
    def storage(self):
        from ib_iam.storages.delete_user_storage_implementation import \
            DeleteUserStorageImplementation
        return DeleteUserStorageImplementation()

    @pytest.mark.django_db
    def test_delete_user_from_user_details_db(self, storage):
        from ib_iam.tests.factories.models import UserDetailsFactory
        user_id = "1234"
        is_admin = False
        UserDetailsFactory.create(user_id=user_id, is_admin=is_admin)

        storage.delete_user(user_id=user_id)

        with pytest.raises(UserDetails.DoesNotExist):
            UserDetails.objects.get(user_id=user_id)

    @pytest.mark.django_db
    def test_delete_user_roles_from_user_role_db(self, storage):
        # Arrange
        from ib_iam.tests.factories.models import UserDetailsFactory
        user_id = "1234"
        is_admin = False
        after_delete_total_no_of_object = 0
        UserDetailsFactory.create(user_id=user_id, is_admin=is_admin)
        from ib_iam.tests.factories.models import UserRoleFactory
        from ib_iam.tests.factories.models import ProjectRoleFactory
        for _ in range(4):
            role = ProjectRoleFactory.create()
            UserRoleFactory.create(user_id=user_id, project_role=role)

        # Act
        storage.delete_user_roles(user_id=user_id)

        # Assert
        user_roles_objects_count = UserRole.objects.filter(
            user_id=user_id
        ).count()
        assert user_roles_objects_count == after_delete_total_no_of_object

    @pytest.mark.django_db
    def test_delete_user_teams_from_user_team_db(self, storage):
        # Arrange
        from ib_iam.tests.factories.models import UserDetailsFactory
        user_id = "1234"
        is_admin = False
        after_delete_total_no_of_object = 0
        UserDetailsFactory.create(user_id=user_id, is_admin=is_admin)
        from ib_iam.tests.factories.models import TeamUserFactory
        from ib_iam.tests.factories.models import TeamFactory
        for _ in range(4):
            team = TeamFactory.create()
            TeamUserFactory.create(user_id=user_id, team=team)

        # Act
        storage.delete_user_teams(user_id=user_id)

        # Assert
        team_users_objects_count = TeamUser.objects.filter(
            user_id=user_id
        ).count()
        assert team_users_objects_count == after_delete_total_no_of_object

    @pytest.mark.django_db
    def test_get_user_details_from_user_detail_db_given_valid_user_id(
            self, storage
    ):
        # Arrange
        from ib_iam.tests.factories.models import UserDetailsFactory
        user_id = "1234"
        from ib_iam.tests.factories.models import CompanyFactory
        company = CompanyFactory.create()
        is_admin = False
        UserDetailsFactory.create(user_id=user_id, is_admin=is_admin,
                                  company=company)
        # Act
        user_dto = storage.get_user_details(user_id=user_id)

        # Assert
        assert user_dto.user_id == user_id
        assert user_dto.is_admin == is_admin

    @pytest.mark.django_db
    def test_get_user_details_from_user_detail_db_given_invalid_user_id_then_raise_exception(
            self, storage
    ):
        # Arrange
        user_id = "1234"

        # Assert
        from ib_iam.exceptions.custom_exceptions import UserNotFound
        with pytest.raises(UserNotFound):
            storage.get_user_details(user_id=user_id)
