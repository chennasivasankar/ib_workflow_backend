"""
test when no stage assignees exists returns empty list
"""
import json

import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase05GetStageSearchablePossibleAssigneesOfATaskAPITestCase(
        TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker, api_user):
        from ib_tasks.tests.factories.adapter_dtos import \
            UserIdWIthTeamDetailsDTOFactory, TeamDetailsDTOFactory, \
            UserDetailsDTOFactory
        from ib_tasks.tests.factories.models import \
            StagePermittedRolesFactory, StageModelFactory, TaskFactory
        StagePermittedRolesFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        UserIdWIthTeamDetailsDTOFactory.reset_sequence(1)
        TeamDetailsDTOFactory.reset_sequence(1)
        UserDetailsDTOFactory.reset_sequence()
        TaskFactory.reset_sequence()

        stage = StageModelFactory(
            task_template_id='template_1',
            display_logic="variable0==stage_id_0",
            card_info_kanban=json.dumps(["FIELD_ID-1", "FIELD_ID-2"]),
            card_info_list=json.dumps(["FIELD_ID-1", "FIELD_ID-2"]),
        )
        StagePermittedRolesFactory.create_batch(size=2, stage=stage)

        user_id_with_team_details_dtos = \
            UserIdWIthTeamDetailsDTOFactory.create_batch(size=2)
        user_ids = [
            user_id_with_team_details_dto.user_id
            for user_id_with_team_details_dto in user_id_with_team_details_dtos
        ]
        user_details_dtos = UserDetailsDTOFactory.create_batch(
            size=2, user_id=factory.Iterator(user_ids))
        TaskFactory.create()

        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_user_details_for_the_given_role_ids_based_on_query_mock, \
            get_team_info_for_given_user_ids_mock
        user_details_mock_method = \
            get_user_details_for_the_given_role_ids_based_on_query_mock(mocker)
        team_info_mock_method = get_team_info_for_given_user_ids_mock(mocker)

        user_details_mock_method.return_value = []
        team_info_mock_method.return_value = []

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {}
        path_params = {"stage_id": 1}
        query_params = {
            'limit': 10, 'offset': 0, 'search_query': 'string',
            'task_id': 'IBWF-1'
        }
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
