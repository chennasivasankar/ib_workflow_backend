"""
test with empty stage ids
"""

import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from freezegun import freeze_time

from ib_tasks.constants.enum import PermissionTypes, FieldTypes
from ib_tasks.tests.views.save_and_act_on_a_task import APP_NAME, \
    OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ib_tasks.tests.common_fixtures.adapters.auth_service import \
    get_projects_info_for_given_ids_mock, get_valid_project_ids_mock, \
    validate_if_user_is_in_project_mock
from ib_tasks.tests.common_fixtures.adapters.roles_service import \
    get_user_role_ids_based_on_project_mock
from ib_tasks.tests.common_fixtures.storages import \
    elastic_storage_implementation_mock
from ib_tasks.tests.factories.adapter_dtos import ProjectDetailsDTOFactory
from ib_tasks.tests.factories import models


class TestCase43SaveAndActOnATaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def reset_sequence(self):
        models.TaskFactory.reset_sequence()
        models.StageActionFactory.reset_sequence()
        models.StageFactory.reset_sequence()
        models.GoFFactory.reset_sequence()
        models.TaskTemplateFactory.reset_sequence()
        models.FieldFactory.reset_sequence()
        models.GoFToTaskTemplateFactory.reset_sequence()
        models.StageGoFFactory.reset_sequence()
        models.FieldRoleFactory.reset_sequence()
        ProjectDetailsDTOFactory.reset_sequence()
        models.StagePermittedRolesFactory.reset_sequence()

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        task_display_id = "IBWF-1"
        action_id = 1
        stage_id = 1
        gof_id = "gof_1"
        field_id = "FIELD_ID-1"
        template_id = "template_1"
        project_id = "project_1"

        elastic_storage_implementation_mock(mocker)
        get_user_role_ids_based_on_project_mock(mocker)
        project_info_dtos = ProjectDetailsDTOFactory.create(
            project_id=project_id)
        project_info_mock = get_projects_info_for_given_ids_mock(mocker)
        project_info_mock.return_value = [project_info_dtos]
        get_valid_project_ids_mock(mocker, [project_id])
        validate_if_user_is_in_project_mock(mocker, True)

        template = models.TaskTemplateFactory.create(template_id=template_id)
        task = models.TaskFactory.create(
            task_display_id=task_display_id, template_id=template_id,
            project_id=project_id)
        gof = models.GoFFactory.create(gof_id=gof_id)

        field = models.FieldFactory.create(
            field_id=field_id, gof=gof,
            field_type=FieldTypes.PLAIN_TEXT.value)

        models.GoFToTaskTemplateFactory.create(task_template=template, gof=gof)
        stage = models.StageFactory.create(
            id=stage_id, task_template_id=template.template_id)
        action_stage = models.StageFactory(id=3)
        models.StageGoFFactory.create(stage=stage, gof=gof)
        action = models.StageActionFactory.create(
            id=action_id, stage=action_stage, action_type=None)

        models.FieldRoleFactory.create(
            role="FIN_PAYMENT_REQUESTER", field=field,
            permission_type=PermissionTypes.WRITE.value)
        models.StagePermittedRolesFactory.create(stage=stage,
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
                            "field_response": "hello world"
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
