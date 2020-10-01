"""
test with an action which is not NO_VALIDATIONS
and priority is not filled
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...common_fixtures.adapters.roles_service import \
    get_user_role_ids_based_on_project_mock
from ...factories.models import TaskFactory, StageActionFactory, \
    ActionPermittedRolesFactory


class TestCase06ValidateTaskFilledFieldsAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        task_id = "IBWF-1"
        action_id = 1
        user_roles = ["FIN_PAYMENT_REQUESTER"]

        TaskFactory.create(task_display_id=task_id, priority=None)
        action = StageActionFactory.create(id=action_id, action_type=None)
        ActionPermittedRolesFactory.create(action=action,
                                           role_id=user_roles[0])
        user_roles_mock = get_user_role_ids_based_on_project_mock(mocker)
        user_roles_mock.return_value = user_roles

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {'task_id': 'IBWF-1', 'action_id': "1"}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
