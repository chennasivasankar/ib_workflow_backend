"""
test with just a task title in save as draft use case creates a task with
just title
"""
import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.constants.enum import ActionTypes
from ib_tasks.tests.common_fixtures.adapters.auth_service import \
    get_user_id_team_details_dtos_mock
from ib_tasks.tests.common_fixtures.adapters.project_service import \
    get_valid_project_ids_mock
from ib_tasks.tests.views.create_task import APP_NAME, OPERATION_NAME, \
    REQUEST_METHOD, URL_SUFFIX
from ib_tasks.tests.common_fixtures.adapters.roles_service import \
    get_user_role_ids_based_on_project_mock
from ib_tasks.tests.common_fixtures.storages import \
    elastic_storage_implementation_mock


class TestCase40CreateTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        from ib_tasks.tests.factories.models import \
            ProjectTaskTemplateFactory, TaskTemplateFactory, \
            StageModelFactory, ActionPermittedRolesFactory, \
            StageActionFactory, GoFFactory, FieldFactory, \
            GoFToTaskTemplateFactory, GoFRoleFactory, FieldRoleFactory, \
            TaskTemplateStatusVariableFactory, \
            StagePermittedRolesFactory, TaskTemplateInitialStageFactory
        from ib_tasks.tests.factories.adapter_dtos import \
            UserDetailsDTOFactory, AssigneeDetailsDTOFactory

        ProjectTaskTemplateFactory.reset_sequence()
        TaskTemplateFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        GoFFactory.reset_sequence()
        FieldFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()
        GoFRoleFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()
        TaskTemplateStatusVariableFactory.reset_sequence()
        StagePermittedRolesFactory.reset_sequence()
        TaskTemplateInitialStageFactory.reset_sequence()
        UserDetailsDTOFactory.reset_sequence()
        AssigneeDetailsDTOFactory.reset_sequence()

        template_id = 'template_1'
        project_id = "project_1"
        stage_id = "stage_1"
        variable = "variable0"

        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_if_user_is_in_project_mock, \
            get_valid_project_ids_mock as auth_service_project_ids_mock,\
            get_projects_info_for_given_ids_mock, \
            get_team_info_for_given_user_ids_mock, \
            prepare_permitted_user_details_mock
        from ib_tasks.tests.common_fixtures. \
            adapters.assignees_details_service import \
            assignee_details_dtos_mock

        elastic_storage_implementation_mock(mocker)
        get_user_role_ids(mocker)
        is_user_in_project = True
        validate_if_user_is_in_project_mock(mocker, is_user_in_project)
        auth_service_project_ids_mock(mocker, [project_id])
        project_mock = get_valid_project_ids_mock(mocker)
        project_mock.return_value = [project_id]
        get_projects_info_for_given_ids_mock(mocker)
        get_user_id_team_details_dtos_mock(mocker)
        get_team_info_for_given_user_ids_mock(mocker)
        get_user_role_ids_based_on_project_mock(mocker)
        prepare_permitted_user_details_mock_method = \
            prepare_permitted_user_details_mock(mocker)
        assignee_details_dtos_mock_method = assignee_details_dtos_mock(mocker)

        prepare_permitted_user_details_mock_method.return_value = \
            UserDetailsDTOFactory.create_batch(
                size=2, user_id=factory.Iterator(["user_1", "user_2"]))
        assignee_details_dtos_mock_method.return_value = \
            AssigneeDetailsDTOFactory.create_batch(
                size=2, assignee_id=factory.Iterator(["user_1", "user_2"]))

        task_template_obj = TaskTemplateFactory.create(template_id=template_id)
        ProjectTaskTemplateFactory.create(
            task_template=task_template_obj, project_id=project_id)
        stage = StageModelFactory(
            stage_id=stage_id, stage_color="blue",
            task_template_id='template_1',
            display_logic="variable0==stage_1")
        path = 'ib_tasks.tests.populate.' \
               'stage_actions_logic.stage_1_action_name_1_logic'
        action = StageActionFactory(
            stage=stage, py_function_import_path=path,
            action_type=ActionTypes.NO_VALIDATIONS.value)
        ActionPermittedRolesFactory.create(
            action=action, role_id="FIN_PAYMENT_REQUESTER")
        TaskTemplateStatusVariableFactory.create(
            task_template_id=template_id, variable=variable)

        from ib_tasks.constants.constants import ALL_ROLES_ID
        StagePermittedRolesFactory.create(stage=stage, role_id=ALL_ROLES_ID)
        TaskTemplateInitialStageFactory.create(
            task_template_id=template_id, stage=stage)

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            "project_id": "project_1",
            "task_template_id": "template_1",
            "action_id": 1,
            "title": "task_title",
            "description": None,
            "start_datetime": None,
            "due_datetime": None,
            "priority": None,
            "task_gofs": []
        }
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)
