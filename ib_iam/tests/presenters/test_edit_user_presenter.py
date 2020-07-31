import json

from ib_iam.constants.enums import StatusCode
from ib_iam.presenters.edit_user_presenter_implementation \
    import EditUserPresenterImplementation


class TestEditUserPresenter:
    def test_edit_user_response_successfull_returns_success_response(self):
        # Arrange
        presenter = EditUserPresenterImplementation()
        from ib_iam.constants.exception_messages \
            import EDIT_USER_SUCCESSFULLY
        expected_response = EDIT_USER_SUCCESSFULLY[0]
        response_status_code = EDIT_USER_SUCCESSFULLY[1]

        # Act
        response_object = presenter.edit_user_success_response()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.SUCCESS.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_invalid_name_exception(self):
        # Arrange
        presenter = EditUserPresenterImplementation()
        from ib_iam.constants.exception_messages import EMPTY_NAME_IS_INVALID
        expected_response = EMPTY_NAME_IS_INVALID[0]
        response_status_code = EMPTY_NAME_IS_INVALID[1]

        # Act
        response_object = presenter.raise_invalid_name_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_name_should_not_contain_special_characters_exception(self):
        # Arrange
        presenter = EditUserPresenterImplementation()
        from ib_iam.constants.exception_messages \
            import NAME_SHOULD_NOT_CONTAINS_SPECIAL_CHARACTERS_AND_NUMBERS
        expected_response = \
            NAME_SHOULD_NOT_CONTAINS_SPECIAL_CHARACTERS_AND_NUMBERS[0]
        response_status_code = \
            NAME_SHOULD_NOT_CONTAINS_SPECIAL_CHARACTERS_AND_NUMBERS[1]

        # Act
        response_object = presenter. \
            raise_name_should_not_contain_special_characters_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_invalid_email_exception(self):
        # Arrange
        presenter = EditUserPresenterImplementation()
        from ib_iam.constants.exception_messages import INVALID_EMAIL
        expected_response = INVALID_EMAIL[0]
        response_status_code = INVALID_EMAIL[1]

        # Act
        response_object = presenter.raise_invalid_email_exception()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.BAD_REQUEST.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_invalid_role_ids_exception(self):
        # Arrange
        presenter = EditUserPresenterImplementation()
        from ib_iam.constants.exception_messages import INVALID_ROLE_IDS
        expected_response = INVALID_ROLE_IDS[0]
        response_status_code = INVALID_ROLE_IDS[1]

        # Act
        response_object = presenter.raise_role_ids_are_invalid()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.NOT_FOUND.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_invalid_company_id_exception(self):
        # Arrange
        presenter = EditUserPresenterImplementation()
        from ib_iam.constants.exception_messages import INVALID_COMPANY_ID
        expected_response = INVALID_COMPANY_ID[0]
        response_status_code = INVALID_COMPANY_ID[1]

        # Act
        response_object = presenter.raise_company_ids_is_invalid()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.NOT_FOUND.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_invalid_team_ids_exception(self):
        # Arrange
        presenter = EditUserPresenterImplementation()
        from ib_iam.constants.exception_messages import INVALID_TEAM_IDS
        expected_response = INVALID_TEAM_IDS[0]
        response_status_code = INVALID_TEAM_IDS[1]

        # Act
        response_object = presenter.raise_team_ids_are_invalid()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.NOT_FOUND.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response

    def test_raise_user_does_not_exist_exception(self):
        # Arrange
        presenter = EditUserPresenterImplementation()
        from ib_iam.constants.exception_messages import USER_DOES_NOT_EXIST
        expected_response = USER_DOES_NOT_EXIST[0]
        response_status_code = USER_DOES_NOT_EXIST[1]

        # Act
        response_object = presenter.raise_user_does_not_exist()

        # Assert
        response = json.loads(response_object.content)
        assert response['http_status_code'] == StatusCode.NOT_FOUND.value
        assert response['res_status'] == response_status_code
        assert response['response'] == expected_response