"""
test when fields having gof selector that does not have stage permissions for
gof ids returns without that field
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase13GetTaskTemplatesAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture(autouse=True)
    def setup(self, mocker):
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids(mocker)

        import factory
        from ib_tasks.tests.factories.models import TaskTemplateFactory, \
            StageModelFactory, StageActionFactory, GoFFactory, \
            GoFRoleFactory, FieldFactory, FieldRoleFactory, StageGoFFactory, \
            GoFToTaskTemplateFactory, TaskTemplateInitialStageFactory, \
            ProjectTaskTemplateFactory, StagePermittedRolesFactory
        from ib_tasks.constants.enum import ValidationType

        TaskTemplateFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        StageActionFactory.reset_sequence()
        GoFRoleFactory.reset_sequence()
        GoFFactory.reset_sequence()
        FieldFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()
        GoFToTaskTemplateFactory.reset_sequence()
        GoFToTaskTemplateFactory.enable_add_another_gof.reset()
        TaskTemplateInitialStageFactory.reset_sequence()
        ProjectTaskTemplateFactory.reset_sequence(1)
        StageGoFFactory.reset_sequence()
        StagePermittedRolesFactory.reset_sequence()

        template_ids = ['template_1', 'template_2']

        task_template_objs = TaskTemplateFactory.create_batch(
            size=2, template_id=factory.Iterator(template_ids)
        )
        ProjectTaskTemplateFactory.create_batch(
            size=2, task_template=factory.Iterator(task_template_objs))
        gof_objs = GoFFactory.create_batch(size=4)
        GoFToTaskTemplateFactory.create_batch(size=6,
                                              gof=factory.Iterator(gof_objs),
                                              task_template=factory.Iterator(
                                                  task_template_objs))

        stage_objs = StageModelFactory.create_batch(
            size=4, task_template_id=factory.Iterator(template_ids)
        )
        StageActionFactory.create_batch(
            size=4, stage=factory.Iterator(stage_objs),
            action_type=ValidationType.NO_VALIDATIONS.value,
            transition_template=None
        )
        TaskTemplateInitialStageFactory.create_batch(
            size=2, stage=factory.Iterator(stage_objs),
            task_template=factory.Iterator(task_template_objs)
        )
        GoFRoleFactory.create_batch(
            size=4, gof=factory.Iterator(gof_objs),
            role=factory.Iterator(["FIN_PAYMENT_REQUESTER", "ALL_ROLES"])
        )

        from ib_tasks.constants.enum import FieldTypes
        field_objs = FieldFactory.create_batch(
            size=6, gof=factory.Iterator(gof_objs),
            field_type=FieldTypes.GOF_SELECTOR.value,
            field_values='[{"name": "Vendor Payment", "gof_ids": ['
                         '"FIN_VENDOR_PAYMENT_DETAILS", '
                         '"FIN_VENDOR_ONLINE_EXPENSE_TYPE"]}]'
        )
        FieldRoleFactory.create_batch(
            size=6, field=factory.Iterator(field_objs)
        )
        StageGoFFactory.create_batch(
            size=4, stage=factory.Iterator(stage_objs),
            gof=factory.Iterator(gof_objs)
        )
        StagePermittedRolesFactory.create_batch(
            size=4, stage=factory.Iterator(stage_objs)
        )

    @pytest.mark.django_db
    def test_case(self, snapshot):
        body = {}
        path_params = {}
        query_params = {}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
