import pytest


class TestGetImmediateSuperiorUserId:
    @pytest.fixture()
    def create_team(self):
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

    @pytest.fixture()
    def service_interface(self):
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()
        return service_interface

    @pytest.mark.django_db
    def test_with_valid_details_return_immediate_superior_user_id(
            self, create_team, service_interface):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        immediate_superior_user_id = "21be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_iam.tests.factories.models import TeamUserFactory
        immediate_superior_user_object = TeamUserFactory(
            team_id=team_id, user_id=immediate_superior_user_id
        )

        TeamUserFactory(
            team_id=team_id, user_id=user_id,
            immediate_superior_team_user=immediate_superior_user_object
        )

        # Act
        response = service_interface.get_immediate_superior_user_id(
            team_id=team_id, user_id=user_id
        )

        # Assert
        assert response == immediate_superior_user_id

    @pytest.mark.django_db
    def test_with_valid_details_return_None(
            self, create_team, service_interface):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "21be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_iam.tests.factories.models import TeamUserFactory
        TeamUserFactory(
            team_id=team_id, user_id=user_id
        )

        # Act
        response = service_interface.get_immediate_superior_user_id(
            team_id=team_id, user_id=user_id
        )

        # Assert
        assert response is None

    @pytest.mark.django_db
    def test_with_invalid_team_id_raise_exception(
            self, service_interface):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "21be920b-7b4c-49e7-8adb-41a0c18da848"

        # Assert
        from ib_iam.exceptions.custom_exceptions import InvalidTeamId
        with pytest.raises(InvalidTeamId):
            service_interface.get_immediate_superior_user_id(
                team_id=team_id, user_id=user_id
            )

    @pytest.mark.django_db
    def test_with_user_not_belong_to_team_raise_exception(
            self, service_interface, create_team
    ):
        # Arrange
        team_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id = "21be920b-7b4c-49e7-8adb-41a0c18da848"

        # Assert
        from ib_iam.exceptions.custom_exceptions import UserNotBelongToTeam
        with pytest.raises(UserNotBelongToTeam):
            service_interface.get_immediate_superior_user_id(
                team_id=team_id, user_id=user_id
            )
