import json

import pytest

from ib_iam.constants.enums import StatusCode


class TestAddSpecificProjectDetailsPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_iam.presenters.add_specific_project_details_presenter_implementation import \
            AddSpecificProjectDetailsPresenterImplementation
        presenter = AddSpecificProjectDetailsPresenterImplementation()
        return presenter

    def test_prepare_success_response_for_add_specific_project_details(
            self, presenter):
        # Act
        response_object = presenter. \
            prepare_success_response_for_add_specific_project_details()

        # Assert
        assert response_object.status_code == StatusCode.SUCCESS_CREATE.value

    def test_response_for_invalid_user_ids_for_project(self, presenter):
        # Arrange
        invalid_user_ids = [
            "01be920b-7b4c-49e7-8adb-41a0c18da848",
            "77be920b-7b4c-49e7-8adb-41a0c18da848"
        ]
        from ib_iam.exceptions.custom_exceptions import InvalidUserIdsForProject
        error_object = InvalidUserIdsForProject(user_ids=invalid_user_ids)

        from ib_iam.presenters.add_specific_project_details_presenter_implementation import \
            INVALID_USER_IDS_FOR_PROJECT
        expected_response = INVALID_USER_IDS_FOR_PROJECT[0].format(
            invalid_user_ids=invalid_user_ids
        )
        response_status_code = INVALID_USER_IDS_FOR_PROJECT[1]

        # Act
        response_object = presenter.response_for_invalid_user_ids_for_project(
            err=error_object
        )

        # Assert
        response = json.loads(response_object.content)

        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_response_for_invalid_role_ids_for_project(self, presenter):
        # Arrange
        invalid_role_ids = [
            "ROLE_3"
        ]
        from ib_iam.exceptions.custom_exceptions import InvalidRoleIdsForProject
        error_object = InvalidRoleIdsForProject(role_ids=invalid_role_ids)

        from ib_iam.presenters.add_specific_project_details_presenter_implementation import \
            INVALID_ROLE_IDS_FOR_PROJECT
        expected_response = INVALID_ROLE_IDS_FOR_PROJECT[0].format(
            invalid_role_ids=invalid_role_ids
        )
        response_status_code = INVALID_ROLE_IDS_FOR_PROJECT[1]

        # Act
        response_object = presenter.response_for_invalid_role_ids_for_project(
            err=error_object
        )

        # Assert
        response = json.loads(response_object.content)

        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response
