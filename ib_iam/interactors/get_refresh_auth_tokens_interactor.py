from ib_iam.interactors.presenter_interfaces.get_refresh_auth_tokens_presenter_interface import \
    GetRefreshTokensPresenterInterface


class GetRefreshTokensInteractor:

    def get_refresh_tokens_wrapper(
            self, access_token: str, refresh_token: str,
            presenter: GetRefreshTokensPresenterInterface
    ):
        from ib_iam.adapters.auth_service import (
            AccessTokenNotFound, UserAccountNotFound,
            RefreshTokenHasExpired, RefreshTokenHasNotFound
        )
        try:
            response = self._get_refresh_tokens_response(
                access_token=access_token, presenter=presenter,
                refresh_token=refresh_token
            )
        except AccessTokenNotFound:
            response = presenter.response_for_access_token_not_found()
        except RefreshTokenHasExpired:
            response = presenter.response_for_refresh_token_expired()
        except RefreshTokenHasNotFound:
            response = presenter.response_for_refresh_token_not_found()
        except UserAccountNotFound:
            response = presenter.response_for_user_account_not_found()
        return response

    def _get_refresh_tokens_response(
            self, access_token: str, refresh_token: str,
            presenter: GetRefreshTokensPresenterInterface,
    ):
        user_tokens_dto = self.get_refresh_tokens(
            access_token=access_token, refresh_token=refresh_token
        )
        response = presenter.response_for_user_tokens_dto(
            user_tokens_dto=user_tokens_dto)
        return response

    @staticmethod
    def get_refresh_tokens(access_token: str, refresh_token: str):
        from ib_iam.adapters.service_adapter import ServiceAdapter
        service_adapter = ServiceAdapter()
        user_tokens_dto = \
            service_adapter.auth_service.get_refresh_auth_tokens_dto(
                access_token=access_token, refresh_token=refresh_token
            )
        return user_tokens_dto
