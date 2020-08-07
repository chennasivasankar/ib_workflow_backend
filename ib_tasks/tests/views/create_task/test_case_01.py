"""
create task with valid details
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01CreateTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        import factory
        from ib_tasks.tests.factories.models import \
            ActionPermittedRolesFactory, \
            StageModelFactory, TaskTemplateStatusVariableFactory, \
            TaskTemplateWith2GoFsFactory, TaskTemplateFactory, FieldFactory, \
            StageActionFactory, TaskTemplateInitialStageFactory

        TaskTemplateFactory.reset_sequence()
        TaskTemplateStatusVariableFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        FieldFactory.reset_sequence()
        StageActionFactory.reset_sequence(1)
        TaskTemplateInitialStageFactory.reset_sequence()

        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids(mocker)

        import json
        template_id = 'template_1'
        TaskTemplateWith2GoFsFactory.create(template_id=template_id)

        TaskTemplateStatusVariableFactory.create_batch(
            4, task_template_id=template_id
        )

        from ib_tasks.models import GoF
        gofs = GoF.objects.all()
        FieldFactory.create_batch(12, gof=factory.Iterator(gofs))

        stage = StageModelFactory(
            task_template_id='template_1',
            display_logic="variable0==stage_id_0",
            card_info_kanban=json.dumps(["FIELD_ID-1", "FIELD_ID-2"]),
            card_info_list=json.dumps(["FIELD_ID-1", "FIELD_ID-2"]),
        )
        path = \
            'ib_tasks.tests.populate.stage_actions_logic.stage_1_action_name_3'
        action = StageActionFactory(stage=stage, py_function_import_path=path)
        TaskTemplateInitialStageFactory.create_batch(
            1, task_template_id=template_id, stage=stage
        )
        ActionPermittedRolesFactory.create(
            action=action, role_id="FIN_PAYMENT_REQUESTER")

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            "task_template_id": "template_1",
            "action_id": 1,
            "title": "task_title",
            "description": "task_description",
            "start_date": "2099-12-31",
            "due_date": {
                "date": "2099-12-31",
                "time": "12:00:00"
            },
            "priority": "HIGH",
            "task_gofs": [
                {
                    "gof_id": "gof_1",
                    "same_gof_order": 0,
                    "gof_fields": [
                        {
                            "field_id": "FIELD_ID-0",
                            "field_response": "string"
                        }
                    ]
                }
            ]
        }
        path_params = {}
        query_params = {}
        headers = {}

        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
        from ib_tasks.models.task import Task
        task_object = Task.objects.get(id=1)
        snapshot.assert_match(task_object.id, 'task_id')
        snapshot.assert_match(task_object.template_id, 'template_id')
        snapshot.assert_match(task_object.title, 'task_title')
        snapshot.assert_match(task_object.description, 'task_description')
        snapshot.assert_match(task_object.start_date, 'task_start_date')
        snapshot.assert_match(task_object.due_date, 'task_due_date')
        snapshot.assert_match(task_object.priority, 'task_priority')

        from ib_tasks.models.task_gof import TaskGoF
        task_gofs = TaskGoF.objects.filter(task_id=1)
        counter = 1
        for task_gof in task_gofs:
            snapshot.assert_match(
                task_gof.same_gof_order, f'same_gof_order_{counter}')
            snapshot.assert_match(task_gof.gof_id, f'gof_id_{counter}')
            snapshot.assert_match(task_gof.task_id, f'gof_task_id_{counter}')
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
