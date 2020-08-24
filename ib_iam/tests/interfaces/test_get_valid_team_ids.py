import pytest


class TestGetValidTeamIds:

    @pytest.mark.django_db
    def test_get_valid_team_ids_returns_valid_team_ids(self):
        # Arrange
        team_ids = ["641bfcc5-e1ea-4231-b482-f7f34fb5c7c4",
                    "641bfcc5-e1ea-4231-b482-f7f34fb5c7c5",
                    "641bfcc5-e1ea-4231-b482-f7f34fb5c7c6"]
        expected_team_ids = ["641bfcc5-e1ea-4231-b482-f7f34fb5c7c4",
                             "641bfcc5-e1ea-4231-b482-f7f34fb5c7c5"]
        from ib_iam.tests.factories.models import TeamFactory
        for team_id in expected_team_ids:
            TeamFactory.create(team_id=team_id)

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        # Act
        valid_team_ids = service_interface.get_valid_team_ids(
            team_ids=team_ids)

        # Assert
        assert valid_team_ids == expected_team_ids
