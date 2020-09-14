from unittest.mock import create_autospec

import pytest


class TestProjectRoleInteractor:

    @pytest.fixture()
    def project_storage(self):
        from ib_iam.interactors.storage_interfaces.project_storage_interface import \
            ProjectStorageInterface
        project_storage = create_autospec(ProjectStorageInterface)
        return project_storage

    @pytest.fixture()
    def interactor(self, project_storage):
        from ib_iam.interactors.project_role_interactor import \
            ProjectRoleInteractor
        interactor = ProjectRoleInteractor(project_storage=project_storage)
        return interactor

    def test_with_invalid_project_id_raise_exception(
            self, project_storage, interactor):
        # Arrange
        project_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        user_id = "aca1a0c1-b9ef-4e59-b415-60a28ef17b10"

        project_storage.is_valid_project_id.return_value = False

        # Assert
        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        with pytest.raises(InvalidProjectId):
            interactor.get_user_role_ids_based_on_project(
                user_id=user_id, project_id=project_id
            )

        project_storage.is_valid_project_id.assert_called_with(
            project_id=project_id)

    def test_with_user_is_not_a_member_of_project_raise_exception(
            self, project_storage, interactor):
        # Arrange
        project_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        user_id = "aca1a0c1-b9ef-4e59-b415-60a28ef17b10"

        project_storage.is_valid_project_id.return_value = True
        project_storage.is_user_in_a_project.return_value = False

        # Assert
        from ib_iam.interactors.project_role_interactor import \
            UserNotAMemberOfAProject
        with pytest.raises(UserNotAMemberOfAProject):
            interactor.get_user_role_ids_based_on_project(
                user_id=user_id, project_id=project_id
            )

        project_storage.is_user_in_a_project.assert_called_with(
            project_id=project_id, user_id=user_id)

    def test_with_valid_details_return_response(
            self, interactor, project_storage):
        # Arrange
        project_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        user_id = "aca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        expected_role_ids = [
            "FIN_DEVELOPER", "FIN_SD"
        ]

        project_storage.is_valid_project_id.return_value = True
        project_storage.is_user_in_a_project.return_value = True
        project_storage.get_user_role_ids.return_value = expected_role_ids

        # Assert
        response = interactor.get_user_role_ids_based_on_project(
            user_id=user_id, project_id=project_id
        )

        # Assert
        assert response == expected_role_ids
        project_storage.get_user_role_ids.assert_called_with(
            project_id=project_id, user_id=user_id
        )
