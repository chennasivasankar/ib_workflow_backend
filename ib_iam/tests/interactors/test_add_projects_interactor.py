import pytest


class TestAddProjectsInteractor:

    @pytest.fixture
    def storage(self):
        from ib_iam.interactors.storage_interfaces \
            .project_storage_interface import ProjectStorageInterface
        from mock import create_autospec
        storage = create_autospec(ProjectStorageInterface)
        return storage

    @pytest.fixture
    def interactor(self, storage):
        from ib_iam.interactors.project_interactor import ProjectInteractor
        interactor = ProjectInteractor(project_storage=storage)
        return interactor

    def test_given_valid_project_dtos_adds_projects_to_db_successfully(
            self, storage, interactor):
        # Arrange
        from ib_iam.tests.factories.storage_dtos import ProjectDTOFactory
        project_dtos = ProjectDTOFactory.create_batch(size=2)

        # Act
        interactor.add_projects(project_dtos=project_dtos)

        # Assert
        storage.add_projects.assert_called_once_with(project_dtos=project_dtos)
