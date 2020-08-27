import pytest


class TestIsValidUserIdForGivenProject:
    @pytest.fixture
    def set_up(self):
        from ib_iam.tests.factories.models import \
            ProjectFactory, TeamFactory, ProjectTeamFactory, TeamUserFactory
        project_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        team_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c5"
        user_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c6"
        project = ProjectFactory.create(project_id=project_id)
        team = TeamFactory.create(team_id=team_id)
        user_team = TeamUserFactory.create(team_id=team_id, user_id=user_id)
        project_team = ProjectTeamFactory.create(
            project_id=project_id,
            team_id=team_id
        )
        return project, team, user_team, project_team

    @pytest.mark.django_db
    def test_check_is_exists_user_id_for_given_project_then_return_true(self,
                                                                        set_up):
        project_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        user_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c6"
        expected_result = True
        from ib_iam.storages.project_storage_implementation import \
            ProjectStorageImplementation
        project_storage = ProjectStorageImplementation()

        actual_result = project_storage.is_user_exist_given_project(
            user_id=user_id, project_id=project_id)

        assert actual_result == expected_result

    @pytest.mark.django_db
    def test_check_is_exists_user_id_for_given_project_then_return_false(self):
        project_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        user_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c6"
        expected_result = False
        from ib_iam.storages.project_storage_implementation import \
            ProjectStorageImplementation
        project_storage = ProjectStorageImplementation()

        actual_result = project_storage.is_user_exist_given_project(
            user_id=user_id, project_id=project_id)

        assert actual_result == expected_result
