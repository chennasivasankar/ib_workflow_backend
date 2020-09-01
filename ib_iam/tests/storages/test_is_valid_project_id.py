import pytest


class TestIsValidProjectId:

    @pytest.fixture()
    def user_storage(self):
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        storage = UserStorageImplementation()
        return storage

    @pytest.mark.django_db
    def test_with_invalid_project_id_return_false(
            self, user_storage
    ):
        # Arrange
        project_id = "project_1"

        # Act
        response = user_storage.is_valid_project_id(
            project_id=project_id
        )

        # Assert
        assert response is False

    @pytest.mark.django_db
    def test_with_invalid_project_id_return_true(
            self, user_storage
    ):
        # Arrange
        project_id = "project_1"
        from ib_iam.tests.factories.models import ProjectFactory
        ProjectFactory(project_id=project_id)

        # Act
        response = user_storage.is_valid_project_id(
            project_id=project_id
        )

        # Assert
        assert response is True

