"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX

COMPANY_ID = "b9d000c7-c14f-4909-8c5a-6a6c02abb200"
TEAM_IDS = ["6ce31e92-f188-4019-b295-2e5ddc9c7a11",
            "6ce31e92-f188-4019-b295-2e5ddc9c7a22",
            "6ce31e92-f188-4019-b295-2e5ddc9c7a33"]
ROLE_IDS = ["b9d000c7-c14f-4909-8c5a-6a6c02abb211",
            "b9d000c7-c14f-4909-8c5a-6a6c02abb222",
            "b9d000c7-c14f-4909-8c5a-6a6c02abb233"]
USER_IDS = ['7e39bf1c-f9a5-4e76-8451-b962ddd52011',
            '7e39bf1c-f9a5-4e76-8451-b962ddd52122',
            '7e39bf1c-f9a5-4e76-8451-b962ddd52033']


class TestCase02GetConfigurationDetailsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture
    def user_set_up(self, api_user):
        user_id = api_user.user_id
        from ib_iam.tests.factories.models import UserDetailsFactory
        from ib_iam.tests.common_fixtures.reset_fixture \
            import reset_sequence_user_details_factory
        reset_sequence_user_details_factory()
        UserDetailsFactory.create(user_id=user_id, is_admin=True, company=None)

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
        teams = [TeamFactory.create(team_id=team_id) for team_id in TEAM_IDS]
        roles = [RoleFactory.create(id=role_id) for role_id in ROLE_IDS]
        for count, user_id in enumerate(USER_IDS):
            from ib_iam.tests.factories.models import UserDetailsFactory
            UserDetailsFactory.create(user_id=user_id, company=company)
            UserTeamFactory.create(user_id=user_id, team=teams[count])
            UserRoleFactory.create(user_id=user_id, role=roles[count])

    @pytest.mark.django_db
    def test_case(self, set_up, user_set_up, snapshot):
        body = {}
        path_params = {}
        query_params = {}
        headers = {}
        self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
