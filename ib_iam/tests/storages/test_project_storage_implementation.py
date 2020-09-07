import pytest

from ib_iam.storages.project_storage_implementation import \
    ProjectStorageImplementation
from ib_iam.tests.factories.storage_dtos import (
    ProjectDTOFactory, ProjectRoleDTOFactory, ProjectWithoutIdDTOFactory,
    RoleDTOFactory, ProjectWithDisplayIdDTOFactory, PaginationDTOFactory)


class TestProjectStorageImplementation:

    @pytest.fixture
    def project_with_display_id_dtos(self):
        project_ids = ["641bfcc5-e1ea-4231-b482-f7f34fb5c7c4",
                       "641bfcc5-e1ea-4231-b482-f7f34fb5c7c5"]
        ProjectWithDisplayIdDTOFactory.reset_sequence(1)
        project_dtos = [ProjectWithDisplayIdDTOFactory(project_id=project_id)
                        for project_id in project_ids]
        return [project_dtos, project_ids]

    @pytest.fixture()
    def project_storage(self):
        project_storage = ProjectStorageImplementation()
        return project_storage

    @pytest.mark.django_db
    def test_add_projects_adds_projects_successfully(
            self, project_with_display_id_dtos):
        # Arrange
        expected_project_ids = project_with_display_id_dtos[1]
        expected_project_dtos = project_with_display_id_dtos[0]

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
            .get_valid_project_ids(
            project_ids=invalid_project_ids)

        assert actual_project_ids == expected_project_ids

    @pytest.mark.django_db
    def test_get_projects_with_total_count_dto_returns_projects_with_total_count_dto(
            self):
        from ib_iam.tests.factories.models import ProjectFactory
        project_ids_to_create = ["641bfcc5-e1ea-4231-b482-f7f34fb5c7c4",
                                 "641bfcc5-e1ea-4231-b482-f7f34fb5c7c5",
                                 "641bfcc5-e1ea-4231-b482-f7f34fb5c7c6"]
        ProjectFactory.reset_sequence(1)
        for project_id in project_ids_to_create:
            ProjectFactory.create(project_id=project_id)
        ProjectWithDisplayIdDTOFactory.reset_sequence(1)
        project_ids = project_ids_to_create[0:2]
        expected_project_dtos = [ProjectWithDisplayIdDTOFactory(
            project_id=project_id) for project_id in project_ids]
        from ib_iam.interactors.storage_interfaces.dtos import \
            ProjectsWithTotalCountDTO
        pagination_dto = PaginationDTOFactory(limit=2, offset=0)
        expected_projects_with_total_count_dto = ProjectsWithTotalCountDTO(
            projects=expected_project_dtos,
            total_projects_count=3)
        project_storage = ProjectStorageImplementation()

        actual_projects_with_total_count_dto = project_storage \
            .get_projects_with_total_count_dto(pagination_dto=pagination_dto)

        assert actual_projects_with_total_count_dto == \
               expected_projects_with_total_count_dto

    @pytest.mark.django_db
    def test_get_project_team_ids_dtos_returns_project_tem_ids_dtos(self):
        from ib_iam.tests.factories.models import \
            ProjectFactory, TeamFactory, ProjectTeamFactory
        project_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        project_object = ProjectFactory.create(project_id=project_id)
        team_ids = ["641bfcc5-e1ea-4231-b482-f7f34fb5c7c5",
                    "641bfcc5-e1ea-4231-b482-f7f34fb5c7c6"]
        team_objects = [TeamFactory.create(team_id=team_id)
                        for team_id in team_ids]
        for team_object in team_objects:
            ProjectTeamFactory(project=project_object, team=team_object)
        from ib_iam.interactors.storage_interfaces.dtos import \
            ProjectTeamIdsDTO
        expected_project_team_ids_dto = [ProjectTeamIdsDTO(
            project_id=project_id, team_ids=team_ids)]
        project_storage = ProjectStorageImplementation()

        actual_project_team_ids_dto = project_storage \
            .get_project_team_ids_dtos(project_ids=[project_id])

        assert actual_project_team_ids_dto == expected_project_team_ids_dto

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
        project_object = ProjectFactory.create(project_id=project_id)
        team_object = TeamFactory.create(team_id=team_id_to_create)
        ProjectTeamFactory.create(project=project_object,
                                  team=team_object)
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
            UserDetailsFactory, TeamFactory, TeamUserFactory
        team_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        user_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c5"
        UserDetailsFactory.create(user_id=user_id_to_create)
        TeamFactory.create(team_id=team_id)
        TeamUserFactory.create(team_id=team_id,
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
            self, project_storage):
        # Arrange
        project_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        user_id = "001bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        team_id = "111bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        from ib_iam.tests.factories.models import ProjectFactory
        ProjectFactory.reset_sequence(0)
        project_object = ProjectFactory.create(project_id=project_id)
        from ib_iam.tests.factories.models import TeamFactory
        TeamFactory.reset_sequence(0)
        team_object = TeamFactory.create(team_id=team_id)
        from ib_iam.tests.factories.models import ProjectTeamFactory
        ProjectTeamFactory.reset_sequence(0)
        ProjectTeamFactory.create(team=team_object, project=project_object)
        from ib_iam.tests.factories.models import TeamUserFactory
        TeamUserFactory.reset_sequence(0)
        TeamUserFactory.create(user_id=user_id, team=team_object)

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

    @pytest.mark.django_db
    def test_get_all_project_roles_gives_project_role_dtos(self):
        from ib_iam.tests.factories.models import ProjectRoleFactory
        ProjectRoleFactory.reset_sequence(1)
        project_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        project_role_object = ProjectRoleFactory(
            project__project_id=project_id)
        ProjectRoleDTOFactory.reset_sequence(1)
        expected_project_role_dtos = [ProjectRoleDTOFactory(
            project_id=project_role_object.project_id,
            role_id=project_role_object.role_id)]
        project_storage = ProjectStorageImplementation()

        project_role_dtos = project_storage.get_all_project_roles()

        assert project_role_dtos == expected_project_role_dtos

    @pytest.mark.django_db
    def test_add_project_returns_project_id(self):
        ProjectWithoutIdDTOFactory.reset_sequence(1)
        project_without_id_dto = ProjectWithoutIdDTOFactory()
        project_storage = ProjectStorageImplementation()

        project_id = project_storage.add_project(
            project_without_id_dto=project_without_id_dto)

        from ib_iam.models import Project
        project_object = Project.objects.get(project_id=project_id)
        assert project_object.name == project_without_id_dto.name
        assert project_object.display_id == project_without_id_dto.display_id
        assert project_object.description == project_without_id_dto.description
        assert project_object.logo_url == project_without_id_dto.logo_url

    @pytest.mark.django_db
    def test_assign_teams_to_projects_adds_teams_to_project(self):
        project_id = "641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        team_ids = ["641bfcc5-e1ea-4231-b482-f7f34fb5c7c5"]
        from ib_iam.tests.factories.models import ProjectFactory, TeamFactory
        ProjectFactory.reset_sequence(1)
        ProjectFactory(project_id=project_id)
        _ = [TeamFactory(team_id=team_id) for team_id in team_ids]
        project_storage = ProjectStorageImplementation()

        project_storage.assign_teams_to_projects(
            project_id=project_id, team_ids=team_ids)

        from ib_iam.models import ProjectTeam
        project_team_ids = ProjectTeam.objects.filter(project_id=project_id) \
            .values_list("team_id", flat=True)
        project_team_ids = list(map(str, project_team_ids))
        assert team_ids == project_team_ids

    @pytest.mark.django_db
    def test_add_project_roles_adds_project_roles(self):
        from ib_iam.tests.factories.models import ProjectFactory
        from ib_iam.interactors.storage_interfaces.dtos import \
            RoleNameAndDescriptionDTO
        project_id = "project_641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"
        description = None
        role_name = "role1"
        roles = [RoleNameAndDescriptionDTO(name=role_name,
                                           description=description)]
        ProjectFactory.reset_sequence(1)
        ProjectFactory(project_id=project_id)
        project_storage = ProjectStorageImplementation()

        project_storage.add_project_roles(project_id=project_id, roles=roles)

        from ib_iam.models import ProjectRole
        project_roles = ProjectRole.objects.filter(project_id=project_id) \
            .values_list("name", "description")
        assert project_roles[0][0] == role_name
        assert project_roles[0][1] == description

    @pytest.mark.django_db
    def test_update_project_updates_project_details(self):
        project_id = "project_1"
        from ib_iam.tests.factories.models import ProjectFactory
        ProjectFactory.create(project_id=project_id)
        from ib_iam.interactors.storage_interfaces.dtos import ProjectDTO
        project_dto = ProjectDTO(project_id=project_id,
                                 name="project_name1",
                                 logo_url=None,
                                 description=None)
        project_storage = ProjectStorageImplementation()

        project_storage.update_project(project_dto=project_dto)

        from ib_iam.models import Project
        project_object = Project.objects.get(project_id=project_id)
        assert project_object.name == project_dto.name
        assert project_object.description == project_dto.description
        assert project_object.logo_url == project_dto.logo_url

    @pytest.mark.django_db
    def test_delete_teams_from_project_deletes_given_teams(self):
        project_id = "project_1"
        team_ids = ["641bfcc5-e1ea-4231-b482-f7f34fb5c7c4",
                    "641bfcc5-e1ea-4231-b482-f7f34fb5c7c5"]
        team_ids_to_be_removed = ["641bfcc5-e1ea-4231-b482-f7f34fb5c7c5"]
        expected_project_team_ids = ["641bfcc5-e1ea-4231-b482-f7f34fb5c7c4"]
        from ib_iam.tests.factories.models import \
            ProjectFactory, TeamFactory, ProjectTeamFactory
        project_object = ProjectFactory.create(project_id=project_id)
        team_objects = [TeamFactory.create(team_id=team_id)
                        for team_id in team_ids]
        _ = [ProjectTeamFactory(project=project_object, team=team_object)
             for team_object in team_objects]
        project_storage = ProjectStorageImplementation()

        project_storage.remove_teams(
            project_id=project_id, team_ids=team_ids_to_be_removed)

        from ib_iam.models import ProjectTeam
        project_team_ids = ProjectTeam.objects.filter(project_id=project_id) \
            .values_list("team_id", flat=True)
        project_team_ids = list(map(str, project_team_ids))
        assert list(project_team_ids) == expected_project_team_ids

    @pytest.mark.django_db
    def test_get_project_role_ids_gives_project_related_role_ids(self):
        from ib_iam.tests.factories.models import \
            ProjectFactory, ProjectRoleFactory
        project_id = "project_1"
        role_id = "role_1"
        expected_role_ids = ["role_1"]
        project_object = ProjectFactory(project_id=project_id)
        ProjectRoleFactory(role_id=role_id, project=project_object)
        project_storage = ProjectStorageImplementation()

        role_ids = project_storage.get_project_role_ids(project_id=project_id)

        assert role_ids == expected_role_ids

    @pytest.mark.django_db
    def test_update_project_roles_will_update_project_roles(self):
        from ib_iam.tests.factories.models import \
            ProjectFactory, ProjectRoleFactory
        role_id = "role_1"
        project_object = ProjectFactory(project_id="project_1")
        ProjectRoleFactory(role_id=role_id, project=project_object)
        expected_name = "role_name1"
        expected_description = "desc"
        roles = [RoleDTOFactory(role_id=role_id,
                                name=expected_name,
                                description=expected_description)]
        project_storage = ProjectStorageImplementation()

        project_storage.update_project_roles(roles=roles)

        from ib_iam.models import ProjectRole
        role_object = ProjectRole.objects.get(role_id=role_id)
        assert role_object.name == expected_name
        assert role_object.description == expected_description

    @pytest.mark.django_db
    def test_delete_project_roles_deletes_given_roles(self):
        from ib_iam.tests.factories.models import \
            ProjectFactory, ProjectRoleFactory
        role_ids = ["role_1", "role_2"]
        expected_role_ids = ["role_2"]
        project_object = ProjectFactory(project_id="project_1")
        _ = [ProjectRoleFactory(role_id=role_id, project=project_object)
             for role_id in role_ids]
        project_storage = ProjectStorageImplementation()

        project_storage.delete_project_roles(role_ids=["role_1"])

        from ib_iam.models import ProjectRole
        role_ids = ProjectRole.objects.filter(role_id__in=role_ids) \
            .values_list("role_id", flat=True)
        assert list(role_ids) == expected_role_ids

    @pytest.mark.django_db
    def test_get_user_team_ids_dtos_for_given_project(self):
        from ib_iam.tests.factories.models import (
            ProjectFactory, ProjectTeamFactory, TeamFactory, TeamUserFactory)
        project_id = "project_1"
        project_object = ProjectFactory.create(project_id=project_id)
        team_ids = ["31be920b-7b4c-49e7-8adb-41a0c18da848",
                    "31be920b-7b4c-49e7-8adb-41a0c18da849"]
        team_objects = [TeamFactory.create(team_id=team_id)
                        for team_id in team_ids]
        project_team_objects = [
            ProjectTeamFactory.create(project=project_object, team=team_object)
            for team_object in team_objects]
        team_users = [
            {"team": team_objects[0], "user_id": "user1"},
            {"team": team_objects[0], "user_id": "user2"},
            {"team": team_objects[1], "user_id": "user1"}
        ]
        team_user_objects = [TeamUserFactory.create(
            team=team_user["team"], user_id=team_user["user_id"])
            for team_user in team_users]
        from ib_iam.interactors.storage_interfaces.dtos import \
            UserIdAndTeamIdsDTO
        expected_user_id_and_team_ids_dtos = [
            UserIdAndTeamIdsDTO(
                user_id='user1',
                team_ids=['31be920b-7b4c-49e7-8adb-41a0c18da848',
                          '31be920b-7b4c-49e7-8adb-41a0c18da849']),
            UserIdAndTeamIdsDTO(
                user_id='user2',
                team_ids=['31be920b-7b4c-49e7-8adb-41a0c18da848'])
        ]
        project_storage = ProjectStorageImplementation()

        actual_user_id_and_team_ids_dtos = project_storage \
            .get_user_id_with_teams_ids_dtos(project_id=project_id)

        assert actual_user_id_and_team_ids_dtos == \
               expected_user_id_and_team_ids_dtos

    @pytest.mark.django_db
    def test_remove_user_roles_related_to_given_project_and_user(self):
        from ib_iam.tests.factories.models import (
            ProjectFactory, ProjectRoleFactory, UserRoleFactory)
        project_id = "project_1"
        project_object = ProjectFactory.create(project_id=project_id)
        project_role_ids = ["ROLE_1", "ROLE_2"]
        project_role_objects = [
            ProjectRoleFactory.create(project=project_object,
                                      role_id=project_role_id)
            for project_role_id in project_role_ids]
        expected_role_id = "ROLE_3"
        project_role_objects.append(ProjectRoleFactory(
            role_id=expected_role_id))
        user_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_role_objects = [
            UserRoleFactory(user_id=user_id, project_role=project_role_object)
            for project_role_object in project_role_objects
        ]
        user_ids = [user_id]
        project_storage = ProjectStorageImplementation()

        project_storage.remove_user_roles(
            project_id=project_id, user_ids=user_ids)

        from ib_iam.models import UserRole
        user_role_objects = UserRole.objects.filter(user_id__in=user_ids)
        assert len(user_role_objects) == 1
        assert user_role_objects[0].project_role_id == expected_role_id

    @pytest.mark.django_db
    @pytest.mark.parametrize("name, expected_result", [("name 1", "project 1"),
                                                       ("name 2", None)])
    def test_get_project_id_if_project_name_already_exists(
            self, name, expected_result):
        from ib_iam.tests.factories.models import ProjectFactory
        ProjectFactory.reset_sequence(1)
        ProjectFactory.create()
        project_storage = ProjectStorageImplementation()

        actual_result = project_storage \
            .get_project_id(name=name)

        assert actual_result == expected_result

    @pytest.mark.django_db
    @pytest.mark.parametrize(
        "display_id, expected_result",
        [("display_id 1", True), ("display_id 2", False)])
    def test_is_exists_project_display_id(
            self, display_id, expected_result):
        from ib_iam.tests.factories.models import ProjectFactory
        ProjectFactory.reset_sequence(1)
        ProjectFactory.create()
        project_storage = ProjectStorageImplementation()

        actual_result = project_storage.is_exists_display_id(
            display_id=display_id
        )

        assert actual_result == expected_result

    @pytest.mark.django_db
    def test_get_valid_role_names_from_given_role_names_returns_role_names(
            self):
        from ib_iam.tests.factories.models import ProjectRoleFactory
        role_names = ["role 1", "role2"]
        for role_name in role_names:
            ProjectRoleFactory.create(name=role_name)
        expected_role_names = ["role 1"]
        role_names_to_check = ["role 1", "role3"]
        project_storage = ProjectStorageImplementation()

        actual_role_names = project_storage.get_valid_role_names(
            role_names=role_names_to_check
        )

        assert actual_role_names == expected_role_names
