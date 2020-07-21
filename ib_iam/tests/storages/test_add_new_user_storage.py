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
    roles = [RoleFactory.create(id=id) for id in role_ids]
    return roles


class TestAddNewUserStorage:
    @pytest.mark.django_db
    def test_add_new_user(self, companies, roles, teams):
        # Arrange
        user_id = "user_1"
        is_admin = True
        name = "user"
        email = "user@email.com"
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
