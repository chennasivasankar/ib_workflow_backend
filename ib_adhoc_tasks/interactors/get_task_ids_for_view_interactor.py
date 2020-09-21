import collections
from typing import List

from ib_adhoc_tasks.interactors.dtos.dtos import GroupByDTO, \
    TaskOffsetAndLimitValuesDTO
from ib_adhoc_tasks.interactors.storage_interfaces.elastic_storage_interface import \
    ElasticStorageInterface


class GetTaskIdsForViewInteractor:

    def __init__(self, elastic_storage: ElasticStorageInterface):
        self.elastic_storage = elastic_storage

    def get_task_ids_for_view(
            self, user_id: str, project_id: str, adhoc_template_id: str,
            group_by_dtos: List[GroupByDTO],
            task_offset_and_limit_values_dto: TaskOffsetAndLimitValuesDTO
    ):
        self._validate_project_id(project_id=project_id)
        self._validate_template_id(task_template_id=adhoc_template_id)
        self._validate_group_by_dtos(group_by_dtos=group_by_dtos)
        self._validate_task_limit_and_offset_value(
            task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
        )

        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        user_role_ids = service_adapter.iam_service.get_user_role_ids(user_id=user_id)
        stage_ids = service_adapter.task_service.get_user_permitted_stage_ids(
            user_role_ids=user_role_ids
        )

        group_details_dtos, group_count_dtos, child_group_count_dtos = \
            self.elastic_storage.get_group_details_of_project(
                project_id=project_id, stage_ids=stage_ids,
                adhoc_template_id=adhoc_template_id,
                group_by_dtos=group_by_dtos,
                task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
            )
        return group_details_dtos, group_count_dtos, child_group_count_dtos

    @staticmethod
    def _validate_template_id(task_template_id: str):
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        service_adapter.task_service.validate_task_template_id(
            task_template_id=task_template_id
        )
        return

    @staticmethod
    def _validate_project_id(project_id: str):
        from ib_adhoc_tasks.exceptions.custom_exceptions import \
            InvalidProjectId
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        valid_project_ids = service_adapter.iam_service.get_valid_project_ids(
            project_ids=[project_id]
        )
        is_project_id_invalid = not valid_project_ids
        if is_project_id_invalid:
            raise InvalidProjectId

    @staticmethod
    def _validate_group_by_dtos(group_by_dtos: List[GroupByDTO]):
        group_by_orders = [
            group_by_dto.order
            for group_by_dto in group_by_dtos
        ]
        duplicate_orders = [
            group_by_order
            for group_by_order, count in
            collections.Counter(group_by_orders).items() if count > 1
        ]
        from ib_adhoc_tasks.exceptions.custom_exceptions import \
            DuplicateGroupByOrder
        if duplicate_orders:
            raise DuplicateGroupByOrder

        from ib_adhoc_tasks.exceptions.custom_exceptions import \
            InvalidGroupLimitValue, InvalidGroupOffsetValue
        for group_by_dto in group_by_dtos:
            if group_by_dto.limit < 0:
                raise InvalidGroupLimitValue
            if group_by_dto.offset < 0:
                raise InvalidGroupOffsetValue
        # TODO: validate group by key
        return

    @staticmethod
    def _validate_task_limit_and_offset_value(
            task_offset_and_limit_values_dto: TaskOffsetAndLimitValuesDTO
    ):
        from ib_adhoc_tasks.exceptions.custom_exceptions import \
            InvalidTaskLimitValue, InvalidTaskOffsetValue
        if task_offset_and_limit_values_dto.limit < 0:
            raise InvalidTaskLimitValue
        if task_offset_and_limit_values_dto.offset < 0:
            raise InvalidTaskOffsetValue
