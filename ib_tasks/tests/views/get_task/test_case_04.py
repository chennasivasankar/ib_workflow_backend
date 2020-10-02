"""
test with user doesn't have permission for at least one stage for a task
raise user permission denied exception
"""
from unittest.mock import patch

import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.adapters.auth_service import AuthService
from ib_tasks.tests.factories.models import (
    TaskFactory, StageModelFactory, CurrentTaskStageModelFactory,
    TaskStageHistoryModelFactory, StagePermittedRolesFactory,
    TaskTemplateFactory
)
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase04GetTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write', 'read']}}

    @pytest.fixture
    def reset_factories(self):
        TaskFactory.reset_sequence()
        CurrentTaskStageModelFactory.reset_sequence()
        TaskStageHistoryModelFactory.reset_sequence()
        StagePermittedRolesFactory.reset_sequence()
        TaskTemplateFactory.reset_sequence()

    @pytest.fixture
    def setup(self, reset_factories, api_user):
        user_id = api_user.user_id
        task_obj = TaskFactory(
            project_id="project0", created_by=user_id
        )
        template_id = task_obj.template_id
        TaskTemplateFactory(template_id=template_id)
        stage_objs = StageModelFactory.create_batch(size=4)
        CurrentTaskStageModelFactory.create_batch(size=4, task=task_obj,
                                                  stage=factory.Iterator(
                                                      stage_objs))
        TaskStageHistoryModelFactory.create_batch(
            size=3, task=task_obj, stage=factory.Iterator(stage_objs),
            assignee_id=None
        )
        TaskStageHistoryModelFactory.create(
            task=task_obj, stage=stage_objs[3], assignee_id=None
        )
        StagePermittedRolesFactory.create_batch(
            size=3,
            stage=factory.Iterator(stage_objs),
            role_id="FIN_ADMIN"
        )

    @pytest.mark.django_db
    @patch.object(AuthService, "get_user_ids_based_on_user_level")
    def test_case(self, user_ids_mock, snapshot, setup, mocker, api_user):
        user_id = api_user.user_id
        user_ids_mock.return_value = [user_id]
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        get_valid_project_ids_mock(mocker, project_ids=["project0"])
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_if_user_is_in_project_mock
        validate_if_user_is_in_project_mock(mocker, True)
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids_based_on_project_mock
        get_user_role_ids_based_on_project_mock(mocker)
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_projects_info_for_given_ids_mock
        get_projects_info_for_given_ids_mock(mocker)
        body = {}
        path_params = {}
        query_params = {'task_id': "IBWF-1"}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
