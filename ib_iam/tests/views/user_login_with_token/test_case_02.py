"""
Given valid token for which user not already exists returns tokens successfully

Tested assuming that the project and team are already created and
team is assigned to project
"""
import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_workflows_backend.settings.base_swagger_utils import \
    JGC_DRIVE_PROJECT_ID
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02UserLoginWithTokenAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_auth_user_not_already_exist_returns_response(
            self, setup_for_auth_user_not_already_exist_case, snapshot
    ):
        token = setup_for_auth_user_not_already_exist_case["token"]
        body = {
            "name": "username",
            "user_id": "89d96f4b-c19d-4e69-8eae-e818f3123b09"
        }
        path_params = {}
        query_params = {'token': token}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)
        self.checks_to_perform(token=token, snapshot=snapshot)

    @pytest.fixture
    def setup_for_auth_user_not_already_exist_case(
            self, elastic_storage_mock, mocker
    ):
        from ib_iam.tests.factories.models import TeamFactory, ProjectFactory, ProjectRoleFactory
        from ib_iam.constants.config import DEFAULT_TEAM_ID, DEFAULT_TEAM_NAME
        from ib_iam.tests.factories.adapter_dtos import UserTokensDTOFactory
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks \
            import create_auth_tokens_for_user_mock, create_user_profile_mock, \
            create_user_account_with_email_mock
        user_id = "89d96f4b-c19d-4e69-8eae-e818f3123b09"
        token = "token1"
        elastic_user_id = "elastic_user_id_1"
        role_ids = ["ROLE_1", "ROLE_2"]
        create_user_account_with_email_mock = \
            create_user_account_with_email_mock(mocker)
        create_user_account_with_email_mock.return_value = user_id
        create_user_profile_mock(mocker)
        create_elastic_user_mock(mocker=mocker, response=elastic_user_id)
        TeamFactory.create(team_id=DEFAULT_TEAM_ID, name=DEFAULT_TEAM_NAME)
        project_object = ProjectFactory.create(
            project_id=JGC_DRIVE_PROJECT_ID, name="JGC_Proj"
        )
        ProjectRoleFactory.create_batch(
            size=2, project=project_object, role_id=factory.Iterator(role_ids)
        )
        UserTokensDTOFactory.reset_sequence(0)
        user_tokens_dto = UserTokensDTOFactory(user_id=user_id)
        create_auth_tokens_for_user_mock = create_auth_tokens_for_user_mock(
            mocker=mocker
        )
        create_auth_tokens_for_user_mock.return_value = user_tokens_dto
        return {"token": token}

    def checks_to_perform(self, token, snapshot):
        from ib_iam.models import UserAuthToken, UserDetails, TeamUser, \
            TeamMemberLevel, UserRole
        user_auth_values = UserAuthToken.objects.filter(token=token).values()
        user_id = user_auth_values[0]["user_id"]
        snapshot.assert_match(user_auth_values[0], "UserAuthDetails")

        user_details = UserDetails.objects.filter(user_id=user_id).values()
        snapshot.assert_match(user_details[0], "UserDetails")

        team_users = TeamUser.objects.filter(user_id=user_id).values(
            'id', 'team_id', 'user_id', 'immediate_superior_team_user_id'
        )
        snapshot.assert_match(team_users[0], "TeamUsers")

        team_member_levels = TeamMemberLevel.objects.values(
            'level_hierarchy', 'level_name', 'team_id'
        )
        snapshot.assert_match(team_member_levels[0], "TeamMemberLevels")

        user_roles = UserRole.objects.filter(
            user_id=user_id).values()
        snapshot.assert_match(list(user_roles), "UserRoles")





    @pytest.fixture()
    def elastic_storage_mock(self):
        from unittest.mock import create_autospec
        from ib_iam.storages.elastic_storage_implementation import \
            ElasticStorageImplementation
        return create_autospec(ElasticStorageImplementation)


def create_elastic_user_mock(mocker, response):
    mock = mocker.patch(
        "ib_iam.storages.elastic_storage_implementation.ElasticStorageImplementation.create_elastic_user"
    )
    mock.return_value = response
