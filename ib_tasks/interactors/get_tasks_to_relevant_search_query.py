from dataclasses import dataclass
from typing import Any

from ib_tasks.exceptions.fields_custom_exceptions import LimitShouldBeGreaterThanZeroException, \
    OffsetShouldBeGreaterThanZeroException
from ib_tasks.exceptions.stage_custom_exceptions import StageIdsListEmptyException
from ib_tasks.interactors.presenter_interfaces.get_all_tasks_overview_for_user_presenter_interface import \
    GetAllTasksOverviewForUserPresenterInterface
from ib_tasks.interactors.storage_interfaces.action_storage_interface import ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import ElasticSearchStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import TaskStorageInterface


@dataclass
class SearchQueryDTO:
    user_id: str
    offset: int
    limit: int
    query_value: Any


class GetTasksToRelevantSearchQuery:

    def __init__(self, stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface,
                 field_storage: FieldsStorageInterface,
                 action_storage: ActionStorageInterface,
                 elastic_storage: ElasticSearchStorageInterface):
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.field_storage = field_storage
        self.action_storage = action_storage
        self.elastic_storage = elastic_storage

    def get_all_tasks_overview_for_user_wrapper(
            self, search_query_dto: SearchQueryDTO,
            presenter: GetAllTasksOverviewForUserPresenterInterface):
        try:
            all_tasks_overview_details_dto = \
                self.get_tasks_for_search_query(search_query_dto)
        except StageIdsListEmptyException:
            return presenter.raise_stage_ids_empty_exception()
        except LimitShouldBeGreaterThanZeroException:
            return presenter.raise_limit_should_be_greater_than_zero_exception()
        except OffsetShouldBeGreaterThanZeroException:
            return presenter. \
                raise_offset_should_be_greater_than_zero_exception()
        return presenter.all_tasks_overview_details_response(
            all_tasks_overview_details_dto)

    def get_tasks_for_search_query(
            self, search_query_dto: SearchQueryDTO):
        offset = search_query_dto.offset
        limit = search_query_dto.limit
        query_value = search_query_dto.query_value
        self._validations_of_limit_and_offset(offset=offset, limit=limit)
        query_tasks_dto = self.elastic_storage.query_tasks(
            offset=offset, limit=limit, search_query=query_value
        )

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