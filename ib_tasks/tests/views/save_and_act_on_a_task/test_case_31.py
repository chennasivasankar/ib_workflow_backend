"""
test with incorrect checkbox options in checkbox group field
"""

import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from freezegun import freeze_time

from ib_tasks.constants.enum import PermissionTypes, FieldTypes
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...common_fixtures.adapters.auth_service import \
    get_projects_info_for_given_ids_mock, get_valid_project_ids_mock, \
    validate_if_user_is_in_project_mock
from ...common_fixtures.adapters.roles_service import \
    get_user_role_ids_based_on_project_mock
from ...factories.adapter_dtos import ProjectDetailsDTOFactory
from ...factories.models import (
    TaskFactory, StageActionFactory, StageFactory, GoFFactory,
    TaskTemplateFactory, FieldFactory, GoFToTaskTemplateFactory,
    StageGoFFactory, FieldRoleFactory, StagePermittedRolesFactory)


class TestCase31SaveAndActOnATaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        TaskFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        StageFactory.reset_sequence()
        GoFFactory.reset_sequence()
        TaskTemplateFactory.reset_sequence()
        FieldFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()
        StageGoFFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()
        ProjectDetailsDTOFactory.reset_sequence()
        StagePermittedRolesFactory.reset_sequence()

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        task_display_id = "IBWF-1"
        action_id = 1
        stage_id = 1
        gof_id = "gof_1"
        field_id = "FIELD_ID-1"
        template_id = "template_1"
        project_id = "project_1"

        get_user_role_ids_based_on_project_mock(mocker)
        project_info_dtos = ProjectDetailsDTOFactory.create(
            project_id=project_id)
        project_info_mock = get_projects_info_for_given_ids_mock(mocker)
        project_info_mock.return_value = [project_info_dtos]
        get_valid_project_ids_mock(mocker, [project_id])
        validate_if_user_is_in_project_mock(mocker, True)

        template = TaskTemplateFactory.create(template_id=template_id)
        task = TaskFactory.create(
            task_display_id=task_display_id, template_id=template_id,
            project_id=project_id)
        gof = GoFFactory.create(gof_id=gof_id)

        field = FieldFactory.create(
            field_id=field_id, gof=gof,
            field_type=FieldTypes.CHECKBOX_GROUP.value,
            field_values='["interactors", "storages"]'
        )

        GoFToTaskTemplateFactory.create(task_template=template, gof=gof)
        stage = StageFactory.create(
            id=stage_id, task_template_id=template.template_id)
        StageGoFFactory.create(stage=stage, gof=gof)
        action = StageActionFactory.create(
            id=action_id, stage=stage, action_type=None)

        FieldRoleFactory.create(
            role="FIN_PAYMENT_REQUESTER", field=field,
            permission_type=PermissionTypes.WRITE.value)
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
            "start_datetime": "2020-08-25 12:00:00",
            "due_datetime": "2020-09-20 12:00:00",
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
                            "field_id": "FIELD_ID-1",
                            "field_response": '["interactors", "views"]'
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
