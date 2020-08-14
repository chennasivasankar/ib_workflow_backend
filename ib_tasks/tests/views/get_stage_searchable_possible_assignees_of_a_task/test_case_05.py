"""
test when no stage assignees exists returns empty list
"""
import json

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...common_fixtures.adapters.auth_service import \
    get_user_details_for_the_given_role_ids_based_on_query
from ...factories.models import StagePermittedRolesFactory, StageModelFactory


class TestCase05GetStageSearchablePossibleAssigneesOfATaskAPITestCase(
        TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker, api_user):
        StagePermittedRolesFactory.reset_sequence()
        StageModelFactory.reset_sequence()

        mock_method = \
            get_user_details_for_the_given_role_ids_based_on_query(mocker)
        mock_method.return_value = []
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
        query_params = {'limit': 10, 'offset': 0, 'search_query': 'string'}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
