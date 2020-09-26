import abc
from typing import List

from ib_adhoc_tasks.constants.enum import ViewType
from ib_adhoc_tasks.interactors.dtos.dtos import GroupByParameter, \
    GroupBYKeyDTO
from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
    GroupByResponseDTO, AddOrEditGroupByParameterDTO, GroupByDetailsDTO


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_group_by_dtos(
            self, user_id: str, view_type: ViewType
    ) -> List[GroupByResponseDTO]:
        pass

    @abc.abstractmethod
    def add_group_by(
            self,
            add_or_edit_group_by_parameter_dto: AddOrEditGroupByParameterDTO
    ) -> GroupByResponseDTO:
        pass

    @abc.abstractmethod
    def edit_group_by(
            self,
            add_or_edit_group_by_parameter_dto: AddOrEditGroupByParameterDTO
    ) -> GroupByResponseDTO:
        pass

    @abc.abstractmethod
    def get_group_by_details_dtos(
            self, user_id: str, view_type: ViewType
    ) -> List[GroupByDetailsDTO]:
        pass

    @abc.abstractmethod
    def get_view_types_of_user(self, user_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def add_or_edit_group_by_for_list_view(
            self,
            add_or_edit_group_by_parameter_dto: AddOrEditGroupByParameterDTO
    ):
        pass

    @abc.abstractmethod
    def delete_all_user_group_by(self, user_id: str):
        pass

    @abc.abstractmethod
    def add_group_by_for_kanban_view_in_bulk(
            self,
            group_by_parameter: GroupByParameter,
            group_by_key_dtos: List[GroupBYKeyDTO]
    ):
        pass
