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
