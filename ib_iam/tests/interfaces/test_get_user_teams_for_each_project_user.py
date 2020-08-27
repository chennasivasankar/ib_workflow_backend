import pytest


class TestGetUserTeamsForEachProjectUser:
    @pytest.fixture
    def user_set_up(self):
        user_id = "123"
        from ib_iam.tests.factories.models import UserDetailsFactory
        UserDetailsFactory.reset_sequence(0)
        user_object = UserDetailsFactory.create(user_id=user_id)
        return user_object

    @pytest.fixture
    def project_set_up(self):
        project_id = "FA"
        from ib_iam.tests.factories.models import ProjectFactory
        ProjectFactory.reset_sequence(0)
        project_object = ProjectFactory.create(project_id=project_id)
        return project_object

    @pytest.fixture
    def team_set_up(self):
        team_id = "89d96f4b-c19d-4e69-8eae-e818f3123b09"
        from ib_iam.tests.factories.models import TeamFactory
        TeamFactory.reset_sequence(0)
        team_object = TeamFactory.create(team_id=team_id)
        return team_object

    @pytest.fixture
    def project_team_set_up(self, project_set_up, team_set_up):
        team_id = "89d96f4b-c19d-4e69-8eae-e818f3123b09"
        project_id = "FA"
        from ib_iam.tests.factories.models import ProjectTeamFactory
        ProjectTeamFactory.reset_sequence(0)
        project_team_object = ProjectTeamFactory.create(
            team_id=team_id, project_id=project_id)
        return project_team_object

    @pytest.fixture
    def team_user_set_up(self, team_set_up, user_set_up):
        user_id = "123"
        team_id = "89d96f4b-c19d-4e69-8eae-e818f3123b09"
        from ib_iam.tests.factories.models import UserTeamFactory
        UserTeamFactory.reset_sequence(0)
        team_user_object = UserTeamFactory.create(
            user_id=user_id, team_id=team_id)
        return team_user_object

    @pytest.fixture
    def set_up(
            self, user_set_up, project_set_up, team_set_up,
            project_team_set_up, team_user_set_up
    ):
        return user_set_up, project_set_up, team_set_up, project_team_set_up, \
               team_user_set_up

    @pytest.mark.django_db
    def test_get_user_teams_for_each_project_user_given_valid_details_then_return_response(
            self, set_up):
        user_ids = ["123"]
        project_id = "FA"
        team_id = "89d96f4b-c19d-4e69-8eae-e818f3123b09"
        team_name = "team 0"
        from ib_iam.app_interfaces.dtos import UserTeamsDTO
        from ib_iam.interactors.storage_interfaces.dtos import TeamIdAndNameDTO
        user_teams = [TeamIdAndNameDTO(team_id=team_id, team_name=team_name)]
        expected_result = [UserTeamsDTO(
            user_id=user_ids[0], user_teams=user_teams)]

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        actual_result = service_interface.get_user_teams_for_each_project_user(
            user_ids=user_ids, project_id=project_id)

        assert len(actual_result) == len(expected_result)
        assert actual_result == expected_result

    @pytest.mark.django_db
    def test_get_user_teams_for_each_project_user_given_invalid_user_ids_then_raise_exceptions(
            self, project_set_up):
        user_ids = ["123"]
        project_id = "FA"

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        from ib_iam.exceptions.custom_exceptions import InvalidUserIds
        with pytest.raises(InvalidUserIds) as err:
            service_interface.get_user_teams_for_each_project_user(
                user_ids=user_ids, project_id=project_id)

        assert err.value.user_ids == user_ids

    @pytest.mark.django_db
    def test_get_user_teams_for_each_project_user_given_invalid_project_id_then_raise_exceptions(
            self):
        user_ids = ["123"]
        invalid_project_id = "FA"

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        with pytest.raises(InvalidProjectId):
            service_interface.get_user_teams_for_each_project_user(
                user_ids=user_ids, project_id=invalid_project_id)

    @pytest.mark.django_db
    def test_get_user_teams_for_each_project_user_given_invalid_users_for_given_project_then_raise_exceptions(
            self, project_set_up, user_set_up, team_set_up,
            project_team_set_up):
        invalid_project_user_ids = ["123"]
        project_id = "FA"

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        from ib_iam.interactors.project_interactor import \
            UsersNotExistsForGivenProject
        with pytest.raises(UsersNotExistsForGivenProject) as err:
            service_interface.get_user_teams_for_each_project_user(
                user_ids=invalid_project_user_ids, project_id=project_id)

        assert err.value.user_ids == invalid_project_user_ids