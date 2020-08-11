"""
# Given valid details get all tasks overview details
"""
import json

import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_iam.tests.factories.models import UserRoleFactory, RoleFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import TaskFactory, StageModelFactory, \
    TaskStageModelFactory, StageActionFactory, TaskGoFFieldFactory, \
    TaskGoFFactory, FieldFactory, GoFFactory, ActionPermittedRolesFactory, \
    FieldRoleFactory, TaskTemplateFactory


class TestCase04GetAllTasksOverviewAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture(autouse=True)
    def setup(self, api_user, mocker):
        user_obj = api_user
        user_id = str(user_obj.user_id)
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids, get_assignees_details_dtos
        from ib_tasks.tests.common_fixtures.storages import mock_filter_tasks
        mock_filter_tasks(mocker)
        get_user_role_ids(mocker)
        get_assignees_details_dtos(mocker)
        from ib_tasks.constants.enum import ValidationType

        from ib_iam.tests.factories.models import UserDetailsFactory
        UserDetailsFactory.reset_sequence()
        UserDetailsFactory.create(user_id=user_id, is_admin=True)
        TaskFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        TaskStageModelFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        TaskTemplateFactory.reset_sequence()
        TaskGoFFactory.reset_sequence()
        TaskGoFFieldFactory.reset_sequence()
        FieldFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()
        ActionPermittedRolesFactory.reset_sequence()
        UserRoleFactory.reset_sequence()
        RoleFactory.reset_sequence()
        role_obj_1 = RoleFactory(role_id="FIN_PAYMENT_REQUESTER")
        role_obj_2 = RoleFactory(role_id="FIN_PAYMENT_APPROVER")
        UserRoleFactory(user_id=user_id, role=role_obj_1)
        UserRoleFactory(user_id=user_id, role=role_obj_2)
        task_objs = TaskFactory.create_batch(3,
                                             created_by=user_id,
                                             template_id="task_template_id_1")
        stage_objs = StageModelFactory.create_batch(
            3,
            task_template_id='task_template_id_1',
            card_info_list=json.dumps(['FIELD_ID-2', "FIELD_ID-1"]),
            card_info_kanban=json.dumps(['FIELD_ID-2', "FIELD_ID-1"]))
        stage_other_objs = StageModelFactory. \
            create_batch(2, value=2, task_template_id='task_template_id_1',
                         card_info_list=json.dumps(
                             ['FIELD_ID-0', "FIELD_ID-1", 'FIELD_ID-2']),
                         card_info_kanban=json.dumps(
                             ['FIELD_ID-0', "FIELD_ID-1", 'FIELD_ID-2']))

        task_stage_obj_1 = TaskStageModelFactory(task=task_objs[0],
                                                 stage=stage_objs[2])
        task_stage_obj_2 = TaskStageModelFactory(task=task_objs[1],
                                                 stage=stage_objs[2])
        task_stage_obj_3 = TaskStageModelFactory(task=task_objs[2],
                                                 stage=stage_other_objs[1])
        task_stage_obj_4 = TaskStageModelFactory(task=task_objs[0],
                                                 stage=stage_objs[0])

        action_obj_1 = StageActionFactory(
            stage=stage_objs[2],
            action_type=ValidationType.NO_VALIDATIONS.value)
        action_obj_2 = StageActionFactory(stage=stage_other_objs[1])
        ActionPermittedRolesFactory(action=action_obj_1, role_id="ALL_ROLES")
        ActionPermittedRolesFactory(action=action_obj_2, role_id="ALL_ROLES")
        gof_obj = GoFFactory()
        field_objs_of_gof_1 = FieldFactory.create_batch(3, gof=gof_obj)
        task_gof_obj_1 = TaskGoFFactory(task=task_objs[0], gof=gof_obj)
        task_gof_obj_2 = TaskGoFFactory(task=task_objs[1], gof=gof_obj)
        task_gof_obj_3 = TaskGoFFactory(task=task_objs[2], gof=gof_obj)
        TaskGoFFieldFactory(task_gof=task_gof_obj_1,
                            field=field_objs_of_gof_1[0])
        TaskGoFFieldFactory(task_gof=task_gof_obj_1,
                            field=field_objs_of_gof_1[1])
        TaskGoFFieldFactory(task_gof=task_gof_obj_1,
                            field=field_objs_of_gof_1[2])
        TaskGoFFieldFactory(task_gof=task_gof_obj_2,
                            field=field_objs_of_gof_1[0])
        TaskGoFFieldFactory(task_gof=task_gof_obj_2,
                            field=field_objs_of_gof_1[1])
        TaskGoFFieldFactory(task_gof=task_gof_obj_2,
                            field=field_objs_of_gof_1[2])
        TaskGoFFieldFactory(task_gof=task_gof_obj_3,
                            field=field_objs_of_gof_1[0])
        TaskGoFFieldFactory(task_gof=task_gof_obj_3,
                            field=field_objs_of_gof_1[1])
        TaskGoFFieldFactory(task_gof=task_gof_obj_3,
                            field=field_objs_of_gof_1[2])
        FieldRoleFactory(field=field_objs_of_gof_1[0])
        FieldRoleFactory(field=field_objs_of_gof_1[0])
        FieldRoleFactory(field=field_objs_of_gof_1[1])
        FieldRoleFactory(field=field_objs_of_gof_1[1])
        FieldRoleFactory(field=field_objs_of_gof_1[2])
        FieldRoleFactory(field=field_objs_of_gof_1[2])

    @pytest.mark.django_db
    def test_case(self, snapshot, setup):
        body = {}
        path_params = {}
        query_params = {'limit': 3, 'offset': 0}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
