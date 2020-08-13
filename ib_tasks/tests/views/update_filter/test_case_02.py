"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase02UpdateFilterAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker, api_user):
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids(mocker)

        import factory
        from ib_tasks.tests.factories.models import TaskTemplateFactory, \
            GoFFactory, FieldFactory, FieldRoleFactory, GoFToTaskTemplateFactory

        TaskTemplateFactory.reset_sequence()
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

        field_objs = FieldFactory.create_batch(
            size=6, gof=factory.Iterator(gof_objs)
        )
        FieldRoleFactory.create_batch(
            size=6, field=factory.Iterator(field_objs)
        )
        from ib_tasks.tests.factories.models import FilterFactory
        FilterFactory.create_batch(2, created_by=api_user.user_id)
        from ib_tasks.tests.factories.models import FilterConditionFactory
        FilterConditionFactory.create_batch(1, filter_id=1)


    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {'name': 'string', 'template_id': 'template_1', 'conditions': [{'field_id': 'FIELD_ID-0', 'operator': 'EQ', 'value': 'string'}]}
        path_params = {"filter_id": "100"}
        query_params = {}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )