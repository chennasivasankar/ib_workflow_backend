"""
Given valid details user will be added successfully
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase03AddUserAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture
    def user_set_up(self, api_user):
        user_id = api_user.user_id
        from ib_iam.tests.common_fixtures.reset_fixture \
            import reset_sequence_for_model_factories
        reset_sequence_for_model_factories()
        from ib_iam.tests.factories.models import UserDetailsFactory
        UserDetailsFactory.create(user_id=user_id, is_admin=True)
        from ib_iam.tests.factories.models \
            import CompanyFactory, TeamFactory, ProjectRoleFactory
        CompanyFactory.create(
            company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331')
        TeamFactory.create(team_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331')
        ProjectRoleFactory.create(
            role_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331')

    @staticmethod
    def elastic_storage_create_elastic_user_mock(mocker):
        mock = mocker.patch(
            "ib_iam.storages.elastic_storage_implementation.ElasticStorageImplementation.create_elastic_user"
        )
        mock.create_elastic_user.return_value = "elastic_user1"
        return mock

    @staticmethod
    def elastic_storage_create_elastic_user_intermediary_mock(mocker):
        mock = mocker.patch(
            "ib_iam.storages.elastic_storage_implementation.ElasticStorageImplementation.create_elastic_user_intermediary"
        )
        mock.create_elastic_user_intermediary.return_value = None
        return mock

    @staticmethod
    def send_verification_email_mock(mocker):
        mock = mocker.patch(
            "ib_iam.interactors.send_verify_email_link_interactor.SendVerifyEmailLinkInteractor.send_verification_email"
        )
        return mock

    @pytest.mark.django_db
    def test_case(self, user_set_up, snapshot, mocker):
        self.elastic_storage_create_elastic_user_mock(mocker=mocker)
        self.elastic_storage_create_elastic_user_intermediary_mock(
            mocker=mocker)
        body = {'name': 'parker', 'email': 'parker@gmail.com',
                'company_id': 'ef6d1fc6-ac3f-4d2d-a983-752c992e8331',
                'team_ids': ['ef6d1fc6-ac3f-4d2d-a983-752c992e8331'],
                'role_ids': ['ROLE_0']}
        path_params = {}
        query_params = {}
        headers = {}
        new_user_id = "user2"
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import create_user_account_adapter_mock, \
            create_user_profile_adapter_mock
        user_account_adapter_mock = \
            create_user_account_adapter_mock(mocker=mocker)
        user_profile_adapter_mock = \
            create_user_profile_adapter_mock(mocker=mocker)
        from ib_iam.tests.common_fixtures.adapters.auth_service_adapter_mocks import \
            update_is_email_verified_value_mock
        update_is_email_verified_value_mock = update_is_email_verified_value_mock(
            mocker=mocker)
        send_verification_email_mock = self.send_verification_email_mock(
            mocker=mocker)
        send_verification_email_mock.return_value = None

        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )

        user_account_adapter_mock.assert_called_once()
        user_profile_adapter_mock.assert_called_once()
        update_is_email_verified_value_mock.assert_called_once_with(
            user_id=new_user_id, is_email_verified=False)
