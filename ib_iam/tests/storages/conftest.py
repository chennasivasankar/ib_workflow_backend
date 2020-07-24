from ib_iam.tests.factories.models import (
    UserFactory, TeamFactory, TeamMemberFactory
)
import pytest

admin_id = "155f3fa1-e4eb-4bfa-89e7-ca80edd23a6e"
team_ids = [
    "f2c02d98-f311-4ab2-8673-3daa00757002",
    "aa66c40f-6d93-484a-b418-984716514c7b",
    "c982032b-53a7-4dfa-a627-4701a5230765",
]
member_ids = [
    '2bdb417e-4632-419a-8ddd-085ea272c6eb',
    '548a803c-7b48-47ba-a700-24f2ea0d1280',
    '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
    '7ee2c7b4-34c8-4d65-a83a-f87da75db24e',
    '09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a',
    '8bcf545d-4573-4bc2-b037-16c856d37287',
]


@pytest.fixture()
def create_users():
    UserFactory.reset_sequence(1)
    for is_admin_value in [True, False]:
        UserFactory(is_admin=is_admin_value)


@pytest.fixture()
def create_teams():
    TeamFactory.reset_sequence(1)
    team_objects = [
        TeamFactory.create(team_id=team_id, created_by=admin_id)
        for team_id in team_ids
    ]
    return team_objects


@pytest.fixture()
def create_members(create_teams):
    team_objects = create_teams
    TeamMemberFactory.reset_sequence(1)
    team_members = [
        {
            "team_id": team_ids[0],
            "member_ids": [member_ids[0], member_ids[2]]
        },
        {
            "team_id": team_ids[1],
            "member_ids": [member_ids[0], member_ids[2]]
        },
        {
            "team_id": team_ids[2],
            "member_ids": [member_ids[0], member_ids[2]]
        }

    ]
    team_member_objects = [
        TeamMemberFactory.create(team_id=team["team_id"], member_id=member_id)
        for team in team_members for member_id in team["member_ids"]
    ]
    return team_member_objects
