"""
save and act on a task (update task) success test case
"""
import json

import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from freezegun import freeze_time

from ib_tasks.constants.enum import FieldTypes, PermissionTypes
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...common_fixtures.adapters.auth_service import \
    get_projects_info_for_given_ids_mock, get_valid_project_ids_mock, \
    validate_if_user_is_in_project_mock, \
    prepare_empty_permitted_user_details_mock, \
    get_team_info_for_given_user_ids_mock
from ...common_fixtures.adapters.roles_service import get_some_user_role_ids
from ...factories.adapter_dtos import ProjectDetailsDTOFactory, \
    AssigneeDetailsDTOFactory, UserDetailsDTOFactory, TeamDetailsDTOFactory, \
    UserIdWIthTeamDetailsDTOsFactory
from ...factories.models import StageModelFactory, StageActionFactory, \
    ActionPermittedRolesFactory, \
    CurrentTaskStageModelFactory, TaskStatusVariableFactory, \
    StagePermittedRolesFactory, StageGoFFactory, ProjectTaskTemplateFactory


class TestCase01SaveAndActOnATaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture
    def get_assignees_details_dtos_mock(self, mocker):
        path = "ib_tasks.adapters.assignees_details_service" \
               ".AssigneeDetailsService.get_assignees_details_dtos"
        mock = mocker.patch(path)
        return mock

    @pytest.fixture(autouse=True)
    def setup(self, mocker, get_assignees_details_dtos_mock):
        import factory
        from ib_tasks.tests.factories.models import TaskTemplateFactory, \
            GoFFactory, GoFRoleFactory, TaskFactory, TaskGoFFactory, \
            FieldFactory, FieldRoleFactory, GoFToTaskTemplateFactory, \
            TaskGoFFieldFactory

        TaskTemplateFactory.reset_sequence()
        GoFRoleFactory.reset_sequence()
        GoFFactory.reset_sequence()
        FieldFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()
        StagePermittedRolesFactory.reset_sequence()
        StageGoFFactory.reset_sequence()
        ProjectDetailsDTOFactory.reset_sequence()
        ProjectTaskTemplateFactory.reset_sequence()
        AssigneeDetailsDTOFactory.reset_sequence()
        TeamDetailsDTOFactory.reset_sequence()
        UserIdWIthTeamDetailsDTOsFactory.reset_sequence()

        project_id = "project_1"
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids_based_on_project_mock
        get_user_role_ids_based_on_project_mock(mocker)
        get_some_user_role_ids(mocker)
        permitted_user_details_mock = \
            prepare_empty_permitted_user_details_mock(mocker)
        user_details = UserDetailsDTOFactory()
        permitted_user_details_mock.return_value = [user_details]
        get_team_info_for_given_user_ids_mock(mocker).return_value = \
            [UserIdWIthTeamDetailsDTOsFactory(user_id=user_details.user_id)]

        project_info_dtos = ProjectDetailsDTOFactory.create(
            project_id=project_id)
        project_info_mock = get_projects_info_for_given_ids_mock(mocker)
        project_info_mock.return_value = [project_info_dtos]
        get_valid_project_ids_mock(mocker, [project_id])
        validate_if_user_is_in_project_mock(mocker, True)
        get_assignees_details_dtos_mock.return_value = [
            AssigneeDetailsDTOFactory(assignee_id="assignee_id_1")]

        template_id = "template_1"
        gofs = GoFFactory.create_batch(size=2)
        task_template = TaskTemplateFactory.create(template_id=template_id)
        ProjectTaskTemplateFactory.create(task_template=task_template,
                                          project_id=project_id)
        GoFToTaskTemplateFactory.create_batch(
            size=2, task_template=task_template, gof=factory.Iterator(gofs))
        plain_text = FieldFactory.create(
            gof=gofs[0], field_type=FieldTypes.PLAIN_TEXT.value
        )
        image_field = FieldFactory.create(
            gof=gofs[0], field_type=FieldTypes.IMAGE_UPLOADER.value,
            allowed_formats='[".jpeg", ".png", ".svg"]'
        )
        checkbox_group = FieldFactory.create(
            gof=gofs[1], field_type=FieldTypes.CHECKBOX_GROUP.value,
            field_values='["interactors", "storages", "presenters"]')
        fields = [plain_text, image_field, checkbox_group]
        FieldRoleFactory.create_batch(
            size=len(fields), role="FIN_PAYMENT_REQUESTER",
            field=factory.Iterator(fields),
            permission_type=PermissionTypes.WRITE.value)
        task_obj = TaskFactory.create(
            task_display_id="IBWF-1", template_id="template_1",
            project_id=project_id)
        task_gofs = TaskGoFFactory.create_batch(
            size=len(gofs), gof=factory.Iterator(gofs), task=task_obj)
        TaskGoFFieldFactory.create(
            task_gof=task_gofs[0],
            field=plain_text, field_response="string")
        TaskGoFFieldFactory.create(
            task_gof=task_gofs[0],
            field=image_field,
            field_response="https://www.freepngimg.com/thumb/light/20246-4" \
                           "-light-transparent.png"
        )
        TaskGoFFieldFactory.create(
            task_gof=task_gofs[1],
            field=checkbox_group,
            field_response='["interactors", "storages"]'
        )
        stage = StageModelFactory(
            task_template_id=task_template.template_id,
            display_logic="variable0==stage_id_0",
            card_info_kanban=json.dumps(["FIELD_ID-1", "FIELD_ID-2"]),
            card_info_list=json.dumps(["FIELD_ID-1", "FIELD_ID-2"]),
        )
        StageGoFFactory.create_batch(
            size=len(gofs), gof=factory.Iterator(gofs), stage=stage)
        TaskStatusVariableFactory.create(
            task_id=task_obj.id, variable="variable0", value=stage.stage_id)
        TaskStatusVariableFactory.create(
            task_id=task_obj.id, variable="stage_id_0", value=stage.stage_id)
        path = \
            'ib_tasks.tests.populate.stage_actions_logic.stage_1_action_name_3'
        action = StageActionFactory(stage=stage, py_function_import_path=path)
        ActionPermittedRolesFactory.create(
            action=action, role_id="FIN_PAYMENT_REQUESTER")
        CurrentTaskStageModelFactory.create(task=task_obj, stage=stage)
        StagePermittedRolesFactory.create(stage=stage,
                                          role_id="FIN_PAYMENT_REQUESTER")

    @freeze_time("2020-09-09 12:00:00")
    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            "task_id": "IBWF-1",
            "action_id": 1,
            "title": "updated_title",
            "description": "updated_description",
            "start_datetime": "2020-08-20 00:00:00",
            "due_datetime": "2020-09-20 00:00:00",
            "priority": "HIGH",
            "stage_assignee": {
                "stage_id": 1,
                "assignee_id": "assignee_id_1",
                "team_id": "team_alpha"
            },
            "task_gofs": [
                {
                    "gof_id": "gof_1",
                    "same_gof_order": 0,
                    "gof_fields": [
                        {
                            "field_id": "FIELD_ID-0",
                            "field_response": "new updated string"
                        },
                        {
                            "field_id": "FIELD_ID-1",
                            "field_response":
                                "https://image.flaticon.com/icons/svg/1829/1829070.svg"
                        }
                    ]
                },
                {
                    "gof_id": "gof_2",
                    "same_gof_order": 0,
                    "gof_fields": [
                        {
                            "field_id": "FIELD_ID-2",
                            "field_response": "[\"interactors\"]"
                        }
                    ]
                }
            ]
        }
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
        from ib_tasks.models.task import Task
        task_object = Task.objects.get(task_display_id="IBWF-1")
        task_id = task_object.id
        snapshot.assert_match(task_object.template_id, 'template_id')
        snapshot.assert_match(task_object.created_by, 'created_by_id')
        snapshot.assert_match(task_object.template_id, 'task_template_id')
        snapshot.assert_match(task_object.title, 'task_title')
        snapshot.assert_match(task_object.description, 'task_description')
        snapshot.assert_match(str(task_object.start_date), 'task_start_date')
        snapshot.assert_match(str(task_object.due_date), 'task_due_date')
        snapshot.assert_match(task_object.priority, 'task_priority')

        from ib_tasks.models.task_gof import TaskGoF
        task_gofs = TaskGoF.objects.filter(task_id=1)
        counter = 1
        for task_gof in task_gofs:
            snapshot.assert_match(task_gof.same_gof_order,
                                  f'same_gof_order_{counter}')
            snapshot.assert_match(task_gof.gof_id, f'gof_id_{counter}')
            snapshot.assert_match(
                task_gof.task.task_display_id, f'task_id_{counter}')

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
                current_task_stage.task_id,
                f'current_task_stage_task_id_{counter}')
            snapshot.assert_match(
                current_task_stage.stage_id, f'task_stage_{counter}')
            counter += 1

        counter = 1
        from ib_tasks.models import TaskStageHistory
        task_stage_histories = TaskStageHistory.objects.filter(task_id=task_id)
        for task_stage_history in task_stage_histories:
            snapshot.assert_match(
                task_stage_history.task_id,
                f'stage_history_task_id_{counter}')
            snapshot.assert_match(
                task_stage_history.stage_id, f'stage_{counter}')
            snapshot.assert_match(
                task_stage_history.team_id, f'team_id_{counter}')
            snapshot.assert_match(
                task_stage_history.assignee_id, f'assignee_id_{counter}')
            snapshot.assert_match(
                str(task_stage_history.joined_at), f'joined_at_{counter}')
            snapshot.assert_match(
                str(task_stage_history.left_at), f'left_at_{counter}')
            counter += 1
