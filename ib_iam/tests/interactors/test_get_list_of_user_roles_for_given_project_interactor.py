from unittest.mock import Mock

import pytest


class TestGetListOfUserRolesForGivenProjectInteractor:

    @pytest.fixture()
    def presenter_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.presenter_interfaces.user_presenter_interface import \
            GetListOfUserRolesForGivenProjectPresenterInterface
        presenter = create_autospec(
            GetListOfUserRolesForGivenProjectPresenterInterface)
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
        from ib_iam.interactors.users.get_list_of_user_roles_for_given_project_interactor import \
            GetListOfUserRolesForGivenProjectInteractor
        interactor = GetListOfUserRolesForGivenProjectInteractor(
            user_storage=storage_mock)
        return interactor

    def test_with_invalid_project_id_return_response(
            self, storage_mock, presenter_mock, interactor
    ):
        # Arrange
        project_id = "project_1"
        user_id = "1"
        expected_presenter_response_for_invalid_project_id = Mock()
        storage_mock.is_user_admin.return_value = True
        storage_mock.is_valid_project_id.return_value = False
        presenter_mock.response_for_invalid_project_id_exception.return_value = \
            expected_presenter_response_for_invalid_project_id

        # Act
        response = interactor.get_list_of_user_roles_for_given_project_wrapper(
            project_id=project_id, presenter=presenter_mock, user_id=user_id
        )

        # Assert
        assert response == expected_presenter_response_for_invalid_project_id

        storage_mock.is_valid_project_id.assert_called_with(
            project_id=project_id)
        presenter_mock.response_for_invalid_project_id_exception.assert_called_once()

    def test_with_user_is_not_admin_then_raise_exception(
            self, storage_mock, presenter_mock, interactor
    ):
        # Arrange
        project_id = "project_1"
        user_id = "1"
        expected_presenter_response_for_user_is_not_admin = Mock()
        storage_mock.is_user_admin.return_value = False
        presenter_mock.response_for_user_not_have_permission_exception \
            .return_value = expected_presenter_response_for_user_is_not_admin

        # Act
        response = interactor.get_list_of_user_roles_for_given_project_wrapper(
            project_id=project_id, presenter=presenter_mock, user_id=user_id
        )

        # Assert
        assert response == expected_presenter_response_for_user_is_not_admin

        storage_mock.is_user_admin.assert_called_with(
            user_id=user_id
        )
        presenter_mock.response_for_user_not_have_permission_exception. \
            assert_called_once()

    def test_with_valid_details_return_response(
            self, storage_mock, presenter_mock, interactor,
            prepare_basic_user_details_dtos, prepare_user_role_dtos
    ):
        # Arrange
        project_id = "project_1"
        user_id = "1"
        expected_result = Mock()
        expected_user_ids = [
            "31be920b-7b4c-49e7-8adb-41a0c18da848",
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "77be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        storage_mock.is_user_admin.return_value = True
        storage_mock.get_basic_user_dtos_for_given_project.return_value = \
            prepare_basic_user_details_dtos
        storage_mock.get_user_role_dtos_of_a_project.return_value = \
            prepare_user_role_dtos
        presenter_mock.get_response_for_get_users_with_roles. \
            return_value = expected_result

        # Act
        response = interactor.get_list_of_user_roles_for_given_project_wrapper(
            project_id=project_id, presenter=presenter_mock, user_id=user_id
        )

        # Assert
        assert response == expected_result
        storage_mock.get_basic_user_dtos_for_given_project.assert_called_once_with(
            project_id=project_id
        )
        storage_mock.get_user_role_dtos_of_a_project.assert_called_once_with(
            project_id=project_id, user_ids=expected_user_ids
        )
        presenter_mock.get_response_for_get_users_with_roles. \
            assert_called_once_with(
            basic_user_details_dtos=prepare_basic_user_details_dtos,
            user_role_dtos=prepare_user_role_dtos
        )

    @pytest.fixture()
    def prepare_basic_user_details_dtos(self):
        user_ids = [
            "31be920b-7b4c-49e7-8adb-41a0c18da848",
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "77be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_iam.tests.factories.storage_dtos import (
            BasicUserDetailsDTOFactory
        )
        BasicUserDetailsDTOFactory.reset_sequence(1)
        basic_user_details_dtos = [
            BasicUserDetailsDTOFactory(user_id=user_id)
            for user_id in user_ids
        ]
        return basic_user_details_dtos

    @pytest.fixture()
    def prepare_user_role_dtos(self):
        user_roles_list = [
            {
                "user_id": "31be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_id": "ROLE_1"
            },
            {
                "user_id": "31be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_id": "ROLE_2"
            },
            {
                "user_id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_id": "ROLE_3"
            }
        ]
        from ib_iam.tests.factories.storage_dtos import UserRoleDTOFactory
        UserRoleDTOFactory.reset_sequence(1)
        user_roles_dtos = [
            UserRoleDTOFactory(
                user_id=user_roles_dict["user_id"],
                role_id=user_roles_dict["role_id"]
            )
            for user_roles_dict in user_roles_list
        ]
        return user_roles_dtos
