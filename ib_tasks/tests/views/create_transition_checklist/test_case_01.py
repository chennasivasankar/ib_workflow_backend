"""
test with invalid file format for file uploader field raises exception
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase32CreateTransitionChecklistAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read', 'write']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        import json
        from ib_tasks.tests.factories.models import TaskTemplateFactory, \
            TaskFactory, StageActionFactory, StageModelFactory, \
            ActionPermittedRolesFactory, GoFFactory, FieldFactory, \
            GoFToTaskTemplateFactory, GoFRoleFactory, FieldRoleFactory

        TaskTemplateFactory.reset_sequence()
        TaskFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        GoFFactory.reset_sequence()
        FieldFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()
        GoFRoleFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()

        transition_template_id = "transition_template_1"
        stage_id = "stage_1"
        gof_id = "gof_1"
        field_id = "field_1"

        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids_based_on_project_mock
        get_user_role_ids_based_on_project_mock(mocker)

        transition_template_obj = TaskTemplateFactory.create(
            template_id=transition_template_id, is_transition_template=True)
        TaskFactory.create()
        stage = StageModelFactory(
            stage_id=stage_id,
            task_template_id=transition_template_id,
            display_logic="variable0==stage_1",
            card_info_kanban=json.dumps(["FIELD_ID-0", "FIELD_ID-1"]),
            card_info_list=json.dumps(["FIELD_ID-0", "FIELD_ID-1"]))
        path = 'ib_tasks.tests.populate.' \
               'stage_actions_logic.stage_1_action_name_1_logic'
        action = StageActionFactory(
            stage=stage, py_function_import_path=path,
            transition_template=transition_template_obj,
            action_type=None)
        ActionPermittedRolesFactory.create(
            action=action, role_id="FIN_PAYMENT_REQUESTER")
        gof_obj = GoFFactory.create(gof_id=gof_id)

        from ib_tasks.constants.enum import FieldTypes
        field_obj = FieldFactory.create(
            field_id=field_id, gof=gof_obj,
            field_type=FieldTypes.PLAIN_TEXT.value)

        GoFToTaskTemplateFactory.create(
            gof=gof_obj, task_template=transition_template_obj)

        from ib_tasks.constants.enum import PermissionTypes
        GoFRoleFactory.create(
            gof=gof_obj, permission_type=PermissionTypes.WRITE.value,
            role="FIN_PAYMENT_REQUESTER"
        )
        FieldRoleFactory.create(
            field=field_obj, role="FIN_PAYMENT_REQUESTER",
            permission_type=PermissionTypes.WRITE.value
        )

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            'task_id': 'IBWF-1',
            'transition_checklist_template_id': 'transition_template_1',
            'action_id': 1,
            'stage_id': 1,
            'transition_checklist_gofs': [
                {
                    'gof_id': 'gof_1',
                    'same_gof_order': 1,
                    'gof_fields': [
                        {
                            'field_id': 'field_1',
                            'field_response': "hello world"
                        }
                    ]
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

        from ib_tasks.models.task import Task
        task_object = Task.objects.get(id=1)
        snapshot.assert_match(task_object.id, 'task_id')
        snapshot.assert_match(task_object.template_id, 'template_id')
        snapshot.assert_match(task_object.title, 'task_title')
        snapshot.assert_match(task_object.description, 'task_description')
        snapshot.assert_match(str(task_object.start_date), 'task_start_date')
        snapshot.assert_match(str(task_object.due_date), 'task_due_date')
        snapshot.assert_match(task_object.priority, 'task_priority')

        from ib_tasks.models.task_gof import TaskGoF
        task_gofs = TaskGoF.objects.filter(task_id=1)
        counter = 1
        for task_gof in task_gofs:
            snapshot.assert_match(
                task_gof.same_gof_order, f'same_gof_order_{counter}')
            snapshot.assert_match(task_gof.gof_id, f'gof_id_{counter}')
            snapshot.assert_match(task_gof.task_id,
                                  f'gof_task_id_{counter}')
            counter = counter + 1

        from ib_tasks.models.task_gof_field import TaskGoFField
        task_gof_fields = TaskGoFField.objects.filter(task_gof__task_id=1)
        counter = 1
        for task_gof_field in task_gof_fields:
            snapshot.assert_match(task_gof_field.task_gof_id,
                                  f'task_gof_{counter}')
            snapshot.assert_match(task_gof_field.field_id, f'field_{counter}')
            snapshot.assert_match(task_gof_field.field_response,
                                  f'field_response_{counter}')
            counter = counter + 1
