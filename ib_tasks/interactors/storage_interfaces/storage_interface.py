
import abc

from typing import List

from ib_tasks.interactors.storage_interfaces.dtos import GoFDTO, GoFRolesDTO, \
    GoFFieldsDTO


class StorageInterface(abc.ABC):

    @abc.abstractmethod
    def create_gofs(self, gof_dtos: List[GoFDTO]):
        pass

    @abc.abstractmethod
    def create_gof_roles(self, gof_roles_dtos: List[GoFRolesDTO]):
        pass

    @abc.abstractmethod
    def create_gof_fields(self, gof_fields_dtos: List[GoFFieldsDTO]):
        pass
