"""
test all cases
"""
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
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

    def _get_or_create_user(self):
        user_id = '217abeb3-6466-4440-96e7-bf02ee941bf8'
        user = UserAccount.objects.create(user_id=user_id)
        return user

    @pytest.mark.django_db
    def test_valid_user_id(self, setup, mocker, snapshot):
        from ib_iam.tests.common_fixtures.adapters.user_service_mocks import (
            prepare_user_profile_dtos_mock)
        from ib_iam.tests.common_fixtures.adapters.user_service import \
            prepare_get_user_profile_dto_mock
        body = {}
        path_params = {}
        query_params = {}
        headers = {}
        user_ids = setup
        login_user_id = user_ids[0]
        from ib_iam.tests.factories.adapter_dtos import UserProfileDTOFactory
        UserProfileDTOFactory.reset_sequence(1)
        user_dtos = [
            UserProfileDTOFactory(user_id=user_id)
            for user_id in user_ids
        ]
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(mocker)
        get_user_profile_dto_mock.return_value = UserProfileDTOFactory(
            user_id=login_user_id,
            email="test@gmail.com",
            profile_pic_url="test.com",
            name="test")
        get_basic_user_dtos_mock = prepare_user_profile_dtos_mock(mocker)
        get_basic_user_dtos_mock.return_value = user_dtos

        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
        print(response.content)

    @pytest.fixture
    def setup(self):
        user_ids = ['217abeb3-6466-4440-96e7-bf02ee941bf8',
                    '4b8fb6eb-fa7d-47c1-8726-cd917901104e',
                    '548a803c-7b48-47ba-a700-24f2ea0d1280', ]
        company_id = 'f2c02d98-f311-4ab2-8673-3daa00757002'
        team_id = '2bdb417e-4632-419a-8ddd-085ea272c6eb'
        from ib_iam.tests.factories.models import \
            UserDetailsFactory, UserTeamFactory, CompanyFactory, TeamFactory
        TeamFactory.reset_sequence(1)
        CompanyFactory.reset_sequence(1)
        company_object = CompanyFactory.create(company_id=company_id)
        user_details = [
            {"user_id": user_ids[0], "company": company_object},
            {"user_id": user_ids[1], "company": company_object},
            {"user_id": user_ids[2], "company": None}
        ]
        for user_detail in user_details:
            UserDetailsFactory.create(user_id=user_detail["user_id"],
                                      company=user_detail["company"])
        team_object = TeamFactory.create(team_id=team_id)
        for user_id in [user_ids[0], user_ids[2]]:
            UserTeamFactory.create(team=team_object, user_id=user_id)

        return user_ids


