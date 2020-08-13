# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot


snapshots = Snapshot()

snapshots['TestCase01RefreshTokensAPITestCase.test_with_invalid_access_token_return_response status_code'] = '404'

snapshots['TestCase01RefreshTokensAPITestCase.test_with_invalid_access_token_return_response body'] = {
    'http_status_code': 404,
    'res_status': 'ACCESS_TOKEN_NOT_FOUND',
    'response': 'Please send valid access token, to get refresh tokens'
}

snapshots['TestCase01RefreshTokensAPITestCase.test_with_refresh_token_expire_return_response status_code'] = '400'

snapshots['TestCase01RefreshTokensAPITestCase.test_with_refresh_token_expire_return_response body'] = {
    'http_status_code': 400,
    'res_status': 'REFRESH_TOKEN_HAS_EXPIRED',
    'response': 'Please send valid refresh token, send refresh token expired'
}

snapshots['TestCase01RefreshTokensAPITestCase.test_with_refresh_token_not_found_return_response status_code'] = '404'

snapshots['TestCase01RefreshTokensAPITestCase.test_with_refresh_token_not_found_return_response body'] = {
    'http_status_code': 404,
    'res_status': 'REFRESH_TOKEN_NOT_FOUND',
    'response': 'Please send valid refresh token, your refresh token not found'
}

snapshots['TestCase01RefreshTokensAPITestCase.test_with_user_account_not_found_return_response status_code'] = '404'

snapshots['TestCase01RefreshTokensAPITestCase.test_with_user_account_not_found_return_response body'] = {
    'http_status_code': 404,
    'res_status': 'USER_ACCOUNT_NOT_FOUND',
    'response': 'Please send valid access token, your account is not found'
}
