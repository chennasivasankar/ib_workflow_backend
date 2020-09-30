"""
test when no fields exists returns empty fields list
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase04GetTransitionTemplateAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        import factory
        from ib_tasks.tests.factories.models import TaskTemplateFactory, \
            GoFFactory, GoFRoleFactory, GoFToTaskTemplateFactory

        TaskTemplateFactory.reset_sequence()
        GoFRoleFactory.reset_sequence()
        GoFFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()
        GoFToTaskTemplateFactory.enable_add_another_gof.reset()

        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids(mocker)

        transition_template_id = 'template_1'
        template_obj = TaskTemplateFactory.create(
            template_id=transition_template_id,
            is_transition_template=True
        )
        gof_objs = GoFFactory.create_batch(size=4)
        GoFToTaskTemplateFactory.create_batch(size=2,
                                              gof=factory.Iterator(gof_objs),
                                              task_template=template_obj)

        GoFRoleFactory.create_batch(
            size=4, gof=factory.Iterator(gof_objs),
            role=factory.Iterator(["FIN_PAYMENT_REQUESTER", "ALL_ROLES"])
        )

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {}
        path_params = {"transition_template_id": "template_1"}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
