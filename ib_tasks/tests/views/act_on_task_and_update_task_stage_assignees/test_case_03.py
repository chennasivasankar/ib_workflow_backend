"""
# Given Invalid Task Id Raise exception
"""
import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.models import TaskTemplateGoFs, ProjectTaskTemplate
from ib_tasks.tests.factories.models import TaskTemplateFactory, \
    TaskTemplateStatusVariableFactory, GoFFactory, \
    FieldFactory, StageModelFactory, StageActionFactory, \
    TaskFactory, TaskStatusVariableFactory, TaskGoFFactory, \
    TaskGoFFieldFactory, \
    CurrentTaskStageModelFactory, GoFToTaskTemplateFactory, \
    ActionPermittedRolesFactory, \
    TaskTemplateInitialStageFactory, GoFRoleFactory, FieldRoleFactory, \
    StagePermittedRolesFactory, ProjectTaskTemplateFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01ActOnTaskAndUpdateTaskStageAssigneesAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            "task_id": "IBWF-2",
            "action_id": "1",
            "board_id": "board_1",
            "stage_assignees": [
                {
                    "stage_id": 1,
                    "assignee_id": "123e4567-e89b-12d3-a456-426614174004",
                    "team_id": "123e4567-e89b-12d3-a456-426614174001"
                }
            ]
        }
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)
