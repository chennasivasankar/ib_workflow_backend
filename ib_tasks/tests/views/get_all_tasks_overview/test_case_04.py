"""
# Given valid details get all tasks overview details
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils

from ib_tasks.models import Task, Stage, TaskStage, TaskGoFField, \
    TaskTemplateGoFs, Field
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import TaskFactory, StageModelFactory, \
    TaskStageModelFactory, StageActionFactory, TaskGoFFieldFactory, \
    FieldFactory, GoFToTaskTemplateFactory, TaskTemplateFactory


class TestCase01GetAllTasksOverviewAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture(autouse=True)
    def setup(self):
        task_objs = TaskFactory.create_batch(3, created_by_id=1)
        print("tasks", Task.objects.all().values())
        stage_objs = StageModelFactory.create_batch(
            3, task_template_id='task_template_id_1')
        stage_other_obj_1 = StageModelFactory(
            value=2, task_template_id='task_template_id_1')
        stage_other_obj_2 = StageModelFactory(
            value=2, task_template_id='task_template_id_1')
        print("stages", Stage.objects.all().values())
        task_stage_obj_1 = TaskStageModelFactory(task=task_objs[0],
                                                 stage=stage_objs[2])
        task_stage_obj_2 = TaskStageModelFactory(task=task_objs[1],
                                                 stage=stage_other_obj_1)
        task_stage_obj_3 = TaskStageModelFactory(task=task_objs[2],
                                                 stage=stage_other_obj_2)
        task_stage_obj_4 = TaskStageModelFactory(task=task_objs[0],
                                                 stage=stage_objs[0])
        # print("task_stages", TaskStage.objects.all().values())
        StageActionFactory(stage=stage_objs[2])
        StageActionFactory(stage=stage_other_obj_1)

        field_objs = FieldFactory.create_batch(4)
        print("field_objs", Field.objects.all().values('field_id','gof_id','display_name'))
        task_template_obj = TaskTemplateFactory(template_id='task_template_id_1')
        GoFToTaskTemplateFactory(gof=field_objs[1].gof,
                                 task_template=task_template_obj)

        print("TaskTemplateGoFs", TaskTemplateGoFs.objects.all().values())
        GoFToTaskTemplateFactory(gof=field_objs[0].gof,
                                 task_template='task_template_id_1')


    @pytest.mark.django_db
    def test_case(self, snapshot, setup):
        body = {}
        path_params = {}
        query_params = {'limit': 2, 'offset': 0}
        headers = {}
        response = self.default_test_case(body=body,
                                          path_params=path_params,
                                          query_params=query_params,
                                          headers=headers,
                                          snapshot=snapshot)
