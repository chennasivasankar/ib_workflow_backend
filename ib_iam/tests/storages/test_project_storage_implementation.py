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
        project_ids = Project.objects.values_list("project_id", flat=True)
        actual_project_ids = list(map(str, project_ids))

        assert actual_project_ids == expected_project_ids
