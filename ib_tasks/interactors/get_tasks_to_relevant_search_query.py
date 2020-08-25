from typing import List

from ib_tasks.adapters.auth_service import InvalidProjectIdsException, \
    UserIsNotInProjectException
from ib_tasks.constants.enum import ViewType
from ib_tasks.documents.elastic_task import QueryTasksDTO
from ib_tasks.exceptions.fields_custom_exceptions import LimitShouldBeGreaterThanZeroException, \
    OffsetShouldBeGreaterThanZeroException
from ib_tasks.exceptions.stage_custom_exceptions import StageIdsListEmptyException
from ib_tasks.interactors.mixins.validation_mixin import ValidationMixin
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
from ib_tasks.interactors.task_dtos import SearchQueryDTO


class GetTasksToRelevantSearchQuery(ValidationMixin):

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
                self.get_tasks_for_search_query(search_query_dto,
                                                apply_filters_dto)
        except StageIdsListEmptyException:
            return presenter.raise_stage_ids_empty_exception()
        except InvalidProjectIdsException as err:
            return presenter.get_response_for_invalid_project_id(err=err)
        except UserIsNotInProjectException:
            return presenter.get_response_for_user_not_in_project()
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
        view_type = search_query_dto.view_type
        project_id = search_query_dto.project_id
        self._validate_project_data(project_id=project_id, user_id=user_id)
        filter_dtos = self.filter_storage.get_enabled_filters_dto_to_user(
            user_id=user_id, project_id=project_id
        )
        apply_filters_dto = apply_filters_dto + filter_dtos
        field_ids = [filter_dto.field_id for filter_dto in apply_filters_dto]
        field_type_dtos = self.field_storage.get_field_type_dtos(
            field_ids=field_ids)
        from ib_tasks.adapters.service_adapter import get_service_adapter
        roles_service = get_service_adapter().roles_service
        user_roles = roles_service.get_user_role_ids(
            user_id=user_id)
        stage_ids_having_actions = self.stage_storage \
            .get_stage_ids_having_actions(user_roles=user_roles)
        self._validations_of_limit_and_offset(offset=offset, limit=limit)
        query_tasks_dto = self.elasticsearch_storage.search_tasks(
            search_query_dto=search_query_dto,
            apply_filter_dtos=apply_filters_dto,
            stage_ids=stage_ids_having_actions,
            field_type_dtos=field_type_dtos
        )
        return self._get_all_tasks_overview_details(
            query_tasks_dto, view_type, user_id, project_id
        )

    def _validate_project_data(self, project_id: str, user_id: str):

        self.validate_given_project_ids(project_ids=[project_id])
        self.validate_if_user_is_in_project(
            project_id=project_id, user_id=user_id
        )

    def _get_all_tasks_overview_details(self, query_tasks_dto: QueryTasksDTO,
                                        view_type: ViewType,
                                        user_id: str,
                                        project_id: str):
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
            view_type=view_type,
            project_id=project_id
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
