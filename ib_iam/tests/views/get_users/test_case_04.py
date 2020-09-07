"""
Users list with different possibilities like
some will have only company
some will have only teams
some will have only roles
like wise
"""
from typing import Optional

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_iam.tests.common_fixtures.reset_fixture import \
    reset_sequence_for_user_profile_dto_factory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import UserDetailsFactory, UserRoleFactory, \
    ProjectRoleFactory, CompanyFactory, TeamUserFactory, TeamFactory


class TestCase04GetUsersAPITestCase(TestUtils):
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
                "company_id": "b9d000c7-c14f-4909-8c5a-6a6c02abb200"
            },
            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52022",
                "company_id": "b9d000c7-c14f-4909-8c5a-6a6c02abb201"
            },
            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52033",
                "company_id": "b9d000c7-c14f-4909-8c5a-6a6c02abb200"
            },
            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52044",
                "company_id": None
            }
        ]
        from ib_iam.tests.common_fixtures.reset_fixture import \
            reset_sequence_company_factory, reset_sequence_user_details_factory
        reset_sequence_company_factory()
        reset_sequence_user_details_factory()
        users = [UserDetailsFactory.create(
            user_id=user["user_id"],
            company=self._get_or_create_company(company_id=user["company_id"])
        ) for user in users]
        return users

    @staticmethod
    def _get_or_create_company(company_id: Optional[str]):
        if company_id is None:
            return None
        from ib_iam.models import Company
        try:
            return Company.objects.get(company_id=company_id)
        except Company.DoesNotExist:
            return CompanyFactory.create(company_id=company_id)

    @staticmethod
    def _get_or_create_role(role_id: Optional[str]):
        from ib_iam.models import ProjectRole
        try:
            return ProjectRole.objects.get(role_id=role_id)
        except ProjectRole.DoesNotExist:
            return ProjectRoleFactory.create(role_id=role_id)

    @staticmethod
    def _get_or_create_team(team_id: Optional[str]):
        from ib_iam.models import Team
        try:
            return Team.objects.get(team_id=team_id)
        except Team.DoesNotExist:
            return TeamFactory.create(team_id=team_id)

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
            },
            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52033",
                "team_id": "6ce31e92-f188-4019-b295-2e5ddc9c7a22"
            },

            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52033",
                "team_id": "6ce31e92-f188-4019-b295-2e5ddc9c7a11"
            }
        ]
        from ib_iam.tests.common_fixtures.reset_fixture import \
            reset_sequence_team_factory, reset_sequence_user_team_factory
        reset_sequence_team_factory()
        reset_sequence_user_team_factory()
        user_team_objects = [TeamUserFactory.create(
            user_id=user_team["user_id"],
            team=self._get_or_create_team(team_id=user_team["team_id"])
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
            },
            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52044",
                "role_id": "b9d000c7-c14f-4909-8c5a-6a6c02abb211"
            },
            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52044",
                "role_id": "b9d000c7-c14f-4909-8c5a-6a6c02abb222"
            }
        ]
        from ib_iam.tests.common_fixtures.reset_fixture import \
            reset_sequence_role_factory, reset_sequence_user_role_factory
        reset_sequence_user_role_factory()
        reset_sequence_role_factory()
        user_role_objects = [UserRoleFactory.create(
            user_id=user_role["user_id"],
            project_role=self._get_or_create_role(role_id=user_role["role_id"])
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
        ib_users = [
            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52011"
            },
            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52022"
            },
            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52033"
            },
            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52044"
            }
        ]
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        reset_sequence_for_user_profile_dto_factory()
        get_user_profile_bulk_mock.return_value = [
            UserProfileDTOFactory.create(user_id=user["user_id"])
            for user in ib_users
        ]
        body = {}
        path_params = {}
        query_params = {'offset': 0, 'limit': 6, 'search_query': ''}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
