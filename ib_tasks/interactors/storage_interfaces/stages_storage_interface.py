import abc
from typing import Optional, List

from ib_tasks.interactors.stages_dtos import StageDTO, \
    TaskIdWithStageAssigneeDTO, StageAssigneeDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import StageDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import StageRoleDTO, \
    TaskStagesDTO, TaskTemplateStageDTO, StageValueWithTaskIdsDTO, \
    TaskIdWithStageDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskStageHavingAssigneeIdDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskWithDbStageIdDTO
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO


class StageStorageInterface(abc.ABC):

    @abc.abstractmethod
    def get_existing_status_ids(self, status_ids: List[str]):
        pass

    @abc.abstractmethod
    def create_stages(self, stage_details: List[StageDTO]):
        pass

    @abc.abstractmethod
    def update_stages(self, stage_details: List[StageDTO]):
        pass

    @abc.abstractmethod
    def get_existing_stage_ids(self, stage_ids) -> Optional[List[str]]:
        pass

    @abc.abstractmethod
    def validate_stages_related_task_template_ids(self,
                                                  task_stages_dto: List[
                                                      TaskStagesDTO]) -> \
            Optional[List[TaskStagesDTO]]:
        pass

    @abc.abstractmethod
    def create_initial_stage_to_task_template(self, task_template_stage_dtos):
        pass

    @abc.abstractmethod
    def get_permitted_stage_ids(self, user_role_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_valid_stage_ids_in_given_stage_ids(self, stage_ids: List[str]) -> \
            List[str]:
        pass

    @abc.abstractmethod
    def get_valid_db_stage_ids_excluding_virtual_stages_in_given_db_stage_ids(
            self, db_stage_ids: List[
                int]) -> List[int]:
        pass

    @abc.abstractmethod
    def get_stage_details(self, task_dtos: List[GetTaskDetailsDTO]) -> \
            List[TaskTemplateStageDTO]:
        pass

    @abc.abstractmethod
    def get_task_id_with_stage_details_dtos_based_on_stage_value(
            self, stage_values: List[int],
            task_ids_group_by_stage_value_dtos: List[
                StageValueWithTaskIdsDTO], user_id: str) \
            -> List[TaskIdWithStageDetailsDTO]:
        pass

    @abc.abstractmethod
    def get_stage_role_dtos_given_db_stage_ids(self,
                                               db_stage_ids: List[int]) -> \
            List[StageRoleDTO]:
        pass

    @abc.abstractmethod
    def get_task_stage_ids_in_given_stage_ids(self, task_id: int,
                                              stage_ids: List[int]) -> \
            List[int]:
        pass

    @abc.abstractmethod
    def create_task_stage_assignees(
            self, task_id_with_stage_assignee_dtos: List[
                TaskIdWithStageAssigneeDTO]):
        pass

    @abc.abstractmethod
    def get_stage_ids_excluding_virtual_stages(
            self, stage_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_stage_detail_dtos_given_stage_ids(self, stage_ids: List[str]) -> \
            List[StageDetailsDTO]:
        pass

    @abc.abstractmethod
    def get_stage_details_having_assignees_in_given_stage_ids(
            self, task_id: int, db_stage_ids: List[int]) -> List[
        TaskStageHavingAssigneeIdDTO]:
        pass

    @abc.abstractmethod
    def update_task_stages_with_left_at_status(
            self, task_id: int, db_stage_ids: List[int]):
        pass

    @abc.abstractmethod
    def get_current_stages_of_all_tasks(self) -> List[TaskWithDbStageIdDTO]:
        pass

    @abc.abstractmethod
    def check_is_stage_exists(self, stage_id: int) -> bool:
        pass

    @abc.abstractmethod
    def get_stage_permitted_user_roles(self, stage_id: int) -> List[str]:
        pass

    @abc.abstractmethod
    def get_task_stages_having_assignees_without_having_left_at_status(
            self, task_id: int, db_stage_ids: List[int]) \
            -> List[StageAssigneeDTO]:
        pass

    @abc.abstractmethod
    def get_virtual_stages_already_having_in_task(
            self, task_id: int,
            stage_ids_having_virtual_stages: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_db_stage_ids_for_given_stage_ids(
            self, stage_ids: List[str]) -> List[int]:
        pass

    @abc.abstractmethod
    def get_valid_template_ids(self, template_ids: List[str]) -> List[str]:
        pass

    @abc.abstractmethod
    def get_stage_ids_having_actions(self):
        pass
