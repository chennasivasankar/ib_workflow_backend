import json

import pytest

from ib_iam.constants.enums import StatusCode


class TestGetRefreshTokensPresenterImplementation:

    @pytest.fixture()
    def presenter(self):
        from ib_iam.presenters.get_refresh_auth_tokens_presenter_implementation import \
            GetRefreshTokensPresenterImplementation
        presenter = GetRefreshTokensPresenterImplementation()
        return presenter

    def test_response_for_access_token_not_found(self, presenter):
        # Arrange
        from ib_iam.presenters.get_refresh_auth_tokens_presenter_implementation import \
            ACCESS_TOKEN_NOT_FOUND
        expected_response = ACCESS_TOKEN_NOT_FOUND[0]
        expected_http_status_code = StatusCode.NOT_FOUND.value
        expected_res_status = ACCESS_TOKEN_NOT_FOUND[1]

        # Act
        response_object = presenter.response_for_access_token_not_found()

        # Assert
        response_data = json.loads(response_object.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_response_for_refresh_token_expired(self, presenter):
        # Arrange
        from ib_iam.presenters.get_refresh_auth_tokens_presenter_implementation import \
            REFRESH_TOKEN_HAS_EXPIRED
        expected_response = REFRESH_TOKEN_HAS_EXPIRED[0]
        expected_http_status_code = StatusCode.BAD_REQUEST.value
        expected_res_status = REFRESH_TOKEN_HAS_EXPIRED[1]

        # Act
        response_object = presenter.response_for_refresh_token_expired()

        # Assert
        response_data = json.loads(response_object.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_response_for_refresh_token_not_found(self, presenter):
        # Arrange
        from ib_iam.presenters.get_refresh_auth_tokens_presenter_implementation import \
            REFRESH_TOKEN_NOT_FOUND
        expected_response = REFRESH_TOKEN_NOT_FOUND[0]
        expected_http_status_code = StatusCode.NOT_FOUND.value
        expected_res_status = REFRESH_TOKEN_NOT_FOUND[1]

        # Act
        response_object = presenter.response_for_refresh_token_not_found()

        # Assert
        response_data = json.loads(response_object.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_response_for_user_account_not_found(self, presenter):
        # Arrange
        from ib_iam.presenters.get_refresh_auth_tokens_presenter_implementation import \
            USER_ACCOUNT_NOT_FOUND
        expected_response = USER_ACCOUNT_NOT_FOUND[0]
        expected_http_status_code = StatusCode.NOT_FOUND.value
        expected_res_status = USER_ACCOUNT_NOT_FOUND[1]

        # Act
        response_object = presenter.response_for_user_account_not_found()

        # Assert
        response_data = json.loads(response_object.content)

        assert response_data["response"] == expected_response
        assert response_data["http_status_code"] == expected_http_status_code
        assert response_data["res_status"] == expected_res_status

    def test_response_for_user_tokens_dto(self, presenter):
        # Arrange
        access_token = "rNYAlle5thjiWD5MIt63GkhAws5suQ"
        refresh_token = "pNYAlle5thjiWD5MIt63GkhAws5suQ"
        expected_output = {
            'access_token': 'rNYAlle5thjiWD5MIt63GkhAws5suQ',
            'refresh_token': 'pNYAlle5thjiWD5MIt63GkhAws5suQ',
            'expires_in_seconds': 5647665599
        }

        from ib_iam.adapters.dtos import UserTokensDTO
        user_tokens_dto = UserTokensDTO(
            access_token=access_token,
            refresh_token=refresh_token,
            expires_in_seconds=5647665599,
            user_id='11'
        )

        # Act
        response_object = presenter.response_for_user_tokens_dto(
            user_tokens_dto=user_tokens_dto
        )

        # Assert
        response_data = json.loads(response_object.content)

        assert response_data == expected_output
