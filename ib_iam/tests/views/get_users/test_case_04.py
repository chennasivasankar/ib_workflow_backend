"""
Users list with different possibilities like
some will have only company
some will have only teams
some will have only roles
like wise
"""

from unittest.mock import patch

import pytest
from django_swagger_utils.utils.test_v1 import TestUtils

from ib_iam.tests.common_fixtures.reset_fixture import \
    reset_sequence_for_user_profile_dto_factory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import UserDetailsFactory

USER_ID_01 = '7e39bf1c-f9a5-4e76-8451-b962ddd52011'
TEAM_ID_01 = "6ce31e92-f188-4019-b295-2e5ddc9c7a11"
ROLE_ID_01 = "b9d000c7-c14f-4909-8c5a-6a6c02abb211"
USER_ID_02 = '7e39bf1c-f9a5-4e76-8451-b962ddd52122'
TEAM_ID_02 = "6ce31e92-f188-4019-b295-2e5ddc9c7a22"
ROLE_ID_02 = "b9d000c7-c14f-4909-8c5a-6a6c02abb222"
COMPANY_ID = "b9d000c7-c14f-4909-8c5a-6a6c02abb200"
USER_ID_03 = '7e39bf1c-f9a5-4e76-8451-b962ddd52033'
USER_ID_04 = "b9d000c7-c14f-4909-8c5a-6a6c02abb300"
USER_ID_05 = "b9d000c7-c14f-4909-8c5a-6a6c02abb600"
Company_ID_04 = "b9d000c7-c14f-4909-8c5a-6a6c02abb400"


class TestCase04GetUsersAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture
    def user_set_up(self, api_user):
        user_id = api_user.user_id
        from ib_iam.models import UserDetails
        UserDetails.objects.create(user_id=user_id, is_admin=True)

    @pytest.fixture
    def set_up(self):
        from ib_iam.tests.factories.models \
            import TeamFactory, CompanyFactory, RoleFactory, \
            UserTeamFactory, \
            UserRoleFactory
        from ib_iam.tests.common_fixtures.reset_fixture \
            import reset_sequence_for_model_factories
        reset_sequence_for_model_factories()
        company = CompanyFactory.create(company_id=COMPANY_ID)
        team1 = TeamFactory.create(team_id=TEAM_ID_01)
        role1 = RoleFactory.create(id=ROLE_ID_01)
        team2 = TeamFactory.create(team_id=TEAM_ID_02)
        role2 = RoleFactory.create(id=ROLE_ID_02)
        UserDetailsFactory.create(user_id=USER_ID_01, company=company)
        UserTeamFactory.create(user_id=USER_ID_01, team=team1)
        UserRoleFactory.create(user_id=USER_ID_01, role=role1)
        UserDetailsFactory.create(user_id=USER_ID_02, company=company)
        UserDetailsFactory.create(user_id=USER_ID_03, company=company)
        UserTeamFactory.create(user_id=USER_ID_03, team=team2)
        UserDetailsFactory.create(user_id=USER_ID_04, company=None)
        UserDetailsFactory.create(user_id=USER_ID_05, company=None)
        UserTeamFactory.create(user_id=USER_ID_05, team=team1)
        UserRoleFactory.create(user_id=USER_ID_05, role=role1)

    @pytest.mark.django_db
    @patch(
        "ib_iam.adapters.user_service.UserService.get_user_profile_bulk")
    def test_case(self, get_user_profile_bulk, set_up, user_set_up, snapshot):
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        reset_sequence_for_user_profile_dto_factory()
        get_user_profile_bulk.return_value = [
            UserProfileDTOFactory.create(user_id=USER_ID_01),
            UserProfileDTOFactory.create(user_id=USER_ID_02),
            UserProfileDTOFactory.create(user_id=USER_ID_03),
            UserProfileDTOFactory.create(user_id=USER_ID_04),
            UserProfileDTOFactory.create(user_id=USER_ID_05)
        ]
        body = {}
        path_params = {}
        query_params = {'offset': 0, 'limit': 6}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
