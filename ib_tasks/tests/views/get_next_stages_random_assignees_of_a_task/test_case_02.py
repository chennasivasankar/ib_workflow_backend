"""
# Success Test Case
"""
import json

import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...common_fixtures.adapters.auth_service import \
    prepare_permitted_user_details_mock

from ...factories.models import StagePermittedRolesFactory, TaskFactory, \
    StageModelFactory, CurrentTaskStageModelFactory, StageActionFactory, \
    TaskStatusVariableFactory, ActionPermittedRolesFactory


class TestCase01GetNextStagesRandomAssigneesOfATaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker, api_user):
        user_obj = api_user
        user_id = str(user_obj.user_id)
        StagePermittedRolesFactory.reset_sequence()

        TaskFactory.reset_sequence()
        task = TaskFactory(template_id='template_1')


    @pytest.mark.django_db
    def test_case(self, snapshot, setup, mocker):
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_team_info_for_given_user_ids_mock
        get_team_info_for_given_user_ids_mock(mocker)

        body = {"task_id": "IBWF-2", "action_id": 1}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
