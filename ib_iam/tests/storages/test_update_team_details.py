import pytest
from ib_iam.storages.team_storage_implementation import \
    TeamStorageImplementation
from ib_iam.models import Team
from ib_iam.interactors.storage_interfaces.dtos import \
    TeamWithUserIdsDTO


@pytest.fixture
def create_team():
    team_id = 'f2c02d98-f311-4ab2-8673-3daa00757002'
    from ib_iam.tests.factories.models import TeamFactory
    team_object = TeamFactory.create(team_id=team_id)
    return team_object


@pytest.mark.django_db
class TestUpdateTeamDetails:
    def test_whether_it_updates_the_team_details(self, create_team):
        team_id = create_team.team_id
        expected_team_name = "new team"
        expected_description = "description"
        expected_logo_url = ""
        storage = TeamStorageImplementation()
        team_with_user_ids_dto = TeamWithUserIdsDTO(
            team_id=team_id,
            name=expected_team_name,
            description=expected_description,
            user_ids=[])

        storage.update_team_details(
            team_with_user_ids_dto=team_with_user_ids_dto)

        team_object = Team.objects.get(team_id=team_id)
        assert team_object.name == expected_team_name
        assert team_object.description == expected_description
