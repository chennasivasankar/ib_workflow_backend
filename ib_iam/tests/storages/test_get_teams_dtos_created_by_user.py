import pytest
from ib_iam.storages.team_storage_implementation import TeamStorageImplementation
from ib_iam.interactors.storage_interfaces.team_storage_interface import PaginationDTO


@pytest.mark.django_db
class TestGetTeamsDtosCreatedByUser:

    def test_given_admin_returns_list_of_teams(
            self, snapshot, create_teams
    ):
        sql_storage = TeamStorageImplementation()
        pagination_dto = PaginationDTO(limit=5, offset=0)

        result = sql_storage.get_team_dtos_created_by_user(
            user_id="155f3fa1-e4eb-4bfa-89e7-ca80edd23a6e",
            pagination_dto=pagination_dto
        )

        snapshot.assert_match(result, "result")
