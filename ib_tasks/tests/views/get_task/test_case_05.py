"""
test with invalid city ids for searchable raise exceception
"""
from unittest.mock import patch

import factory
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_tasks.adapters.auth_service import AuthService
from ib_tasks.constants.enum import PermissionTypes, FieldTypes, Searchable
from ib_tasks.tests.factories.models import (
    TaskFactory,
    TaskGoFFactory,
    TaskGoFFieldFactory,
    GoFRoleFactory,
    GoFFactory,
    FieldRoleFactory,
    FieldFactory, TaskTemplateFactory, StagePermittedRolesFactory,
    GoFToTaskTemplateFactory, TaskStageHistoryModelFactory, StageModelFactory,
    StageGoFFactory, CurrentTaskStageModelFactory,
)
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase05GetTaskAPITestCase(TestUtils):
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

    @pytest.fixture
    def setup(self, reset_factories, api_user):
        user_id = api_user.user_id
        task_obj = TaskFactory(
            task_display_id="iBWF-1", project_id="project0", created_by=user_id
        )
        template_id = task_obj.template_id
        TaskTemplateFactory(template_id=template_id)
        gof_objs = GoFFactory.create_batch(size=3)
        GoFToTaskTemplateFactory.create_batch(
            size=3, gof=factory.Iterator(gof_objs),
            task_template_id=template_id
        )
        task_gof_objs = TaskGoFFactory.create_batch(
            size=3, task=task_obj, gof=factory.Iterator(gof_objs)
        )
        searchable = [
            Searchable.CITY.value,
            Searchable.CITY.value,
            Searchable.STATE.value,
            Searchable.COUNTRY.value
        ]
        field_objs = FieldFactory.create_batch(
            size=10, gof=factory.Iterator(gof_objs),
            field_type=FieldTypes.SEARCHABLE.value,
            field_values=factory.Iterator(searchable)
        )
        field_responses = [100, 110, 4, 6]
        TaskGoFFieldFactory.create_batch(
            size=10,
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
            size=10,
            field=factory.Iterator(field_objs),
            role=factory.Iterator(roles),
            permission_type=factory.Iterator(permission_type)
        )
        stage_colors = ["white", "black", "blue"]
        stage_objs = StageModelFactory.create_batch(
            size=4,
            stage_color=factory.Iterator(stage_colors)
        )
        assignee_ids = [
            "123e4567-e89b-12d3-a456-426614174000",
            "123e4567-e89b-12d3-a456-426614174001",
            "123e4567-e89b-12d3-a456-426614174002"
        ]
        CurrentTaskStageModelFactory.create_batch(size=4, task=task_obj,
                                                  stage=factory.Iterator(
                                                      stage_objs))
        TaskStageHistoryModelFactory.create_batch(
            size=3, task=task_obj, stage=factory.Iterator(stage_objs),
            assignee_id=factory.Iterator(assignee_ids), left_at=None
        )
        TaskStageHistoryModelFactory.create(
            task=task_obj, stage=stage_objs[3], assignee_id=None, left_at=None
        )
        StagePermittedRolesFactory.create_batch(
            size=3,
            stage=factory.Iterator(stage_objs),
            role_id=factory.Iterator(roles)
        )
        StageGoFFactory.create_batch(
            size=4, stage=factory.Iterator(stage_objs),
            gof=factory.Iterator(gof_objs)
        )

    @pytest.mark.django_db
    @patch.object(AuthService, "get_user_ids_based_on_user_level")
    def test_case(
            self, user_ids_mock, snapshot, setup, mocker, api_user
    ):
        user_id = api_user.user_id
        user_ids_mock.return_value = [user_id]
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_valid_project_ids_mock
        get_valid_project_ids_mock(mocker, project_ids=["project0"])
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            validate_if_user_is_in_project_mock
        validate_if_user_is_in_project_mock(mocker, True)
        from ib_tasks.tests.common_fixtures.adapters.roles_service import \
            get_user_role_ids_based_on_project_mock
        get_user_role_ids_based_on_project_mock(mocker)
        from ib_tasks.tests.common_fixtures.adapters.auth_service import \
            get_projects_info_for_given_ids_mock
        get_projects_info_for_given_ids_mock(mocker)
        from ib_tasks.tests.common_fixtures.adapters \
            .searchable_details_service import \
            searchable_details_dtos_invalid_city_ids_mock
        searchable_details_dtos_invalid_city_ids_mock(mocker)
        body = {}
        path_params = {}
        query_params = {'task_id': "iBWF-1"}
        headers = {}
        self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
