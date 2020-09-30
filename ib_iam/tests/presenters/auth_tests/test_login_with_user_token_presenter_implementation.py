import json


class TestLoginWithUserTokePresenterImplementation:

    def test_prepare_response_for_tokens_dto_and_is_admin(self):
        # Arrange
        from ib_iam.adapters.dtos import UserTokensDTO
        is_admin = True
        tokens_dto = UserTokensDTO(
            access_token="access_token",
            refresh_token="refresh_token",
            expires_in_seconds=1000,
            user_id="121"
        )

        from ib_iam.presenters.login_with_user_token_presenter_implementation \
            import LoginWithUserTokePresenterImplementation
        presenter = LoginWithUserTokePresenterImplementation()

        # Act
        response_object = presenter \
            .prepare_response_for_user_tokens_dto_and_is_admin(
            tokens_dto=tokens_dto, is_admin=is_admin
        )

        # Assert
        response = json.loads(response_object.content)

        assert response['access_token'] == tokens_dto.access_token
        assert response['refresh_token'] == tokens_dto.refresh_token
        assert response['expires_in_seconds'] == tokens_dto.expires_in_seconds
        assert response['is_admin'] == is_admin
