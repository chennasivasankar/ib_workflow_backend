"""
test with valid details create transition checklist
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01CreateTransitionChecklistAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read', 'write']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        import json
        import factory
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
        gof_ids = ["gof_1", "gof_2"]
        field_ids = ["field_1", "field_2", "field_3"]

        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids(mocker)

        transition_template_obj = TaskTemplateFactory.create(
            template_id=transition_template_id, is_transition_template=True)
        TaskFactory.create(template_id=transition_template_id)
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
            transition_template=transition_template_obj
        )
        ActionPermittedRolesFactory.create(
            action=action, role_id="FIN_PAYMENT_REQUESTER")
        gof_objs = GoFFactory.create_batch(
            size=2, gof_id=factory.Iterator(gof_ids))

        from ib_tasks.constants.enum import FieldTypes
        field_objs_of_gof_1 = \
            FieldFactory.create_batch(
                size=2,
                field_id=factory.Iterator([field_ids[0], field_ids[1]]),
                gof=gof_objs[0])
        field_objs_of_gof_2 = FieldFactory.create(
            field_id=field_ids[2], gof=gof_objs[1],
            field_type=FieldTypes.PASSWORD.value
        )
        field_objs = field_objs_of_gof_1
        field_objs.append(field_objs_of_gof_2)

        GoFToTaskTemplateFactory.create_batch(
            size=2, gof=factory.Iterator(gof_objs),
            task_template=transition_template_obj)

        from ib_tasks.constants.enum import PermissionTypes
        GoFRoleFactory.create_batch(
            size=2, gof=factory.Iterator(gof_objs),
            permission_type=PermissionTypes.WRITE.value,
            role="FIN_PAYMENT_REQUESTER"
        )
        FieldRoleFactory.create_batch(
            size=3, field=factory.Iterator(field_objs),
            role="FIN_PAYMENT_REQUESTER",
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
                            'field_response': "iBHubs"
                        },
                        {
                            'field_id': 'field_2',
                            'field_response': "ProYuga"
                        }
                    ]
                },
                {
                    'gof_id': 'gof_2',
                    'same_gof_order': 1,
                    'gof_fields': [
                        {
                            'field_id': 'field_3',
                            'field_response': "iB@123!"
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

        gof_ids = ["gof_1", "gof_2"]
        field_ids = ["field_1", "field_2", "field_3"]

        from ib_tasks.models import Task
        task_object = Task.objects.get(id=1)

        snapshot.assert_match(task_object.id, 'task_id')
        snapshot.assert_match(task_object.template_id, 'template_id')
        snapshot.assert_match(task_object.title, 'task_title')
        snapshot.assert_match(task_object.description, 'task_description')
        snapshot.assert_match(str(task_object.start_date), 'task_start_date')
        snapshot.assert_match(str(task_object.due_date), 'task_due_date')
        snapshot.assert_match(task_object.priority, 'task_priority')

        from ib_tasks.models.task_gof import TaskGoF
        task_gof_objs = TaskGoF.objects.filter(task_id=1, gof_id__in=gof_ids)

        counter = 1
        for task_gof_obj in task_gof_objs:
            snapshot.assert_match(
                task_gof_obj.same_gof_order,
                f'same_gof_order_of_gof_{counter}')
            snapshot.assert_match(
                task_gof_obj.gof_id, f'gof_id_of_gof_{counter}')
            snapshot.assert_match(
                task_gof_obj.task_id, f'task_id_for_gof_{counter}')
            counter = counter + 1

        from ib_tasks.models.task_gof_field import TaskGoFField
        task_gof_field_objs = TaskGoFField.objects.filter(
            task_gof__task_id=1, field_id__in=field_ids
        )

        counter = 1
        for task_gof_field_obj in task_gof_field_objs:
            snapshot.assert_match(task_gof_field_obj.task_gof_id,
                                  f'gof_id_of_gof_field_{counter}')
            snapshot.assert_match(
                task_gof_field_obj.field_id,
                f'field_id_of_gof_field_{counter}')
            snapshot.assert_match(
                task_gof_field_obj.field_response,
                f'field_response_of_gof_field_{counter}')
            counter = counter + 1
