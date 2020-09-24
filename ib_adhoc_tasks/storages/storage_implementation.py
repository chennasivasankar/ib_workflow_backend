from typing import List

from ib_adhoc_tasks.constants.enum import ViewType
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
    GroupByResponseDTO, AddOrEditGroupByParameterDTO, GroupByDetailsDTO
from ib_adhoc_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface


class StorageImplementation(StorageInterface):

    def get_group_by_details_dtos(
            self, user_id: str, view_type: ViewType
    ) -> List[GroupByDetailsDTO]:
        from ib_adhoc_tasks.models import GroupByInfo
        group_by_objects = GroupByInfo.objects.filter(
            user_id=user_id, view_type=view_type
        )
        group_by_details_dtos = [
            GroupByDetailsDTO(
                group_by=group_by_object.group_by,
                order=group_by_object.order
            )
            for group_by_object in group_by_objects
        ]
        return group_by_details_dtos

    def get_group_by_dtos(
            self, user_id: str, view_type: ViewType
    ) -> List[GroupByResponseDTO]:
        from ib_adhoc_tasks.models import GroupByInfo
        group_by_info_objects = GroupByInfo.objects.filter(
            user_id=user_id, view_type=view_type
        )
        group_by_response_dtos = [
            self._convert_to_group_by_response_dto(
                group_by_info_object=group_by_info_object
            ) for group_by_info_object in group_by_info_objects
        ]
        return group_by_response_dtos

    def add_group_by(
            self,
            add_or_edit_group_by_parameter_dto: AddOrEditGroupByParameterDTO
    ) -> GroupByResponseDTO:
        from ib_adhoc_tasks.models import GroupByInfo
        group_by_info_object = GroupByInfo.objects.create(
            user_id=add_or_edit_group_by_parameter_dto.user_id,
            group_by=add_or_edit_group_by_parameter_dto.group_by_key,
            view_type=add_or_edit_group_by_parameter_dto.view_type,
            order=add_or_edit_group_by_parameter_dto.order,
        )
        group_by_response_dto = self._convert_to_group_by_response_dto(
            group_by_info_object=group_by_info_object
        )
        return group_by_response_dto

    def edit_group_by(
            self,
            add_or_edit_group_by_parameter_dto: AddOrEditGroupByParameterDTO
    ) -> GroupByResponseDTO:
        from ib_adhoc_tasks.models import GroupByInfo
        GroupByInfo.objects.filter(
            id=add_or_edit_group_by_parameter_dto.group_by_id
        ).update(
            group_by=add_or_edit_group_by_parameter_dto.group_by_key,
            view_type=add_or_edit_group_by_parameter_dto.view_type,
            order=add_or_edit_group_by_parameter_dto.order,
        )
        group_by_info_object = GroupByInfo.objects.get(
            id=add_or_edit_group_by_parameter_dto.group_by_id
        )
        group_by_response_dto = self._convert_to_group_by_response_dto(
            group_by_info_object=group_by_info_object
        )
        return group_by_response_dto

    @staticmethod
    def _convert_to_group_by_response_dto(group_by_info_object):
        return GroupByResponseDTO(
            group_by_key=group_by_info_object.group_by,
            display_name=group_by_info_object.group_by,
            group_by_id=group_by_info_object.id,
            order=group_by_info_object.order
        )
