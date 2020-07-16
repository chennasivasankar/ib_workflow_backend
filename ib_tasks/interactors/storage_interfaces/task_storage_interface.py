import abc
from typing import List
from ib_tasks.interactors.dtos import GoFIDAndOrderDTO
from ib_tasks.interactors.dtos import GlobalConstantsDTO


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
    def check_is_template_exists(self, template_id: str) -> bool:
        pass

    @abc.abstractmethod
    def get_existing_gof_ids_of_template(self, template_id: str) -> List[str]:
        pass

    @abc.abstractmethod
    def create_global_constants_to_template(
            self, template_id: str,
            global_constants_dtos: List[GlobalConstantsDTO]):
        pass

    @abc.abstractmethod
    def get_constant_names_of_existing_global_constants_of_template(
            self, template_id: str):
        pass
