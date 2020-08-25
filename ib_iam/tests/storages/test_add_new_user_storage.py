import pytest

from ib_iam.storages.user_storage_implementation \
    import UserStorageImplementation
from ib_iam.tests.factories.models import CompanyFactory, TeamFactory, ProjectRoleFactory


@pytest.fixture()
def reset_sequence_for_model_factories():
    CompanyFactory.reset_sequence(0)
    ProjectRoleFactory.reset_sequence(0)
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
    roles = [ProjectRoleFactory.create(id=role_id) for role_id in role_ids]
    return roles


class TestAddNewUserStorage:

    @pytest.mark.django_db
    def test_create_user(self, company_id):
        # Arrange
        user_id = "user_1"
        name = "test_name"
        is_admin = True
        company_id = "ef6d1fc6-ac3f-4d2d-a983-752c992e8331"
        storage = UserStorageImplementation()
        CompanyFactory(company_id=company_id)

        # Act
        storage.create_user(
            company_id=company_id, is_admin=is_admin, user_id=user_id,
            name=name
        )

        # Assert
        from ib_iam.models import UserDetails
        user_object = UserDetails.objects.get(user_id=user_id)

        assert str(user_object.company_id) == company_id
        assert user_object.name == name
        assert user_object.user_id == user_id
        assert user_object.is_admin == is_admin

    @pytest.mark.django_db
    def test_create_user(self):
        # Arrange
        user_id = "user_1"
        name = "test_name"
        is_admin = True
        company_id = None
        storage = UserStorageImplementation()
        CompanyFactory(company_id=company_id)

        # Act
        storage.create_user(
            company_id=company_id, is_admin=is_admin, user_id=user_id,
            name=name
        )

        # Assert
        from ib_iam.models import UserDetails
        user_object = UserDetails.objects.get(user_id=user_id)

        assert user_object.company_id == company_id
        assert user_object.name == name
        assert user_object.user_id == user_id
        assert user_object.is_admin == is_admin

    @pytest.mark.django_db
    def test_validate_role_ids_when_invalid_then_returns_false(
            self, reset_sequence_for_model_factories, roles):
        # Arrange
        storage = UserStorageImplementation()
        role_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8000",
                    "ef6d1fc6-ac3f-4d2d-a983-752c992e8000"]
        expected_output = False

        # Act
        output = storage.check_are_valid_role_ids(role_ids=role_ids)

        # Assert
        assert output == expected_output

    @pytest.mark.django_db
    def test_validate_teams_if_invalid_returns_false(
            self, reset_sequence_for_model_factories, teams):
        # Arrange
        storage = UserStorageImplementation()
        team_ids = ["ef6d1fc6-ac3f-4d2d-a983-752c992e8333",
                    "ef6d1fc6-ac3f-4d2d-a983-752c992e8344"]
        expected_output = False

        # Act
        output = storage.check_are_valid_team_ids(team_ids=team_ids)

        # Assert
        assert output == expected_output

    @pytest.mark.django_db
    def test_validate_company_when_invalid_returns_false(
            self, reset_sequence_for_model_factories, companies):
        # Arrange
        storage = UserStorageImplementation()
        comapany_id = "ef6d1fc6-ac3f-4d2d-a983-752c992e8333"
        expected_output = False

        # Act
        output = storage.check_is_exists_company_id(company_id=comapany_id)

        # Assert
        assert output == expected_output
