from typing import List

from ib_tasks.interactors \
    .get_next_stages_random_assignees_of_a_task_interactor import \
    GetNextStagesRandomAssigneesOfATaskInteractor
from ib_tasks.interactors.get_users_with_less_tasks_for_stages import \
    GetUsersWithLessTasksInGivenStagesInteractor
from ib_tasks.interactors.stages_dtos import StageAssigneeDTO, \
    TaskIdWithStageAssigneesDTO
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.storage_interface import \
    StorageInterface
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import \
    TaskStageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.update_task_stage_assignees_interactor import \
    UpdateTaskStageAssigneesInteractor


class GetNextStageRandomAssigneesOfTaskAndUpdateInDbInteractor:
    def __init__(self, storage: StorageInterface,
                 stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface,
                 action_storage: ActionStorageInterface,
                 task_stage_storage: TaskStageStorageInterface
                 ):
        self.task_stage_storage = task_stage_storage
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.action_storage = action_storage
        self.storage = storage

    def get_random_assignees_of_next_stages_and_update_in_db(
            self, task_id: int, stage_ids: List[str]):
        get_users_with_less_tasks_interactor = \
            GetUsersWithLessTasksInGivenStagesInteractor(
                action_storage=self.action_storage,
                stage_storage=self.stage_storage,
                task_stage_storage=self.task_stage_storage)
        stage_ids_excluding_virtual_stages = self.stage_storage. \
            get_stage_ids_excluding_virtual_stages(stage_ids)
        self._create_task_stage_history_records_for_virtua_stages(
            task_id=task_id, stage_ids_excluding_virtual_stages=
            stage_ids_excluding_virtual_stages, stage_ids=stage_ids)
        stages_having_user_details_dtos = \
            get_users_with_less_tasks_interactor. \
                get_users_with_less_tasks_in_given_stages(
                stage_ids=stage_ids_excluding_virtual_stages)

        stage_assignee_dtos = [
            StageAssigneeDTO(
                db_stage_id=stage_with_user_details_dto.db_stage_id,
                assignee_id=stage_with_user_details_dto.
                    assignee_details_dto.assignee_id
            )
            for stage_with_user_details_dto in
            stages_having_user_details_dtos
        ]
        task_id_with_stage_assignees_dto = TaskIdWithStageAssigneesDTO(
            task_id=task_id, stage_assignees=stage_assignee_dtos)
        update_task_stage_assignees_interactor = \
            UpdateTaskStageAssigneesInteractor(
                stage_storage=self.stage_storage,
                task_storage=self.task_storage)
        update_task_stage_assignees_interactor.\
            validate_and_update_task_stage_assignees(
            task_id_with_stage_assignees_dto=task_id_with_stage_assignees_dto)
        return

    def _create_task_stage_history_records_for_virtua_stages(
            self, task_id: int, stage_ids_excluding_virtual_stages: List[str],
            stage_ids: List[str]):
        stage_ids_having_virtual_stages = \
            [stage_id for stage_id in stage_ids
             if stage_id not in stage_ids_excluding_virtual_stages]
        virtual_stages_already_having_task = self.stage_storage. \
            get_virtual_stages_already_having_in_task(
            task_id, stage_ids_having_virtual_stages)
        virtual_stages_not_in_task = [stage_id for stage_id in
                                      stage_ids_having_virtual_stages if
                                      stage_id not in
                                      virtual_stages_already_having_task]
        virtual_stage_db_stage_ids_not_in_task = self.stage_storage. \
            get_db_stage_ids_for_given_stage_ids(virtual_stages_not_in_task)
        self.task_stage_storage. \
            create_task_stage_history_records_for_virtual_stages(
            stage_ids=virtual_stage_db_stage_ids_not_in_task, task_id=task_id)
        return
