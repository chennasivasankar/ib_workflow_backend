import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_iam.tests.common_fixtures.reset_fixture import \
    reset_sequence_for_user_profile_dto_factory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import UserDetailsFactory, CompanyFactory, \
    UserTeamFactory, TeamFactory, UserRoleFactory, RoleFactory


class TestCase03GetUsersAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture()
    def users_set_up(self):
        users = [
            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52011",
                "name": "durga"
            },
            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52022",
                "name": "devi"
            },
            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52033",
                "name": "raju"
            }
        ]
        from ib_iam.tests.common_fixtures.reset_fixture import \
            reset_sequence_company_factory, reset_sequence_user_details_factory
        reset_sequence_company_factory()
        reset_sequence_user_details_factory()
        company_object = CompanyFactory.create(
            company_id="b9d000c7-c14f-4909-8c5a-6a6c02abb200")
        users = [UserDetailsFactory.create(
            user_id=user["user_id"], name=user["name"], company=company_object)
            for user in users]
        return users, company_object

    @pytest.fixture()
    def user_teams_set_up(self):
        user_teams = [
            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52011",
                "team_id": "6ce31e92-f188-4019-b295-2e5ddc9c7a11"
            },
            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52022",
                "team_id": "6ce31e92-f188-4019-b295-2e5ddc9c7a22"
            }
        ]
        from ib_iam.tests.common_fixtures.reset_fixture import \
            reset_sequence_team_factory, reset_sequence_user_team_factory
        reset_sequence_team_factory()
        reset_sequence_user_team_factory()
        user_team_objects = [UserTeamFactory.create(
            user_id=user_team["user_id"],
            team=TeamFactory.create(team_id=user_team["team_id"])
        ) for user_team in user_teams]
        return user_team_objects

    @pytest.fixture()
    def user_roles_set_up(self):
        user_roles = [
            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52011",
                "role_id": "b9d000c7-c14f-4909-8c5a-6a6c02abb211"
            },
            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52022",
                "role_id": "b9d000c7-c14f-4909-8c5a-6a6c02abb222"
            }
        ]
        from ib_iam.tests.common_fixtures.reset_fixture import \
            reset_sequence_role_factory, reset_sequence_user_role_factory
        reset_sequence_user_role_factory()
        reset_sequence_role_factory()
        user_role_objects = [UserRoleFactory.create(
            user_id=user_role["user_id"],
            role=RoleFactory.create(role_id=user_role["role_id"])
        ) for user_role in user_roles]
        return user_role_objects

    @pytest.fixture()
    def setup(self, api_user):
        user_id = api_user.user_id
        from ib_iam.tests.common_fixtures.reset_fixture \
            import reset_sequence_user_details_factory
        reset_sequence_user_details_factory()
        from ib_iam.tests.factories.models import UserDetailsFactory
        admin_user = UserDetailsFactory.create(user_id=user_id, is_admin=True,
                                               company=None)
        return admin_user

    @pytest.mark.django_db
    def test_case(self, setup, users_set_up, user_teams_set_up,
                  user_roles_set_up, snapshot, mocker):
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dtos_mock
        get_user_profile_bulk_mock = prepare_get_user_profile_dtos_mock(
            mocker=mocker)
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        reset_sequence_for_user_profile_dto_factory()
        ib_users = [
            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52011",
                "name": "durga"
            },
            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52022",
                "name": "devi"
            }
        ]
        get_user_profile_bulk_mock.return_value = [
            UserProfileDTOFactory.create(user_id=user["user_id"],
                                         name=user["name"])
            for user in ib_users
        ]
        body = {}
        path_params = {}
        query_params = {'offset': 0, 'limit': 2, 'search_query': 'd'}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
