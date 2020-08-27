"""
All exceptions
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02AddSpecificProjectDetailsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_with_invalid_user_ids_for_project(
            self, snapshot, create_user_roles
    ):
        project_id = "project_id"
        user_id_with_role_ids_list = [
            {
                "user_id": "11be920b-7b4c-49e7-8adb-41a0c18da848",
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
        body = {
            'users': user_id_with_role_ids_list
        }
        path_params = {"project_id": project_id}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)

    @pytest.fixture()
    def create_project(self):
        project_id = "project_id"
        from ib_iam.tests.factories.models import ProjectFactory
        ProjectFactory.reset_sequence(1)
        project_object = ProjectFactory(project_id=project_id)
        return project_object

    @pytest.fixture()
    def create_project_roles(self, create_project):
        project_id = "project_id"
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
