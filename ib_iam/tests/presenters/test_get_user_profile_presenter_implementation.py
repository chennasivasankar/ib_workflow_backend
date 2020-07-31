import json

import pytest


class TestGetUserProfilePresenterImplementation:

    @pytest.fixture()
    def presenter_implementation(self):
        from ib_iam.presenters.get_user_profile_presenter_implementation \
            import GetUserProfilePresenterImplementation
        presenter = GetUserProfilePresenterImplementation()
        return presenter

    def test_raise_exception_for_invalid_user_id(self,
                                                 presenter_implementation):
        # Arrange
        from ib_iam.presenters.get_user_profile_presenter_implementation \
            import INVALID_USER_ID
        expected_response = INVALID_USER_ID[0]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = INVALID_USER_ID[1]

        # Act
        response_object \
            = presenter_implementation.raise_exception_for_invalid_user_id()

        # Assert
        response_data = json.loads(response_object.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_raise_exception_for_user_account_does_not_exist(
            self, presenter_implementation
    ):
        # Arrange
        from ib_iam.presenters.get_user_profile_presenter_implementation \
            import USER_ACCOUNT_DOES_NOT_EXIST
        expected_response = USER_ACCOUNT_DOES_NOT_EXIST[0]
        from ib_iam.constants.enums import StatusCode
        expected_http_status_code = StatusCode.NOT_FOUND.value
        expected_res_status = USER_ACCOUNT_DOES_NOT_EXIST[1]

        # Act
        response_object = presenter_implementation. \
            raise_exception_for_user_account_does_not_exist()

        # Assert
        response_data = json.loads(response_object.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_prepare_response_for_user_profile_dto(self,
                                                   presenter_implementation):
        # Arrange
        from ib_iam.adapters.dtos import UserProfileDTO
        user_id = "eca1a0c1-b9ef-4e59-b415-60a28ef17b10"
        user_profile_dto = UserProfileDTO(
            user_id=user_id,
            email="test@gmail.com",
            profile_pic_url="test.com",
            is_admin=True,
            name="test"
        )
        expected_response = {
            'user_id': 'eca1a0c1-b9ef-4e59-b415-60a28ef17b10',
            'name': 'test',
            'is_admin': True,
            'email': 'test@gmail.com',
            'profile_pic_url': 'test.com'
        }

        # Act
        response_object = presenter_implementation. \
            prepare_response_for_user_profile_dto(user_profile_dto)

        # Assert
        response_data = json.loads(response_object.content)

        assert response_data == expected_response
