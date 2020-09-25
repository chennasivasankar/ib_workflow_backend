"""
test with valid details when only task title is give creates a sub task
"""
import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from freezegun import freeze_time

from ib_tasks.constants.constants import ALL_ROLES_ID
from ib_tasks.constants.enum import ActionTypes
from ib_tasks.tests.common_fixtures.adapters.project_service import \
    get_valid_project_ids_mock
from ib_tasks.tests.views.create_sub_task import APP_NAME, OPERATION_NAME, \
    REQUEST_METHOD, URL_SUFFIX
from ib_tasks.tests.common_fixtures.adapters.assignees_details_service import \
    assignee_details_dtos_mock
from ib_tasks.tests.common_fixtures.adapters.auth_service import \
    validate_if_user_is_in_project_mock, \
    get_valid_project_ids_mock as auth_service_project_ids_mock, \
    get_projects_info_for_given_ids_mock, \
    get_team_info_for_given_user_ids_mock, prepare_permitted_user_details_mock, \
    get_user_id_team_details_dtos_mock
from ib_tasks.tests.common_fixtures.adapters.roles_service import \
    get_user_role_ids, get_user_role_ids_based_on_project_mock
from ib_tasks.tests.common_fixtures.storages import \
    elastic_storage_implementation_mock
from ib_tasks.tests.factories.adapter_dtos import UserDetailsDTOFactory, \
    AssigneeDetailsDTOFactory
from ib_tasks.tests.factories import models


