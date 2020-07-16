import pytest
import uuid
from mock import patch

from ib_iam.exceptions import DuplicateTeamName
from ib_iam.interactors.storage_interfaces.dtos import AddTeamParametersDTO
from ib_iam.models import Team
from ib_iam.storages.team_storage_implementation import TeamStorageImplementation
from ib_iam.tests.storages.conftest import admin1_id, team1_id


@pytest.mark.django_db
class TestAddTeam:

    def test_if_team_name_is_not_unique_raises_duplicate_team_name_exception(
            self, create_teams
    ):
        storage = TeamStorageImplementation()
        user_id = admin1_id
        team_name = "team_name1"
        add_team_params_dto = AddTeamParametersDTO(
            name=team_name, description="desc1"
        )

        with pytest.raises(DuplicateTeamName) as exception:
            storage.add_team(user_id=user_id, add_team_params_dto=add_team_params_dto)

    @patch("uuid.uuid4")
    def test_given_parameters_are_valid_returns_team_id(self, uuid4_mock):
        storage = TeamStorageImplementation()

        user_id = admin1_id
        uuid4_mock.return_value = "f2c02d98-f311-4ab2-8673-3daa00757002"
        team_name = "team_name1"
        team_description = "desc1"
        add_team_params_dto = AddTeamParametersDTO(
            name=team_name, description=team_description
        )
        expected_team_id = team1_id

        actual_team_id = storage.add_team(
            user_id=user_id, add_team_params_dto=add_team_params_dto
        )

        team_object = Team.objects.get(team_id=team1_id)
        assert actual_team_id == expected_team_id
        assert team_object.name == team_name
        assert team_object.description == team_description
