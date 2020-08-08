"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import StageModelFactory, StageActionFactory


class TestCase01CreateTransitionChecklistAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
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
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids(mocker)

        gof_objs = GoFFactory.create_batch(size=2)
        gof_ids = [
            gof.gof_id
            for gof in gof_objs
        ]
        GoFToTaskTemplateFactory.create_batch(
            size=2,
            template_id="template_1", template__is_transition_template=True,
            gof=factory.Iterator(gof_objs)
        )
        from ib_tasks.constants.enum import FieldTypes
        plain_text = FieldFactory.create(
            gof=gof_objs[0], field_type=FieldTypes.PLAIN_TEXT.value
        )
        image_field = FieldFactory.create(
            gof=gof_objs[0], field_type=FieldTypes.IMAGE_UPLOADER.value,
            allowed_formats='[".jpeg", ".png", ".svg"]'
        )
        checkbox_group = FieldFactory.create(
            gof=gof_objs[1], field_type=FieldTypes.CHECKBOX_GROUP.value,
            field_values='["interactors", "storages", "presenters"]'
        )

        task_obj = TaskFactory.create(
            template_id="template_1")
        task_gofs = TaskGoFFactory.create_batch(
            size=2, gof_id=factory.Iterator(gof_ids), task=task_obj
        )
        TaskGoFFieldFactory.create(
            task_gof=task_gofs[0],
            field=plain_text, field_response="string"
        )
        TaskGoFFieldFactory.create(
            task_gof=task_gofs[0],
            field=image_field,
            field_response="https://www.freepngimg.com/thumb/light/20246-4"
                           "-light-transparent.png"
        )
        TaskGoFFieldFactory.create(
            task_gof=task_gofs[1],
            field=checkbox_group,
            field_response='["interactors", "storages"]'
        )
        import json
        stage = StageModelFactory(
            task_template_id='template_1',
            display_logic="variable0==stage_id_0",
            card_info_kanban=json.dumps(["FIELD_ID-1", "FIELD_ID-2"]),
            card_info_list=json.dumps(["FIELD_ID-1", "FIELD_ID-2"]),
        )
        StageActionFactory.create(
            stage=stage, transition_template_id="template_1"
        )

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            'task_id':
                1,
            'transition_checklist_template_id':
                'string',
            'action_id':
                1,
            'stage_id':
                1,
            'transition_checklist_gofs': [{
                'gof_id':
                    'string',
                'same_gof_order':
                    1,
                'gof_fields': [{
                    'field_id': 'string',
                    'field_response': 'string'
                }]
            }]
        }
        path_params = {}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
