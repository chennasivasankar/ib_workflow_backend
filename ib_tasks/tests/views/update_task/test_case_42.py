"""
test with valid details
"""

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.constants.enum import PermissionTypes, FieldTypes
from ib_tasks.tests.common_fixtures.adapters.auth_service import \
    get_projects_info_for_given_ids_mock, get_valid_project_ids_mock, \
    validate_if_user_is_in_project_mock
from ib_tasks.tests.factories.adapter_dtos import AssigneeDetailsDTOFactory
from ib_tasks.tests.factories.models import TaskFactory, GoFFactory, \
    TaskTemplateFactory, GoFToTaskTemplateFactory, FieldFactory, \
    GoFRoleFactory, FieldRoleFactory, StageFactory, StagePermittedRolesFactory, \
    ProjectTaskTemplateFactory, CurrentTaskStageModelFactory, StageGoFFactory
from ib_tasks.tests.views.update_task import APP_NAME, OPERATION_NAME, \
    REQUEST_METHOD, URL_SUFFIX


class TestCase42UpdateTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskFactory.reset_sequence()
        GoFFactory.reset_sequence()
        FieldFactory.reset_sequence()
        TaskTemplateFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()
        GoFRoleFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()
        StageFactory.reset_sequence()
        StagePermittedRolesFactory.reset_sequence()
        ProjectTaskTemplateFactory.reset_sequence()
        StageGoFFactory.reset_sequence()
        CurrentTaskStageModelFactory.reset_sequence()
        AssigneeDetailsDTOFactory.reset_sequence()

    @pytest.fixture
    def get_assignees_details_dtos_mock(self, mocker):
        path = "ib_tasks.adapters.assignees_details_service" \
               ".AssigneeDetailsService.get_assignees_details_dtos"
        mock = mocker.patch(path)
        return mock

    @pytest.fixture(autouse=True)
    def setup(self, mocker, get_assignees_details_dtos_mock):
        task_id = "IBWF-1"
        stage_id = 1
        template_id = "TEMPLATE-1"
        gof_id = "GOF-1"
        field_id = "FIELD-1"
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids_based_on_project_mock
        mock_method = get_user_role_ids_based_on_project_mock(mocker)
        get_assignees_details_dtos_mock.return_value = \
            [AssigneeDetailsDTOFactory(assignee_id="assignee_id_1")]
        user_roles = mock_method.return_value
        gof = GoFFactory.create(gof_id=gof_id)
        gof_role = GoFRoleFactory.create(
            role=user_roles[0], gof=gof,
            permission_type=PermissionTypes.WRITE.value)

        project_details_mock = get_projects_info_for_given_ids_mock(mocker)
        project_details_dtos = project_details_mock.return_value
        project_id = project_details_dtos[0].project_id
        get_valid_project_ids_mock(mocker, [project_id])
        validate_if_user_is_in_project_mock(mocker, True)

        field = FieldFactory.create(
            field_id=field_id, gof=gof,
            field_type=FieldTypes.FILE_UPLOADER.value,
            allowed_formats='[".zip", ".pdf"]'
        )

        field_role = FieldRoleFactory.create(
            role=user_roles[0], field=field,
            permission_type=PermissionTypes.WRITE.value)
        task_template = TaskTemplateFactory.create(template_id=template_id)
        ProjectTaskTemplateFactory.create(
            task_template=task_template, project_id=project_id)
        task_template_gofs = GoFToTaskTemplateFactory.create(
            task_template=task_template, gof=gof)
        task = TaskFactory.create(
            task_display_id=task_id, template_id=task_template.template_id,
            project_id=project_id
        )
        stage = StageFactory.create(
            id=1, task_template_id=task_template.template_id)
        StagePermittedRolesFactory.create(stage=stage, role_id=user_roles[0])
        StageGoFFactory.create(gof=gof, stage=stage)
        current_task_stage = CurrentTaskStageModelFactory.create(task=task,
                                                                 stage=stage)

    @pytest.mark.django_db
    def test_case(self, snapshot, mocker):
        body = {
            "task_id": "IBWF-1",
            "title": "updated_title",
            "description": "updated_description",
            "start_datetime": "2020-09-20 00:00:00",
            "due_datetime": "2020-10-31 00:00:00",
            "priority": "HIGH",
            "stage_assignee": {
                "stage_id": 1,
                "assignee_id": "assignee_id_1",
                "team_id": "team_1"
            },
            "task_gofs": [
                {
                    "gof_id": "GOF-1",
                    "same_gof_order": 0,
                    "gof_fields": [
                        {
                            "field_id": "FIELD-1",
                            "field_response": "https://www.url.com/file.zip"
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
        from ib_tasks.models import Task
        task = Task.objects.get(task_display_id="IBWF-1")
        snapshot.assert_match(name="task_title", value=task.title)
        snapshot.assert_match(name="task_description", value=task.description)
        snapshot.assert_match(name="task_start_date",
                              value=str(task.start_date))
        snapshot.assert_match(name="task_due_date",
                              value=str(task.due_date))
        snapshot.assert_match(name="task_priority", value=task.priority)
        from ib_tasks.models import TaskGoF
        task_gofs = TaskGoF.objects.filter(
            gof_id="GOF-1", task=task)
        from ib_tasks.models import TaskGoFField
        task_gof_fields = TaskGoFField.objects.filter(task_gof__in=task_gofs)

        for task_gof_field in task_gof_fields:
            snapshot.assert_match(
                name=task_gof_field.field_id,
                value=task_gof_field.field_response)
            snapshot.assert_match(
                name=f"{task_gof_field.field_id} response",
                value=task_gof_field.field_response)
        from ib_tasks.models import TaskStageHistory
        task_stage_history = TaskStageHistory.objects.get(task=task,
                                                          stage_id=1)
        snapshot.assert_match(
            name="task_stage_id", value=task_stage_history.stage_id)
        snapshot.assert_match(
            name="task_stage_assignee_id", value=task_stage_history.assignee_id
        )
