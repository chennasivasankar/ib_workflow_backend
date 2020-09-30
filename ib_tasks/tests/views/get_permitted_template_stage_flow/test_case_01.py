"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetPermittedTemplateStageFlowAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        project_id = "ibgroup"
        template_id = "template_1"

        import factory
        from ib_tasks.tests.factories.models import StageModelFactory, \
            StageActionFactory, TaskTemplateFactory, \
            StagePermittedRolesFactory, StageFlowFactory, \
            ActionPermittedRolesFactory

        TaskTemplateFactory.reset_sequence()
        StageModelFactory.reset_sequence(1)
        StageActionFactory.reset_sequence(1)
        StagePermittedRolesFactory.reset_sequence()
        StagePermittedRolesFactory.role_id.reset()
        ActionPermittedRolesFactory.reset_sequence()
        StageFlowFactory.reset_sequence()

        task_template = TaskTemplateFactory.create()
        stages = StageModelFactory.create_batch(
            size=2, task_template_id=task_template.template_id)
        stage_actions = StageActionFactory.create_batch(
            size=2, stage=factory.Iterator(stages))
        StagePermittedRolesFactory.create_batch(
            size=2, stage=factory.Iterator(stages))
        ActionPermittedRolesFactory.create_batch(
            size=2, action=factory.Iterator(stage_actions),
            role_id="FIN_PAYMENT_APPROVER"
        )
        StageFlowFactory.create(
            previous_stage=stages[0], next_stage=stages[1],
            action=stage_actions[0])

        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_project_ids_mock, validate_if_user_is_in_project_mock
        validate_project_ids_mock(mocker, [project_id])
        validate_if_user_is_in_project_mock(mocker, True)

        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids_based_on_project_mock
        get_user_role_ids_based_on_project_mock(mocker)

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {}
        path_params = {"project_id": "ibgroup", "template_id": "template_1"}
        query_params = {}
        headers = {}
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
