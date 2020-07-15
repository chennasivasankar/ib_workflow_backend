import json


class TestAuthPresenterImplementation:

    def test_raise_invalid_email_exception(self):
        # Arrange
        from ib_iam.presenters.presenter_implementation import \
            AuthPresenterImplementation
        presenter = AuthPresenterImplementation()

        from ib_iam.presenters.presenter_implementation import INVALID_EMAIL
        expected_response = INVALID_EMAIL[0]
        expected_http_status_code = 404
        expected_res_status = INVALID_EMAIL[1]

        # Act
        response_object = presenter.raise_invalid_email()

        # Assert
        response = json.loads(response_object.content)

        assert response['response'] == expected_response
        assert response['http_status_code'] == expected_http_status_code
        assert response['res_status'] == expected_res_status

    def test_raise_invalid_password_exception(self):
        # Arrange
        from ib_iam.presenters.presenter_implementation import \
            AuthPresenterImplementation
        presenter = AuthPresenterImplementation()

        from ib_iam.presenters.presenter_implementation import INVALID_PASSWORD
        expected_response = INVALID_PASSWORD[0]
        expected_http_status_code = 400
        expected_res_status = INVALID_PASSWORD[1]

        # Act
        response_object = presenter.raise_invalid_password()

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
            AuthPresenterImplementation
        presenter = AuthPresenterImplementation()

        # Act
        response_object = presenter.prepare_response_for_tokens_dto(
            tokens_dto=tokens_dto
        )

        # Assert
        response = json.loads(response_object.content)

        assert response['access_token'] == tokens_dto.access_token
        assert response['refresh_token'] == tokens_dto.refresh_token
        assert response['expires_in_seconds'] == tokens_dto.expires_in_seconds

    def test_raise_user_account_does_not_exist(self):
        # Arrange
        from ib_iam.presenters.presenter_implementation import \
            AuthPresenterImplementation
        presenter = AuthPresenterImplementation()

        from ib_iam.presenters.presenter_implementation import \
            USER_ACCOUNT_DOES_NOT_EXIST
        expected_response = USER_ACCOUNT_DOES_NOT_EXIST[0]
        expected_http_status_code = 404
        expected_res_status = USER_ACCOUNT_DOES_NOT_EXIST[1]

        # Act
        response_object = presenter.raise_user_account_does_not_exist()

        # Assert
        response = json.loads(response_object.content)

        assert response['response'] == expected_response
        assert response['http_status_code'] == expected_http_status_code
        assert response['res_status'] == expected_res_status

    def test_get_success_response_for_reset_password_link_to_user_email(self):
        # Arrange
        from ib_iam.presenters.presenter_implementation import \
            AuthPresenterImplementation
        presenter = AuthPresenterImplementation()

        # Act
        response_object \
            = presenter.get_success_response_for_reset_password_link_to_user_email()

        # Assert
        assert response_object.status_code == 200
