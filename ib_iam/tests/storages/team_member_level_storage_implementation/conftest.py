import pytest


@pytest.fixture()
def create_team():
    from ib_iam.tests.factories.models import TeamFactory
    team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
    user_id = "21be920b-7b4c-49e7-8adb-41a0c18da848"
    team_object = TeamFactory(
        team_id=team_id,
        name="name",
        description="description",
        created_by=user_id
    )
    return team_object


@pytest.fixture()
def create_teams():
    from ib_iam.tests.factories.models import TeamFactory
    team1_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
    team2_id = "00ae920b-7b4c-49e7-8adb-41a0c18da848"
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
def create_user_teams(create_teams):
    team_objects = create_teams
    from ib_iam.tests.factories.models import TeamMemberLevelFactory
    team_member_level_object = TeamMemberLevelFactory(
        id="00be920b-7b4c-49e7-8adb-41a0c18da848",
        team=team_objects[0],
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
            team=team_objects[0],
            team_member_level=team_member_level_object
        )
        for user_id in user_ids
    ]
    for user_id in user_ids:
        TeamUserFactory(
            user_id=user_id,
            team=team_objects[1],
            team_member_level=team_member_level_object
        )

    team_member_level_object = TeamMemberLevelFactory(
        id="10be920b-7b4c-49e7-8adb-41a0c18da848",
        team=team_objects[0],
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
            team=team_objects[0],
            team_member_level=team_member_level_object
        )
        for user_id in user_ids
    ]
    for user_id in user_ids:
        TeamUserFactory(
            user_id=user_id,
            team=team_objects[1],
            team_member_level=team_member_level_object
        )

    return user_team_objects_of_level_one
