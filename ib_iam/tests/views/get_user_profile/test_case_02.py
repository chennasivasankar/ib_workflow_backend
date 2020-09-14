"""
test success case but user has no company or team
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
    def test_valid_user_id(
            self, adapters_mock_setup, snapshot):
        body = {}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(
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
        for user_dto in user_dtos:
            if user_dto.user_id == login_user_id:
                login_user_profile_dto = user_dto
        get_user_profile_dto_mock = prepare_get_user_profile_dto_mock(mocker)
        get_user_profile_dto_mock.return_value = login_user_profile_dto
        get_basic_user_dtos_mock = get_basic_user_profile_dtos_mock(mocker)
        get_basic_user_dtos_mock.return_value = user_dtos

    @pytest.fixture()
    def users_set_up(self):
        user_ids = ["217abeb3-6466-4440-96e7-bf02ee941bf8",
                    "7e39bf1c-f9a5-4e76-8451-b962ddd52044"]
        from ib_iam.tests.common_fixtures.reset_fixture import \
            reset_sequence_company_factory, reset_sequence_user_details_factory
        reset_sequence_company_factory()
        reset_sequence_user_details_factory()
        from ib_iam.tests.factories.models import UserDetailsFactory
        users = [UserDetailsFactory.create(user_id=user_id, company=None)
                 for user_id in user_ids]
        return users

    @staticmethod
    def _get_user_ids_from_objects(user_objects):
        user_ids = [str(user_object.user_id) for user_object in user_objects]
        return user_ids
