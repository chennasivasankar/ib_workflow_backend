import collections
from typing import List

from ib_adhoc_tasks.adapters.iam_service import UserIdAndNameDTO
from ib_adhoc_tasks.adapters.task_service import StageIdAndNameDTO
from ib_adhoc_tasks.constants.enum import GroupByEnum
from ib_adhoc_tasks.interactors.dtos.dtos import GroupByDTO, \
    TaskOffsetAndLimitValuesDTO
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import GroupDetailsDTO
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
        service_adapter.iam_service.is_valid_user_id_for_given_project(
            user_id=user_id, project_id=project_id
        )

        user_role_ids = \
            service_adapter.iam_service.get_user_role_ids_based_on_project(
                user_id=user_id, project_id=project_id
            )
        stage_ids = service_adapter.task_service.get_user_permitted_stage_ids(
            user_role_ids=user_role_ids
        )

        type_of_group_by = ""
        type_of_child_group_by = ""
        for group_by_dto in group_by_dtos:
            if group_by_dto.order == 1:
                type_of_group_by = group_by_dto.group_by_value
            if group_by_dto.order == 2:
                type_of_child_group_by = group_by_dto.group_by_value

        group_details_dtos, group_count_dtos, child_group_count_dtos = \
            self.elastic_storage.get_group_details_of_project(
                project_id=project_id, stage_ids=stage_ids,
                adhoc_template_id=adhoc_template_id,
                group_by_dtos=group_by_dtos,
                task_offset_and_limit_values_dto=task_offset_and_limit_values_dto
            )
        if type_of_group_by:
            group_details_dtos = self.add_group_by_display_name_to_dtos(
                group_details_dtos=group_details_dtos,
                type_of_group_by=type_of_group_by
            )

        if type_of_child_group_by:
            group_details_dtos = self.add_child_group_by_display_name_to_dtos(
                group_details_dtos=group_details_dtos,
                type_of_child_group_by=type_of_child_group_by
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

    def add_group_by_display_name_to_dtos(
            self, group_details_dtos: List[GroupDetailsDTO],
            type_of_group_by: GroupByEnum
    ):
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        if type_of_group_by == GroupByEnum.ASSIGNEE.value:
            assignee_ids = self._get_group_by_values(group_details_dtos)
            assignee_id_and_name_dtos = \
                service_adapter.iam_service.get_user_details_bulk(
                    user_ids=assignee_ids
                )
            group_details_dtos = self._update_group_by_display_name_for_assignee(
                group_details_dtos=group_details_dtos,
                assignee_id_and_name_dtos=assignee_id_and_name_dtos
            )

        if type_of_group_by == GroupByEnum.STAGE.value:
            stage_ids = self._get_group_by_values(group_details_dtos)
            stage_id_and_name_dtos = \
                service_adapter.task_service.get_stage_details(
                    stage_ids=stage_ids)
            group_details_dtos = self._update_group_by_display_name_for_stage(
                group_details_dtos=group_details_dtos,
                stage_id_and_name_dtos=stage_id_and_name_dtos
            )
        return group_details_dtos

    @staticmethod
    def _get_group_by_values(group_details_dtos: List[GroupDetailsDTO]):
        group_by_values = [
            group_details_dto.group_by_value
            for group_details_dto in group_details_dtos
        ]
        return group_by_values

    @staticmethod
    def _update_group_by_display_name_for_assignee(
            group_details_dtos: List[GroupDetailsDTO],
            assignee_id_and_name_dtos: List[UserIdAndNameDTO]):
        assignee_id_wise_name_dict = {
            assignee_id_and_name_dto.user_id: assignee_id_and_name_dto.name
            for assignee_id_and_name_dto in assignee_id_and_name_dtos
        }

        for group_details_dto in group_details_dtos:
            group_details_dto.group_by_display_name = \
                assignee_id_wise_name_dict[group_details_dto.group_by_value]

        return group_details_dtos

    def add_child_group_by_display_name_to_dtos(
            self, group_details_dtos: List[GroupDetailsDTO],
            type_of_child_group_by):
        from ib_adhoc_tasks.adapters.service_adapter import get_service_adapter
        service_adapter = get_service_adapter()
        if type_of_child_group_by == GroupByEnum.ASSIGNEE.value:
            assignee_ids = self._get_child_group_by_values(group_details_dtos)
            assignee_id_and_name_dtos = \
                service_adapter.iam_service.get_user_details_bulk(
                    user_ids=assignee_ids
                )
            group_details_dtos = self._update_child_group_by_display_name_for_assingee(
                group_details_dtos=group_details_dtos,
                assignee_id_and_name_dtos=assignee_id_and_name_dtos
            )

        if type_of_child_group_by == GroupByEnum.STAGE.value:
            stage_ids = self._get_child_group_by_values(group_details_dtos)
            stage_id_and_name_dtos = \
                service_adapter.task_service.get_stage_details(
                    stage_ids=stage_ids)
            group_details_dtos = self._update_child_group_by_display_name_for_stage(
                group_details_dtos=group_details_dtos,
                stage_id_and_name_dtos=stage_id_and_name_dtos
            )
        return group_details_dtos

    @staticmethod
    def _get_child_group_by_values(group_details_dtos: List[GroupDetailsDTO]):
        group_by_values = [
            group_details_dto.child_group_by_value
            for group_details_dto in group_details_dtos
        ]
        return group_by_values

    @staticmethod
    def _update_child_group_by_display_name_for_assingee(
            group_details_dtos: List[GroupDetailsDTO],
            assignee_id_and_name_dtos: List[UserIdAndNameDTO]
    ):
        assignee_id_wise_name_dict = {
            assignee_id_and_name_dto.user_id: assignee_id_and_name_dto.name
            for assignee_id_and_name_dto in assignee_id_and_name_dtos
        }

        for group_details_dto in group_details_dtos:
            group_details_dto.child_group_by_display_name = \
                assignee_id_wise_name_dict[group_details_dto.group_by_value]

        return group_details_dtos

    @staticmethod
    def _update_group_by_display_name_for_stage(
            group_details_dtos: List[GroupDetailsDTO],
            stage_id_and_name_dtos: List[StageIdAndNameDTO]
    ):
        stage_id_wise_name_dict = {
            stage_id_and_name_dto.stage_id: stage_id_and_name_dto.name
            for stage_id_and_name_dto in stage_id_and_name_dtos
        }
        for group_details_dto in group_details_dtos:
            group_details_dto.group_by_display_name = \
                stage_id_wise_name_dict[group_details_dto.group_by_value]

        return group_details_dtos

    @staticmethod
    def _update_child_group_by_display_name_for_stage(
            group_details_dtos: List[GroupDetailsDTO],
            stage_id_and_name_dtos: List[StageIdAndNameDTO]
    ):
        stage_id_wise_name_dict = {
            stage_id_and_name_dto.stage_id: stage_id_and_name_dto.name
            for stage_id_and_name_dto in stage_id_and_name_dtos
        }
        for group_details_dto in group_details_dtos:
            group_details_dto.child_group_by_display_name = \
                stage_id_wise_name_dict[group_details_dto.child_group_by_value]

        return group_details_dtos
