import pytest

from ib_iam.models import UserDetails, UserRole, TeamUser
from ib_iam.storages.delete_user_storage_implementation import \
    DeleteUserStorageImplementation


class TestDeleteUSerStorageImplementation:

    @pytest.mark.django_db
    def test_delete_user_from_user_details_db(self):
        from ib_iam.tests.factories.models import UserDetailsFactory
        user_id = "1234"
        is_admin = False
        UserDetailsFactory.create(user_id=user_id, is_admin=is_admin)
        storage = DeleteUserStorageImplementation()

        storage.delete_user(user_id=user_id)

        with pytest.raises(UserDetails.DoesNotExist):
            UserDetails.objects.get(user_id=user_id)

    @pytest.mark.django_db
    def test_delete_user_roles_from_user_role_db(self):
        from ib_iam.tests.factories.models import UserDetailsFactory
        user_id = "1234"
        is_admin = False
        UserDetailsFactory.create(user_id=user_id, is_admin=is_admin)
        from ib_iam.tests.factories.models import UserRoleFactory
        from ib_iam.tests.factories.models import RoleFactory
        for _ in range(4):
            role = RoleFactory.create()
            UserRoleFactory.create(user_id=user_id, role=role)
        storage = DeleteUserStorageImplementation()

        storage.delete_user_roles(user_id=user_id)

        user_roles = UserRole.objects.filter(user_id=user_id)
        assert len(user_roles) == 0

    @pytest.mark.django_db
    def test_delete_user_teams_from_user_team_db(self):
        from ib_iam.tests.factories.models import UserDetailsFactory
        user_id = "1234"
        is_admin = False
        UserDetailsFactory.create(user_id=user_id, is_admin=is_admin)
        from ib_iam.tests.factories.models import TeamUserFactory
        from ib_iam.tests.factories.models import TeamFactory
        for _ in range(4):
            team = TeamFactory.create()
            TeamUserFactory.create(user_id=user_id, team=team)
        storage = DeleteUserStorageImplementation()

        storage.delete_user_teams(user_id=user_id)

        user_roles = TeamUser.objects.filter(user_id=user_id)
        assert len(user_roles) == 0

    @pytest.mark.django_db
    def test_get_user_details_from_user_detail_db_given_valid_user_id(self):
        from ib_iam.tests.factories.models import UserDetailsFactory
        user_id = "1234"
        from ib_iam.tests.factories.models import CompanyFactory
        company = CompanyFactory.create()
        is_admin = False
        UserDetailsFactory.create(user_id=user_id, is_admin=is_admin,
                                  company=company)
        storage = DeleteUserStorageImplementation()

        user_dto = storage.get_user_details(user_id=user_id)

        assert user_dto.user_id == user_id
        assert user_dto.is_admin == is_admin

    @pytest.mark.django_db
    def test_get_user_details_from_user_detail_db_given_invalid_user_id_then_raise_exception(
            self):
        user_id = "1234"

        storage = DeleteUserStorageImplementation()

        from ib_iam.exceptions.custom_exceptions import UserNotFound
        with pytest.raises(UserNotFound):
            storage.get_user_details(user_id=user_id)
