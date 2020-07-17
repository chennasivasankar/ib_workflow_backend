from unittest.mock import patch

import pytest
from django_swagger_utils.utils.test_v1 import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import UserProfileFactory

USER_ID_01 = '7e39bf1c-f9a5-4e76-8451-b962ddd52011'
TEAM_ID_01 = "6ce31e92-f188-4019-b295-2e5ddc9c7a11"
ROLE_ID_01 = "b9d000c7-c14f-4909-8c5a-6a6c02abb211"
USER_ID_02 = '7e39bf1c-f9a5-4e76-8451-b962ddd52122'
TEAM_ID_02 = "6ce31e92-f188-4019-b295-2e5ddc9c7a22"
ROLE_ID_02 = "b9d000c7-c14f-4909-8c5a-6a6c02abb222"
COMPANY_ID = "b9d000c7-c14f-4909-8c5a-6a6c02abb200"
USER_ID_03 = '7e39bf1c-f9a5-4e76-8451-b962ddd52033'


class TestCase03GetUsersAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture
    def user_set_up(self, api_user):
        user_id = api_user.id
        from ib_iam.models import UserDetails
        UserDetails.objects.create(user_id=user_id, is_admin=True)

    @pytest.fixture
    def set_up(self):
        from ib_iam.tests.factories.models \
            import TeamFactory, CompanyFactory, RoleFactory, \
            UserTeamFactory, \
            UserRoleFactory
        from ib_iam.tests.common_fixtures.storages import reset_sequence
        reset_sequence()
        company = CompanyFactory.create(company_id=COMPANY_ID)
        team1 = TeamFactory.create(team_id=TEAM_ID_01)
        role1 = RoleFactory.create(id=ROLE_ID_01)
        team2 = TeamFactory.create(team_id=TEAM_ID_02)
        role2 = RoleFactory.create(id=ROLE_ID_02)
        UserProfileFactory.create(user_id=USER_ID_01, company=company)
        UserTeamFactory.create(user_id=USER_ID_01, team=team1)
        UserRoleFactory.create(user_id=USER_ID_01, role=role1)
        UserProfileFactory.create(user_id=USER_ID_02, company=company)
        UserTeamFactory.create(user_id=USER_ID_02, team=team2)
        UserRoleFactory.create(user_id=USER_ID_02, role=role2)
        UserProfileFactory.create(user_id=USER_ID_03, company=company)
        UserTeamFactory.create(user_id=USER_ID_03, team=team2)
        UserRoleFactory.create(user_id=USER_ID_03, role=role2)

    @pytest.mark.django_db
    @patch(
        "ib_iam.adapters.user_service.UserService.get_user_profile_bulk")
    def test_case(self, get_user_profile_bulk, set_up, user_set_up, snapshot):
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory

        get_user_profile_bulk.return_value = [
            UserProfileDTOFactory.create(user_id=USER_ID_01),
            UserProfileDTOFactory.create(user_id=USER_ID_02),
            UserProfileDTOFactory.create(user_id=USER_ID_03)
        ]
        body = {}
        path_params = {}
        query_params = {'offset': 0, 'limit': 5}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
