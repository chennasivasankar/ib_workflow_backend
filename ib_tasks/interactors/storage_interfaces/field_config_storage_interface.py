import abc
from typing import List

from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDTO, \
    FieldRoleDTO


class FieldConfigStorageInterface(abc.ABC):
    @abc.abstractmethod
    def create_fields(self, field_dtos: List[FieldDTO]):
        pass

    @abc.abstractmethod
    def update_fields(self, field_dtos: List[FieldDTO]):
        pass

    @abc.abstractmethod
    def create_fields_roles(self, field_role_dtos: List[FieldRoleDTO]):
        pass

    @abc.abstractmethod
    def get_existing_field_ids(self, field_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def delete_field_roles(self, field_ids: List[str]):
        pass

