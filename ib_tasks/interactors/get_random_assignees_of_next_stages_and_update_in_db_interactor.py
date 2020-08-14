from ib_tasks.interactors \
    .get_next_stages_random_assignees_of_a_task_interactor import \
    GetNextStagesRandomAssigneesOfATaskInteractor
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

    def get_random_assignees_of_next_stages_and_update_in_db(self,
                                                             task_id: int,
                                                             action_id: int):
        get_next_stages_random_assignees_of_a_task_interactor = \
            GetNextStagesRandomAssigneesOfATaskInteractor(
                storage=self.storage, action_storage=self.action_storage,
                task_storage=self.task_storage,
                stage_storage=self.stage_storage,
                task_stage_storage=self.task_stage_storage
            )
        random_users_for_each_stage_dtos = \
            get_next_stages_random_assignees_of_a_task_interactor. \
                get_next_stages_random_assignees_of_a_task(
                task_id=task_id, action_id=action_id)
        stage_assignee_dtos = [
            StageAssigneeDTO(
                db_stage_id=random_user_for_each_stage_dto.db_stage_id,
                assignee_id=random_user_for_each_stage_dto.assignee_details_dto.assignee_id
            )
            for random_user_for_each_stage_dto in
            random_users_for_each_stage_dtos
        ]
        task_id_with_stage_assignees_dto = TaskIdWithStageAssigneesDTO(
            task_id=task_id, stage_assignees=stage_assignee_dtos)
        update_task_stage_assignees_interactor = \
            UpdateTaskStageAssigneesInteractor(
                stage_storage=self.stage_storage,
                task_storage=self.task_storage)
        update_task_stage_assignees_interactor.update_task_stage_assignees(
            task_id_with_stage_assignees_dto=task_id_with_stage_assignees_dto)
        return
