"""
test with an action which is not NO_VALIDATIONS
and user permitted fields are not filled
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.constants.enum import PermissionTypes
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...common_fixtures.adapters.roles_service import \
    get_user_role_ids_based_on_project_mock
from ...factories.models import TaskFactory, StageActionFactory, \
    ActionPermittedRolesFactory, TaskTemplateFactory, GoFFactory, \
    GoFToTaskTemplateFactory, FieldFactory, StageModelFactory, StageGoFFactory, \
    GoFRoleFactory, FieldRoleFactory, TaskTemplateInitialStageFactory


class TestCase07ValidateTaskFilledFieldsAPITestCase(TestUtils):
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
        TaskTemplateFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        task_id = "IBWF-1"
        action_id = 1
        user_roles = ["FIN_PAYMENT_REQUESTER"]
        template_id = "FIN_PAYMENT_REQUEST"
        gof_id = "FIN_PAYMENT_REQUESTER_DETAILS"
        gof_display_name = "payment requester details"
        field_id = "FIN_PAYMENT_REQUESTER_NAME"
        field_display_name = "payment requester name"

        template = TaskTemplateFactory.create(template_id=template_id)
        gof = GoFFactory.create(gof_id=gof_id, display_name=gof_display_name)
        template_gof = GoFToTaskTemplateFactory.create(
            task_template=template, gof=gof)
        field = FieldFactory.create(
            field_id=field_id, gof=gof, display_name=field_display_name)
        stage = StageModelFactory.create()
        TaskTemplateInitialStageFactory.create(
            task_template=template, stage=stage)
        action = StageActionFactory.create(
            id=action_id, stage=stage, action_type=None)
        StageGoFFactory.create(stage=stage, gof=gof)
        ActionPermittedRolesFactory.create(action=action,
                                           role_id=user_roles[0])
        GoFRoleFactory.create(
            gof=gof, role=user_roles[0],
            permission_type=PermissionTypes.WRITE.value)
        FieldRoleFactory.create(
            field=field, role=user_roles[0],
            permission_type=PermissionTypes.WRITE.value)
        user_roles_mock = get_user_role_ids_based_on_project_mock(mocker)
        user_roles_mock.return_value = user_roles

        TaskFactory.create(task_display_id=task_id, template_id=template_id)

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
