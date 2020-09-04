from unittest.mock import Mock

import pytest


class TestAssignUserRolesForGivenProjectBulkInteractor:

    @pytest.fixture()
    def presenter_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.presenter_interfaces.assign_user_roles_for_given_project_presenter_interface import \
            AssignUserRolesForGivenProjectBulkPresenterInterface
        presenter = create_autospec(
            AssignUserRolesForGivenProjectBulkPresenterInterface)
        return presenter

    @pytest.fixture()
    def storage_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.storage_interfaces.user_storage_interface import \
            UserStorageInterface
        storage = create_autospec(UserStorageInterface)
        return storage

    @pytest.fixture()
    def interactor(self, storage_mock):
        from ib_iam.interactors.assign_user_roles_for_given_project_bulk_interactor import \
            AssignUserRolesForGivenProjectBulkInteractor
        interactor = AssignUserRolesForGivenProjectBulkInteractor(
            user_storage=storage_mock)
        return interactor

    def test_with_invalid_project_id_return_response(
            self, storage_mock, presenter_mock, interactor,
            prepare_user_id_with_role_ids_dtos
    ):
        # Arrange
        project_id = "project_1"
        user_id_with_role_ids_dtos = prepare_user_id_with_role_ids_dtos

        expected_presenter_response_for_invalid_project_id_mock = Mock()

        presenter_mock.response_for_invalid_project_id.return_value = \
            expected_presenter_response_for_invalid_project_id_mock

        from ib_iam.exceptions.custom_exceptions import InvalidProjectId
        storage_mock.validate_project_id.side_effect = InvalidProjectId

        # Act
        response = interactor.assign_user_roles_for_given_project_bulk_wrapper(
            project_id=project_id, presenter=presenter_mock,
            user_id_with_role_ids_dtos=user_id_with_role_ids_dtos
        )

        # Assert
        assert response == \
               expected_presenter_response_for_invalid_project_id_mock

        presenter_mock.response_for_invalid_project_id.assert_called_once()
        storage_mock.validate_project_id.assert_called_once_with(
            project_id=project_id)

    def test_with_invalid_user_ids_for_project_return_response(
            self, storage_mock, presenter_mock, interactor,
            prepare_user_id_with_role_ids_dtos
    ):
        # Arrange
        project_id = "project_1"
        user_id_with_role_ids_dtos = prepare_user_id_with_role_ids_dtos
        expected_user_ids = [
            "31be920b-7b4c-49e7-8adb-41a0c18da848",
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "77be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        invalid_user_ids = [
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "77be920b-7b4c-49e7-8adb-41a0c18da848"
        ]

        expected_presenter_response_for_invalid_user_ids_for_project_mock = \
            Mock()

        presenter_mock.response_for_invalid_user_ids_for_project.return_value = \
            expected_presenter_response_for_invalid_user_ids_for_project_mock

        from ib_iam.exceptions.custom_exceptions import \
            InvalidUserIdsForProject
        storage_mock.validate_users_for_project.side_effect = \
            InvalidUserIdsForProject(user_ids=invalid_user_ids)

        # Act
        response = interactor.assign_user_roles_for_given_project_bulk_wrapper(
            user_id_with_role_ids_dtos=user_id_with_role_ids_dtos,
            project_id=project_id, presenter=presenter_mock
        )

        # Assert
        assert response == \
               expected_presenter_response_for_invalid_user_ids_for_project_mock

        storage_mock.validate_users_for_project.assert_called_with(
            user_ids=expected_user_ids, project_id=project_id
        )
        call_obj = \
            presenter_mock.response_for_invalid_user_ids_for_project.call_args
        assert call_obj[0][0].user_ids == invalid_user_ids

    def test_with_invalid_role_ids_for_project_return_response(
            self, storage_mock, presenter_mock, interactor,
            prepare_user_id_with_role_ids_dtos
    ):
        # Arrange
        project_id = "project_1"
        user_id_with_role_ids_dtos = prepare_user_id_with_role_ids_dtos
        expected_role_ids = [
            "ROLE_1", "ROLE_2", "ROLE_3"
        ]
        invalid_role_ids = [
            "ROLE_3"
        ]

        expected_presenter_response_for_invalid_role_ids_for_project_mock = \
            Mock()

        presenter_mock.response_for_invalid_role_ids_for_project.return_value = \
            expected_presenter_response_for_invalid_role_ids_for_project_mock

        from ib_iam.exceptions.custom_exceptions import \
            InvalidRoleIdsForProject
        storage_mock.validate_role_ids_for_project.side_effect = \
            InvalidRoleIdsForProject(role_ids=invalid_role_ids)

        # Act
        response = interactor.assign_user_roles_for_given_project_bulk_wrapper(
            user_id_with_role_ids_dtos=user_id_with_role_ids_dtos,
            project_id=project_id, presenter=presenter_mock
        )

        # Assert
        assert response == \
               expected_presenter_response_for_invalid_role_ids_for_project_mock

        storage_mock.validate_role_ids_for_project.assert_called_with(
            role_ids=expected_role_ids, project_id=project_id
        )
        call_obj = \
            presenter_mock.response_for_invalid_role_ids_for_project.call_args
        assert call_obj[0][0].role_ids == invalid_role_ids

    def test_with_valid_details_return_response(
            self, storage_mock, presenter_mock, interactor,
            prepare_user_id_with_role_ids_dtos
    ):
        # Arrange
        project_id = "project_1"
        user_id_with_role_ids_dtos = prepare_user_id_with_role_ids_dtos

        expected_presenter_prepare_success_response_for_add_specific_project_details = \
            Mock()
        presenter_mock.prepare_success_response_for_assign_user_roles_for_given_project. \
            return_value = expected_presenter_prepare_success_response_for_add_specific_project_details

        # Act
        response = interactor.assign_user_roles_for_given_project_bulk_wrapper(
            user_id_with_role_ids_dtos=user_id_with_role_ids_dtos,
            project_id=project_id, presenter=presenter_mock
        )

        # Assert
        assert response == \
               expected_presenter_prepare_success_response_for_add_specific_project_details

        storage_mock.assign_user_roles_for_given_project.assert_called_once_with(
            user_id_with_role_ids_dtos=user_id_with_role_ids_dtos,
            project_id=project_id
        )
        presenter_mock.prepare_success_response_for_assign_user_roles_for_given_project. \
            assert_called_once()

    @pytest.fixture()
    def prepare_user_id_with_role_ids_dtos(self):
        user_id_with_role_ids_list = [
            {
                "user_id": "31be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_ids": ["ROLE_1", "ROLE_2"]
            },
            {
                "user_id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_ids": ["ROLE_3"]
            },
            {
                "user_id": "77be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_ids": []
            }
        ]
        from ib_iam.tests.factories.interactor_dtos import \
            UserIdWithRoleIdsDTOFactory
        user_id_with_role_ids_dtos = [
            UserIdWithRoleIdsDTOFactory(
                user_id=user_id_with_role_ids_dict["user_id"],
                role_ids=user_id_with_role_ids_dict["role_ids"]
            )
            for user_id_with_role_ids_dict in user_id_with_role_ids_list
        ]
        return user_id_with_role_ids_dtos
