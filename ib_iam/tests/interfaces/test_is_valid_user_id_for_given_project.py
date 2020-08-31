import pytest


class TestIsValidUserIdForGivenProject:
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
        from ib_iam.tests.factories.models import TeamUserFactory
        TeamUserFactory.reset_sequence(0)
        team_user_object = TeamUserFactory.create(
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
    def test_is_valid_user_id_for_given_project_then_return_true(self, set_up):
        user_id = "123"
        project_id = "FA"
        expected_result = True

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        actual_result = service_interface.is_valid_user_id_for_given_project(
            user_id=user_id, project_id=project_id)

        assert actual_result == expected_result

    @pytest.mark.django_db
    def test_is_valid_user_id_for_given_project_with_invalid_project_id_then_raise_exception(
            self, user_set_up):
        user_id = "123"
        project_id = "FA"

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        with pytest.raises(InvalidProjectId):
            service_interface.is_valid_user_id_for_given_project(
                user_id=user_id, project_id=project_id)

    @pytest.mark.django_db
    def test_is_valid_user_id_for_given_project_with_invalid_user_id_then_raise_exception(
            self, project_set_up):
        user_id = "123"
        project_id = "FA"

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        from ib_iam.exceptions.custom_exceptions import InvalidUserId
        with pytest.raises(InvalidUserId):
            service_interface.is_valid_user_id_for_given_project(
                user_id=user_id, project_id=project_id)

    @pytest.mark.django_db
    def test_is_valid_user_id_for_given_project_then_return_false_for_not_exists_user_in_given_project(
            self, project_set_up, user_set_up):
        user_id = "123"
        project_id = "FA"
        expected_result = False

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        actual_reseult = service_interface.is_valid_user_id_for_given_project(
            user_id=user_id, project_id=project_id)

        assert actual_reseult == expected_result
