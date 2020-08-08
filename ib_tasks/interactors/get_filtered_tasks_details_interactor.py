"""
Created on: 07/08/20
Author: Pavankumar Pamuru

"""
from ib_tasks.constants.enum import VIEWTYPE
from ib_tasks.exceptions.fields_custom_exceptions import \
    LimitShouldBeGreaterThanZeroException, \
    OffsetShouldBeGreaterThanZeroException
from ib_tasks.exceptions.stage_custom_exceptions import \
    StageIdsListEmptyException
from ib_tasks.interactors.presenter_interfaces.get_all_tasks_overview_for_user_presenter_interface import \
    GetFilteredTasksOverviewForUserPresenterInterface
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
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


class GetTaskDetailsByFilterInteractor:
    def __init__(self, stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface,
                 field_storage: FieldsStorageInterface,
                 action_storage: ActionStorageInterface,
                 filter_storage: FilterStorageInterface,
                 elasticsearch_storage: ElasticSearchStorageInterface):
        self.filter_storage = filter_storage
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.field_storage = field_storage
        self.action_storage = action_storage
        self.elasticsearch_storage = elasticsearch_storage

    def get_filtered_tasks_overview_for_user_wrapper(
            self, user_id: str, limit: int, offset: int, view_type: VIEWTYPE,
            presenter: GetFilteredTasksOverviewForUserPresenterInterface):
        try:
            filtered_tasks_overview_details_dto, total_tasks = self.get_filtered_tasks_overview_for_user(
                user_id=user_id, limit=limit, offset=offset, view_type=view_type
            )
        except StageIdsListEmptyException:
            return presenter.raise_stage_ids_empty_exception()

        except LimitShouldBeGreaterThanZeroException:
            return presenter.raise_limit_should_be_greater_than_zero_exception(
            )

        except OffsetShouldBeGreaterThanZeroException:
            return presenter. \
                raise_offset_should_be_greater_than_zero_exception(
            )
        return presenter.get_response_for_filtered_tasks_overview_details_response(
            filtered_tasks_overview_details_dto=filtered_tasks_overview_details_dto,
            total_tasks=total_tasks
        )

    def get_filtered_tasks_overview_for_user(
            self, user_id: str, limit: int, offset: int, view_type: VIEWTYPE):

        from ib_tasks.interactors.get_task_ids_by_applying_filters_interactor import \
            GetTaskIdsBasedOnUserFilters
        filtered_task_ids_interactor = GetTaskIdsBasedOnUserFilters(
            filter_storage=self.filter_storage,
            elasticsearch_storage=self.elasticsearch_storage
        )
        task_ids, total_tasks = filtered_task_ids_interactor.get_task_ids_by_applying_filters(
            user_id=user_id, limit=limit, offset=offset
        )
        from ib_tasks.interactors.get_all_task_overview_with_filters_and_searches_for_user import \
            GetTasksOverviewForUserInteractor
        task_details_interactor = GetTasksOverviewForUserInteractor(
            stage_storage=self.stage_storage,
            task_storage=self.task_storage,
            field_storage=self.field_storage,
            action_storage=self.action_storage
        )
        all_tasks_overview_details_dto = task_details_interactor.\
            get_filtered_tasks_overview_for_user(
                user_id=user_id, task_ids=task_ids, view_type=view_type
        )
        return all_tasks_overview_details_dto, total_tasks

