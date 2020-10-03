# -*- coding: utf-8 -*-
# snapshottest: v1 - https://goo.gl/zC4yUc
from __future__ import unicode_literals

from snapshottest import Snapshot, GenericRepr


snapshots = Snapshot()

snapshots['TestCase02UserLoginWithTokenAPITestCase.test_auth_user_not_already_exist_returns_response status_code'] = '200'

snapshots['TestCase02UserLoginWithTokenAPITestCase.test_auth_user_not_already_exist_returns_response body'] = {
    'access_token': 'access_token_0',
    'expires_in_seconds': 10000000000,
    'is_admin': False,
    'refresh_token': 'refresh_token_token_0'
}

snapshots['TestCase02UserLoginWithTokenAPITestCase.test_auth_user_not_already_exist_returns_response UserAuthDetails'] = {
    'auth_token_user_id': '89d96f4b-c19d-4e69-8eae-e818f3123b09',
    'id': 1,
    'token': 'token1',
    'user_id': '89d96f4b-c19d-4e69-8eae-e818f3123b09'
}

snapshots['TestCase02UserLoginWithTokenAPITestCase.test_auth_user_not_already_exist_returns_response UserDetails'] = {
    'company_id': None,
    'cover_page_url': None,
    'id': 1,
    'is_admin': False,
    'name': 'username',
    'user_id': '89d96f4b-c19d-4e69-8eae-e818f3123b09'
}

snapshots['TestCase02UserLoginWithTokenAPITestCase.test_auth_user_not_already_exist_returns_response TeamUsers'] = {
    'id': 1,
    'immediate_superior_team_user_id': None,
    'team_id': GenericRepr("UUID('b8cb1520-279a-44bb-95bf-bbca3aa057ba')"),
    'user_id': '89d96f4b-c19d-4e69-8eae-e818f3123b09'
}

snapshots['TestCase02UserLoginWithTokenAPITestCase.test_auth_user_not_already_exist_returns_response TeamMemberLevels'] = {
    'level_hierarchy': 0,
    'level_name': 'level_0',
    'team_id': GenericRepr("UUID('b8cb1520-279a-44bb-95bf-bbca3aa057ba')")
}

snapshots['TestCase02UserLoginWithTokenAPITestCase.test_auth_user_not_already_exist_returns_response UserRoles'] = [
    {
        'id': 1,
        'project_role_id': 'ROLE_1',
        'user_id': '89d96f4b-c19d-4e69-8eae-e818f3123b09'
    },
    {
        'id': 2,
        'project_role_id': 'ROLE_2',
        'user_id': '89d96f4b-c19d-4e69-8eae-e818f3123b09'
    }
]
