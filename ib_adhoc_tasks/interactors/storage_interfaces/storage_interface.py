import abc
from typing import List

from ib_adhoc_tasks.interactors.storage_interfaces.dtos import \
    GroupByResponseDTO, AddOrEditGroupByParameterDTO


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_group_by_dtos(self, user_id: str) -> List[GroupByResponseDTO]:
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
