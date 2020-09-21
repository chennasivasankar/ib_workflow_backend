"""
# Given action is which is not in current stage raises exception
"""
import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.models import TaskTemplateGoFs, ProjectTaskTemplate
from ib_tasks.tests.factories.models import TaskTemplateFactory, \
    TaskTemplateStatusVariableFactory, GoFFactory, \
    FieldFactory, StageModelFactory, StageActionFactory, \
    TaskFactory, TaskStatusVariableFactory, TaskGoFFactory, \
    TaskGoFFieldFactory, \
    CurrentTaskStageModelFactory, GoFToTaskTemplateFactory, \
    ActionPermittedRolesFactory, \
    TaskTemplateInitialStageFactory, GoFRoleFactory, FieldRoleFactory, \
    StagePermittedRolesFactory, ProjectTaskTemplateFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01ActOnTaskAndUpdateTaskStageAssigneesAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskTemplateInitialStageFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        CurrentTaskStageModelFactory.reset_sequence()
        TaskGoFFieldFactory.reset_sequence()
        TaskGoFFactory.reset_sequence()
        TaskTemplateStatusVariableFactory.reset_sequence()
        TaskStatusVariableFactory.reset_sequence()
        TaskTemplateFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()
        TaskFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        GoFRoleFactory.reset_sequence()
        GoFFactory.reset_sequence()
        FieldFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()
        StagePermittedRolesFactory.reset_sequence()
        ProjectTaskTemplateFactory.reset_sequence()

    @pytest.fixture()
    def setup(self, reset_sequence):
        tts = TaskTemplateFactory.create_batch(3)
        TaskTemplateStatusVariableFactory.create_batch(
            4, task_template_id='template_1')
        import json
        gofs = GoFFactory.create_batch(3)
        ttg1 = TaskTemplateGoFs(task_template=tts[0], gof_id='gof_1', order=1)
        ttg2 = TaskTemplateGoFs(task_template=tts[0], gof_id='gof_2', order=1)
        ttg3 = TaskTemplateGoFs(task_template=tts[0], gof_id='gof_3', order=1)
        ttgs = [ttg1, ttg2, ttg3]
        TaskTemplateGoFs.objects.bulk_create(ttgs)
        fields = FieldFactory.create_batch(12, gof=factory.Iterator(gofs))

        stage1 = StageModelFactory(
            task_template_id='template_1',
            display_logic="variable0==stage_id_0",
            card_info_kanban=json.dumps(["FIELD_ID-1", "FIELD_ID-2"]),
            card_info_list=json.dumps(["FIELD_ID-1", "FIELD_ID-2"]),
        )
        stage2 = StageModelFactory(
            task_template_id='template_1',
            display_logic="variable1==stage_id_1",
            card_info_kanban=json.dumps(["FIELD_ID-1", "FIELD_ID-2"]),
            card_info_list=json.dumps(["FIELD_ID-1", "FIELD_ID-2"])
        )
        stage3 = StageModelFactory(
            task_template_id='template_1',
            display_logic="variable2==stage_id_2",
            card_info_kanban=json.dumps(["FIELD_ID-1", "FIELD_ID-2"]),
            card_info_list=json.dumps(["FIELD_ID-1", "FIELD_ID-2"])
        )
        stages = [stage1, stage2]
        actions = StageActionFactory.create_batch(6, stage=factory.Iterator(
            stages))
        action = StageActionFactory(stage=stage3)

        task = TaskFactory(template_id='template_1', task_display_id="IBWF-1")

        TaskStatusVariableFactory(task_id=1, variable='variable0',
                                  value="stage_id_0")
        TaskStatusVariableFactory(task_id=1, variable='variable1',
                                  value="stage_id_1")
        TaskStatusVariableFactory(task_id=1, variable='variable2',
                                  value="stage_id_2")
        TaskStatusVariableFactory(task_id=1, variable='variable3',
                                  value="stage_id_1")
        task_gofs = TaskGoFFactory.create_batch(
            6, task=task, gof_id=factory.Iterator(
                ['gof_1', 'gof_2', 'gof_3']),
            same_gof_order=factory.sequence(lambda n: "{}".format(n + 1)))

        TaskGoFFieldFactory.create_batch(
            6, task_gof=factory.Iterator(task_gofs),
            field=factory.Iterator(fields)
        )
        CurrentTaskStageModelFactory.create_batch(
            2, task=task,
            stage=factory.Iterator(stages)
        )
        ActionPermittedRolesFactory.create_batch(3, action=action)
        StagePermittedRolesFactory.create_batch(6, stage=factory.Iterator(
            stages), role_id=factory.Iterator(['role_1', 'role_2']))
        ProjectTaskTemplateFactory(task_template=tts[0], project_id='project_id_1')

    @pytest.mark.django_db
    def test_case(self, snapshot, setup, mocker):
        path = 'ib_tasks.adapters.boards_service.BoardsService.validate_board_id'
        mock_obj = mocker.patch(path)
        mock_obj.return_value = True
        user_path = 'ib_tasks.adapters.auth_service.AuthService.validate_if_user_is_in_project'
        mock_obj = mocker.patch(user_path)
        mock_obj.return_value = True
        roles_path = 'ib_iam.app_interfaces.service_interface.ServiceInterface.get_user_role_ids'
        roles_mock = mocker.patch(roles_path)
        roles_mock.return_value = ['role_1', 'role_2', 'role_3']
        path = 'ib_tasks.adapters.boards_service.BoardsService.get_display_boards_and_column_details'
        board_mock = mocker.patch(path)
        project_details_path = 'ib_tasks.adapters.auth_service.AuthService.get_projects_info_for_given_ids'
        project_mock = mocker.patch(project_details_path)
        elastic_search_path = 'ib_tasks.interactors.' \
                              'create_or_update_data_in_elasticsearch_interactor.' \
                              'CreateOrUpdateDataInElasticSearchInteractor.create_or_update_task_in_elasticsearch'
        elastic_search_mock = mocker.patch(elastic_search_path)
        project_ids_validation_mock = mocker.patch(
            'ib_tasks.adapters.auth_service.AuthService.validate_project_ids')
        project_ids_validation_mock.return_value = ['project_id_1']
        user_roles_mock = mocker.patch(
            "ib_tasks.adapters.roles_service.RolesService."
            "get_user_role_ids_based_on_project")
        user_roles_mock.return_value = ['role_1', 'role_2']

        from ib_tasks.tests.common_fixtures.interactors \
            import prepare_integration_task_boards_details
        task_board_dto = prepare_integration_task_boards_details()
        board_mock.return_value = task_board_dto
        body = {
            "task_id": "IBWF-1",
            "action_id": "7",
            "board_id": "board_1",
            "stage_assignees": [
                {
                    "stage_id": 1,
                    "assignee_id": "123e4567-e89b-12d3-a456-426614174004",
                    "team_id": "123e4567-e89b-12d3-a456-426614174001"
                },
                {
                    "stage_id": 2,
                    "assignee_id": "123e4567-e89b-12d3-a456-427614174008",
                    "team_id": "123e4567-e89b-12d3-a456-426614174002"
                },
                {
                    "stage_id": 3,
                    "assignee_id": "123e4567-e89b-12d3-a476-427614174006",
                    "team_id": "123e4567-e89b-12d3-a456-426614174003"
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

        from ib_tasks.models import TaskStageHistory
        task_stage_objs = TaskStageHistory.objects.all()
        counter = 1
        for task_stage_obj in task_stage_objs:
            snapshot.assert_match(
                name=f'stage_{counter}', value=task_stage_obj.stage_id
            )
            snapshot.assert_match(
                name=f'assignee_{counter}', value=task_stage_obj.assignee_id
            )
            snapshot.assert_match(
                name=f'left_{counter}', value=task_stage_obj.left_at
            )
            counter += counter
