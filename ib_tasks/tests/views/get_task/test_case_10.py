"""
# TODO: Update test case description
"""
from unittest.mock import patch

import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.adapters.auth_service import AuthService, \
    InvalidProjectIdsException
from ib_tasks.constants.enum import PermissionTypes, FieldTypes, Searchable
from ib_tasks.tests.factories.models import (
    TaskFactory,
    TaskGoFFactory,
    TaskGoFFieldFactory,
    GoFRoleFactory,
    GoFFactory,
    FieldRoleFactory,
    FieldFactory, StageModelFactory, CurrentTaskStageModelFactory,
    TaskStageHistoryModelFactory, StagePermittedRolesFactory,
)
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase10GetTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write', 'read']}}

    @pytest.fixture
    def reset_factories(self):
        TaskFactory.reset_sequence()
        TaskGoFFactory.reset_sequence()
        GoFRoleFactory.reset_sequence()
        GoFFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()
        FieldFactory.reset_sequence()
        TaskGoFFieldFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        CurrentTaskStageModelFactory.reset_sequence()
        TaskStageHistoryModelFactory.reset_sequence()

    @pytest.fixture
    def setup(self, reset_factories):
        TaskFactory(task_display_id="IBWF-1", project_id="project0")

    @pytest.mark.django_db
    @patch.object(AuthService, "get_projects_info_for_given_ids")
    def test_case(
            self, project_info_mock, snapshot, setup, mocker
    ):
        project_ids = ["project0"]
        exception_object = InvalidProjectIdsException(project_ids)
        project_info_mock.side_effect = exception_object
        body = {}
        path_params = {}
        query_params = {'task_id': "IBWF-1"}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
