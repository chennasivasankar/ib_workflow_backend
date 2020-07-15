"""
Created on: 15/07/20
Author: Pavankumar Pamuru

"""

import abc
from typing import List

from ib_tasks.interactors.dtos import CreateTaskTemplateDTO, FieldDTO
from ib_tasks.interactors.storage_interfaces.dtos import GOFDTO


class TaskStorageInterface(abc.ABC):

    @abc.abstractmethod
    def create_task_template(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        pass

    @abc.abstractmethod
    def update_task_template(
            self, create_task_template_dto: CreateTaskTemplateDTO):
        pass

    @abc.abstractmethod
    def get_task_template_name_if_exists(self, template_id: str) -> str:
        pass

    @abc.abstractmethod
    def get_task_template_ids(self) -> List[str]:
        pass

    @abc.abstractmethod
    def create_fields(self, field_dtos: List[FieldDTO]):
        pass

    @abc.abstractmethod
    def get_existing_gof_of_template(self, template_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def create_gofs(self, gof_dtos: List[GOFDTO]):
        pass

