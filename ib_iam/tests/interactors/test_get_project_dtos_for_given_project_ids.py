import pytest


class TestGetProjectDTOs:
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

    def test_get_project_dtos_for_give_project_ids(
            self, storage, interactor):
        # Arrange
        project_ids = ["1"]
        from ib_iam.tests.factories.storage_dtos import ProjectDTOFactory
        project_dtos = [
            ProjectDTOFactory.create(project_id=project_id)
            for project_id in project_ids]
        storage.get_project_dtos_for_given_project_ids.return_value = \
            project_dtos

        # Act
        interactor.get_project_dtos_bulk(
            project_ids=project_ids)

        # Assert
        storage.get_project_dtos_for_given_project_ids.assert_called_once_with(
            project_ids=project_ids)

    def test_get_project_dtos_for_give_invalid_project_ids_then_raise_exception(
            self, storage, interactor):
        project_ids = ["1", "2"]
        from ib_iam.exceptions.custom_exceptions import InvalidProjectIds
        storage.get_project_dtos_for_given_project_ids.side_effect = \
            InvalidProjectIds

        with pytest.raises(InvalidProjectIds):
            interactor.get_project_dtos_bulk(project_ids=project_ids)
