from typing import List, Optional

from ib_tasks.adapters.dtos import AssigneeDetailsDTO
from ib_tasks.adapters.service_adapter import get_service_adapter
from ib_tasks.interactors.stages_dtos import StageAssigneeDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskStageAssigneeDTO
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import \
    TaskStageStorageInterface
from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidStageIdsForTask


class GetStagesAssigneesDetailsInteractor:
    def __init__(self, task_stage_storage: TaskStageStorageInterface):
        self.task_stage_storage = task_stage_storage

    def get_stages_assignee_details_dtos(
            self, task_id: int, stage_ids: List[int]
    ) -> List[StageAssigneeDetailsDTO]:

        self._validate_stage_ids_of_task(task_id, stage_ids)
        stage_assignee_dtos = self.task_stage_storage.get_stage_assignee_dtos(
            task_id, stage_ids
        )
        assignee_ids = self._get_assignee_ids(stage_assignee_dtos)
        assignee_details_dtos = self._get_assignee_details_dtos(assignee_ids)
        stage_assignee_details_dtos = self._get_stage_assignee_details_dtos(
            stage_assignee_dtos, assignee_details_dtos
        )
        return stage_assignee_details_dtos

    def _get_stage_assignee_details_dtos(
            self, stage_assignee_dtos: List[TaskStageAssigneeDTO],
            assignee_details_dtos: List[AssigneeDetailsDTO]
    ) -> List[StageAssigneeDetailsDTO]:

        stage_assignee_details_dtos = []
        for stage_assignee_dto in stage_assignee_dtos:
            stage_assignee_details_dto = self._get_stage_assignee_details_dto(
                stage_assignee_dto, assignee_details_dtos
            )
            stage_assignee_details_dtos.append(stage_assignee_details_dto)
        return stage_assignee_details_dtos

    @staticmethod
    def _get_stage_assignee_details_dto(
            stage_assignee_dto: TaskStageAssigneeDTO,
            assignee_details_dtos: List[AssigneeDetailsDTO]
    ) -> StageAssigneeDetailsDTO:
        stage_assignee_id = stage_assignee_dto.assignee_id

        assignee_details = None
        for assignee_details_dto in assignee_details_dtos:
            assignee_id = assignee_details_dto.assignee_id
            if stage_assignee_id == assignee_id:
                assignee_details = assignee_details_dto
                break

        stage_assignee_details_dto = StageAssigneeDetailsDTO(
            task_stage_id=stage_assignee_dto.task_stage_id,
            stage_id=stage_assignee_dto.stage_id,
            assignee_details_dto=assignee_details
        )
        return stage_assignee_details_dto

    @staticmethod
    def _get_assignee_details_dtos(
            assignee_ids: List[str]
    ) -> List[AssigneeDetailsDTO]:

        service_adapter = get_service_adapter()
        assignees_details_service = service_adapter.assignee_details_service
        assignee_details_dtos = \
            assignees_details_service.get_assignees_details_dtos(
                assignee_ids
            )
        return assignee_details_dtos

    def _validate_stage_ids_of_task(
            self, task_id: int, stage_ids: List[int]
    ) -> Optional[InvalidStageIdsForTask]:

        from ib_tasks.constants.exception_messages import \
            INVALID_STAGE_IDS_FOR_TASK
        valid_stage_ids = self.task_stage_storage.get_valid_stage_ids_of_task(
            task_id, stage_ids
        )
        invalid_stage_ids = []
        for stage_id in stage_ids:
            if stage_id not in valid_stage_ids:
                invalid_stage_ids.append(stage_id)
        if invalid_stage_ids:
            raise InvalidStageIdsForTask(
                INVALID_STAGE_IDS_FOR_TASK.format(invalid_stage_ids, task_id)
            )
        return

    @staticmethod
    def _get_assignee_ids(stage_assignee_dtos: List[TaskStageAssigneeDTO]):
        assignee_ids = []
        for stage_assignee_dto in stage_assignee_dtos:
            assignee_id = not stage_assignee_dto.assignee_id
            if assignee_id:
                continue
            assignee_ids.append(stage_assignee_dto.assignee_id)
        return assignee_ids
