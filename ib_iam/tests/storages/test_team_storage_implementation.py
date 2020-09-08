import pytest


class TestTeamStorageImplementation:

    @pytest.fixture
    def team_storage(self):
        from ib_iam.storages.team_storage_implementation import (
            TeamStorageImplementation
        )
        return TeamStorageImplementation()

    @pytest.fixture
    def team_set_up(self):
        team_id = "91be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_iam.tests.factories.models import TeamFactory
        TeamFactory.reset_sequence(1)
        team_object = TeamFactory.create(team_id=team_id)
        return team_id, team_object

    @pytest.fixture
    def team_dtos_set_up(self, team_set_up):
        team_id, _ = team_set_up
        from ib_iam.tests.factories.storage_dtos import TeamDTOFactory
        TeamDTOFactory.reset_sequence(1)
        team_dtos = [TeamDTOFactory(team_id=team_id)]
        return team_dtos

    @pytest.mark.django_db
    def test_get_team_dtos(self, team_storage, team_set_up, team_dtos_set_up):
        # Arrange
        expected_result = team_dtos_set_up
        team_id, _ = team_set_up

        # Act
        actual_result = team_storage.get_team_dtos(team_ids=[team_id])

        # Asserts
        assert actual_result == expected_result

    @pytest.fixture
    def setup_team_user_dtos(self):
        from ib_iam.tests.factories.models import TeamFactory, TeamUserFactory
        TeamFactory.reset_sequence(1)
        team_ids = [
            "91be920b-7b4c-49e7-8adb-41a0c18da848",
            "91be920b-7b4c-49e7-8adb-41a0c18da849"
        ]
        team_objects = [
            TeamFactory.create(team_id=team_id) for team_id in team_ids
        ]
        user_ids = [
            "81be920b-7b4c-49e7-8adb-41a0c18da841",
            "81be920b-7b4c-49e7-8adb-41a0c18da842",
            "81be920b-7b4c-49e7-8adb-41a0c18da843"
        ]
        team_users = [
            {"team": team_objects[0], "user_id": user_ids[0]},
            {"team": team_objects[0], "user_id": user_ids[1]},
            {"team": team_objects[1], "user_id": user_ids[2]}
        ]
        _ = [
            TeamUserFactory.create(
                team=team_user["team"],
                user_id=team_user["user_id"]
            ) for team_user in team_users
        ]
        return {"team_ids": team_ids, "user_ids": user_ids}

    @pytest.mark.django_db
    def test_get_team_user_dtos(self, team_storage, setup_team_user_dtos):
        # Arrange
        from ib_iam.interactors.storage_interfaces.dtos import (
            TeamWithUserIdDTO
        )
        user_ids = setup_team_user_dtos["user_ids"]
        team_ids = setup_team_user_dtos["team_ids"]
        expected_user_team_dtos = [
            TeamWithUserIdDTO(
                user_id=user_ids[0], team_id=team_ids[0],
                team_name='team 1'
            ),
            TeamWithUserIdDTO(
                user_id=user_ids[1], team_id=team_ids[0],
                team_name='team 1'
            ),
            TeamWithUserIdDTO(
                user_id=user_ids[2], team_id=team_ids[1],
                team_name='team 2'
            )
        ]

        # Act
        actual_user_team_dtos = team_storage.get_team_user_dtos(
            user_ids=user_ids, team_ids=team_ids
        )

        # Assert
        assert actual_user_team_dtos == expected_user_team_dtos
