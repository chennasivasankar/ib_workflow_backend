import abc

from typing import List

from ib_tasks.interactors.dtos.dtos import FieldDTO


class CreateFieldsStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_available_roles(self) -> List[str]:
        pass

    @abc.abstractmethod
    def create_fields(self, field_dtos: List[FieldDTO]):
        pass
