import pytest


class TestGetProjectRoleIds:
    @pytest.fixture
    def setup(self):
        project_id = "project_1"
        role_ids = ["role_1", "role_2"]
        from ib_iam.tests.factories.models import (
            ProjectFactory, ProjectRoleFactory)
        project_object = ProjectFactory.create(project_id=project_id)
        _ = [ProjectRoleFactory.create(project=project_object, role_id=role_id)
             for role_id in role_ids]

        return {"project_id": project_id, "role_ids": role_ids}

    @pytest.mark.django_db
    def test_given_invalid_project_id_raises_invalid_project_id_exception(
            self):
        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        project_id = "project_1"
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        with pytest.raises(InvalidProjectId):
            service_interface.get_project_role_ids(project_id=project_id)

    @pytest.mark.django_db
    def test_given_valid_project_id_returns_project_role_ids(self, setup):
        project_id = setup["project_id"]
        expected_project_role_ids = setup["role_ids"]
        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        actual_project_role_ids = service_interface.get_project_role_ids(
            project_id=project_id)

        assert actual_project_role_ids == expected_project_role_ids
