"""
1. User does not exist exception test
2. success test with all details
"""
from typing import Optional

import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from ib_users.models import UserAccount

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetUserProfileAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_user_account_does_not_exist(self, mocker, snapshot):
        body = {}
        path_params = {}
        query_params = {}
        headers = {}

        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dto_mock
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(mocker)
        from ib_iam.adapters.user_service import UserAccountDoesNotExist
        get_user_profile_dto_mock.side_effect = UserAccountDoesNotExist
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    def _get_or_create_user(self):
        user_id = '217abeb3-6466-4440-96e7-bf02ee941bf8'
        user = UserAccount.objects.create(user_id=user_id)
        return user

    @pytest.mark.django_db
    def test_given_valid_user_id_returns_user_profile_data(
            self, user_teams_set_up, user_roles_set_up,
            adapters_mock_setup, snapshot):
        body = {}
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.fixture
    def adapters_mock_setup(self, users_set_up, mocker):
        login_user_id = '217abeb3-6466-4440-96e7-bf02ee941bf8'
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import (
            get_basic_user_profile_dtos_mock)
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dto_mock
        user_ids = self._get_user_ids_from_objects(user_objects=users_set_up)
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        UserProfileDTOFactory.reset_sequence(1)
        user_dtos = [UserProfileDTOFactory(user_id=user_id)
                     for user_id in user_ids]
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(mocker)
        for user_dto in user_dtos:
            if user_dto.user_id == login_user_id:
                login_user_profile_dto = user_dto
                get_user_profile_dto_mock.return_value = login_user_profile_dto
        get_basic_user_dtos_mock = get_basic_user_profile_dtos_mock(mocker)
        get_basic_user_dtos_mock.return_value = user_dtos

    @pytest.fixture()
    def users_set_up(self):
        users = [
            {
                "user_id": "217abeb3-6466-4440-96e7-bf02ee941bf8",
                "company_id": "b9d000c7-c14f-4909-8c5a-6a6c02abb200"
            },
            {
                "user_id": "4b8fb6eb-fa7d-47c1-8726-cd917901104e",
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
        from ib_iam.tests.factories.models import UserDetailsFactory
        users = [UserDetailsFactory.create(
            user_id=user["user_id"],
            company=self._get_or_create_company(company_id=user["company_id"])
        ) for user in users]
        return users

    @pytest.fixture()
    def user_teams_set_up(self):
        user_teams = [
            {
                "user_id": "217abeb3-6466-4440-96e7-bf02ee941bf8",
                "team_id": "6ce31e92-f188-4019-b295-2e5ddc9c7a11"
            },
            {
                "user_id": "7e39bf1c-f9a5-4e76-8451-b962ddd52044",
                "team_id": "6ce31e92-f188-4019-b295-2e5ddc9c7a11"
            }
        ]
        from ib_iam.tests.common_fixtures.reset_fixture import \
            reset_sequence_team_factory, reset_sequence_user_team_factory
        reset_sequence_team_factory()
        reset_sequence_user_team_factory()
        from ib_iam.tests.factories.models import TeamUserFactory
        user_team_objects = [TeamUserFactory.create(
            user_id=user_team["user_id"],
            team=self._get_or_create_team(team_id=user_team["team_id"])
        ) for user_team in user_teams]
        return user_team_objects

    @pytest.fixture()
    def user_roles_set_up(self):
        user_roles = [
            {
                "user_id": "217abeb3-6466-4440-96e7-bf02ee941bf8",
                "role_id": "b9d000c7-c14f-4909-8c5a-6a6c02abb211"
            },
            {
                "user_id": "217abeb3-6466-4440-96e7-bf02ee941bf8",
                "role_id": "b9d000c7-c14f-4909-8c5a-6a6c02abb222"
            }
        ]
        from ib_iam.tests.factories.models import UserRoleFactory
        from ib_iam.tests.factories.models import ProjectRoleFactory
        ProjectRoleFactory.reset_sequence(0)
        user_role_objects = [UserRoleFactory.create(
            user_id=user_role["user_id"],
            project_role=self._get_or_create_role(role_id=user_role["role_id"])
        ) for user_role in user_roles]
        return user_role_objects

    @staticmethod
    def _get_or_create_role(role_id: Optional[str]):
        from ib_iam.models import ProjectRole
        try:
            return ProjectRole.objects.get(role_id=role_id)
        except ProjectRole.DoesNotExist:
            from ib_iam.tests.factories.models import ProjectRoleFactory
            return ProjectRoleFactory.create(role_id=role_id)

    @staticmethod
    def _get_or_create_company(company_id: Optional[str]):
        if company_id is None:
            return None
        from ib_iam.models import Company
        try:
            return Company.objects.get(company_id=company_id)
        except Company.DoesNotExist:
            from ib_iam.tests.factories.models import CompanyFactory
            return CompanyFactory.create(company_id=company_id)

    @staticmethod
    def _get_or_create_team(team_id: Optional[str]):
        from ib_iam.models import Team
        try:
            return Team.objects.get(team_id=team_id)
        except Team.DoesNotExist:
            from ib_iam.tests.factories.models import TeamFactory
            return TeamFactory.create(team_id=team_id)

    @staticmethod
    def _get_user_ids_from_objects(user_objects):
        user_ids = [str(user_object.user_id) for user_object in user_objects]
        return user_ids
