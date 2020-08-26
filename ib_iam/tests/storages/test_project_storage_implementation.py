import pytest

from ib_iam.storages.project_storage_implementation import \
    ProjectStorageImplementation
from ib_iam.tests.factories.storage_dtos import ProjectDTOFactory


class TestProjectStorageImplementation:

    @pytest.fixture
    def project_dtos(self):
        project_ids = ["641bfcc5-e1ea-4231-b482-f7f34fb5c7c4",
                       "641bfcc5-e1ea-4231-b482-f7f34fb5c7c5"]
        ProjectDTOFactory.reset_sequence(1)
        project_dtos = [ProjectDTOFactory(project_id=project_id)
                        for project_id in project_ids]
        return [project_dtos, project_ids]

    @pytest.fixture()
    def project_storage(self):
        project_storage = ProjectStorageImplementation()
        return project_storage

    @pytest.mark.django_db
    def test_add_projects_adds_projects_successfully(self, project_dtos):
        # Arrange
        expected_project_ids = project_dtos[1]
        expected_project_dtos = project_dtos[0]

        # Act
        project_storage = ProjectStorageImplementation()
        project_storage.add_projects(project_dtos=expected_project_dtos)

        # Assert
        from ib_iam.models import Project
        actual_project_ids = Project.objects.values_list("project_id",
                                                         flat=True)

        assert list(actual_project_ids) == expected_project_ids

    @pytest.mark.django_db
    def test_get_valid_project_ids_from_given_project_ids_returns_project_ids(
            self):
        from ib_iam.tests.factories.models import ProjectFactory
        expected_project_ids = ["641bfcc5-e1ea-4231-b482-f7f34fb5c7c4",
                                "641bfcc5-e1ea-4231-b482-f7f34fb5c7c5"]
        for project_id in expected_project_ids:
            ProjectFactory.create(project_id=project_id)
        invalid_project_ids = expected_project_ids.copy()
        invalid_project_ids.append("641bfcc5-e1ea-4231-b482-f7f34fb5c7c6")
        project_storage = ProjectStorageImplementation()

        actual_project_ids = project_storage \
            .get_valid_project_ids_from_given_project_ids(
            project_ids=invalid_project_ids)

        assert actual_project_ids == expected_project_ids

    # todo update the below test with new things
    # @pytest.mark.django_db
    # def test_get_project_dtos_returns_project_dtos(self):
    #     from ib_iam.tests.factories.models import ProjectFactory
    #     project_ids = ["641bfcc5-e1ea-4231-b482-f7f34fb5c7c4",
    #                    "641bfcc5-e1ea-4231-b482-f7f34fb5c7c5"]
    #     ProjectFactory.reset_sequence(1)
    #     ProjectDTOFactory.reset_sequence(1)
    #     for project_id in project_ids:
    #         ProjectFactory.create(project_id=project_id)
    #     expected_project_dtos = [ProjectDTOFactory(project_id=project_id)
    #                              for project_id in project_ids]
    #     project_storage = ProjectStorageImplementation()
    #
    #     actual_project_dtos = project_storage.get_project_dtos()
    #
    #     assert actual_project_dtos == expected_project_dtos

    @pytest.mark.django_db
    def test_get_project_dtos_for_given_project_ids(self):
        from ib_iam.tests.factories.models import ProjectFactory
        project_ids = [
            "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4",
            "641bfcc5-e1ea-4231-b482-f7f34fb5c7c5",
            "641bfcc5-e1ea-4231-b482-f7f34fb5c7c6"
        ]
        input_project_ids = [
            "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4",
            "641bfcc5-e1ea-4231-b482-f7f34fb5c7c5"
        ]
        ProjectFactory.reset_sequence(1)
        ProjectDTOFactory.reset_sequence(1)
        for project_id in project_ids:
            ProjectFactory.create(project_id=project_id)
        expected_project_dtos = [ProjectDTOFactory(project_id=project_id)
                                 for project_id in input_project_ids]
        project_storage = ProjectStorageImplementation()

        actual_project_dtos = \
            project_storage.get_project_dtos_for_given_project_ids(
                project_ids=input_project_ids)

        assert actual_project_dtos == expected_project_dtos

    @pytest.mark.django_db
    @pytest.mark.parametrize("team_id_to_create, expected_response",
                             [("641bfcc5-e1ea-4231-b482-f7f34fb5c7c5", True),
                              ("641bfcc5-e1ea-4231-b482-f7f34fb5c7c6", False)])
    def test_is_team_exists_in_project(
            self, team_id_to_create, expected_response):
        from ib_iam.tests.factories.models import \
            ProjectFactory, TeamFactory, ProjectTeamFactory
        project_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        team_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c5"
        ProjectFactory.create(project_id=project_id)
        TeamFactory.create(team_id=team_id_to_create)
        ProjectTeamFactory.create(project_id=project_id,
                                  team_id=team_id_to_create)
        project_storage = ProjectStorageImplementation()

        actual_response = project_storage.is_team_exists_in_project(
            project_id=project_id, team_id=team_id)

        assert actual_response == expected_response

    @pytest.mark.django_db
    @pytest.mark.parametrize("user_id_to_create, expected_response",
                             [("641bfcc5-e1ea-4231-b482-f7f34fb5c7c5", True),
                              ("641bfcc5-e1ea-4231-b482-f7f34fb5c7c6", False)])
    def test_is_user_exists_in_team(
            self, user_id_to_create, expected_response):
        from ib_iam.tests.factories.models import \
            UserDetailsFactory, TeamFactory, UserTeamFactory
        team_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        user_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c5"
        UserDetailsFactory.create(user_id=user_id_to_create)
        TeamFactory.create(team_id=team_id)
        UserTeamFactory.create(team_id=team_id,
                               user_id=user_id_to_create)
        project_storage = ProjectStorageImplementation()

        actual_response = project_storage.is_user_exists_in_team(
            team_id=team_id, user_id=user_id)

        assert actual_response == expected_response

    @pytest.mark.django_db
    def test_get_team_name_returns_team_name(self):
        from ib_iam.tests.factories.models import TeamFactory
        team_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        expected_name = "team1"
        TeamFactory.create(team_id=team_id, name=expected_name)
        project_storage = ProjectStorageImplementation()

        actual_name = project_storage.get_team_name(team_id=team_id)

        assert actual_name == expected_name

    @pytest.mark.django_db
    def test_get_user_role_ids_return_role_ids(
            self, prepare_create_project_with_user_roles):
        # Arrange
        project_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        user_id = "001bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        expected_role_ids = ['ROLE_1', 'ROLE_2']

        project_storage = ProjectStorageImplementation()

        # Act
        response = project_storage.get_user_role_ids(
            user_id=user_id, project_id=project_id
        )

        # Assert
        assert response == expected_role_ids

    @pytest.mark.django_db
    def test_is_user_not_in_a_project_return_false(
            self, project_storage, prepare_create_project_with_user_roles):
        # Arrange
        project_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        user_id = "901bfcc5-e1ea-4231-b482-f7f34fb5c7c4"

        # Act
        response = project_storage.is_user_in_a_project(
            user_id=user_id, project_id=project_id)

        # Assert
        assert response is False

    @pytest.mark.django_db
    def test_is_user_in_a_project_return_true(
            self, project_storage, prepare_create_project_with_user_roles):
        # Arrange
        project_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        user_id = "001bfcc5-e1ea-4231-b482-f7f34fb5c7c4"

        # Act
        response = project_storage.is_user_in_a_project(
            user_id=user_id, project_id=project_id)

        # Assert
        assert response is True

    @pytest.mark.django_db
    def test_is_invalid_project_id_return_false(
            self, project_storage, prepare_create_project_with_user_roles):
        # Arrange
        project_id = "041bfcc5-e1ea-4231-b482-f7f34fb5c7c4"

        # Act
        response = project_storage.is_valid_project_id(project_id=project_id)

        # Assert
        assert response is False

    @pytest.mark.django_db
    def test_is_valid_project_id_return_true(
            self, project_storage, prepare_create_project_with_user_roles):
        # Arrange
        project_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"

        # Act
        response = project_storage.is_valid_project_id(project_id=project_id)

        # Assert
        assert response is True

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
        return project_objects
