"""
test with user who does not have permission to perform the give action
"""
import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from freezegun import freeze_time

from ib_tasks.constants.constants import ALL_ROLES_ID
from ib_tasks.constants.enum import PermissionTypes, FieldTypes
from ib_tasks.tests.common_fixtures.adapters.assignees_details_service import \
    assignee_details_dtos_mock
from ib_tasks.tests.common_fixtures.adapters.auth_service import \
    get_valid_project_ids_mock as auth_service_project_ids_mock, \
    validate_if_user_is_in_project_mock, get_projects_info_for_given_ids_mock, \
    get_team_info_for_given_user_ids_mock, prepare_permitted_user_details_mock, \
    get_user_id_team_details_dtos_mock
from ib_tasks.tests.common_fixtures.adapters.project_service import \
    get_valid_project_ids_mock
from ib_tasks.tests.common_fixtures.adapters.roles_service import \
    get_user_role_ids_based_on_project_mock, get_user_role_ids
from ib_tasks.tests.common_fixtures.storages import \
    elastic_storage_implementation_mock
from ib_tasks.tests.factories.adapter_dtos import UserDetailsDTOFactory, \
    AssigneeDetailsDTOFactory
from ib_tasks.tests.factories.models import TaskFactory, TaskTemplateFactory, \
    TaskTemplateInitialStageFactory, StageModelFactory, \
    ProjectTaskTemplateFactory, StageActionFactory, GoFFactory, FieldFactory, \
    GoFToTaskTemplateFactory, StageGoFFactory, GoFRoleFactory, \
    FieldRoleFactory, ActionPermittedRolesFactory, \
    TaskTemplateStatusVariableFactory, StagePermittedRolesFactory
from ib_tasks.tests.views.create_sub_task import APP_NAME, OPERATION_NAME, \
    REQUEST_METHOD, URL_SUFFIX


class TestCase46CreateSubTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def setup(self, api_user, mocker):
        TaskTemplateFactory.reset_sequence()
        TaskFactory.reset_sequence()
        TaskTemplateInitialStageFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        ProjectTaskTemplateFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        GoFFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()
        StageGoFFactory.reset_sequence()
        GoFRoleFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()
        FieldFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        TaskTemplateStatusVariableFactory.reset_sequence()
        StagePermittedRolesFactory.reset_sequence()

        project_id = "project_1"
        template_id = "template_1"
        parent_task_display_id = "IBWF-1"
        stage_id = 1
        given_action_id = 1
        present_stage_action_id = 2
        gof_id = "FIN_PAYMENT_REQUESTER_DETAILS"
        field_id = "FIN_PAYMENT_REQUESTER_FIELD"
        variable = "variable0"

        elastic_storage_implementation_mock(mocker)
        auth_service_project_ids_mock(mocker, [project_id])
        project_mock = get_valid_project_ids_mock(mocker)
        project_mock.return_value = [project_id]
        get_user_role_ids_based_on_project_mock(mocker)
        get_user_id_team_details_dtos_mock(mocker)
        is_user_in_project = True
        validate_if_user_is_in_project_mock(mocker, is_user_in_project)
        get_projects_info_for_given_ids_mock(mocker)
        get_team_info_for_given_user_ids_mock(mocker)
        get_user_role_ids(mocker)

        prepare_permitted_user_details_mock_method = \
            prepare_permitted_user_details_mock(mocker)
        assignee_details_dtos_mock_method = assignee_details_dtos_mock(mocker)
        prepare_permitted_user_details_mock_method.return_value = \
            UserDetailsDTOFactory.create_batch(
                size=2, user_id=factory.Iterator(["user_1", "user_2"]))
        assignee_details_dtos_mock_method.return_value = \
            AssigneeDetailsDTOFactory.create_batch(
                size=2, assignee_id=factory.Iterator(["user_1", "user_2"]))

        template_obj = TaskTemplateFactory.create(template_id=template_id)
        ProjectTaskTemplateFactory.create(
            project_id=project_id, task_template=template_obj)
        stage = StageModelFactory(
            stage_id=stage_id, stage_color="blue",
            task_template_id=template_id,
            display_logic="variable0==stage_1")
        path = 'ib_tasks.tests.populate.' \
               'stage_actions_logic.stage_1_action_name_1_logic'
        action = StageActionFactory(
            id=present_stage_action_id, stage=stage, py_function_import_path=path,
            action_type=None)
        given_action = StageActionFactory(
            id=given_action_id, action_type=None)
        TaskTemplateInitialStageFactory.create(
            task_template_id=template_id, stage=stage)
        parent_task = TaskFactory.create(
            task_display_id=parent_task_display_id)

        gof = GoFFactory.create(gof_id=gof_id)
        field = FieldFactory.create(
            field_id=field_id, gof=gof,
            field_type=FieldTypes.PLAIN_TEXT.value)
        GoFToTaskTemplateFactory.create(
            task_template=template_obj, gof=gof)
        StageGoFFactory.create(stage=stage, gof=gof)
        GoFRoleFactory.create(
            gof=gof, permission_type=PermissionTypes.WRITE.value,
            role="FIN_PAYMENT_REQUESTER")
        FieldRoleFactory.create(
            field=field, permission_type=PermissionTypes.WRITE.value,
            role="FIN_PAYMENT_REQUESTER")
        StagePermittedRolesFactory.create(stage=stage, role_id=ALL_ROLES_ID)
        ActionPermittedRolesFactory.create(action=action, role_id=ALL_ROLES_ID)
        ActionPermittedRolesFactory.create(action=given_action, role_id=ALL_ROLES_ID)
        TaskTemplateStatusVariableFactory.create(
            task_template_id=template_id, variable=variable)

    @freeze_time("2020-09-09 12:00:00")
    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            "project_id": "project_1",
            "task_template_id": "template_1",
            "action_id": 1,
            "parent_task_id": "IBWF-1",
            "title": "Sub Task",
            "description": None,
            "start_datetime": "2020-08-09 12:00:00",
            "due_datetime": "2020-09-10 12:00:00",
            "priority": "HIGH",
            "task_gofs": [
                {
                    "gof_id": "FIN_PAYMENT_REQUESTER_DETAILS",
                    "same_gof_order": 1,
                    "gof_fields": [
                        {
                            "field_id": "FIN_PAYMENT_REQUESTER_FIELD",
                            "field_response": "Jason Momoa"
                        }
                    ]
                }
            ]
        }
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
