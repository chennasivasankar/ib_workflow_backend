"""
# Given valid details get all tasks overview details
"""
import json

import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import TaskFactory, StageModelFactory, \
    TaskStageModelFactory, StageActionFactory, TaskGoFFieldFactory, \
    TaskGoFFactory, FieldFactory


class TestCase04GetAllTasksOverviewAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture(autouse=True)
    def setup(self, api_user):
        user_obj = api_user
        user_id = str(user_obj.user_id)
        TaskFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        TaskStageModelFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        TaskGoFFactory.reset_sequence()
        TaskGoFFieldFactory.reset_sequence()
        FieldFactory.reset_sequence()
        task_objs = TaskFactory.create_batch(3,
                                             created_by=user_id,
                                             template_id="task_template_id_1")
        stage_objs = StageModelFactory.create_batch(
            3,
            task_template_id='task_template_id_1',
            card_info_list=json.dumps(['FIELD_ID-2', "FIELD_ID-1"]),
            card_info_kanban=json.dumps(['FIELD_ID-2', "FIELD_ID-1"]))
        stage_other_obj_1 = StageModelFactory(
            value=2,
            task_template_id='task_template_id_1',
            card_info_list=json.dumps(['FIELD_ID-2', "FIELD_ID-1"]),
            card_info_kanban=json.dumps(['FIELD_ID-2', "FIELD_ID-1"]))
        stage_other_obj_2 = StageModelFactory(
            value=2,
            task_template_id='task_template_id_1',
            card_info_list=json.dumps(['FIELD_ID-2', "FIELD_ID-1"]),
            card_info_kanban=json.dumps(['FIELD_ID-2', "FIELD_ID-1"]))
        task_stage_obj_1 = TaskStageModelFactory(task=task_objs[0],
                                                 stage=stage_objs[2])
        task_stage_obj_2 = TaskStageModelFactory(task=task_objs[1],
                                                 stage=stage_other_obj_1)
        task_stage_obj_3 = TaskStageModelFactory(task=task_objs[2],
                                                 stage=stage_other_obj_2)
        task_stage_obj_4 = TaskStageModelFactory(task=task_objs[0],
                                                 stage=stage_objs[0])
        StageActionFactory(stage=stage_objs[2])
        StageActionFactory(stage=stage_other_obj_1)
        StageActionFactory(stage=stage_other_obj_2)
        task_gof_obj_1 = TaskGoFFactory(task=task_objs[0])
        task_gof_obj_2 = TaskGoFFactory(task=task_objs[1])
        task_gof_obj_3 = TaskGoFFactory(task=task_objs[0])
        TaskGoFFieldFactory(task_gof=task_gof_obj_1)
        TaskGoFFieldFactory(task_gof=task_gof_obj_2)
        TaskGoFFieldFactory(task_gof=task_gof_obj_3)

    @pytest.mark.django_db
    def test_case(self, snapshot, setup):
        body = {}
        path_params = {}
        query_params = {'limit': 3, 'offset': 0}
        headers = {}
        response = self.default_test_case(body=body,
                                          path_params=path_params,
                                          query_params=query_params,
                                          headers=headers,
                                          snapshot=snapshot)
