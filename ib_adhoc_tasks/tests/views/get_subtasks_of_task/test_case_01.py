"""
# TODO: Update test case description
"""
import factory
import mock
import pytest
from django_swagger_utils.utils.test_utils import TestUtils

from ib_adhoc_tasks.adapters.task_service import TaskService
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX


class TestCase01GetSubtasksOfTaskAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    @mock.patch.object(TaskService, "get_task_id")
    @mock.patch.object(TaskService, "get_project_id_based_on_task_id")
    @mock.patch.object(TaskService, "get_subtask_ids_for_task_id")
    @mock.patch.object(TaskService, "get_task_complete_details_dto")
    def test_case(
            self, get_task_complete_details_dto_mock,
            get_subtask_ids_for_task_id_mock,
            get_project_id_based_on_task_id_mock,
            get_task_id_mock, task_complete_details_dto, task_ids, snapshot
    ):
        project_id = "project_id_1"
        subtask_ids = task_ids
        task_id = 1
        get_task_id_mock.return_value = task_id
        get_project_id_based_on_task_id_mock.return_value = project_id
        get_subtask_ids_for_task_id_mock.return_value = subtask_ids
        get_task_complete_details_dto_mock.return_value = task_complete_details_dto
        body = {'task_id': 'IBWF-1', 'view_type': 'LIST'}
        path_params = {}
        query_params = {'limit': 7, 'offset': 0}
        headers = {}
        self.make_api_call(body=body,
                           path_params=path_params,
                           query_params=query_params,
                           headers=headers,
                           snapshot=snapshot)

    @pytest.fixture
    @mock.patch.object(TaskService, "get_task_id")
    @mock.patch.object(TaskService, "get_project_id_based_on_task_id")
    @mock.patch.object(TaskService, "get_subtask_ids_for_task_id")
    @mock.patch.object(TaskService, "get_task_complete_details_dto")
    def setup(
            self, get_task_complete_details_dto_mock,
            get_subtask_ids_for_task_id_mock,
            get_project_id_based_on_task_id_mock,
            get_task_id_mock, task_complete_details_dto, task_ids
    ):
        project_id = "project_id_1"
        subtask_ids = task_ids
        task_id = 1
        get_task_id_mock.return_value = task_id
        get_project_id_based_on_task_id_mock.return_value = project_id
        get_subtask_ids_for_task_id_mock.return_value = subtask_ids
        get_task_complete_details_dto_mock.return_value = task_complete_details_dto

    @pytest.fixture
    def task_ids(self):
        task_ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
        return task_ids

    @pytest.fixture
    def stage_ids(self):
        stage_ids = [
            "stage1", "stage2", "stage3", "stage4", "stage5", "stage6",
            "stage7", "stage8", "stage9", "stage10", "stage11", "stage12",
            "stage13", "stage14", "stage15"
        ]
        return stage_ids

    @pytest.fixture
    def task_base_details_dtos(self):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            TaskBaseDetailsDTOFactory
        TaskBaseDetailsDTOFactory.reset_sequence()
        task_base_details_dtos = TaskBaseDetailsDTOFactory.create_batch(
            size=15
        )
        return task_base_details_dtos

    @pytest.fixture
    def task_stage_complete_details_dtos(self, task_ids, stage_ids):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            GetTaskStageCompleteDetailsDTOFactory
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            FieldDetailsDTOFactory
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            StageActionDetailsDTOFactory
        GetTaskStageCompleteDetailsDTOFactory.reset_sequence()
        StageActionDetailsDTOFactory.reset_sequence()
        task_stage_complete_details_dtos = \
            GetTaskStageCompleteDetailsDTOFactory.create_batch(
                size=15,
                field_dtos=FieldDetailsDTOFactory.create_batch(
                    size=3, field_type="PLAIN_TEXT"
                ),
                stage_id=factory.Iterator(stage_ids),
                action_dtos=StageActionDetailsDTOFactory.create_batch(
                    size=1, stage_id=factory.Iterator(stage_ids),
                    action_id=1
                )
            )
        return task_stage_complete_details_dtos

    @pytest.fixture
    def task_stage_assignee_details_dto(self, stage_ids):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            TaskStageAssigneeDetailsDTOFactory
        TaskStageAssigneeDetailsDTOFactory.reset_sequence()
        task_stage_assignee_details_dto = \
            TaskStageAssigneeDetailsDTOFactory.create_batch(
                size=15,
                stage_id=factory.Iterator(stage_ids)
            )
        return task_stage_assignee_details_dto

    @pytest.fixture
    def task_complete_details_dto(
            self, task_base_details_dtos, task_stage_complete_details_dtos,
            task_stage_assignee_details_dto
    ):
        from ib_adhoc_tasks.tests.factories.adapter_dtos import \
            TasksCompleteDetailsDTOFactory
        task_complete_details_dto = TasksCompleteDetailsDTOFactory(
            task_base_details_dtos=task_base_details_dtos,
            task_stage_details_dtos=task_stage_complete_details_dtos,
            task_stage_assignee_dtos=task_stage_assignee_details_dto
        )
        return task_complete_details_dto
