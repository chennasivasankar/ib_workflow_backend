"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01CreateTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def setup(self):
        import factory
        from ib_tasks.tests.factories.models import TaskTemplateFactory, \
            GoFFactory, GoFRoleFactory, \
            FieldFactory, FieldRoleFactory, GoFToTaskTemplateFactory

        TaskTemplateFactory.reset_sequence()
        GoFRoleFactory.reset_sequence()
        GoFFactory.reset_sequence()
        FieldFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()

        template_ids = ['template_1', 'template_2']

        task_template_objs = TaskTemplateFactory.create_batch(
            size=2, template_id=factory.Iterator(template_ids)
        )
        gof_objs = GoFFactory.create_batch(size=4)
        GoFToTaskTemplateFactory.create_batch(size=6,
                                              gof=factory.Iterator(gof_objs),
                                              task_template=factory.Iterator(
                                                  task_template_objs))
        GoFRoleFactory.create_batch(size=4, gof=factory.Iterator(gof_objs))
        field_objs = FieldFactory.create_batch(
            size=6, gof=factory.Iterator(gof_objs)
        )
        FieldRoleFactory.create_batch(
            size=6, field=factory.Iterator(field_objs)
        )

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {
          "task_template_id": "template_1",
          "action_id": 0,
          "task_gofs": [
            {
              "gof_id": "gof_1",
              "same_gof_order": 0,
              "gof_fields": [
                {
                  "field_id": "FIELD_ID-0",
                  "field_response": "string"
                }
              ]
            }
          ]
        }
        path_params = {}
        query_params = {}
        headers = {}
        response = self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
        from ib_tasks.models.task import Task
        task_object = Task.objects.get(id=1)
        snapshot.assert_match(task_object.template_id, 'template_id')
        snapshot.assert_match(task_object.created_by, 'created_by_id')
        snapshot.assert_match(task_object.template_id, 'task')

        from ib_tasks.models.task_gof import TaskGoF
        task_gofs = TaskGoF.objects.filter(task_id=1)
        counter = 1
        for task_gof in task_gofs:
            snapshot.assert_match(
                task_gof.same_gof_order, f'same_gof_order_{counter}')
            snapshot.assert_match(task_gof.gof_id, f'gof_id_{counter}')
            snapshot.assert_match(task_gof.task_id, f'task_id_{counter}')
            counter = counter + 1

        from ib_tasks.models.task_gof_field import TaskGoFField
        task_gof_fields = TaskGoFField.objects.filter(task_gof__task_id=1)
        counter = 1
        for task_gof_field in task_gof_fields:
            snapshot.assert_match(task_gof_field.task_gof_id, f'task_gof_{counter}')
            snapshot.assert_match(task_gof_field.field_id, f'field_{counter}')
            snapshot.assert_match(task_gof_field.field_response, f'field_response_{counter}')
            counter = counter + 1