class TestCase02CreateSubTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def setup(self, api_user, mocker):
        models.TaskFactory.reset_sequence()
        models.TaskTemplateFactory.reset_sequence()
        models.StageActionFactory.reset_sequence()
        models.ProjectTaskTemplateFactory.reset_sequence()
        models.StageModelFactory.reset_sequence()
        models.ActionPermittedRolesFactory.reset_sequence()
        models.TaskTemplateStatusVariableFactory.reset_sequence()
        models.TaskTemplateInitialStageFactory.reset_sequence()
        models.StagePermittedRolesFactory.reset_sequence()

        parent_task_id = "IBWF-1"
        template_id = "template_1"
        project_id = "project_1"
        stage_id = 1
        action_id = 1
        variable = "variable0"

        elastic_storage_implementation_mock(mocker)
        get_user_role_ids(mocker)
        is_user_in_project = True
        validate_if_user_is_in_project_mock(mocker, is_user_in_project)
        auth_service_project_ids_mock(mocker, [project_id])
        project_mock = get_valid_project_ids_mock(mocker)
        project_mock.return_value = [project_id]
        get_projects_info_for_given_ids_mock(mocker)
        get_user_id_team_details_dtos_mock(mocker)
        get_projects_info_for_given_ids_mock(mocker)
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

        template_obj = models.TaskTemplateFactory.create(template_id=template_id)
        models.TaskFactory.create(task_display_id=parent_task_id,
                                  template_id=template_id)
        models.ProjectTaskTemplateFactory.create(
            project_id=project_id, task_template=template_obj)
        stage = models.StageModelFactory(
            stage_id=stage_id, stage_color="blue",
            task_template_id='template_1',
            display_logic="variable0==stage_1")
        path = 'ib_tasks.tests.populate.' \
               'stage_actions_logic.stage_1_action_name_1_logic'
        action = models.StageActionFactory(
            id=action_id, stage=stage, py_function_import_path=path,
            action_type=ActionTypes.NO_VALIDATIONS.value)
        models.ActionPermittedRolesFactory.create(
            action=action, role_id="FIN_PAYMENT_REQUESTER")
        models.StagePermittedRolesFactory.create(stage=stage, role_id=ALL_ROLES_ID)
        models.TaskTemplateInitialStageFactory.create(
            task_template_id=template_id, stage=stage)
        models.TaskTemplateStatusVariableFactory.create(
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
            "start_datetime": None,
            "due_datetime": None,
            "priority": None,
            "task_gofs": []
        }
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)

        from ib_tasks.models.task import Task
        parent_task_object = Task.objects.get(task_display_id="IBWF-1")
        snapshot.assert_match(parent_task_object.id, 'parent_task_id')
        snapshot.assert_match(parent_task_object.template_id,
                              'parent_task_template_id')
        snapshot.assert_match(parent_task_object.title, 'parent_task_title')
        snapshot.assert_match(parent_task_object.description,
                              'parent_task_description')
        snapshot.assert_match(str(parent_task_object.start_date),
                              'parent_task_start_date')
        snapshot.assert_match(str(parent_task_object.due_date),
                              'parent_task_due_date')
        snapshot.assert_match(parent_task_object.priority,
                              'parent_task_priority')

        sub_task_object = Task.objects.get(task_display_id="IBWF-2")
        snapshot.assert_match(sub_task_object.id, 'sub_task_id')
        snapshot.assert_match(sub_task_object.template_id,
                              'sub_task_template_id')
        snapshot.assert_match(sub_task_object.title, 'sub_task_title')
        snapshot.assert_match(sub_task_object.description,
                              'sub_task_description')
        snapshot.assert_match(str(sub_task_object.start_date),
                              'sub_task_start_date')
        snapshot.assert_match(str(sub_task_object.due_date),
                              'sub_task_due_date')
        snapshot.assert_match(sub_task_object.priority,
                              'sub_task_priority')

        task_id = 1
        from ib_tasks.models.task_gof import TaskGoF
        task_gofs = TaskGoF.objects.filter(task_id=task_id)
        counter = 1
        for task_gof in task_gofs:
            snapshot.assert_match(
                task_gof.same_gof_order, f'same_gof_order_{counter}')
            snapshot.assert_match(task_gof.gof_id, f'gof_id_{counter}')
            snapshot.assert_match(task_gof.task_id,
                                  f'gof_task_id_{counter}')
            counter = counter + 1

        from ib_tasks.models.task_gof_field import TaskGoFField
        task_gof_fields = TaskGoFField.objects.filter(
            task_gof__task_id=task_id)
        counter = 1
        for task_gof_field in task_gof_fields:
            snapshot.assert_match(task_gof_field.task_gof_id,
                                  f'task_gof_{counter}')
            snapshot.assert_match(task_gof_field.field_id, f'field_{counter}')
            snapshot.assert_match(task_gof_field.field_response,
                                  f'field_response_{counter}')
            counter = counter + 1

        from ib_tasks.models import CurrentTaskStage
        current_task_stages = CurrentTaskStage.objects.filter(task_id=task_id)
        counter = 1
        for current_task_stage in current_task_stages:
            snapshot.assert_match(
                current_task_stage.task_id, f'task_id_{counter}')
            snapshot.assert_match(
                current_task_stage.stage_id, f'task_stage_{counter}'
            )
            counter += 1

        counter = 1
        from ib_tasks.models import TaskStageHistory
        task_stage_histories = TaskStageHistory.objects.filter(task_id=task_id)
        for task_stage_history in task_stage_histories:
            snapshot.assert_match(
                task_stage_history.task_id, f'task_id_{counter}')
            snapshot.assert_match(
                task_stage_history.stage, f'stage_{counter}')
            snapshot.assert_match(
                task_stage_history.team_id, f'team_id_{counter}')
            snapshot.assert_match(
                task_stage_history.assignee_id, f'assignee_id_{counter}')
            snapshot.assert_match(
                task_stage_history.joined_at, f'joined_at_{counter}')
            snapshot.assert_match(
                task_stage_history.left_at, f'left_at_{counter}')
        from ib_tasks.models import SubTask
        sub_task = SubTask.objects.get(task_id=parent_task_object.id)
        snapshot.assert_match(sub_task.task.task_display_id, 'parent_task')
        snapshot.assert_match(sub_task.sub_task.task_display_id, 'sub_task')
        from ib_tasks.models import TaskLog
        task_log = TaskLog.objects.get(task=sub_task_object)
        snapshot.assert_match(task_log.task_json, 'sub_task_request_body')
        snapshot.assert_match(task_log.task.task_display_id,
                              'task_log_sub_task_id')
        snapshot.assert_match(task_log.action_id,
                              'sub_task_performed_action_id')
        snapshot.assert_match(str(task_log.acted_at), 'sub_task_acted_at')
