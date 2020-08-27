import pytest


class TestValidateUsersForProject:

    @pytest.fixture()
    def user_storage(self):
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        storage = UserStorageImplementation()
        return storage

    @pytest.mark.django_db
    def test_with_invalid_user_ids_for_project(
            self, user_storage, create_project_teams, create_user_teams
    ):
        # Arrange
        user_ids = [
            "40be920b-7b4c-49e7-8adb-41a0c18da848",
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "77be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        invalid_user_ids = [
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "77be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        project_id = "project_1"

        # Assert
        from ib_iam.exceptions.custom_exceptions import InvalidUserIdsForProject
        with pytest.raises(InvalidUserIdsForProject) as err:
            user_storage.validate_users_for_project(
                user_ids=user_ids, project_id=project_id
            )
        assert err.value.user_ids == invalid_user_ids

    @pytest.mark.django_db
    def test_with_valid_user_ids_did_not_raise_exception(
            self, user_storage, create_project_teams, create_user_teams
    ):
        user_ids = [
            "40be920b-7b4c-49e7-8adb-41a0c18da848",
            "50be920b-7b4c-49e7-8adb-41a0c18da848",
            "60be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        project_id = "project_1"

        # Assert
        user_storage.validate_users_for_project(
            user_ids=user_ids, project_id=project_id
        )

    @pytest.fixture()
    def create_project(self):
        project_id = "project_1"
        from ib_iam.tests.factories.models import ProjectFactory
        ProjectFactory.reset_sequence(1)
        project_object = ProjectFactory(project_id=project_id)
        return project_object

    @pytest.fixture()
    def create_teams(self):
        from ib_iam.tests.factories.models import TeamFactory
        team1_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        team2_id = "90ae920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "21be920b-7b4c-49e7-8adb-41a0c18da848"
        team_objects = [
            TeamFactory(
                team_id=team1_id,
                name="name",
                description="description",
                created_by=user_id
            ),
            TeamFactory(
                team_id=team2_id,
                name="Tech Team",
                description="description",
                created_by=user_id
            )
        ]
        return team_objects

    @pytest.fixture()
    def create_project_teams(self, create_teams, create_project):
        project_object = create_project
        team_objects = create_teams
        from ib_iam.models import ProjectTeam
        # TODO:  user factory for project team
        project_teams = [
            ProjectTeam(
                project=project_object,
                team_id=team_objects[0].team_id
            ),
            ProjectTeam(
                project=project_object,
                team_id=team_objects[1].team_id
            )
        ]
        ProjectTeam.objects.bulk_create(project_teams)
        return project_teams

    @pytest.fixture()
    def create_user_teams(self, create_teams):
        team_objects = create_teams
        user_ids = [
            "40be920b-7b4c-49e7-8adb-41a0c18da848",
            "50be920b-7b4c-49e7-8adb-41a0c18da848",
            "60be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_iam.tests.factories.models import UserTeamFactory
        user_team_objects = [
            UserTeamFactory(
                user_id=user_id,
                team=team_objects[0]
            )
            for user_id in user_ids
        ]
        return user_team_objects
