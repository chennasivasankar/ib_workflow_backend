import mock
import pytest


class TestAddProjectsInteractor:

    @pytest.fixture
    def storage(self):
        from ib_iam.interactors.storage_interfaces \
            .project_storage_interface import ProjectStorageInterface
        storage = mock.create_autospec(ProjectStorageInterface)
        return storage

    @pytest.fixture
    def presenter(self):
        from ib_iam.interactors.presenter_interfaces \
            .get_projects_presenter_interface import \
            GetProjectsPresenterInterface
        presenter = mock.create_autospec(GetProjectsPresenterInterface)
        return presenter

    @pytest.fixture
    def interactor(self, storage):
        from ib_iam.interactors.get_projects_interactor import \
            GetProjectsInteractor
        interactor = GetProjectsInteractor(project_storage=storage)
        return interactor

    def test_get_projects_returns_projects_response(
            self, storage, interactor, presenter):
        # Arrange
        from ib_iam.tests.factories.storage_dtos import ProjectDTOFactory
        project_dtos = ProjectDTOFactory.create_batch(size=2)
        storage.get_project_dtos.return_value = project_dtos
        presenter.get_response_for_get_projects.return_value = mock.Mock()

        # Act
        interactor.get_projects_wrapper(presenter=presenter)

        # Assert
        storage.get_project_dtos.assert_called_once()
        presenter.get_response_for_get_projects.assert_called_once_with(
            project_dtos=project_dtos)
