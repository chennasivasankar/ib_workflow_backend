import pytest


class TestAssignUserRolesForGivenProject:

    @pytest.fixture()
    def user_storage(self):
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        user_storage = UserStorageImplementation()
        return user_storage

    @pytest.fixture()
    def prepare_user_id_with_role_ids_dtos(self):
        user_id_with_role_ids_list = [
            {
                "user_id": "31be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_ids": [
                    "ROLE_3", "ROLE_4"
                ]
            },
            {
                "user_id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_ids": []
            },
            {
                "user_id": "77be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_ids": [
                    "ROLE_1"
                ]
            }
        ]
        from ib_iam.tests.factories.interactor_dtos import \
            UserIdWithRoleIdsDTOFactory
        user_id_with_role_ids_dtos = [
            UserIdWithRoleIdsDTOFactory(
                user_id=user_id_with_role_ids_dict["user_id"],
                role_ids=user_id_with_role_ids_dict["role_ids"]
            )
            for user_id_with_role_ids_dict in user_id_with_role_ids_list
        ]
        return user_id_with_role_ids_dtos

    @pytest.mark.django_db
    def test_with_valid_details_create_details(
            self, create_user_roles, prepare_user_id_with_role_ids_dtos,
            user_storage, snapshot
    ):
        # Arrange
        project_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        user_id_with_role_ids_dtos = prepare_user_id_with_role_ids_dtos

        # Act
        user_storage.assign_user_roles_for_given_project(
            user_id_with_role_ids_dtos=user_id_with_role_ids_dtos,
            project_id=project_id
        )

        # Assert
        from ib_iam.models import UserRole
        project_user_roles_list = UserRole.objects.filter(
            project_role__project_id=project_id
        ).values("user_id", "project_role_id")
        snapshot.assert_match(
            list(project_user_roles_list), "project_user_roles")

    @pytest.fixture()
    def create_project(self):
        project_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        from ib_iam.tests.factories.models import ProjectFactory
        ProjectFactory.reset_sequence(1)
        project_object = ProjectFactory(project_id=project_id)
        return project_object

    @pytest.fixture()
    def create_project_roles(self, create_project):
        project_id = "31be920b-7b4c-49e7-8adb-41a0c18da848"
        project_role_list = [
            {
                "project_id": project_id,
                "role_id": "ROLE_1",
                "name": "NAME_1",
                "description": "description"
            },
            {
                "project_id": project_id,
                "role_id": "ROLE_2",
                "name": "NAME_2",
                "description": "description"
            },
            {
                "project_id": project_id,
                "role_id": "ROLE_3",
                "name": "NAME_3",
                "description": "description"
            },
            {
                "project_id": project_id,
                "role_id": "ROLE_4",
                "name": "NAME_3",
                "description": "description"
            }
        ]
        from ib_iam.tests.factories.models import ProjectRoleFactory
        project_role_objects = [
            ProjectRoleFactory(
                project_id=project_role_dict["project_id"],
                role_id=project_role_dict["role_id"],
                name=project_role_dict["name"],
                description=project_role_dict["description"]
            )
            for project_role_dict in project_role_list
        ]
        return project_role_objects

    @pytest.fixture()
    def create_user_roles(self, create_project_roles):
        project_role_objects = create_project_roles
        user_role_list = [
            {
                "user_id": "31be920b-7b4c-49e7-8adb-41a0c18da848",
                "project_role": project_role_objects[0]
            },
            {
                "user_id": "31be920b-7b4c-49e7-8adb-41a0c18da848",
                "project_role": project_role_objects[1]
            },
            {
                "user_id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "project_role": project_role_objects[2]
            }
        ]
        from ib_iam.tests.factories.models import UserRoleFactory
        user_role_objects = [
            UserRoleFactory(
                user_id=user_role_dict["user_id"],
                project_role=user_role_dict["project_role"]
            )
            for user_role_dict in user_role_list
        ]
        return user_role_objects
