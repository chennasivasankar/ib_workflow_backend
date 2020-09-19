from dataclasses import dataclass
from typing import List

from ib_adhoc_tasks.constants.enum import GroupByType
from ib_adhoc_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticStorageInterface


@dataclass
class GroupByDTO:
    key: GroupByType
    value: str


@dataclass
class ApplyGroupByDTO:
    project_id: str
    template_id: str
    user_id: str
    groupby_dtos: List[GroupByDTO]
    value: str


class GetTaskIdsForGroupInteractor:

    def __init__(self, elastic_storage: ElasticStorageInterface):
        self.elastic_storage = elastic_storage

    def get_task_ids_for_groups(
            self, apply_group_dto: ApplyGroupByDTO,
    ):
        from ib_adhoc_tasks.adapters.service import Service
        service = Service()
        user_role_ids = service.get_user_role_ids_based_on_project(
            user_id=apply_group_dto.user_id,
            project_id=apply_group_dto.project_id
        )
        stage_ids = service.get_stage_ids_based_on_user_roles(
            user_role_ids=user_role_ids
        )

        task_ids = []
        is_assignee_field_exist = False
        for groupby_dto in apply_group_dto.groupby_dtos:
            if groupby_dto.key != GroupByType.ASSIGNEE.value:
                task_ids.extend(
                    self._get_task_ids_for_given_groupby_dto_and_other_detail(
                        apply_group_dto=apply_group_dto, stage_ids=stage_ids,
                        groupby_dto=groupby_dto
                    )
                )
            else:
                # TODO : need to do what if assignees exist
                is_assignee_field_exist = True

    def _get_task_ids_for_given_groupby_dto_and_other_detail(
            self, apply_group_dto: ApplyGroupByDTO, stage_ids: List[str],
            groupby_dto: GroupByDTO
    ) -> List[str]:
        task_ids = []
        if groupby_dto.key == GroupByType.STAGE.value:
            from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
                FilterForStageDTO
            filter_for_stage_dto = FilterForStageDTO(
                project_id=apply_group_dto.project_id,
                template_id=apply_group_dto.template_id,
                stage_id=groupby_dto.value
            )
            task_ids = self.elastic_storage.get_task_ids_filtered_on_stage_id(
                filter_for_stage_dto=filter_for_stage_dto
            )
        if groupby_dto.key == GroupByType.FIELD.value:
            field_id = groupby_dto.key.value
            from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
                FieldIdAndValueDTO
            field_dto = FieldIdAndValueDTO(field_id=field_id,
                                           value=groupby_dto.value)
            from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
                FilterForFieldDTO
            filter_for_field_dto = FilterForFieldDTO(
                project_id=apply_group_dto.project_id,
                template_id=apply_group_dto.template_id,
                stage_ids=stage_ids,
                field_dto=field_dto
            )
            task_ids = self.elastic_storage.get_task_ids_filtered_on_given_field(
                filter_for_field_dto=filter_for_field_dto
            )
        return task_ids
