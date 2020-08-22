"""
# TODO: Update test case description
"""

import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.constants.enum import PermissionTypes, FieldTypes, Searchable
from ib_tasks.tests.factories.models import (
    TaskFactory,
    TaskGoFFactory,
    TaskGoFFieldFactory,
    GoFRoleFactory,
    GoFFactory,
    FieldRoleFactory,
    FieldFactory, StageModelFactory, CurrentTaskStageModelFactory,
    TaskStageHistoryModelFactory, StagePermittedRolesFactory,
)
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase09GetTaskAPITestCase(TestUtils):
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
        CurrentTaskStageModelFactory.reset_sequence()
        TaskStageHistoryModelFactory.reset_sequence()

    @pytest.fixture
    def setup(self, reset_factories):
        task_obj = TaskFactory(task_display_id="iBWF-1")
        gof_objs = GoFFactory.create_batch(size=3)
        task_gof_objs = TaskGoFFactory.create_batch(
            size=3, task=task_obj, gof=factory.Iterator(gof_objs)
        )
        searchable = [
            Searchable.CITY.value,
            Searchable.USER.value
        ]
        field_objs = FieldFactory.create_batch(
            size=2, gof=factory.Iterator(gof_objs),
            field_type=FieldTypes.SEARCHABLE.value,
            field_values=factory.Iterator(searchable)
        )
        field_responses = ["1", "123e4567-e89b-12d3-a456-426614174000"]
        TaskGoFFieldFactory.create_batch(
            size=2,
            task_gof=factory.Iterator(task_gof_objs),
            field=factory.Iterator(field_objs),
            field_response=factory.Iterator(field_responses)
        )
        roles = ["FIN_PAYMENT_REQUESTER", "FIN_PAYMENT_POC",
                 "FIN_PAYMENT_APPROVER"]
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
            size=2,
            field=factory.Iterator(field_objs),
            role=factory.Iterator(roles),
            permission_type=factory.Iterator(permission_type)
        )
        stage_objs = StageModelFactory.create_batch(size=4)
        assignee_ids = [
            "123e4567-e89b-12d3-a456-426614174001",
            "123e4567-e89b-12d3-a456-426614174002",
            "123e4567-e89b-12d3-a456-426614174003"
        ]

        CurrentTaskStageModelFactory.create_batch(size=4, task=task_obj,
                                                  stage=factory.Iterator(
                                                      stage_objs))
        TaskStageHistoryModelFactory.create_batch(
            size=3, task=task_obj, stage=factory.Iterator(stage_objs),
            assignee_id=factory.Iterator(assignee_ids)
        )
        TaskStageHistoryModelFactory.create(
            task=task_obj, stage=stage_objs[3], assignee_id=None
        )
        StagePermittedRolesFactory.create_batch(
            size=3,
            stage=factory.Iterator(stage_objs),
        )

    @pytest.mark.django_db
    def test_case(
            self, snapshot, setup, mocker
    ):
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids
        get_user_role_ids(mocker)
        from ib_tasks.tests.common_fixtures.adapters \
            .searchable_details_service import \
            searchable_details_dtos_mock
        searchable_details_dtos_mock(mocker)
        from ib_tasks.tests.common_fixtures.adapters \
            .assignees_details_service \
            import assignee_details_dtos_mock
        assignee_details_dtos_mock(mocker)
        body = {}
        path_params = {}
        query_params = {'task_id': "iBWF-1"}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
