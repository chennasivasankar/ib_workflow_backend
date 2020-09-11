import json

import pytest

from ib_iam.constants.enums import StatusCode


class TestGetListOfUserRolesForGivenProjectPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_iam.presenters.get_list_of_user_roles_for_given_project_presenter_implementation import \
            GetListOfUserRolesForGivenProjectPresenterImplementation
        presenter = GetListOfUserRolesForGivenProjectPresenterImplementation()
        return presenter

    def test_response_for_invalid_project_id(self, presenter):
        # Arrange
        from ib_iam.presenters.get_list_of_user_roles_for_given_project_presenter_implementation import \
            INVALID_PROJECT_ID
        expected_response = INVALID_PROJECT_ID[0]
        response_status_code = INVALID_PROJECT_ID[1]

        # Act
        response_object = presenter.response_for_invalid_project_id_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_response_for_user_not_have_permission_exception(self, presenter):
        # Arrange
        from ib_iam.constants.exception_messages import (
            USER_HAS_NO_ACCESS_TO_GET_USERS_WITH_ROLES
        )
        expected_response = USER_HAS_NO_ACCESS_TO_GET_USERS_WITH_ROLES[0]
        response_status_code = USER_HAS_NO_ACCESS_TO_GET_USERS_WITH_ROLES[1]

        # Act
        response_object = presenter.response_for_user_not_have_permission_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.FORBIDDEN.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_prepare_success_response_for_get_list_of_user_roles_to_given_project_id(
            self, presenter, prepare_basic_user_details_dtos,
            prepare_user_role_dtos, snapshot
    ):
        # Arrange
        basic_user_details_dtos = prepare_basic_user_details_dtos
        user_role_dtos = prepare_user_role_dtos

        # Act
        response = presenter.get_response_for_get_users_with_roles(
            user_role_dtos=user_role_dtos,
            basic_user_details_dtos=basic_user_details_dtos
        )

        # Assert
        response_dict = json.loads(response.content)

        snapshot.assert_match(response_dict, "get_team_specific_details")

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
