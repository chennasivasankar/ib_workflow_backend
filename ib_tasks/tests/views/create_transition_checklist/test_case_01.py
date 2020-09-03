"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01CreateTransitionChecklistAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read', 'write']}}

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
        task_template = TaskTemplateFactory(
            template_id="template_1", is_transition_template=True
        )
        GoFToTaskTemplateFactory.create_batch(
            size=2, task_template=task_template,
            gof=factory.Iterator(gof_objs)
        )
        from ib_tasks.constants.enum import FieldTypes
        plain_text = FieldFactory.create(
            gof=gof_objs[0], field_type=FieldTypes.PLAIN_TEXT.value
        )
        # image_field = FieldFactory.create(
        #     gof=gof_objs[0], field_type=FieldTypes.IMAGE_UPLOADER.value,
        #     allowed_formats='[".jpeg", ".png", ".svg"]'
        # )
        # checkbox_group = FieldFactory.create(
        #     gof=gof_objs[1], field_type=FieldTypes.CHECKBOX_GROUP.value,
        #     field_values='["interactors", "storages", "presenters"]'
        # )
        #
        # task_obj = TaskFactory.create(
        #     template_id="template_1")
        # task_gofs = TaskGoFFactory.create_batch(
        #     size=2, gof_id=factory.Iterator(gof_ids), task=task_obj
        # )
        # TaskGoFFieldFactory.create(
        #     task_gof=task_gofs[0],
        #     field=plain_text, field_response="string"
        # )
        # TaskGoFFieldFactory.create(
        #     task_gof=task_gofs[0],
        #     field=image_field,
        #     field_response="https://www.freepngimg.com/thumb/light/20246-4"
        #                    "-light-transparent.png"
        # )
        # TaskGoFFieldFactory.create(
        #     task_gof=task_gofs[1],
        #     field=checkbox_group,
        #     field_response='["interactors", "storages"]'
        # )

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
            "task_id": "IBWF-2",
            "transition_checklist_template_id": "template_1",
            "action_id": 1,
            "stage_id": 1,
            "transition_checklist_gofs": [
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
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)

        # from ib_tasks.models.task import Task
        # task_object = Task.objects.get(id=1)
        # snapshot.assert_match(task_object.id, 'task_id')
        # snapshot.assert_match(task_object.template_id, 'template_id')
        # snapshot.assert_match(task_object.title, 'task_title')
        # snapshot.assert_match(task_object.description, 'task_description')
        # snapshot.assert_match(str(task_object.start_date), 'task_start_date')
        # snapshot.assert_match(str(task_object.due_date), 'task_due_date')
        # snapshot.assert_match(task_object.priority, 'task_priority')
        #
        # from ib_tasks.models.task_gof import TaskGoF
        # task_gofs = TaskGoF.objects.filter(task_id=1)
        # counter = 1
        # for task_gof in task_gofs:
        #     snapshot.assert_match(
        #         task_gof.same_gof_order, f'same_gof_order_{counter}')
        #     snapshot.assert_match(task_gof.gof_id, f'gof_id_{counter}')
        #     snapshot.assert_match(task_gof.task_id,
        #                           f'gof_task_id_{counter}')
        #     counter = counter + 1
        #
        # from ib_tasks.models.task_gof_field import TaskGoFField
        # task_gof_fields = TaskGoFField.objects.filter(task_gof__task_id=1)
        # counter = 1
        # for task_gof_field in task_gof_fields:
        #     snapshot.assert_match(task_gof_field.task_gof_id,
        #                           f'task_gof_{counter}')
        #     snapshot.assert_match(task_gof_field.field_id, f'field_{counter}')
        #     snapshot.assert_match(task_gof_field.field_response,
        #                           f'field_response_{counter}')
        #     counter = counter + 1
