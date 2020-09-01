import pytest


class TestGetUserRoleIdsBasedOnProject:

    @pytest.fixture()
    def service_interface(self):
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()
        return service_interface

    @pytest.mark.django_db
    def test_with_invalid_project_id_raise_exception(self, service_interface):
        # Arrange
        project_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        user_id = "aca1a0c1-b9ef-4e59-b415-60a28ef17b10"

        # Assert
        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        with pytest.raises(InvalidProjectId):
            service_interface.get_user_role_ids_based_on_project(
                user_id=user_id, project_id=project_id
            )

    @pytest.mark.django_db
    def test_with_user_is_not_a_member_of_project_raise_exception(
            self, service_interface, prepare_create_project_with_user_roles):
        # Arrange
        project_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        user_id = "901bfcc5-e1ea-4231-b482-f7f34fb5c7c4"

        # Assert
        from ib_iam.interactors.project_role_interactor import \
            UserNotAMemberOfAProject
        with pytest.raises(UserNotAMemberOfAProject):
            service_interface.get_user_role_ids_based_on_project(
                user_id=user_id, project_id=project_id
            )

    @pytest.mark.django_db
    def test_with_valid_details_return_response(
            self, service_interface, prepare_create_project_with_user_roles):
        # Arrange
        project_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        user_id = "001bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        expected_role_ids = ['ROLE_1', 'ROLE_2']

        # Assert
        response = service_interface.get_user_role_ids_based_on_project(
            user_id=user_id, project_id=project_id
        )

        # Assert
        assert response == expected_role_ids

    @pytest.fixture()
    def prepare_create_project_with_user_roles(self):
        project_ids = [
            "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4",
            "741bfcc5-e1ea-4231-b482-f7f34fb5c7c5",
            "841bfcc5-e1ea-4231-b482-f7f34fb5c7c6"
        ]
        from ib_iam.tests.factories.models import ProjectFactory
        ProjectFactory.reset_sequence(1)
        from ib_iam.tests.factories.models import ProjectRoleFactory
        ProjectRoleFactory.reset_sequence(1)
        project_objects = [
            ProjectFactory.create(project_id=project_id)
            for project_id in project_ids
        ]
        project_role_objects = [
            ProjectRoleFactory(
                project=project_objects[0]
            ),
            ProjectRoleFactory(
                project=project_objects[0]
            ),
            ProjectRoleFactory(
                project=project_objects[0]
            )
        ]
        user_ids = [
            "001bfcc5-e1ea-4231-b482-f7f34fb5c7c4",
            "011bfcc5-e1ea-4231-b482-f7f34fb5c7c5"
        ]
        team_id = "001bfcc5-e1ea-4231-b482-f7f34fb5c7c8"
        from ib_iam.tests.factories.models import TeamFactory
        TeamFactory.reset_sequence(0)
        team_object = TeamFactory.create(team_id=team_id)
        from ib_iam.tests.factories.models import ProjectTeamFactory
        ProjectTeamFactory.reset_sequence(0)
        project_team_object = ProjectTeamFactory.create(
            team_id=team_id, project_id=project_ids[0])
        from ib_iam.tests.factories.models import TeamUserFactory
        TeamUserFactory.reset_sequence(0)
        team_user_object = TeamUserFactory.create(
            user_id=user_ids[0], team=team_object)
        from ib_iam.tests.factories.models import UserRoleFactory
        UserRoleFactory(
            user_id=user_ids[0],
            project_role=project_role_objects[0]
        )
        UserRoleFactory(
            user_id=user_ids[0],
            project_role=project_role_objects[1]
        )
        UserRoleFactory(
            user_id=user_ids[1],
            project_role=project_role_objects[2]
        )
        return project_objects, team_object, project_team_object, team_user_object
