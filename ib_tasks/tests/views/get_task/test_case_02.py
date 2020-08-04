"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_v1 import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ib_tasks.tests.factories.models import (
    TaskFactory,
    TaskGoFFactory,
    TaskGoFFieldFactory,
    GoFRoleFactory,
    GoFFactory,
    FieldRoleFactory,
    FieldFactory,
    StageModelFactory,
    TaskStageModelFactory,
    StageActionFactory,
)
import factory
from ib_tasks.constants.enum import PermissionTypes


class TestCase02GetTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['write', 'read']}}

    @pytest.fixture
    def reset_factories(self):
        TaskFactory.reset_sequence()
        TaskGoFFactory.reset_sequence()
        GoFRoleFactory.reset_sequence()
        GoFFactory.reset_sequence()
        FieldRoleFactory.reset_sequence()
        FieldFactory.reset_sequence()
        TaskGoFFieldFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        TaskStageModelFactory.reset_sequence()
        StageActionFactory.reset_sequence()

    @pytest.fixture
    def setup(self, reset_factories):
        task_obj = TaskFactory()
        gof_objs = GoFFactory.create_batch(size=3)
        task_gof_objs = TaskGoFFactory.create_batch(
            size=3, task=task_obj, gof=factory.Iterator(gof_objs)
        )
        field_objs = FieldFactory.create_batch(
            size=10, gof=factory.Iterator(gof_objs)
        )
        TaskGoFFieldFactory.create_batch(
            size=10,
            task_gof=factory.Iterator(task_gof_objs),
            field=factory.Iterator(field_objs)
        )
        roles = ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC"]
        permission_type = [
            PermissionTypes.READ.value,
            PermissionTypes.WRITE.value
        ]
        GoFRoleFactory.create_batch(
            size=2, gof=factory.Iterator(gof_objs),
            role=factory.Iterator(roles),
            permission_type=factory.Iterator(permission_type)
        )
        FieldRoleFactory.create_batch(
            size=10,
            field=factory.Iterator(field_objs),
            role=factory.Iterator(roles),
            permission_type=factory.Iterator(permission_type)
        )
        stage_objs = StageModelFactory.create_batch(size=10)
        TaskStageModelFactory.create_batch(
            size=3, task=task_obj, stage=factory.Iterator(stage_objs)
        )
        StageActionFactory.create_batch(
            size=20, stage=factory.Iterator(stage_objs)
        )

    @pytest.mark.django_db
    def test_case(self, snapshot, setup, mocker):
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids_mock_method = get_user_role_ids(mocker)
        body = {}
        path_params = {}
        query_params = {'task_id': 1}
        headers = {}
        self.default_test_case(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
