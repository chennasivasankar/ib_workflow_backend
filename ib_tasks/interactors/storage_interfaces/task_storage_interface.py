import abc
from typing import List
from ib_tasks.interactors.dtos import FieldDTO, GoFIDAndOrderDTO
from ib_tasks.interactors.storage_interfaces.dtos import GOFDTO


class TaskStorageInterface(abc.ABC):

    @abc.abstractmethod
    def create_task_template(self, template_id: str, template_name: str):
        pass

    @abc.abstractmethod
    def add_gofs_to_task_template(
            self, template_id: str,
            gof_id_and_order_dtos: List[GoFIDAndOrderDTO]):
        pass

    @abc.abstractmethod
    def get_task_template_ids(self) -> List[str]:
        pass

    @abc.abstractmethod
    def create_fields(self, field_dtos: List[FieldDTO]):
        pass

    @abc.abstractmethod
    def create_gofs(self, gof_dtos: List[GOFDTO]):
        pass

    @abc.abstractmethod
    def check_is_template_exists(self, template_id: str) -> bool:
        pass

    @abc.abstractmethod
    def get_existing_gof_ids_of_template(self, template_id: str) -> List[str]:
        pass
