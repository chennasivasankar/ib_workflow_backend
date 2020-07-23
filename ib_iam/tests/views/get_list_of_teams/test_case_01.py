"""
Success Response
Returns a dictionary with total_teams_count and teams list

"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils

from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ib_iam.tests.factories.models import (
    TeamFactory, UserDetailsFactory, TeamMemberFactory
)
from ib_iam.tests.common_fixtures.adapters.user_service_mocks import (
    prepare_user_profile_dtos_mock
)


class TestCase01GetListOfTeamsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_case(self, mocker, snapshot, setup):
        user_ids = [
            '2bdb417e-4632-419a-8ddd-085ea272c6eb',
            '548a803c-7b48-47ba-a700-24f2ea0d1280',
            '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
            '7ee2c7b4-34c8-4d65-a83a-f87da75db24e'
        ]
        UserProfileDTOFactory.reset_sequence(1)
        mock = prepare_user_profile_dtos_mock(mocker)
        mock.return_value = [
            UserProfileDTOFactory(
                user_id=user_id
            ) for user_id in user_ids
        ]
        body = {}
        path_params = {}
        query_params = {'limit': 5, 'offset': 0}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    @pytest.fixture()
    def setup(self, api_user):
        user_obj = api_user
        UserDetailsFactory.reset_sequence(1)
        TeamFactory.reset_sequence(1)
        TeamMemberFactory.reset_sequence(1)
        UserDetailsFactory.create(user_id=user_obj.user_id, is_admin=True)
        teams = [
            {
                "team_id": "f2c02d98-f311-4ab2-8673-3daa00757002",
                "user_ids": [
                    '2bdb417e-4632-419a-8ddd-085ea272c6eb',
                    '548a803c-7b48-47ba-a700-24f2ea0d1280',
                    '4b8fb6eb-fa7d-47c1-8726-cd917901104e'
                ]
            },
            {
                "team_id": "aa66c40f-6d93-484a-b418-984716514c7b",
                "user_ids": [
                    '2bdb417e-4632-419a-8ddd-085ea272c6eb',
                    '7ee2c7b4-34c8-4d65-a83a-f87da75db24e'
                ]
            },
            {
                "team_id": "c982032b-53a7-4dfa-a627-4701a5230765",
                "user_ids": [
                    '548a803c-7b48-47ba-a700-24f2ea0d1280',
                    '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
                    '7ee2c7b4-34c8-4d65-a83a-f87da75db24e'
                ]

            }
        ]
        for team in teams:
            team_object = TeamFactory(team_id=team["team_id"])
            for user_id in team["user_ids"]:
                TeamMemberFactory(team=team_object, user_id=user_id)
