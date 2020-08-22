import pytest


class TestGetValidProjectIdsInteractor:

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
        project_ids = ["1", "2", "3"]
        valid_project_ids = ["1", "2"]
        storage.get_valid_project_ids_from_given_project_ids \
            .return_value = valid_project_ids
        expected_response = valid_project_ids

        # Act
        response = interactor.get_valid_project_ids(project_ids=project_ids)

        # Assert
        storage.get_valid_project_ids_from_given_project_ids \
            .assert_called_once_with(project_ids=project_ids)
        assert response == expected_response
