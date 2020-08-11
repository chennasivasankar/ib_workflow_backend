"""
# TODO: Update snapshot asserts to get know what are the details getting save in db
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_iam.tests.factories.models import UserRoleFactory, RoleFactory
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from ...factories.models import TaskFactory, StageModelFactory, \
    CurrentTaskStageModelFactory, StagePermittedRolesFactory


class TestCase01UpdateAssigneesOfDiffStagesForATaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.fixture(autouse=True)
    def setup(self, api_user):
        user_obj = api_user
        user_id = str(user_obj.user_id)
        from ib_iam.tests.factories.models import UserDetailsFactory
        UserDetailsFactory.reset_sequence()
        StagePermittedRolesFactory.reset_sequence()
        UserRoleFactory.reset_sequence()
        TaskFactory.reset_sequence()
        StageModelFactory.reset_sequence()
        CurrentTaskStageModelFactory.reset_sequence()
        UserDetailsFactory.create(user_id=user_id, is_admin=True)
        role_obj = RoleFactory(role_id="FIN_PAYMENT_REQUESTER")
        UserRoleFactory(user_id=user_id, role=role_obj)
        task_obj = TaskFactory(template_id="task_template_id_1")
        stage_objs = StageModelFactory.create_batch(2,
                                                    task_template_id=
                                                    'task_template_id_1')
        StagePermittedRolesFactory(stage=stage_objs[0])
        StagePermittedRolesFactory(stage=stage_objs[1])
        task_stage_obj_1 = CurrentTaskStageModelFactory(task=task_obj,
                                                        stage=stage_objs[0])
        task_stage_obj_1 = CurrentTaskStageModelFactory(task=task_obj,
                                                        stage=stage_objs[1])
        return user_id

    @pytest.mark.django_db
    def test_case(self, snapshot, setup):
        body = {'stage_assignees': [
            {'stage_id': 1, 'assignee_id': setup}]}
        path_params = {"task_id": 1}
        query_params = {}
        headers = {}
        response = self.make_api_call(
            body=body, path_params=path_params,
            query_params=query_params, headers=headers, snapshot=snapshot
        )
