"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase03EditUserAPITestCase(TestUtils):
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
        UserDetailsFactory.create(user_id=user_id, is_admin=True, company=None)
        UserDetailsFactory.create(
            user_id="ef6d1fc6-ac3f-4d2d-a983-752c992e8300",
            company=None, is_admin=False)
        from ib_iam.tests.factories.models \
            import CompanyFactory, TeamFactory, ProjectRoleFactory
        CompanyFactory.create(
            company_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8331')
        TeamFactory.create(team_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8344')
        TeamFactory.create(team_id='ef6d1fc6-ac3f-4d2d-a983-752c992e8343')
        ProjectRoleFactory.create(role_id='ROLE_1')

    @staticmethod
    def elastic_search_update_user_mock(mocker):
        mock = mocker.patch(
            "ib_iam.storages.elastic_storage_implementation.ElasticStorageImplementation.update_elastic_user"
        )
        mock.update_elastic_user.return_value = None
        return mock

    @pytest.mark.django_db
    def test_case(self, user_set_up, snapshot, mocker):
        self.elastic_search_update_user_mock(mocker=mocker)
        body = {'name': 'parker', 'email': 'parker2020@gmail.com',
                'company_id': 'ef6d1fc6-ac3f-4d2d-a983-752c992e8331',
                'team_ids': ['ef6d1fc6-ac3f-4d2d-a983-752c992e8344',
                             'ef6d1fc6-ac3f-4d2d-a983-752c992e8343'],
                'role_ids': ['ROLE_1']}
        path_params = {"user_id": "ef6d1fc6-ac3f-4d2d-a983-752c992e8300"}
        query_params = {}
        headers = {}
        from ib_iam.tests.common_fixtures.adapters.user_service \
            import prepare_update_user_profile_adapter_mock
        adapter_mock = prepare_update_user_profile_adapter_mock(mocker=mocker)
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
        adapter_mock.assert_called_once()
