from typing import List

from ib_adhoc_tasks.constants.enum import ViewType
from ib_adhoc_tasks.interactors.dtos.dtos import GroupByParameter, \
    GroupBYKeyDTO
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

    def get_view_types_of_user(self, user_id: str) -> List[str]:
        from ib_adhoc_tasks.models import GroupByInfo
        view_types = GroupByInfo.objects.filter(user_id=user_id) \
            .values_list("view_type", flat=True)
        return list(view_types)

    def add_or_edit_group_by_for_list_view(
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

    def delete_all_user_group_by(self, user_id: str):
        from ib_adhoc_tasks.models import GroupByInfo
        GroupByInfo.objects.filter(user_id=user_id).delete()

    def add_group_by_for_kanban_view_in_bulk(
            self,
            group_by_parameter: GroupByParameter,
            group_by_key_dtos: List[GroupBYKeyDTO]
    ) -> List[GroupByResponseDTO]:
        from ib_adhoc_tasks.models import GroupByInfo
        group_by_info_objects = [
            GroupByInfo(
                user_id=group_by_parameter.user_id,
                group_by=group_by_key_dto.group_by_key,
                order=group_by_key_dto.order,
                view_type=group_by_parameter.view_type,
            ) for group_by_key_dto in group_by_key_dtos
        ]
        group_by_info_objects = GroupByInfo.objects.bulk_create(
            group_by_info_objects
        )
        group_by_response_dtos = [
            self._convert_to_group_by_response_dto(
                group_by_info_object=group_by_info_object
            ) for group_by_info_object in group_by_info_objects
        ]
        return group_by_response_dtos

    @staticmethod
    def _convert_to_group_by_response_dto(group_by_info_object):
        return GroupByResponseDTO(
            group_by_key=group_by_info_object.group_by,
            display_name=group_by_info_object.group_by.capitalize().replace('_', " "),
            order=group_by_info_object.order
        )
