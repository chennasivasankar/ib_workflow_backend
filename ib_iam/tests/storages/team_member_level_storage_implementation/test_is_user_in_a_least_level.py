import pytest


class TestIsUserInaLeastLevel:

    @pytest.fixture()
    def storage(self):
        from ib_iam.storages.team_member_level_storage_implementation import \
            TeamMemberLevelStorageImplementation
        storage = TeamMemberLevelStorageImplementation()
        return storage

    @pytest.fixture
    def create_team(self):
        team_id = '31be920b-7b4c-49e7-8adb-41a0c18da848'
        from ib_iam.tests.factories.models import TeamFactory
        team_object = TeamFactory.create(team_id=team_id)
        return team_object

    @pytest.fixture()
    def create_user_team(self, create_team):
        team_object = create_team
        from ib_iam.tests.factories.models import TeamMemberLevelFactory
        team_member_level_object = TeamMemberLevelFactory(
            id="00be920b-7b4c-49e7-8adb-41a0c18da848",
            team=team_object,
            level_name="SDL",
            level_hierarchy=1
        )
        user_ids = [
            "10be920b-7b4c-49e7-8adb-41a0c18da848",
            "20be920b-7b4c-49e7-8adb-41a0c18da848",
            "30be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_iam.tests.factories.models import TeamUserFactory
        user_team_objects_of_level_one = [
            TeamUserFactory(
                user_id=user_id,
                team=team_object,
                team_member_level=team_member_level_object
            )
            for user_id in user_ids
        ]

        team_member_level_object = TeamMemberLevelFactory(
            id="10be920b-7b4c-49e7-8adb-41a0c18da848",
            team=team_object,
            level_name="Developer",
            level_hierarchy=0
        )
        user_ids = [
            "40be920b-7b4c-49e7-8adb-41a0c18da848",
            "50be920b-7b4c-49e7-8adb-41a0c18da848",
            "60be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_iam.tests.factories.models import TeamUserFactory
        user_team_objects = [
            TeamUserFactory(
                user_id=user_id,
                team=team_object,
                team_member_level=team_member_level_object
            )
            for user_id in user_ids
        ]
        return user_team_objects_of_level_one

    @pytest.fixture()
    def prepare_user_teams_subordinate_members(
            self, create_user_team):
        from ib_iam.models import TeamUser

        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        member_id_with_immediate_superior_team_user_id_list = [{
            'user_id': '10be920b-7b4c-49e7-8adb-41a0c18da848',
            'immediate_superior_team_user_id': None
        }, {
            'user_id': '20be920b-7b4c-49e7-8adb-41a0c18da848',
            'immediate_superior_team_user_id': 1
        }, {
            'user_id': '30be920b-7b4c-49e7-8adb-41a0c18da848',
            'immediate_superior_team_user_id': 1
        }, {
            'user_id': '40be920b-7b4c-49e7-8adb-41a0c18da848',
            'immediate_superior_team_user_id': None
        }, {
            'user_id': '50be920b-7b4c-49e7-8adb-41a0c18da848',
            'immediate_superior_team_user_id': 2
        }, {
            'user_id': '60be920b-7b4c-49e7-8adb-41a0c18da848',
            'immediate_superior_team_user_id': None
        }]
        for member_details_dict in member_id_with_immediate_superior_team_user_id_list:
            TeamUser.objects.filter(
                user_id=member_details_dict["user_id"],
                team_id=team_id
            ).update(
                immediate_superior_team_user_id=member_details_dict[
                    "immediate_superior_team_user_id"]
            )

    @pytest.fixture()
    def create_project_team(self, create_team):
        project_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        team_object = create_team
        from ib_iam.tests.factories.models import ProjectFactory
        ProjectFactory.reset_sequence(0)
        project_object = ProjectFactory.create(project_id=project_id)

        from ib_iam.tests.factories.models import ProjectTeamFactory
        ProjectTeamFactory.reset_sequence(0)
        ProjectTeamFactory.create(team=team_object, project=project_object)

    @pytest.mark.django_db
    def test_is_user_not_in_a_least_level(
            self, prepare_user_teams_subordinate_members, storage,
            create_project_team
    ):
        # Arrange
        project_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        user_id = "10be920b-7b4c-49e7-8adb-41a0c18da848"
        is_user_in_a_least_level = False

        # Act
        response = storage.is_user_in_a_least_level(
            user_id=user_id, project_id=project_id
        )

        # Assert
        assert response == is_user_in_a_least_level

    @pytest.mark.django_db
    def test_is_user_in_a_least_level(
            self, prepare_user_teams_subordinate_members, storage,
            create_project_team
    ):
        # Arrange
        project_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        user_id = "40be920b-7b4c-49e7-8adb-41a0c18da848"
        is_user_in_a_least_level = True

        # Act
        response = storage.is_user_in_a_least_level(
            user_id=user_id, project_id=project_id
        )

        # Assert
        assert response == is_user_in_a_least_level
