import json


class TestLoginPresenterImplementation:

    def test_raise_invalid_email_exception(self):
        # Arrange
        from ib_iam.presenters.presenter_implementation import LoginPresenterImplementation
        preseter = LoginPresenterImplementation()

        from ib_iam.presenters.presenter_implementation import INVALID_EMAIL
        expected_response = INVALID_EMAIL[0]
        expected_http_status_code = 400
        expected_res_status = INVALID_EMAIL[1]

        # Act
        response_object = preseter.raise_invalid_email()

        # Assert
        response = json.loads(response_object.content)

        assert response['response'] == expected_response
        assert response['http_status_code'] == expected_http_status_code
        assert response['res_status'] == expected_res_status

    def test_raise_invalid_password_exception(self):
        # Arrange
        from ib_iam.presenters.presenter_implementation import LoginPresenterImplementation
        preseter = LoginPresenterImplementation()

        from ib_iam.presenters.presenter_implementation import INVALID_PASSWORD
        expected_response = INVALID_PASSWORD[0]
        expected_http_status_code = 400
        expected_res_status = INVALID_PASSWORD[1]

        # Act
        response_object = preseter.raise_invalid_password()

        # Assert
        response = json.loads(response_object.content)

        assert response['response'] == expected_response
        assert response['http_status_code'] == expected_http_status_code
        assert response['res_status'] == expected_res_status

    def test_prepare_response_for_tokens_dto(self):
        # Arrange
        from ib_iam.adapters.auth_service import TokensDTO
        import datetime
        tokens_dto = TokensDTO(
            access_token="asdfaldskfjdfdlsdkf",
            refresh_token="sadfenkljkdfeller",
            expires_in_seconds=1000
        )

        from ib_iam.presenters.presenter_implementation import LoginPresenterImplementation
        preseter = LoginPresenterImplementation()

        # Act
        response_object = preseter.prepare_response_for_tokens_dto(tokens_dto=tokens_dto)

        # Assert
        response = json.loads(response_object.content)

        assert response['access_token'] == tokens_dto.access_token
        assert response['refresh_token'] == tokens_dto.refresh_token
        assert response['expires_in_seconds'] == tokens_dto.expires_in_seconds
