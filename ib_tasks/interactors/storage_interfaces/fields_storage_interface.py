"""
Created on: 15/07/20
Author: Pavankumar Pamuru

"""
import abc
from typing import List

from ib_tasks.interactors.dtos import FieldDTO
from ib_tasks.interactors.storage_interfaces.dtos import GOFDTO


class FieldsStorageInterface(abc.ABC):

    @abc.abstractmethod
    def create_fields(self, field_dtos: List[FieldDTO]):
        pass

    @abc.abstractmethod
    def get_existing_gof_of_template(self, template_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def create_gofs(self, gof_dtos: List[GOFDTO]):
        pass