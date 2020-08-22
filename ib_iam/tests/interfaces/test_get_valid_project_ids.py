import pytest


class TestGetValidProjectIds:

    @pytest.mark.django_db
    def test_get_valid_project_ids_returns_valid_project_ids(self):
        # Arrange
        project_ids = ["641bfcc5-e1ea-4231-b482-f7f34fb5c7c4",
                       "641bfcc5-e1ea-4231-b482-f7f34fb5c7c5",
                       "641bfcc5-e1ea-4231-b482-f7f34fb5c7c6"]
        expected_project_ids = ["641bfcc5-e1ea-4231-b482-f7f34fb5c7c4",
                                "641bfcc5-e1ea-4231-b482-f7f34fb5c7c5"]
        from ib_iam.tests.factories.models import ProjectFactory
        for project_id in expected_project_ids:
            ProjectFactory.create(project_id=project_id)

        from ib_iam.app_interfaces.service_interface import ServiceInterface
        service_interface = ServiceInterface()

        # Act
        valid_project_ids = service_interface.get_valid_project_ids(
            project_ids=project_ids)

        # Assert
        assert valid_project_ids == expected_project_ids
