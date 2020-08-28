from unittest.mock import Mock

import pytest


class TestGetSpecificTeamDetailsInteractor:

    @pytest.fixture()
    def presenter_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.interactors.presenter_interfaces.get_specific_project_details_presenter_interface import \
            GetSpecificProjectDetailsPresenterInterface
        presenter = create_autospec(GetSpecificProjectDetailsPresenterInterface)
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
        from ib_iam.interactors.get_specific_project_details_interactor import \
            GetSpecificProjectDetailsInteractor
        interactor = GetSpecificProjectDetailsInteractor(
            user_storage=storage_mock)
        return interactor

    def test_with_invalid_project_id_return_response(
            self, storage_mock, presenter_mock, interactor
    ):
        # Arrange
        project_id = "project_1"

        expected_presenter_response_for_invalid_project_id = Mock()

        storage_mock.is_valid_project_id.return_value = False

        presenter_mock.response_for_invalid_project_id.return_value = \
            expected_presenter_response_for_invalid_project_id

        # Act
        response = interactor.get_specific_project_details_wrapper(
            project_id=project_id, presenter=presenter_mock
        )

        # Assert
        assert response == expected_presenter_response_for_invalid_project_id

        storage_mock.is_valid_project_id.assert_called_with(
            project_id=project_id)
        presenter_mock.response_for_invalid_project_id.assert_called_once()

    def test_with_valid_details_return_response(
            self, storage_mock, presenter_mock, interactor,
            prepare_basic_user_details_dtos, prepare_user_role_dtos
    ):
        # Arrange
        project_id = "project_1"

        expected_presenter_prepare_success_response_for_get_specific_team_details = \
            Mock()
        expected_user_ids = [
            "31be920b-7b4c-49e7-8adb-41a0c18da848",
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "77be920b-7b4c-49e7-8adb-41a0c18da848"
        ]

        storage_mock.get_basic_user_dtos_for_given_project.return_value = \
            prepare_basic_user_details_dtos
        storage_mock.get_user_role_dtos_of_a_project.return_value = \
            prepare_user_role_dtos

        presenter_mock.prepare_success_response_for_get_specific_project_details. \
            return_value = expected_presenter_prepare_success_response_for_get_specific_team_details

        # Act
        response = interactor.get_specific_project_details_wrapper(
            project_id=project_id, presenter=presenter_mock
        )

        # Assert
        assert response == \
               expected_presenter_prepare_success_response_for_get_specific_team_details

        storage_mock.get_basic_user_dtos_for_given_project.assert_called_once_with(
            project_id=project_id)
        storage_mock.get_user_role_dtos_of_a_project.assert_called_once_with(
            project_id=project_id, user_ids=expected_user_ids)
        presenter_mock.prepare_success_response_for_get_specific_project_details. \
            assert_called_once_with(
            basic_user_details_dtos=prepare_basic_user_details_dtos,
            user_role_dtos=prepare_user_role_dtos)

    @pytest.fixture()
    def prepare_basic_user_details_dtos(self):
        basic_user_details_list = [
            {
                "user_id": "31be920b-7b4c-49e7-8adb-41a0c18da848",
                "name": "user_1",
                "profile_pic_url": None
            },
            {
                "user_id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "name": "user_2",
                "profile_pic_url": None
            },
            {
                "user_id": "77be920b-7b4c-49e7-8adb-41a0c18da848",
                "name": "user_3",
                "profile_pic_url": None
            }
        ]
        from ib_iam.tests.factories.storage_dtos import \
            BasicUserDetailsDTOFactory
        basic_user_details_dtos = [
            BasicUserDetailsDTOFactory(
                user_id=basic_user_details_dict["user_id"],
                name=basic_user_details_dict["name"],
                profile_pic_url=basic_user_details_dict["profile_pic_url"]
            )
            for basic_user_details_dict in basic_user_details_list
        ]
        return basic_user_details_dtos

    @pytest.fixture()
    def prepare_user_role_dtos(self):
        user_roles_list = [
            {
                "user_id": "31be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_id": "ROLE_1",
                "name": "NAME_1",
                "description": "description"
            },
            {
                "user_id": "31be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_id": "ROLE_2",
                "name": "NAME_2",
                "description": "description"
            },
            {
                "user_id": "01be920b-7b4c-49e7-8adb-41a0c18da848",
                "role_id": "ROLE_3",
                "name": "NAME_3",
                "description": "description"
            }
        ]
        from ib_iam.tests.factories.storage_dtos import UserRoleDTOFactory
        user_roles_dtos = [
            UserRoleDTOFactory(
                user_id=user_roles_dict["user_id"],
                role_id=user_roles_dict["role_id"],
                name=user_roles_dict["name"],
                description=user_roles_dict["description"]
            )
            for user_roles_dict in user_roles_list
        ]
        return user_roles_dtos
