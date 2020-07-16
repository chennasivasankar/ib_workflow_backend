"""
# TODO: Update test case description
"""
from unittest.mock import patch

import pytest
from django_swagger_utils.utils.test_v1 import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import UserProfileFactory, CompanyFactory

USER_ID = '7e39bf1c-f9a5-4e76-8451-b962ddd520fc'
TEAM_ID = "6ce31e92-f188-4019-b295-2e5ddc9c7a17"
ROLE_ID = "b9d000c7-c14f-4909-8c5a-6a6c02abb226"
COMPANY_ID = "b9d000c7-c14f-4909-8c5a-6a6c02abb222"


class TestCase03GetUsersAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    # @pytest.fixture
    # def set_up(self):

    @pytest.fixture
    def set_up(self, api_user):
        user_id = api_user.id
        from ib_iam.models import UserProfile
        UserProfile.objects.create(user_id=user_id, is_admin=True)
        from ib_iam.tests.factories.models \
            import TeamFactory, CompanyFactory, RoleFactory, \
            UserTeamFactory, \
            UserRoleFactory
        company = CompanyFactory.create(company_id=COMPANY_ID)
        team = TeamFactory.create(team_id=TEAM_ID)
        role = RoleFactory.create(id=ROLE_ID)
        UserProfileFactory.create(user_id=USER_ID, company=company)
        UserTeamFactory.create(user_id=USER_ID, team=team)
        UserRoleFactory.create(user_id=USER_ID, role=role)

    @pytest.mark.django_db
    @patch(
        "ib_iam.adapters.user_service.UserService.get_user_profile_bulk")
    def test_case(self, get_user_profile_bulk, set_up, snapshot):
        from ib_iam.tests.factories.adapter_dtos import UserDTOFactory
        get_user_profile_bulk.return_value = [UserDTOFactory.create(user_id=USER_ID)]
        body = {}
        path_params = {}
        query_params = {'offset': 0, 'limit': 5}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
