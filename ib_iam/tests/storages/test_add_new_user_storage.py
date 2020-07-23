import pytest

from ib_iam.storages.add_new_user_storage_implementation \
    import AddNewUserStorageImplementation
from ib_iam.tests.factories.models import CompanyFactory, TeamFactory, RoleFactory


@pytest.fixture()
def reset_sequence_for_model_factories():
    CompanyFactory.reset_sequence(0)
    RoleFactory.reset_sequence(0)
    TeamFactory.reset_sequence(0)


@pytest.fixture()
def companies():
    company_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                   "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
    companies = [CompanyFactory.create(company_id=company_id)
                 for company_id in company_ids]
    return companies


@pytest.fixture()
def teams():
    team_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
    teams = [TeamFactory.create(team_id=team_id)
             for team_id in team_ids]
    return teams


@pytest.fixture()
def roles():
    role_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
    roles = [RoleFactory.create(id=role_id) for role_id in role_ids]
    return roles


class TestAddNewUserStorage:
    @pytest.mark.django_db
    def test_add_new_user_create_new_user_with_given_details(
            self, reset_sequence_for_model_factories, companies, roles, teams):
        # Arrange
        user_id = "user_1"
        is_admin = True
        team_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                    "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
        role_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8331",
                    "ef6d1fc6-ac3f-4d2d-a983-752c992e8332"]
        company_id = 'ef6d1fc6-ac3f-4d2d-a983-752c992e8331'
        storage = AddNewUserStorageImplementation()

        # Act
        storage.add_new_user(
            user_id=user_id, is_admin=is_admin,
            company_id=company_id, role_ids=role_ids, team_ids=team_ids)

        # Assert
        from ib_iam.models import UserDetails
        user = UserDetails.objects.get(user_id=user_id)
        assert str(user.company_id) == company_id

    @pytest.mark.django_db
    def test_validate_role_ids_when_invalid_then_returns_false(
            self, reset_sequence_for_model_factories, roles):
        # Arrange
        storage = AddNewUserStorageImplementation()
        role_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8000",
                    "ef6d1fc6-ac3f-4d2d-a983-752c992e8000"]
        expected_output = False

        # Act
        output = storage.validate_role_ids(role_ids=role_ids)

        # Assert
        assert output == expected_output

    @pytest.mark.django_db
    def test_validate_teams_if_invalid_returns_false(
            self, reset_sequence_for_model_factories, teams):
        # Arrange
        storage = AddNewUserStorageImplementation()
        team_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8333",
                    "ef6d1fc6-ac3f-4d2d-a983-752c992e8344"]
        expected_output = False

        # Act
        output = storage.validate_teams(team_ids=team_ids)

        # Assert
        assert output == expected_output

    @pytest.mark.django_db
    def test_validate_company_when_invalid_returns_false(
            self, reset_sequence_for_model_factories, companies):
        # Arrange
        storage = AddNewUserStorageImplementation()
        comapany_id = "ef6d1fc6-ac3f-4d2d-a983-752c992e8333"
        expected_output = False

        # Act
        output = storage.validate_company(company_id=comapany_id)

        # Assert
        assert output == expected_output
