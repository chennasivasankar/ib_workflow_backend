"""
# TODO: Update test case description
"""
import pytest
import factory
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ib_tasks.tests.factories.models import TaskTemplateFactory, \
    TaskTemplateStatusVariableFactory, TaskTemplateWith2GoFsFactory, GoFFactory, \
    FieldFactory, StageModelFactory, StageActionFactory, \
    TaskFactory, TaskStatusVariableFactory, TaskGoFFactory, TaskGoFFieldFactory, \
    TaskStageModelFactory, GoFToTaskTemplateFactory, ActionPermittedRolesFactory, TaskTemplateInitialStageFactory


class TestCase01PerformTaskActionAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['superuser']}}

    @pytest.fixture(autouse=True)
    def setup(self):
        from ib_tasks.tests.factories.models import TaskTemplateFactory, \
            StageModelFactory, StageActionFactory, GoFFactory, GoFRoleFactory, \
            FieldFactory, FieldRoleFactory, GoFToTaskTemplateFactory, TaskFactory

        TaskTemplateFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        GoFRoleFactory.reset_sequence()
        GoFFactory.reset_sequence()
        FieldFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()
        self.create_task_templates()


    @staticmethod
    def create_task_templates():
        tts = TaskTemplateFactory.create_batch(3)
        TaskTemplateStatusVariableFactory.create_batch(
            4, task_template_id='template_1')
        import json
        gofs = GoFFactory.create_batch(3)
        fields = FieldFactory.create_batch(12, gof=factory.Iterator(gofs))
        GoFToTaskTemplateFactory.create_batch(
            6, task_template=factory.Iterator(tts),
            gof=factory.Iterator(gofs)
        )
        stages = StageModelFactory.create_batch(
            3, task_template_id='template_1',
            field_display_config=json.dumps(["FIELD_ID-1", "FIELD_ID-2"])
        )

        path = 'ib_tasks.populate.stage_actions_logic.stage_1_action_name_1'
        action = StageActionFactory(stage=stages[0], py_function_import_path=path)
        actions = StageActionFactory.create_batch(6,stage=factory.Iterator(stages))
        TaskTemplateInitialStageFactory.create_batch(
            6, task_template=factory.Iterator(tts),
            stage=factory.Iterator(stages)
        )

        task = TaskFactory(template_id='template_1')
        TaskStatusVariableFactory(task_id=1, variable='variable0', value="stage_id_0")
        TaskStatusVariableFactory(task_id=1, variable='variable1', value="stage_id_1")
        TaskStatusVariableFactory(task_id=1, variable='variable2', value="stage_id_2")
        TaskStatusVariableFactory(task_id=1, variable='variable3', value="stage_id_1")
        task_gofs = TaskGoFFactory.create_batch(
            6, task=task, gof_id=factory.Iterator(
                ['gof_1', 'gof_2', 'gof_3']
            )
        )
        TaskGoFFieldFactory.create_batch(
            6, task_gof=factory.Iterator(task_gofs),
            field=factory.Iterator(fields)
        )
        TaskStageModelFactory.create_batch(
            3, task=task,
            stage=factory.Iterator(stages)
        )
        ActionPermittedRolesFactory.create_batch(3, action=action)

    @pytest.mark.django_db
    def test_case(self, snapshot, mocker):
        path = 'ib_tasks.adapters.boards_service.BoardsService.validate_board_id'
        mock_obj = mocker.patch(path)
        roles_path = 'ib_iam.app_interfaces.service_interface.ServiceInterface.get_user_role_ids'
        roles_mock = mocker.patch(roles_path)
        roles_mock.return_value = ['role_1', 'role_2', 'role_3']

        body = {"task_id": "1", "action_id": "1",
                       "board_id": "board_1"}
        path_params = {}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
        mock_obj.called_once()