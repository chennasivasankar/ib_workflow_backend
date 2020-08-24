import pytest


class TestGetTeamIdsAndName:
    @pytest.fixture
    def teams_set_up(self):
        team_ids = [
            "ef6d1fc6-ac3f-4d2d-a983-752c992e8344",
            "ef6d1fc6-ac3f-4d2d-a983-752c992e8345",
            "ef6d1fc6-ac3f-4d2d-a983-752c992e8346"
        ]
        from ib_iam.tests.factories.models import TeamFactory
        TeamFactory.reset_sequence(0)
        return [
            TeamFactory.create(team_id=team_id) for team_id in team_ids
        ]

    @pytest.mark.django_db
    def test_get_team_id_and_name_dtos(self, teams_set_up):
        team_ids = [
            "ef6d1fc6-ac3f-4d2d-a983-752c992e8344",
            "ef6d1fc6-ac3f-4d2d-a983-752c992e8345",
        ]
        from ib_iam.interactors.storage_interfaces.dtos import TeamIdAndNameDTO
        expected_result = [
            TeamIdAndNameDTO(
                team_id=team_object.team_id,
                team_name=team_object.name
            ) for team_object in teams_set_up[:2]
        ]
        from ib_iam.storages.team_storage_implementation import \
            TeamStorageImplementation
        team_storage = TeamStorageImplementation()

        actual_result = team_storage.get_team_id_and_name_dtos(
            team_ids=team_ids)

        assert len(actual_result) == len(expected_result)
        for index, team_id_and_name_dto in enumerate(actual_result):
            assert teams_set_up[index].name == team_id_and_name_dto.team_name
            assert teams_set_up[index].team_id == team_id_and_name_dto.team_id
