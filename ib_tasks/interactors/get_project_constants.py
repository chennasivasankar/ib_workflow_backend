"""
Created on: 04/10/20
Author: Pavankumar Pamuru

"""
from typing import List

from ib_tasks.interactors.get_task_details_conditions_dtos import TaskFilterDTO
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticSearchStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.filter_storage_interface import \
    FilterStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


class GetProjectSpecificConstants:
    def __init__(
            self, stage_storage: StageStorageInterface = None,
            task_storage: TaskStorageInterface = None,
            field_storage: FieldsStorageInterface = None,
            filter_storage: FilterStorageInterface = None,
            elasticsearch_storage: ElasticSearchStorageInterface = None):
        self.field_storage = field_storage
        self.elasticsearch_storage = elasticsearch_storage
        self.filter_storage = filter_storage
        self.stage_storage = stage_storage
        self.task_storage = task_storage

    def get_tasks_count_for_stages_in_column(
            self, project_id: str, user_id: str,
            task_condition_dtos: List[TaskFilterDTO], ):
        from ib_tasks.constants.constants import PROJECT_COLUMNS
        if project_id not in PROJECT_COLUMNS.keys():
            return 0, "No Completed Registrations"
        column_id = PROJECT_COLUMNS[project_id]['column_id']
        display_name = PROJECT_COLUMNS[project_id]['display_name']
        from ib_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        stage_ids = service_adapter.boards_service.get_stage_ids_for_the_column(
            column_id=column_id
        )
        from ib_tasks.interactors.get_task_ids_interactor import \
            GetTaskIdsInteractor
        tasks_count_interactor = GetTaskIdsInteractor(
            field_storage=self.field_storage,
            filter_storage=self.filter_storage,
            elasticsearch_storage=self.elasticsearch_storage,
            stage_storage=self.stage_storage,
            task_storage=self.task_storage
        )
        from ib_tasks.interactors.task_dtos import TaskDetailsConfigDTO
        task_details_config = TaskDetailsConfigDTO(
            unique_key=column_id,
            stage_ids=stage_ids,
            user_id=user_id,
            limit=1,
            offset=0,
            search_query=None,
            project_id=project_id
        )

        task_ids, tasks_count = tasks_count_interactor.get_task_ids_by_applying_filters(
            task_details_config=task_details_config,
            task_condition_dtos=task_condition_dtos,
            filter_dtos=[],
            field_type_dtos=[]
        )
        return tasks_count, display_name

    @staticmethod
    def get_complete_stages_project_url_links(project_id: str) -> str:
        from ib_tasks.constants.constants import WORKFLOW_URL_LINK
        url_link = WORKFLOW_URL_LINK[project_id]["CCBP_COMPLETE_WORKFLOW_LINK"]
        return url_link

    @staticmethod
    def get_permitted_stages_project_url_links(project_id: str) -> str:
        from ib_tasks.constants.constants import WORKFLOW_URL_LINK
        url_link = WORKFLOW_URL_LINK[project_id]["CCBP_USER_WORKFLOW_LINK"]
        return url_link
