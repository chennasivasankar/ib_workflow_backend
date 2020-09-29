"""
Created on: 24/07/20
Author: Pavankumar Pamuru

"""
from typing import List, Tuple

from ib_tasks.interactors.get_task_details_conditions_dtos import TaskFilterDTO
from ib_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticSearchStorageInterface, ApplyFilterDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldTypeDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.filter_storage_interface import \
    FilterStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import TaskStageIdsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import TaskDetailsConfigDTO, TaskIdsDTO


class InvalidOffsetValue(Exception):
    pass


class InvalidLimitValue(Exception):
    pass


class GetTaskIdsInteractor:
    def __init__(
            self, stage_storage: StageStorageInterface,
            task_storage: TaskStorageInterface,
            field_storage: FieldsStorageInterface,
            filter_storage: FilterStorageInterface,
            elasticsearch_storage: ElasticSearchStorageInterface):
        self.field_storage = field_storage
        self.elasticsearch_storage = elasticsearch_storage
        self.filter_storage = filter_storage
        self.stage_storage = stage_storage
        self.task_storage = task_storage

    def get_task_ids(self, task_details_configs: List[TaskDetailsConfigDTO]):
        is_empty = not task_details_configs
        if is_empty:
            return []
        self._validate_given_data(task_details_configs=task_details_configs)
        user_id = task_details_configs[0].user_id,
        project_id = task_details_configs[0].project_id
        filter_dtos = self.filter_storage.get_enabled_filters_dto_to_user(
            user_id=user_id,
            project_id=project_id
        )
        field_ids = [filter_dto.field_id for filter_dto in filter_dtos]
        field_type_dtos = self.field_storage.get_field_type_dtos(
            field_ids=field_ids)
        # TODO need optimize db hits
        from ib_tasks.interactors.get_task_details_conditions_dtos import \
            GetConditionsForTaskDetails
        user_ids_interactor = GetConditionsForTaskDetails()
        task_condition_dtos = user_ids_interactor.get_conditions_for_the_task_details(
            project_id=project_id,
            user_id=user_id
        )
        total_task_ids_dtos = []
        for task_details_config in task_details_configs:
            task_ids_dto = self._get_task_ids_dto(
                task_details_config, filter_dtos, field_type_dtos, task_condition_dtos
            )
            total_task_ids_dtos.append(task_ids_dto)
        task_ids = []
        for total_task_ids_dto in total_task_ids_dtos:
            for task_stage_id in total_task_ids_dto.task_stage_ids:
                task_ids.append(task_stage_id.task_id)
        task_ids = list(set(task_ids))
        task_display_id_dtos = self.task_storage.get_task_display_ids_dtos(task_ids=task_ids)
        task_display_id_dtos_dict = {}
        for task_display_id_dto in task_display_id_dtos:
            task_display_id_dtos_dict[task_display_id_dto.task_id] = task_display_id_dto.display_id
        task_stage_details = self._get_task_stage_details(
            task_display_id_dtos_dict=task_display_id_dtos_dict,
            task_stage_dtos=total_task_ids_dtos
        )
        return task_stage_details

    @staticmethod
    def _get_task_stage_details(
            task_display_id_dtos_dict, task_stage_dtos: List[TaskIdsDTO]) -> List[TaskIdsDTO]:
        new_task_stage_details = []
        for task_stage_dto in task_stage_dtos:
            new_task_stage_dtos = []
            for task_stage_id in task_stage_dto.task_stage_ids:
                new_task_stage_dtos.append(
                    TaskStageIdsDTO(
                        task_id=task_stage_id.task_id,
                        task_display_id=task_display_id_dtos_dict[task_stage_id.task_id],
                        stage_id=task_stage_id.stage_id
                    )
                )
            new_task_stage_dto = TaskIdsDTO(
                unique_key=task_stage_dto.unique_key,
                task_stage_ids=new_task_stage_dtos,
                total_tasks=task_stage_dto.total_tasks
            )
            new_task_stage_details.append(new_task_stage_dto)
        return new_task_stage_details

    def _validate_given_data(self, task_details_configs: List[TaskDetailsConfigDTO]):
        for task_details_config in task_details_configs:
            if task_details_config.offset < 0:
                raise InvalidOffsetValue
            if task_details_config.limit < 1:
                raise InvalidLimitValue
        total_stage_ids = []
        for task_details_config in task_details_configs:
            total_stage_ids += task_details_config.stage_ids
        valid_stage_ids = self.stage_storage.get_existing_stage_ids(
            stage_ids=total_stage_ids
        )
        invalid_stage_ids = [
            stage_id for stage_id in total_stage_ids
            if stage_id not in valid_stage_ids
        ]
        if invalid_stage_ids:
            from ib_tasks.exceptions.stage_custom_exceptions import \
                InvalidStageIdsListException
            raise InvalidStageIdsListException(
                invalid_stage_ids=invalid_stage_ids)

    def _get_task_ids_dto(
            self, task_details_config: TaskDetailsConfigDTO,
            filter_dtos: List[ApplyFilterDTO], field_type_dtos: List[FieldTypeDTO],
            task_condition_dtos: List[TaskFilterDTO]) -> TaskIdsDTO:
        task_stage_dtos, total_count = self._get_task_ids_by_applying_filters(
            task_details_config=task_details_config, filter_dtos=filter_dtos,
            field_type_dtos=field_type_dtos, task_condition_dtos=task_condition_dtos
        )

        return TaskIdsDTO(
            unique_key=task_details_config.unique_key,
            task_stage_ids=task_stage_dtos,
            total_tasks=total_count
        )

    def _get_task_ids_by_applying_filters(
            self, task_details_config: TaskDetailsConfigDTO, task_condition_dtos: List[TaskFilterDTO],
            filter_dtos: List[ApplyFilterDTO], field_type_dtos: List[FieldTypeDTO]) -> Tuple[List[TaskStageIdsDTO], int]:
        filtered_task_ids, total_tasks = self.elasticsearch_storage.filter_tasks_with_stage_ids(
            filter_dtos=filter_dtos, task_details_config=task_details_config,
            field_type_dtos=field_type_dtos, task_condition_dtos=task_condition_dtos
        )
        return filtered_task_ids, total_tasks


