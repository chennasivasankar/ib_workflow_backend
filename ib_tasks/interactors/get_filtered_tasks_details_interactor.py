"""
Created on: 07/08/20
Author: Pavankumar Pamuru

"""
from dataclasses import dataclass

from ib_tasks.exceptions.adapter_exceptions  import UserIsNotInProjectException
from ib_tasks.constants.enum import ViewType
from ib_tasks.exceptions.adapter_exceptions import InvalidProjectIdsException
from ib_tasks.exceptions.fields_custom_exceptions import \
    LimitShouldBeGreaterThanZeroException, \
    OffsetShouldBeGreaterThanZeroException
from ib_tasks.exceptions.stage_custom_exceptions import \
    StageIdsListEmptyException
from ib_tasks.interactors.mixins.validation_mixin import ValidationMixin
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
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface import \
    TaskStageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


@dataclass
class ProjectTasksParameterDTO:
    project_id: str
    user_id: str
    limit: int
    offset: int
    view_type: ViewType


class GetTaskDetailsByFilterInteractor(ValidationMixin):
    def __init__(self, stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface,
                 field_storage: FieldsStorageInterface,
                 action_storage: ActionStorageInterface,
                 filter_storage: FilterStorageInterface,
                 elasticsearch_storage: ElasticSearchStorageInterface,
                 task_stage_storage: TaskStageStorageInterface):
        self.task_stage_storage = task_stage_storage
        self.filter_storage = filter_storage
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.field_storage = field_storage
        self.action_storage = action_storage
        self.elasticsearch_storage = elasticsearch_storage

    def get_filtered_tasks_overview_for_user_wrapper(
            self, project_tasks_parameter: ProjectTasksParameterDTO,
            presenter: GetFilteredTasksOverviewForUserPresenterInterface):
        try:
            filtered_tasks_overview_details_dto, total_tasks = \
                self.get_filtered_tasks_overview_for_user(
                    project_tasks_parameter=project_tasks_parameter
                )
        except StageIdsListEmptyException:
            return presenter.raise_stage_ids_empty_exception()

        except LimitShouldBeGreaterThanZeroException:
            return presenter.raise_limit_should_be_greater_than_zero_exception(
            )
        except InvalidProjectIdsException as err:
            return presenter.get_response_for_invalid_project_id(err=err)
        except UserIsNotInProjectException:
            return presenter.get_response_for_user_not_in_project()
        except OffsetShouldBeGreaterThanZeroException:
            return presenter. \
                raise_offset_should_be_greater_than_zero_exception()
        return presenter.get_response_for_filtered_tasks_overview_details_response(
            filtered_tasks_overview_details_dto=filtered_tasks_overview_details_dto,
            total_tasks=total_tasks
        )

    def get_filtered_tasks_overview_for_user(
            self, project_tasks_parameter: ProjectTasksParameterDTO):
        self._validate_project_data(
            project_id=project_tasks_parameter.project_id,
            user_id=project_tasks_parameter.user_id
        )
        from ib_tasks.adapters.service_adapter import get_service_adapter
        roles_service = get_service_adapter().roles_service
        user_roles = roles_service.get_user_role_ids_based_on_project(
            user_id=project_tasks_parameter.user_id,
            project_id=project_tasks_parameter.project_id
        )
        stage_ids_having_actions = self.stage_storage\
            .get_stage_ids_having_actions(user_roles=user_roles)

        from ib_tasks.interactors.get_task_ids_by_applying_filters_interactor import \
            GetTaskIdsBasedOnUserFilters
        filtered_task_ids_interactor = GetTaskIdsBasedOnUserFilters(
            filter_storage=self.filter_storage,
            elasticsearch_storage=self.elasticsearch_storage,
            field_storage=self.field_storage
        )

        from ib_tasks.interactors.get_all_task_overview_with_filters_and_searches_for_user import \
            GetTasksOverviewForUserInteractor
        task_details_interactor = GetTasksOverviewForUserInteractor(
            stage_storage=self.stage_storage,
            task_storage=self.task_storage,
            field_storage=self.field_storage,
            action_storage=self.action_storage,
            task_stage_storage=self.task_stage_storage
        )
        from ib_tasks.interactors.get_task_ids_by_applying_filters_interactor import \
            FilterTasksParameter
        filter_tasks_parameter = FilterTasksParameter(
            project_id=project_tasks_parameter.project_id,
            user_id=project_tasks_parameter.user_id,
            limit=project_tasks_parameter.limit,
            offset=project_tasks_parameter.offset,
            stage_ids=stage_ids_having_actions
        )
        task_ids, total_tasks = filtered_task_ids_interactor.get_task_ids_by_applying_filters(
            filter_tasks_parameter=filter_tasks_parameter,
        )
        project_id = project_tasks_parameter.project_id
        all_tasks_overview_details_dto = task_details_interactor. \
            get_filtered_tasks_overview_for_user(
                user_id=project_tasks_parameter.user_id,
                task_ids=task_ids,
                view_type=project_tasks_parameter.view_type,
                project_id=project_id
            )
        return all_tasks_overview_details_dto, total_tasks

    def _validate_project_data(self, project_id: str, user_id: str):

        self.validate_given_project_ids(project_ids=[project_id])
        self.validate_if_user_is_in_project(
            project_id=project_id, user_id=user_id
        )
