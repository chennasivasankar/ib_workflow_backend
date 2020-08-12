"""
test when stage assignees exists returns list of user details
"""
import json

import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...common_fixtures.adapters.auth_service import \
    prepare_permitted_user_details_mock, \
    get_user_details_for_the_given_role_ids_based_on_query
from ...factories.models import StagePermittedRolesFactory, TaskFactory, \
    StageModelFactory, CurrentTaskStageModelFactory, StageActionFactory, \
    TaskStatusVariableFactory, ActionPermittedRolesFactory


class TestCase01GetStageSearchablePossibleAssigneesOfATaskAPITestCase(
        TestUtils):
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
        StageModelFactory.reset_sequence()

        get_user_details_for_the_given_role_ids_based_on_query(mocker)
        stage = StageModelFactory(
            task_template_id='template_1',
            display_logic="variable0==stage_id_0",
            card_info_kanban=json.dumps(["FIELD_ID-1", "FIELD_ID-2"]),
            card_info_list=json.dumps(["FIELD_ID-1", "FIELD_ID-2"]),
        )
        StagePermittedRolesFactory.create_batch(size=2, stage=stage)

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {}
        path_params = {"stage_id": 1}
        query_params = {'limit': 876, 'offset': 286, 'search_query': 'string'}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
