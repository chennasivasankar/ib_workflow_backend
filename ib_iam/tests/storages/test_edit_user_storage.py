import pytest

from ib_iam.storages.user_storage_implementation import UserStorageImplementation
from ib_iam.tests.factories.models \
    import CompanyFactory, TeamFactory, RoleFactory, UserDetailsFactory, TeamUserFactory, UserRoleFactory


@pytest.fixture()
def model_reset_sequence():
    from ib_iam.tests.common_fixtures.reset_fixture \
        import reset_sequence_for_model_factories
    reset_sequence_for_model_factories()


@pytest.fixture()
def user_companies():
    company_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                   "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
    companies = [CompanyFactory.create(company_id=company_id)
                 for company_id in company_ids]
    UserDetailsFactory.create(user_id="ef6d1fc6-ac3f-4d2d-a983-752c992e8444",
                              company=companies[0])
    return companies


@pytest.fixture()
def user_teams():
    team_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
    teams = [TeamFactory.create(team_id=team_id)
             for team_id in team_ids]
    TeamUserFactory.create(user_id="ef6d1fc6-ac3f-4d2d-a983-752c992e8444",
                           team=teams[0])


@pytest.fixture()
def teams():
    team_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
    teams = [TeamFactory.create(team_id=team_id)
             for team_id in team_ids]
    return teams


@pytest.fixture()
def user_roles():
    role_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
    roles = [RoleFactory.create(id=role_id) for role_id in role_ids]
    UserRoleFactory.create(user_id="ef6d1fc6-ac3f-4d2d-a983-752c992e8444",
                           role=roles[0])


@pytest.fixture()
def roles():
    role_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
    roles = [RoleFactory.create(id=role_id) for role_id in role_ids]
    return roles


class TestEditUserStorage:
    @pytest.mark.django_db
    def test_add_company_to_user_adds_company_with_given_details(
            self, model_reset_sequence, user_companies):
        # Arrange
        user_id = "ef6d1fc6-ac3f-4d2d-a983-752c992e8444"
        is_admin = True
        name = "test_name"
        company_id = 'ef6d1fc6-ac3f-4d2d-a983-752c992e8331'
        storage = UserStorageImplementation()

        # Act
        storage.update_user_details(
            user_id=user_id, company_id=company_id, name=name)

        # Assert
        from ib_iam.models import UserDetails
        user = UserDetails.objects.get(user_id=user_id)
        assert str(user.company_id) == company_id

    @pytest.mark.django_db
    def test_add_roles_to_user_adds_roles_with_given_details(
            self, model_reset_sequence, roles):
        # Arrange
        user_id = "ef6d1fc6-ac3f-4d2d-a983-752c992e8444"
        role_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                    "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
        storage = UserStorageImplementation()

        # Act
        storage.add_roles_to_the_user(
            user_id=user_id, role_ids=role_ids)

        # Assert
        from ib_iam.models import UserRole
        user_objs = UserRole.objects.filter(user_id=user_id)
        assert len(user_objs) == len(role_ids)
        assert str(user_objs[0].role_id) == role_ids[0]

    @pytest.mark.django_db
    def test_add_user_to_teams_adds_to_team_with_given_details(
            self, model_reset_sequence, teams):
        # Arrange
        user_id = "ef6d1fc6-ac3f-4d2d-a983-752c992e8444"
        team_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                    "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
        storage = UserStorageImplementation()

        # Act
        storage.add_user_to_the_teams(
            user_id=user_id, team_ids=team_ids)

        # Assert
        from ib_iam.models import TeamUser
        user_objs = TeamUser.objects.filter(user_id=user_id)
        assert len(user_objs) == len(team_ids)
        assert str(user_objs[0].team_id) == team_ids[0]

    @pytest.mark.django_db
    def test_unassign_roles_for_user_removes_roles(
            self, model_reset_sequence, user_roles):
        # Arrange
        user_id = "ef6d1fc6-ac3f-4d2d-a983-752c992e8444"
        storage = UserStorageImplementation()

        # Act
        storage.remove_roles_for_user(user_id=user_id)

        # Assert
        from ib_iam.models import UserRole
        user_objs = UserRole.objects.filter(user_id=user_id)
        assert len(user_objs) == 0

    @pytest.mark.django_db
    def test_unassign_teams_for_user_removes_teams(
            self, model_reset_sequence, user_teams):
        # Arrange
        user_id = "ef6d1fc6-ac3f-4d2d-a983-752c992e8444"
        storage = UserStorageImplementation()

        # Act
        storage.remove_teams_for_user(user_id=user_id)

        # Assert
        from ib_iam.models import TeamUser
        user_objs = TeamUser.objects.filter(user_id=user_id)
        assert len(user_objs) == 0

    @pytest.mark.django_db
    def test_is_user_exist_returns_false_when_user_did_not_exist(self):
        # Arrange
        user_id = "ef6d1fc6-ac3f-4d2d-a983-752c992e8444"
        storage = UserStorageImplementation()

        # Act
        is_exist = storage.is_user_exist(user_id=user_id)

        # Assert
        assert is_exist is False
