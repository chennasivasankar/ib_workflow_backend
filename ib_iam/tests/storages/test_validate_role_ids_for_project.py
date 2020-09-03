import pytest


class TestValidateRolesForProject:

    @pytest.fixture()
    def user_storage(self):
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        storage = UserStorageImplementation()
        return storage

    @pytest.mark.django_db
    def test_with_invalid_role_ids_for_project(
            self, user_storage, create_project_roles
    ):
        # Arrange
        role_ids = [
            "ROLE_1", "ROLE_5", "ROLE_4"
        ]
        invalid_role_ids = [
            "ROLE_5", "ROLE_4"
        ]
        project_id = "project_1"

        # Assert
        from ib_iam.exceptions.custom_exceptions import InvalidRoleIdsForProject
        with pytest.raises(InvalidRoleIdsForProject) as err:
            user_storage.validate_role_ids_for_project(
                role_ids=role_ids, project_id=project_id
            )
        assert err.value.role_ids == invalid_role_ids

    @pytest.mark.django_db
    def test_with_valid_roles_ids_did_not_raise_exception(
            self, user_storage, create_project_roles
    ):
        role_ids = [
            "ROLE_1", "ROLE_2", "ROLE_3"
        ]
        project_id = "project_1"

        # Assert
        user_storage.validate_role_ids_for_project(
            role_ids=role_ids, project_id=project_id
        )

    @pytest.fixture()
    def create_project(self):
        project_id = "project_1"
        from ib_iam.tests.factories.models import ProjectFactory
        ProjectFactory.reset_sequence(1)
        project_object = ProjectFactory(project_id=project_id)
        return project_object

    @pytest.fixture()
    def create_project_roles(self, create_project):
        project_id = "project_1"
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
