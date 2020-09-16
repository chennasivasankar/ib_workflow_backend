import abc
import datetime
from typing import Union, List

from ib_tasks.exceptions.gofs_custom_exceptions import \
    InvalidSameGoFOrderForAGoF
from ib_tasks.exceptions.task_custom_exceptions \
    import InvalidTaskIdException
from ib_tasks.interactors.field_dtos import FieldIdWithTaskGoFIdDTO
from ib_tasks.interactors.gofs_dtos import GoFIdWithSameGoFOrderDTO
from ib_tasks.interactors.storage_interfaces.get_task_dtos import TaskGoFDTO, \
    TaskGoFFieldDTO, TaskBaseDetailsDTO, FieldSearchableDTO
from ib_tasks.interactors.storage_interfaces.task_dtos import \
    TaskGoFDetailsDTO, TaskGoFWithTaskIdDTO
from ib_tasks.interactors.task_dtos import CreateTaskDTO, UpdateTaskDTO, \
    BasicTaskDetailsDTO, UpdateTaskBasicDetailsDTO


class CreateOrUpdateTaskStorageInterface(abc.ABC):

    @abc.abstractmethod
    def validate_task_id(
            self, task_id: int
    ) -> Union[str, TaskBaseDetailsDTO, InvalidTaskIdException]:
        pass

    @abc.abstractmethod
    def get_task_gof_dtos(
            self, task_id: int, gof_ids: List[str]
    ) -> List[TaskGoFDTO]:
        pass

    @abc.abstractmethod
    def get_gof_ids_having_permission(
            self, gof_ids: List[str], user_roles: List[str]
    ) -> List[str]:
        pass

    @abc.abstractmethod
    def get_task_gof_field_dtos(
            self, task_gof_ids: List[int]
    ) -> List[TaskGoFFieldDTO]:
        pass

    @abc.abstractmethod
    def get_field_ids_having_permission(
            self, field_ids: List[str], user_roles: List[str]
    ) -> List[str]:
        pass

    @abc.abstractmethod
    def is_valid_task_id(self, task_id: int) -> bool:
        pass

    @abc.abstractmethod
    def create_task(self, task_details_dto: BasicTaskDetailsDTO) -> int:
        pass

    @abc.abstractmethod
    def create_task_gofs(
            self, task_gof_dtos: List[TaskGoFWithTaskIdDTO]
    ) -> List[TaskGoFDetailsDTO]:
        pass

    @abc.abstractmethod
    def create_task_gof_fields(
            self, task_gof_field_dtos: List[TaskGoFFieldDTO]
    ):
        pass

    @abc.abstractmethod
    def get_gofs_details_of_task(
            self, task_id: int) -> List[GoFIdWithSameGoFOrderDTO]:
        pass

    @abc.abstractmethod
    def get_fields_details_of_task(
            self, task_id: int
    ) -> List[FieldIdWithTaskGoFIdDTO]:
        pass

    @abc.abstractmethod
    def update_task_gofs(
            self, task_gof_dtos: List[TaskGoFWithTaskIdDTO]
    ) -> Union[List[TaskGoFDetailsDTO], InvalidSameGoFOrderForAGoF]:
        pass

    @abc.abstractmethod
    def update_task_gof_fields(
            self, task_gof_field_dtos: List[TaskGoFFieldDTO]
    ):
        pass

    @abc.abstractmethod
    def set_status_variables_for_template_and_task(self, task_template_id,
                                                   task_id):
        pass

    @abc.abstractmethod
    def get_all_gof_ids_related_to_a_task_template(
            self, task_template_id: str
    ) -> List[str]:
        pass

    @abc.abstractmethod
    def get_template_id_for_given_task(self, task_id: int) -> str:
        pass

    @abc.abstractmethod
    def create_initial_task_stage(self, task_id: int, template_id: str):
        pass

    @abc.abstractmethod
    def get_initial_stage_for_task_template(self, template_id: str) -> str:
        pass

    @abc.abstractmethod
    def update_task(self, task_basic_details: UpdateTaskBasicDetailsDTO):
        pass

    @abc.abstractmethod
    def get_field_searchable_dtos(
            self, field_ids: List[str], task_gof_ids: List[int]
    ) -> List[FieldSearchableDTO]:
        pass

    @abc.abstractmethod
    def get_task_ids(self) -> List[int]:
        pass

    @abc.abstractmethod
    def get_existing_task_due_date(self, task_id):
        pass

    @abc.abstractmethod
    def check_task_delay_reason_updated_or_not(
            self, task_id: int, stage_id: int,
            updated_due_date: datetime.datetime):
        pass

    @abc.abstractmethod
    def get_task_display_id_for_task_id(self, task_id: int):
        pass
