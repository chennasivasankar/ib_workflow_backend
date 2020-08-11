from dataclasses import dataclass
from typing import Any, List

from ib_tasks.constants.enum import ViewType
from ib_tasks.exceptions.fields_custom_exceptions import LimitShouldBeGreaterThanZeroException, \
    OffsetShouldBeGreaterThanZeroException
from ib_tasks.exceptions.stage_custom_exceptions import StageIdsListEmptyException
from ib_tasks.interactors.presenter_interfaces.get_all_tasks_overview_for_user_presenter_interface import \
    GetFilteredTasksOverviewForUserPresenterInterface
from ib_tasks.interactors.storage_interfaces.action_storage_interface import ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import ElasticSearchStorageInterface, \
    ApplyFilterDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.filter_storage_interface import FilterStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface import TaskStageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import TaskStorageInterface


@dataclass
class SearchQueryDTO:
    user_id: str
    offset: int
    limit: int
    query_value: Any
    view_type: ViewType


class GetTasksToRelevantSearchQuery:

    def __init__(self, stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface,
                 field_storage: FieldsStorageInterface,
                 action_storage: ActionStorageInterface,
                 filter_storage: FilterStorageInterface,
                 elasticsearch_storage: ElasticSearchStorageInterface,
                 task_stage_storage: TaskStageStorageInterface):
        self.filter_storage = filter_storage
        self.task_stage_storage = task_stage_storage
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.field_storage = field_storage
        self.action_storage = action_storage
        self.elasticsearch_storage = elasticsearch_storage

    def get_all_tasks_overview_for_user_wrapper(
            self, search_query_dto: SearchQueryDTO,
            presenter: GetFilteredTasksOverviewForUserPresenterInterface,
            apply_filters_dto: List[ApplyFilterDTO]):
        try:
            filtered_tasks_overview_details_dto, total_tasks = \
                self.get_tasks_for_search_query(search_query_dto, apply_filters_dto)
        except StageIdsListEmptyException:
            return presenter.raise_stage_ids_empty_exception()
        except LimitShouldBeGreaterThanZeroException:
            return presenter.raise_limit_should_be_greater_than_zero_exception()
        except OffsetShouldBeGreaterThanZeroException:
            return presenter. \
                raise_offset_should_be_greater_than_zero_exception()
        return presenter.get_response_for_filtered_tasks_overview_details_response(
            filtered_tasks_overview_details_dto=filtered_tasks_overview_details_dto,
            total_tasks=total_tasks
        )

    def get_tasks_for_search_query(
            self, search_query_dto: SearchQueryDTO,
            apply_filters_dto: List[ApplyFilterDTO]):
        offset = search_query_dto.offset
        user_id = search_query_dto.user_id
        limit = search_query_dto.limit
        query_value = search_query_dto.query_value
        view_type = search_query_dto.view_type
        filter_dtos = self.filter_storage.get_enabled_filters_dto_to_user(
            user_id=user_id
        )
        apply_filters_dto = apply_filters_dto + filter_dtos
        self._validations_of_limit_and_offset(offset=offset, limit=limit)
        query_tasks_dto = self.elasticsearch_storage.search_tasks(
            offset=offset, limit=limit, search_query=query_value,
            apply_filter_dtos=apply_filters_dto
        )
        return self._get_all_tasks_overview_details(
            query_tasks_dto, view_type, user_id
        )

    def _get_all_tasks_overview_details(self, query_tasks_dto, view_type, user_id):
        from ib_tasks.interactors.get_all_task_overview_with_filters_and_searches_for_user import \
            GetTasksOverviewForUserInteractor
        task_details_interactor = GetTasksOverviewForUserInteractor(
            stage_storage=self.stage_storage,
            task_storage=self.task_storage,
            field_storage=self.field_storage,
            action_storage=self.action_storage,
            task_stage_storage=self.task_stage_storage
        )
        all_tasks_overview_details_dto = task_details_interactor. \
            get_filtered_tasks_overview_for_user(
            user_id=user_id, task_ids=query_tasks_dto.task_ids,
            view_type=view_type
        )
        return all_tasks_overview_details_dto, query_tasks_dto.total_tasks_count

    @staticmethod
    def _validations_of_limit_and_offset(offset: int, limit: int):
        if limit < 1:
            from ib_tasks.exceptions.fields_custom_exceptions import \
                LimitShouldBeGreaterThanZeroException
            raise LimitShouldBeGreaterThanZeroException

        if offset < 0:
            from ib_tasks.exceptions.fields_custom_exceptions import \
                OffsetShouldBeGreaterThanZeroException
            raise OffsetShouldBeGreaterThanZeroException
