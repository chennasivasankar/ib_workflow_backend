import json

from ib_iam.constants.enums import StatusCode


class TestAuthPresenterImplementation:

    def test_raise_exception_for_invalid_email(self):
        # Arrange
        from ib_iam.presenters.auth_presenter_implementation import \
            AuthPresenterImplementation
        presenter = AuthPresenterImplementation()

        from ib_iam.presenters.auth_presenter_implementation import \
            INVALID_EMAIL
        expected_response = INVALID_EMAIL[0]
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = INVALID_EMAIL[1]

        # Act
        response_object = presenter.raise_exception_for_invalid_email()

        # Assert
        response = json.loads(response_object.content)

        assert response['response'] == expected_response
        assert response['http_status_code'] == expected_http_status_code
        assert response['res_status'] == expected_res_status

    def test_raise_exception_for_incorrect_password(self):
        # Arrange
        from ib_iam.presenters.auth_presenter_implementation import \
            AuthPresenterImplementation
        presenter = AuthPresenterImplementation()

        from ib_iam.presenters.auth_presenter_implementation import \
            INCORRECT_PASSWORD
        expected_response = INCORRECT_PASSWORD[0]
        expected_http_status_code = StatusCode.NOT_FOUND.value
        expected_res_status = INCORRECT_PASSWORD[1]

        # Act
        response_object = presenter.raise_exception_for_incorrect_password()

        # Assert
        response = json.loads(response_object.content)

        assert response['response'] == expected_response
        assert response['http_status_code'] == expected_http_status_code
        assert response['res_status'] == expected_res_status

    def test_prepare_response_for_tokens_dto_and_is_admin(self):
        # Arrange
        from ib_iam.adapters.auth_service import UserTokensDTO
        is_admin = True
        tokens_dto = UserTokensDTO(
            access_token="asdfaldskfjdfdlsdkf",
            refresh_token="sadfenkljkdfeller",
            expires_in_seconds=1000,
            user_id="121"
        )

        from ib_iam.presenters.auth_presenter_implementation import \
            AuthPresenterImplementation
        presenter = AuthPresenterImplementation()

        # Act
        response_object = presenter.prepare_response_for_user_tokens_dto_and_is_admin(
            tokens_dto=tokens_dto, is_admin=is_admin
        )
        # Assert
        response = json.loads(response_object.content)

        assert response['access_token'] == tokens_dto.access_token
        assert response['refresh_token'] == tokens_dto.refresh_token
        assert response['expires_in_seconds'] == tokens_dto.expires_in_seconds
        assert response['is_admin'] == is_admin

    def test_raise_exception_for_user_account_does_not_exists(self):
        # Arrange
        from ib_iam.presenters.auth_presenter_implementation import \
            AuthPresenterImplementation
        presenter = AuthPresenterImplementation()

        from ib_iam.presenters.auth_presenter_implementation import \
            USER_ACCOUNT_DOES_NOT_EXIST
        expected_response = USER_ACCOUNT_DOES_NOT_EXIST[0]
        expected_http_status_code = StatusCode.NOT_FOUND.value
        expected_res_status = USER_ACCOUNT_DOES_NOT_EXIST[1]

        # Act
        response_object \
            = presenter.raise_exception_for_user_account_does_not_exists()

        # Assert
        response = json.loads(response_object.content)

        assert response['response'] == expected_response
        assert response['http_status_code'] == expected_http_status_code
        assert response['res_status'] == expected_res_status

    def test_get_success_response_for_reset_password_link_to_user_email(self):
        # Arrange
        from ib_iam.presenters.auth_presenter_implementation import \
            AuthPresenterImplementation
        presenter = AuthPresenterImplementation()

        # Act
        response_object = presenter. \
            get_success_response_for_reset_password_link_to_user_email()

        # Assert
        assert response_object.status_code == StatusCode.SUCCESS.value

    def test_raise_token_does_not_exists(self):
        # Arrange
        from ib_iam.presenters.auth_presenter_implementation import \
            AuthPresenterImplementation
        presenter = AuthPresenterImplementation()

        from ib_iam.presenters.auth_presenter_implementation import \
            TOKEN_DOES_NOT_EXIST
        expected_response = TOKEN_DOES_NOT_EXIST[0]
        expected_http_status_code = StatusCode.NOT_FOUND.value
        expected_res_status = TOKEN_DOES_NOT_EXIST[1]

        # Act
        response_object = presenter.raise_exception_for_token_does_not_exists()

        # Assert
        response = json.loads(response_object.content)

        assert response['response'] == expected_response
        assert response['http_status_code'] == expected_http_status_code
        assert response['res_status'] == expected_res_status

    def test_raise_token_has_expired(self):
        # Arrange
        from ib_iam.presenters.auth_presenter_implementation import \
            AuthPresenterImplementation
        presenter = AuthPresenterImplementation()

        from ib_iam.presenters.auth_presenter_implementation import \
            TOKEN_HAS_EXPIRED
        expected_response = TOKEN_HAS_EXPIRED[0]
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = TOKEN_HAS_EXPIRED[1]

        # Act
        response_object = presenter.raise_exception_for_token_has_expired()

        # Assert
        response = json.loads(response_object.content)

        assert response['response'] == expected_response
        assert response['http_status_code'] == expected_http_status_code
        assert response['res_status'] == expected_res_status

    def test_get_update_user_password_success_response(self):
        # Arrange
        from ib_iam.presenters.auth_presenter_implementation import \
            AuthPresenterImplementation
        presenter = AuthPresenterImplementation()

        # Act
        response_object = presenter. \
            get_update_user_password_success_response()

        # Assert
        assert response_object.status_code == StatusCode.SUCCESS.value

    def test_raise_exception_for_password_min_length_required(self):
        # Arrange
        from ib_iam.presenters.auth_presenter_implementation import \
            AuthPresenterImplementation
        presenter = AuthPresenterImplementation()

        from ib_iam.presenters.auth_presenter_implementation import \
            PASSWORD_MIN_LENGTH
        from ib_iam.constants.config import REQUIRED_PASSWORD_MIN_LENGTH
        expected_response \
            = PASSWORD_MIN_LENGTH[0].format(
            password_min_length=REQUIRED_PASSWORD_MIN_LENGTH
        )
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = PASSWORD_MIN_LENGTH[1]

        # Act
        response_object \
            = presenter.raise_exception_for_password_min_length_required()

        # Assert
        response = json.loads(response_object.content)

        assert response['response'] == expected_response
        assert response['http_status_code'] == expected_http_status_code
        assert response['res_status'] == expected_res_status

    def test_raise_exception_for_password_at_least_one_special_character_required(
            self
    ):
        # Arrange
        from ib_iam.presenters.auth_presenter_implementation import \
            AuthPresenterImplementation
        presenter = AuthPresenterImplementation()

        from ib_iam.presenters.auth_presenter_implementation import \
            PASSWORD_AT_LEAST_ONE_SPECIAL_CHARACTER
        expected_response = PASSWORD_AT_LEAST_ONE_SPECIAL_CHARACTER[0]
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = PASSWORD_AT_LEAST_ONE_SPECIAL_CHARACTER[1]

        # Act
        response_object = presenter.raise_exception_for_password_at_least_one_special_character_required()

        # Assert
        response = json.loads(response_object.content)

        assert response['response'] == expected_response
        assert response['http_status_code'] == expected_http_status_code
        assert response['res_status'] == expected_res_status

    def test_raise_exception_for_login_with_not_verify_email(self):
        # Arrange
        from ib_iam.presenters.auth_presenter_implementation import \
            AuthPresenterImplementation
        presenter = AuthPresenterImplementation()

        from ib_iam.presenters.auth_presenter_implementation import \
            EMAIL_IS_NOT_VERIFY
        expected_response = EMAIL_IS_NOT_VERIFY[0]
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = EMAIL_IS_NOT_VERIFY[1]

        # Act
        response = presenter.raise_exception_for_login_with_not_verify_email()

        # Assert
        actual_response = json.loads(response.content)

        assert actual_response['response'] == expected_response
        assert actual_response['http_status_code'] == expected_http_status_code
        assert actual_response['res_status'] == expected_res_status
