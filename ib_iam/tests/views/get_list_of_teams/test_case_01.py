"""
# TODO: Success Response case which returns list of teams along with its members
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from mock import patch

from ib_iam.adapters.dtos import BasicUserDTO
from ib_iam.models import Team, User, TeamMember
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ib_iam.tests.factories.models import (
    TeamFactory, UserFactory, TeamMemberFactory
)
from ib_iam.tests.storages.conftest import (
    team1_id, team2_id, team3_id, member1_id,
    member2_id, member3_id, member4_id
)


class TestCase01GetListOfTeamsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    @patch(
        "ib_iam.adapters.user_service.UserService.get_basic_user_dtos"
    )
    def test_case(self, get_basic_user_dtos, snapshot, setup):
        get_basic_user_dtos.return_value = [
            BasicUserDTO(
                user_id=member1_id,
                name="user1",
                profile_pic_url="url1"
            ),
            BasicUserDTO(
                user_id=member2_id,
                name="user2",
                profile_pic_url="url2"
            ),
            BasicUserDTO(
                user_id=member3_id,
                name="user3",
                profile_pic_url="url3"
            ),
            BasicUserDTO(
                user_id=member4_id,
                name="user4",
                profile_pic_url="url4"
            )
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
        UserFactory.reset_sequence(1)
        TeamFactory.reset_sequence(1)
        TeamMemberFactory.reset_sequence(1)
        UserFactory.create(user_id=user_obj.id, admin=True)
        t1 = TeamFactory.create(team_id=team1_id, created_by=user_obj.id)
        t2 = TeamFactory.create(team_id=team2_id, created_by=user_obj.id)
        t3 = TeamFactory.create(team_id=team3_id, created_by=user_obj.id)

        TeamMemberFactory.create(team=t1, member_id=member1_id)
        TeamMemberFactory.create(team=t1, member_id=member2_id)
        TeamMemberFactory.create(team=t1, member_id=member3_id)
        TeamMemberFactory.create(team=t2, member_id=member4_id)
        TeamMemberFactory.create(team=t2, member_id=member1_id)
        TeamMemberFactory.create(team=t3, member_id=member2_id)
        TeamMemberFactory.create(team=t3, member_id=member3_id)
        TeamMemberFactory.create(team=t3, member_id=member4_id)
