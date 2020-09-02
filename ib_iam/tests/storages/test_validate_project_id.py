import pytest


class TestValidateProjectId:

    @pytest.fixture()
    def user_storage(self):
        from ib_iam.storages.user_storage_implementation import \
            UserStorageImplementation
        storage = UserStorageImplementation()
        return storage

    @pytest.mark.django_db
    def test_with_invalid_project_id_raise_exception(self, user_storage):
        # Arrange
        project_id = "project_1"

        # Assert
        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        with pytest.raises(InvalidProjectId):
            user_storage.validate_project_id(project_id=project_id)

    @pytest.mark.django_db
    def test_with_valid_project_id_did_not_raise_exception(self, user_storage):
        # Arrange
        project_id = "project_1"
        from ib_iam.tests.factories.models import ProjectFactory
        ProjectFactory(project_id=project_id)

        # Assert
        user_storage.validate_project_id(project_id=project_id)
