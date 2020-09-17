import pytest

from ib_iam.storages.team_storage_implementation import \
    TeamStorageImplementation
from ib_iam.tests.common_fixtures.adapters.uuid_mock import uuid_mock


@pytest.mark.django_db
class TestAddTeam:

    def test_given_valid_details_return_team_id(self, mocker):
        storage = TeamStorageImplementation()

        user_id = "155f3fa1-e4eb-4bfa-89e7-ca80edd23a6e"
        team_id = "f2c02d98-f311-4ab2-8673-3daa00757002"
        mock = uuid_mock(mocker)
        mock.return_value = team_id
        team_name = "team_name1"
        team_description = "desc1"
        expected_team_id = team_id
        from ib_iam.interactors.storage_interfaces.dtos import \
            TeamNameAndDescriptionDTO
        team_name_and_description_dto = TeamNameAndDescriptionDTO(
            name=team_name, description=team_description)

        actual_team_id = storage.add_team(
            user_id=user_id,
            team_name_and_description_dto=team_name_and_description_dto)

        from ib_iam.models import Team
        team_object = Team.objects.get(team_id=actual_team_id)
        assert actual_team_id == expected_team_id
        assert team_object.name == team_name
        assert team_object.description == team_description
