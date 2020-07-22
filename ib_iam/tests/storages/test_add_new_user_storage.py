import pytest

from ib_iam.storages.storage_implementation import StorageImplementation


@pytest.fixture()
def companies():
    from ib_iam.tests.factories.models import CompanyFactory
    company_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                   "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
    companies = [CompanyFactory.create(company_id=id) for id in company_ids]
    return companies


@pytest.fixture()
def teams():
    from ib_iam.tests.factories.models import TeamFactory
    team_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
    teams = [TeamFactory.create(team_id=id) for id in team_ids]
    return teams


@pytest.fixture()
def roles():
    role_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
    from ib_iam.tests.factories.models import RoleFactory
    roles = [RoleFactory.create(id=role_id) for role_id in role_ids]
    return roles


class TestAddNewUserStorage:
    @pytest.mark.django_db
    def test_add_new_user(self, companies, roles, teams):
        # Arrange
        user_id = "user_1"
        is_admin = True
        team_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                    "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
        role_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
        company_id = 'ef6d1fc6-ac3f-4d2d-a983-752c992e8331'
        storage = StorageImplementation()

        # Act
        storage.add_new_user(
            user_id=user_id, is_admin=is_admin,
            company_id=company_id, role_ids=role_ids, team_ids=team_ids)

        # Assert
        from ib_iam.models import UserDetails
        user = UserDetails.objects.get(user_id=user_id)
        assert str(user.company_id) == company_id

    @pytest.mark.django_db
    def test_validate_role_ids(self, roles):
        # Arrange
        storage = StorageImplementation()
        role_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8000",
                    "ef6d1fc6-ac3f-4d2d-a983-752c992e8000"]
        expected_output = False

        # Act
        output = storage.validate_role_ids(role_ids=role_ids)

        # Assert
        assert output == expected_output

    @pytest.mark.django_db
    def test_validate_teams(self, teams):
        # Arrange
        storage = StorageImplementation()
        team_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8333",
                    "ef6d1fc6-ac3f-4d2d-a983-752c992e8344"]
        expected_output = False

        # Act
        output = storage.validate_teams(team_ids=team_ids)

        # Assert
        assert output == expected_output

    @pytest.mark.django_db
    def test_validate_company(self, companies):
        # Arrange
        storage = StorageImplementation()
        comapany_id = "ef6d1fc6-ac3f-4d2d-a983-752c992e8333"
        expected_output = False

        # Act
        output = storage.validate_company(company_id=comapany_id)

        # Assert
        assert output == expected_output
