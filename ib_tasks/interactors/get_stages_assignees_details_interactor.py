from dataclasses import dataclass
from typing import List, Optional

from ib_tasks.adapters.dtos import AssigneeDetailsDTO, UserIdWithTeamIdDTO, \
    ProjectTeamUserIdsDTO, TeamDetailsWithUserIdDTO
from ib_tasks.adapters.service_adapter import get_service_adapter
from ib_tasks.exceptions.task_custom_exceptions import \
    InvalidStageIdsForTask
from ib_tasks.interactors.stages_dtos import StageAssigneeWithTeamDetailsDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskStageAssigneeDTO
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import \
    TaskStageStorageInterface, TaskStageAssigneeIdDTO
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO, \
    AssigneeWithTeamDetailsDTO, TeamInfoDTO


@dataclass
class TaskStageAssigneeDetailsDTO:
    task_id: int
    stage_id: str
    assignee_details: Optional[AssigneeDetailsDTO]


class GetStagesAssigneesDetailsInteractor:
    def __init__(self, task_stage_storage: TaskStageStorageInterface):
        self.task_stage_storage = task_stage_storage

    def get_stages_assignee_details_dtos(
            self, task_id: int, stage_ids: List[int], project_id: str
    ) -> List[StageAssigneeWithTeamDetailsDTO]:

        self._validate_stage_ids_of_task(task_id, stage_ids)
        stage_assignee_dtos = self.task_stage_storage.get_stage_assignee_dtos(
            task_id, stage_ids
        )
        user_id_with_team_id_dtos = self._get_user_id_with_team_id_dtos(
            stage_assignee_dtos
        )
        project_team_user_ids_dto = ProjectTeamUserIdsDTO(
            project_id=project_id,
            user_id_with_team_id_dtos=user_id_with_team_id_dtos
        )
        assignee_ids = self._get_assignee_ids(user_id_with_team_id_dtos)
        assignee_details_dtos = self._get_assignee_details_dtos(assignee_ids)
        team_details_with_user_id_dtos = \
            self._get_team_details_with_user_id_dtos(
                project_team_user_ids_dto)
        assignee_with_team_details_dtos = \
            self._get_assignee_with_team_details_dtos(
                team_details_with_user_id_dtos, assignee_details_dtos
            )
        stage_assignee_details_dtos = self._get_stage_assignee_details_dtos(
            stage_assignee_dtos, assignee_with_team_details_dtos
        )
        return stage_assignee_details_dtos

    def _get_assignee_with_team_details_dtos(
            self,
            team_details_with_user_id_dtos: List[TeamDetailsWithUserIdDTO],
            assignee_details_dtos: List[AssigneeDetailsDTO]
    ) -> List[AssigneeWithTeamDetailsDTO]:
        assignee_with_team_details_dtos = []
        for assignee_details_dto in assignee_details_dtos:
            assignee_with_team_details_dto = \
                self._get_assignee_with_team_details_dto(
                    assignee_details_dto, team_details_with_user_id_dtos
                )
            assignee_with_team_details_dtos.append(
                assignee_with_team_details_dto
            )
        return assignee_with_team_details_dtos

    @staticmethod
    def _get_assignee_with_team_details_dto(
            assignee_details_dto: AssigneeDetailsDTO,
            team_details_with_user_id_dtos: List[TeamDetailsWithUserIdDTO]
    ) -> Optional[AssigneeWithTeamDetailsDTO]:
        assignee_id = assignee_details_dto.assignee_id
        for team_details_with_user_id_dto in team_details_with_user_id_dtos:
            user_id = team_details_with_user_id_dto.user_id
            if user_id == assignee_id:
                team_info_dto = TeamInfoDTO(
                    team_id=team_details_with_user_id_dto.team_id,
                    team_name=team_details_with_user_id_dto.name
                )
                assignee_with_team_details_dto = AssigneeWithTeamDetailsDTO(
                    assignee_id=assignee_details_dto.assignee_id,
                    name=assignee_details_dto.name,
                    profile_pic_url=assignee_details_dto.profile_pic_url,
                    team_info_dto=team_info_dto
                )
                return assignee_with_team_details_dto
        return

    @staticmethod
    def _get_team_details_with_user_id_dtos(
            project_team_user_ids_dto: ProjectTeamUserIdsDTO
    ) -> List[TeamDetailsWithUserIdDTO]:
        service_interface = get_service_adapter()
        auth_service = service_interface.auth_service
        team_details_with_user_id_dtos = \
            auth_service.get_team_details_for_given_project_team_user_ids_dto(
                project_team_user_ids_dto)
        return team_details_with_user_id_dtos

    @staticmethod
    def _get_assignee_ids(
            user_id_with_team_id_dtos: List[UserIdWithTeamIdDTO]
    ) -> List[str]:
        assignee_ids = [
            user_id_with_team_id_dto.user_id
            for user_id_with_team_id_dto in user_id_with_team_id_dtos
        ]
        return assignee_ids

    @staticmethod
    def _get_user_id_with_team_id_dtos(
            stage_assignee_dtos: List[TaskStageAssigneeDTO]
    ) -> List[UserIdWithTeamIdDTO]:
        user_id_with_team_id_dtos = []
        for stage_assignee_dto in stage_assignee_dtos:
            is_assignee_id = not stage_assignee_dto.assignee_id
            if is_assignee_id:
                user_id_with_team_id_dto = UserIdWithTeamIdDTO(
                    user_id=stage_assignee_dto.assignee_id,
                    team_id=stage_assignee_dto.team_id
                )
                user_id_with_team_id_dtos.append(user_id_with_team_id_dto)
        return user_id_with_team_id_dtos

    def _get_stage_assignee_details_dtos(
            self, stage_assignee_dtos: List[TaskStageAssigneeDTO],
            assignee_with_team_details_dtos: List[AssigneeWithTeamDetailsDTO]
    ) -> List[StageAssigneeWithTeamDetailsDTO]:

        stage_assignee_details_dtos = []
        for stage_assignee_dto in stage_assignee_dtos:
            stage_assignee_details_dto = self._get_stage_assignee_details_dto(
                stage_assignee_dto, assignee_with_team_details_dtos
            )
            stage_assignee_details_dtos.append(stage_assignee_details_dto)
        return stage_assignee_details_dtos

    @staticmethod
    def _get_stage_assignee_details_dto(
            stage_assignee_dto: TaskStageAssigneeDTO,
            assignee_with_team_details_dtos: List[AssigneeWithTeamDetailsDTO]
    ) -> StageAssigneeWithTeamDetailsDTO:
        stage_assignee_id = stage_assignee_dto.assignee_id

        assignee_details = None
        for assignee_with_team_details_dto in assignee_with_team_details_dtos:
            assignee_id = assignee_with_team_details_dto.assignee_id
            if stage_assignee_id == assignee_id:
                assignee_details = assignee_with_team_details_dto
                break

        stage_assignee_details_dto = StageAssigneeWithTeamDetailsDTO(
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

    def get_stages_assignee_details_by_given_task_ids(
            self, task_stage_dtos: List[GetTaskDetailsDTO]
    ) -> List[TaskStageAssigneeDetailsDTO]:
        stage_assignee_dtos = \
            self.task_stage_storage.get_stage_assignee_id_dtos(
                task_stage_dtos=task_stage_dtos
            )
        assignee_ids = self._get_unique_assignee_ids(stage_assignee_dtos)
        assignee_details_dtos = self._get_assignee_details_dtos(assignee_ids)
        return self._get_task_stage_assignee_details_dtos(
            stage_assignee_dtos, assignee_details_dtos
        )

    @staticmethod
    def _get_unique_assignee_ids(
            stage_assignee_dtos: List[TaskStageAssigneeIdDTO]) -> List[str]:
        assignee_ids = [
            stage_assignee_dto.assignee_id
            for stage_assignee_dto in stage_assignee_dtos
        ]
        return list(set(assignee_ids))

    @staticmethod
    def _get_task_stage_assignee_details_dtos(
            stage_assignee_dtos: List[TaskStageAssigneeIdDTO],
            assignee_details_dtos: List[AssigneeDetailsDTO]
    ) -> List[TaskStageAssigneeDetailsDTO]:
        assignees_dict = {}
        for assignee_details_dto in assignee_details_dtos:
            assignees_dict[
                assignee_details_dto.assignee_id] = assignee_details_dto
        return [
            TaskStageAssigneeDetailsDTO(
                task_id=stage_assignee_dto.task_id,
                stage_id=stage_assignee_dto.stage_id,
                assignee_details=assignees_dict[stage_assignee_dto.assignee_id]
            )
            for stage_assignee_dto in stage_assignee_dtos
        ]
