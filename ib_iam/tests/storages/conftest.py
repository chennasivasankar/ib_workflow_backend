from ib_iam.tests.factories.models import UserFactory, TeamFactory, TeamMemberFactory
import pytest

admin1_id = "155f3fa1-e4eb-4bfa-89e7-ca80edd23a6e"
team1_id = "f2c02d98-f311-4ab2-8673-3daa00757002"
team2_id = "aa66c40f-6d93-484a-b418-984716514c7b"
team3_id = "c982032b-53a7-4dfa-a627-4701a5230765"
member1_id = '2bdb417e-4632-419a-8ddd-085ea272c6eb'
member2_id = '548a803c-7b48-47ba-a700-24f2ea0d1280'
member3_id = '4b8fb6eb-fa7d-47c1-8726-cd917901104e'
member4_id = '7ee2c7b4-34c8-4d65-a83a-f87da75db24e'
member5_id = '09b6cf6d-90ea-43ac-b0ee-3cee3c59ce5a'
member6_id = '8bcf545d-4573-4bc2-b037-16c856d37287'


@pytest.fixture()
def create_users():
    UserFactory(id=1, user_id="1", admin=True)
    UserFactory(id=2, user_id="2")


@pytest.fixture()
def create_teams():
    TeamFactory.reset_sequence(1)
    created_by = admin1_id
    t1 = TeamFactory.create(id=1, team_id=team1_id, created_by=created_by)
    t2 = TeamFactory.create(id=2, team_id=team2_id, created_by=created_by)
    t3 = TeamFactory.create(id=3, team_id=team3_id, created_by=created_by)
    return [t1, t2, t3]


@pytest.fixture()
def create_members(create_teams):
    teams = create_teams
    TeamMemberFactory.reset_sequence(1)

    TeamMemberFactory.create(id=1, team=teams[0], member_id=member1_id)
    TeamMemberFactory.create(id=2, team=teams[0], member_id=member2_id)
    TeamMemberFactory.create(id=3, team=teams[0], member_id=member3_id)
    TeamMemberFactory.create(id=4, team=teams[1], member_id=member4_id)
    TeamMemberFactory.create(id=5, team=teams[1], member_id=member1_id)
    TeamMemberFactory.create(id=6, team=teams[2], member_id=member2_id)
    TeamMemberFactory.create(id=7, team=teams[2], member_id=member3_id)
    TeamMemberFactory.create(id=8, team=teams[2], member_id=member4_id)

