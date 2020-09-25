"""
test with user did not fill required and stage permitted fields for the
current task stage
"""
import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.constants.enum import PermissionTypes, FieldTypes
from ib_tasks.tests.common_fixtures.adapters.auth_service import \
    get_projects_info_for_given_ids_mock, get_valid_project_ids_mock, \
    validate_if_user_is_in_project_mock
from ib_tasks.tests.factories.models import TaskFactory, GoFFactory, \
    TaskTemplateFactory, GoFToTaskTemplateFactory, FieldFactory, \
    GoFRoleFactory, FieldRoleFactory, StageFactory, StageGoFFactory, \
    CurrentTaskStageModelFactory
from ib_tasks.tests.views.update_task import APP_NAME, OPERATION_NAME, \
    REQUEST_METHOD, URL_SUFFIX


class TestCase40UpdateTaskAPITestCase(TestUtils):
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
        StageGoFFactory.reset_sequence()
        CurrentTaskStageModelFactory.reset_sequence()

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        task_id = "IBWF-1"
        stage_id = 1
        template_id = "TEMPLATE-1"
        gof_id = "GOF-1"
        field_id = "FIELD-1"
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids_based_on_project_mock
        mock_method = get_user_role_ids_based_on_project_mock(mocker)
        user_roles = mock_method.return_value

        project_details_mock = get_projects_info_for_given_ids_mock(mocker)
        project_details_dtos = project_details_mock.return_value
        project_id = project_details_dtos[0].project_id
        get_valid_project_ids_mock(mocker, [project_id])
        validate_if_user_is_in_project_mock(mocker, True)

        stage = StageFactory.create(id=stage_id)
        gof = GoFFactory.create(gof_id=gof_id)
        permitted_but_unfilled_gof = GoFFactory.create()
        gof_role = GoFRoleFactory.create(
            role=user_roles[0], gof=gof,
            permission_type=PermissionTypes.WRITE.value)
        GoFRoleFactory.create(
            role=user_roles[0], gof=permitted_but_unfilled_gof,
            permission_type=PermissionTypes.WRITE.value)

        field = FieldFactory.create(field_id=field_id, gof=gof)
        permitted_but_unfilled_fields = FieldFactory.create_batch(
            size=2, gof=permitted_but_unfilled_gof)

        field_role = FieldRoleFactory.create(
            role=user_roles[0], field=field,
            permission_type=PermissionTypes.WRITE.value)
        FieldRoleFactory.create_batch(
            size=len(permitted_but_unfilled_fields), role=user_roles[0],
            field=factory.Iterator(permitted_but_unfilled_fields),
            permission_type=PermissionTypes.WRITE.value)
        task_template = TaskTemplateFactory.create(template_id=template_id)
        task_template_gofs = GoFToTaskTemplateFactory.create(
            task_template=task_template, gof=gof)
        GoFToTaskTemplateFactory.create(
            task_template=task_template, gof=permitted_but_unfilled_gof)
        task = TaskFactory.create(
            task_display_id=task_id, template_id=task_template.template_id,
            project_id=project_id)
        StageGoFFactory.create(gof=gof, stage=stage)
        StageGoFFactory.create(gof=permitted_but_unfilled_gof, stage=stage)
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
                            "field_response": "field response"
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
