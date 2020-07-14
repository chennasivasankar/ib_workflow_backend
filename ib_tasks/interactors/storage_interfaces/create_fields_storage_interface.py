import abc
from abc import ABC, abstractmethod

from typing import List

from ib_tasks.interactors.dtos.dtos import FieldDTO


class CreateFieldsStorageInterface(ABC):

    @abstractmethod
    def get_available_roles(self) -> List[str]:
        pass

    @abstractmethod
    def create_fields(self, field_dtos: List[FieldDTO]):
        pass
