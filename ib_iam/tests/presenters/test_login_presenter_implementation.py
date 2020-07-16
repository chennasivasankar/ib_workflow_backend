import json


class TestLoginPresenterImplementation:

    def test_raise_exception_for_invalid_email(self):
        # Arrange
        from ib_iam.presenters.presenter_implementation import \
            LoginPresenterImplementation
        presenter = LoginPresenterImplementation()

        from ib_iam.presenters.presenter_implementation import INVALID_EMAIL
        expected_response = INVALID_EMAIL[0]
        expected_http_status_code = 400
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
        from ib_iam.presenters.presenter_implementation import \
            LoginPresenterImplementation
        presenter = LoginPresenterImplementation()

        from ib_iam.presenters.presenter_implementation import \
            INCORRECT_PASSWORD
        expected_response = INCORRECT_PASSWORD[0]
        expected_http_status_code = 404
        expected_res_status = INCORRECT_PASSWORD[1]

        # Act
        response_object = presenter.raise_exception_for_incorrect_password()

        # Assert
        response = json.loads(response_object.content)

        assert response['response'] == expected_response
        assert response['http_status_code'] == expected_http_status_code
        assert response['res_status'] == expected_res_status

    def test_prepare_response_for_tokens_dto(self):
        # Arrange
        from ib_iam.adapters.auth_service import TokensDTO
        tokens_dto = TokensDTO(
            access_token="asdfaldskfjdfdlsdkf",
            refresh_token="sadfenkljkdfeller",
            expires_in_seconds=1000
        )

        from ib_iam.presenters.presenter_implementation import \
            LoginPresenterImplementation
        presenter = LoginPresenterImplementation()

        # Act
        response_object = presenter.prepare_response_for_tokens_dto(
            tokens_dto=tokens_dto
        )

        # Assert
        response = json.loads(response_object.content)

        assert response['access_token'] == tokens_dto.access_token
        assert response['refresh_token'] == tokens_dto.refresh_token
        assert response['expires_in_seconds'] == tokens_dto.expires_in_seconds

    def test_raise_exception_for_user_account_does_not_exists(self):
        # Arrange
        from ib_iam.presenters.presenter_implementation import \
            LoginPresenterImplementation
        presenter = LoginPresenterImplementation()

        from ib_iam.presenters.presenter_implementation import \
            USER_ACCOUNT_DOES_NOT_EXIST
        expected_response = USER_ACCOUNT_DOES_NOT_EXIST[0]
        expected_http_status_code = 404
        expected_res_status = USER_ACCOUNT_DOES_NOT_EXIST[1]

        # Act
        response_object \
            = presenter.raise_exception_for_user_account_does_not_exists()

        # Assert
        response = json.loads(response_object.content)

        assert response['response'] == expected_response
        assert response['http_status_code'] == expected_http_status_code
        assert response['res_status'] == expected_res_status

    def test_raise_exception_for_password_min_length_required(self):
        # Arrange
        from ib_iam.presenters.presenter_implementation import \
            LoginPresenterImplementation
        presenter = LoginPresenterImplementation()

        from ib_iam.presenters.presenter_implementation import \
            PASSWORD_MIN_LENGTH
        from ib_iam.conf.settings import REQUIRED_PASSWORD_MIN_LENGTH
        expected_response \
            = PASSWORD_MIN_LENGTH[0] % REQUIRED_PASSWORD_MIN_LENGTH
        expected_http_status_code = 400
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
            self):
        # Arrange
        from ib_iam.presenters.presenter_implementation import \
            LoginPresenterImplementation
        presenter = LoginPresenterImplementation()

        from ib_iam.presenters.presenter_implementation import \
            PASSWORD_AT_LEAST_ONE_SPECIAL_CHARACTER
        expected_response = PASSWORD_AT_LEAST_ONE_SPECIAL_CHARACTER[0]
        expected_http_status_code = 400
        expected_res_status = PASSWORD_AT_LEAST_ONE_SPECIAL_CHARACTER[1]

        # Act
        response_object = presenter.raise_exception_for_password_at_least_one_special_character_required()

        # Assert
        response = json.loads(response_object.content)

        assert response['response'] == expected_response
        assert response['http_status_code'] == expected_http_status_code
        assert response['res_status'] == expected_res_status
