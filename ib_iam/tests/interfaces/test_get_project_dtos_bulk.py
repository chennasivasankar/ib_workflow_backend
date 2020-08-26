import pytest


class TestGetProjectDTOsBulk:
    @pytest.fixture
    def set_up(self):
        project_ids = ["FA", "SA", "DE"]
        from ib_iam.tests.factories.models import ProjectFactory
        ProjectFactory.reset_sequence(0)
        project_objects = [
            ProjectFactory.create(project_id=project_id)
            for project_id in project_ids
        ]
        from ib_iam.tests.factories.storage_dtos import ProjectDTOFactory
        ProjectDTOFactory.reset_sequence(0)
        project_dtos = [
            ProjectDTOFactory.create(project_id=project_id)
            for project_id in project_ids
        ]
        return project_objects, project_dtos

    @pytest.mark.django_db
    def test_get_project_dtos_for_given_valid_details_then_return_list_of_project_dtos(
            self, set_up):
        project_ids = ["FA", "SA", "DE"]
        expected_result = set_up[1]
        expected_result = sorted(expected_result, key=lambda x: x.project_id)

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        actual_result = service_interface.get_project_dtos_bulk(
            project_ids=project_ids)
        actual_result = sorted(actual_result, key=lambda x: x.project_id)

        assert len(actual_result) == len(expected_result)
        assert actual_result == expected_result

    @pytest.mark.django_db
    def test_get_project_dtos_for_given_invalid_project_ids_then_raise_exception(
            self):
        project_ids = ["FA", "SA", "DE"]

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        from ib_iam.exceptions.custom_exceptions import InvalidProjectIds
        with pytest.raises(InvalidProjectIds) as err:
            service_interface.get_project_dtos_bulk(
                project_ids=project_ids)

        assert err.value.project_ids == project_ids
