from unittest.mock import create_autospec

import pytest


class TestProjectRoleInteractor:

    @pytest.fixture()
    def project_storage(self):
        from ib_iam.interactors.storage_interfaces.project_storage_interface \
            import \
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
            self, project_storage, interactor
    ):
        # Arrange
        project_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        user_id = "aca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        project_storage.is_valid_project_id.return_value = False

        # Act
        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        with pytest.raises(InvalidProjectId):
            interactor.get_user_role_ids_based_on_project(
                user_id=user_id, project_id=project_id
            )

        # Assert
        project_storage.is_valid_project_id.assert_called_with(
            project_id=project_id)

    def test_with_user_is_not_a_member_of_project_raise_exception(
            self, project_storage, interactor
    ):
        # Arrange
        project_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        user_id = "aca1a0c1-b9ef-4e59-b415-60a28ef17b10"

        project_storage.is_valid_project_id.return_value = True
        project_storage.is_user_in_a_project.return_value = False

        # Act
        from ib_iam.interactors.project_role_interactor import \
            UserNotAMemberOfAProject
        with pytest.raises(UserNotAMemberOfAProject):
            interactor.get_user_role_ids_based_on_project(
                user_id=user_id, project_id=project_id
            )

        # Assert
        project_storage.is_user_in_a_project.assert_called_with(
            project_id=project_id, user_id=user_id)

    def test_with_valid_details_return_response(
            self, interactor, project_storage
    ):
        # Arrange
        project_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        user_id = "aca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        expected_role_ids = [
            "FIN_DEVELOPER", "FIN_SD"
        ]

        project_storage.is_valid_project_id.return_value = True
        project_storage.is_user_in_a_project.return_value = True
        project_storage.get_user_role_ids.return_value = expected_role_ids

        # Act
        response = interactor.get_user_role_ids_based_on_project(
            user_id=user_id, project_id=project_id
        )

        # Assert
        assert response == expected_role_ids
        project_storage.get_user_role_ids.assert_called_with(
            project_id=project_id, user_id=user_id
        )


class TestGetUserRolesForProjects:
    @pytest.fixture
    def project_storage(self):
        from ib_iam.interactors.storage_interfaces.project_storage_interface \
            import \
            ProjectStorageInterface
        project_storage = create_autospec(ProjectStorageInterface)
        return project_storage

    @pytest.fixture
    def interactor(self, project_storage):
        from ib_iam.interactors.project_role_interactor import \
            ProjectRoleInteractor
        interactor = ProjectRoleInteractor(project_storage=project_storage)
        return interactor

    @pytest.fixture
    def user_status_in_projects(self):
        from ib_iam.tests.factories.storage_dtos import \
            UserIdWithProjectIdAndStatusDTOFactory
        UserIdWithProjectIdAndStatusDTOFactory.reset_sequence()
        return UserIdWithProjectIdAndStatusDTOFactory.create_batch(
            size=2, user_id="aca1a0c1-b9ef-4e59-b415-60a28ef17b10")

    @pytest.fixture
    def expected_project_roles(self):
        from ib_iam.tests.factories.storage_dtos import ProjectRolesDTOFactory
        ProjectRolesDTOFactory.reset_sequence()
        return ProjectRolesDTOFactory.create_batch(size=2)

    def test_with_invalid_project_ids_raise_exception(
            self, project_storage, interactor
    ):
        # Arrange
        project_ids = ["eca1a0c1-b9ef-4e59-b415-60a28ef17b10"]
        user_id = "aca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        project_storage.get_valid_project_ids.return_value = []

        # Act
        from ib_iam.exceptions.custom_exceptions import InvalidProjectIds
        with pytest.raises(InvalidProjectIds):
            interactor.get_user_role_ids_for_given_project_ids(
                user_id=user_id, project_ids=project_ids
            )

        # Assert
        project_storage.get_valid_project_ids.assert_called_with(
            project_ids=project_ids)

    def test_with_user_is_not_member_of_given_projects_raise_exception(
            self, project_storage, interactor, user_status_in_projects
    ):
        # Arrange
        project_ids = ["project 1", "project 2"]
        user_id = "aca1a0c1-b9ef-4e59-b415-60a28ef17b10"

        project_storage.get_valid_project_ids.return_value = project_ids
        project_storage.get_user_status_for_given_projects.return_value = \
            user_status_in_projects

        # Act
        from ib_iam.interactors.project_role_interactor import \
            UserNotAMemeberOfProjectsException
        with pytest.raises(UserNotAMemeberOfProjectsException):
            interactor.get_user_role_ids_for_given_project_ids(
                user_id=user_id, project_ids=project_ids
            )

        # Assert
        project_storage.get_user_status_for_given_projects.assert_called_with(
            project_ids=project_ids, user_id=user_id)

    def test_get_user_roles_for_given_projects_with_valid_details_return_response(
            self, interactor, project_storage, user_status_in_projects,
            expected_project_roles
    ):
        # Arrange
        project_ids = ["project 1", "project 2"]
        user_id = "aca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        user_status_in_projects[1].is_exist = True

        project_storage.get_valid_project_ids.return_value = project_ids
        project_storage.get_user_status_for_given_projects.return_value = \
            user_status_in_projects
        project_storage.get_user_roles_for_projects.return_value = \
            expected_project_roles

        # Act
        response = interactor.get_user_role_ids_for_given_project_ids(
            user_id=user_id, project_ids=project_ids
        )

        # Assert
        assert response == expected_project_roles
        project_storage.get_user_roles_for_projects.assert_called_with(
            project_ids=project_ids, user_id=user_id
        )
