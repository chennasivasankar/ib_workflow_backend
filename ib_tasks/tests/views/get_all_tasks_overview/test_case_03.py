"""
# Given no data raise empty stage ids exception
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...common_fixtures.adapters.auth_service import \
    get_valid_project_ids_mock, validate_if_user_is_in_project_mock, \
    check_user_in_least_level_mock
from ...common_fixtures.adapters.roles_service import \
    get_user_role_ids_based_on_project_mock
from ...common_fixtures.adapters.project_service import \
    get_valid_project_ids_mock as project_service_validate_project_ids_mock


class TestCase03GetAllTasksOverviewAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        from ib_tasks.tests.common_fixtures.storages import mock_filter_tasks
        mock = mock_filter_tasks(mocker)
        mock.return_value = ([], 0)

        project_id = "FIN_MAN"

        get_valid_project_ids_mock(mocker, project_id)
        validate_if_user_is_in_project_mock(mocker, True)
        get_user_role_ids_based_on_project_mock(mocker)
        check_user_in_least_level_mock(mocker, True)
        project_mock = project_service_validate_project_ids_mock(mocker)
        project_mock.return_value = project_id

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {}
        path_params = {}
        query_params = {'limit': 1, 'offset': 0, 'project_id': "FIN_MAN"}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
