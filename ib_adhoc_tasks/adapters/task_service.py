from dataclasses import dataclass
from typing import List, Optional

from ib_adhoc_tasks.adapters.dtos import TasksDetailsInputDTO, \
    TasksCompleteDetailsDTO, TaskBaseDetailsDTO, \
    GetTaskStageCompleteDetailsDTO, TaskStageAssigneeDetailsDTO, \
    FieldDetailsDTO, StageActionDetailsDTO, AssigneeDetailsDTO, \
    TeamDetailsDTO, \
    TaskIdWithCompletedSubTasksCountDTO, TaskIdWithSubTasksCountDTO, \
    FieldIdAndNameDTO
from ib_adhoc_tasks.exceptions.custom_exceptions import InvalidTaskTemplateId


class InvalidTaskIds(Exception):
    def __init__(self, task_ids: List[int]):
        self.invalid_task_ids = task_ids


class InvalidGroupById(Exception):
    pass


class InvalidRoleIdsException(Exception):
    def __init__(self, role_ids: List[str]):
        self.role_ids = role_ids


@dataclass
class StageIdAndNameDTO:
    stage_id: str
    name: str


class TaskService:

    @property
    def interface(self):
        from ib_tasks.app_interfaces.service_interface import ServiceInterface
        return ServiceInterface()

    def validate_task_template_id(self, task_template_id: str) -> \
            Optional[InvalidTaskTemplateId]:
        valid_task_template_ids = self.interface.validate_task_template_ids(
            task_template_ids=[task_template_id]
        )
        is_invalid_task_template_id = not valid_task_template_ids
        if is_invalid_task_template_id:
            raise InvalidTaskTemplateId
        return

    def get_user_permitted_stage_ids(self, user_role_ids: List[str]):
        try:
            stage_ids = self.interface.get_user_permitted_stage_ids(
                user_roles=user_role_ids
            )
        except InvalidRoleIdsException:
            raise InvalidRoleIdsException
        return stage_ids

    def get_stage_details(self, stage_ids: List[str]):
        stage_details_dtos = self.interface.get_stage_details(
            stage_ids=stage_ids
        )
        stage_id_and_name_dtos = [
            StageIdAndNameDTO(
                stage_id=stage_details_dto.stage_id,
                name=stage_details_dto.name
            )
            for stage_details_dto in stage_details_dtos
        ]
        return stage_id_and_name_dtos

    def get_subtask_ids_for_task_id(self, task_id: int) -> List[int]:
        from ib_tasks.app_interfaces.service_interface import ServiceInterface
        service = ServiceInterface()
        subtask_ids_dtos = service.get_sub_task_ids_to_task_ids(
            task_ids=[task_id]
        )
        subtask_ids = subtask_ids_dtos[0].sub_task_ids
        return subtask_ids

    def get_project_id_based_on_task_id(self, task_id: int) -> str:
        task_project_dtos = self.interface.get_tasks_project_ids([task_id])
        task_project_dto = task_project_dtos[0]
        return task_project_dto.project_id

    @staticmethod
    def get_field_display_name(
            field_id: str, user_id: str, project_id: str
    ) -> str:
        from ib_tasks.app_interfaces.service_interface import ServiceInterface
        service = ServiceInterface()
        field_display_name_dtos = service.get_field_display_names(
            field_ids=[field_id], user_id=user_id, project_id=project_id
        )
        field_display_name = field_display_name_dtos[0].field_display_name
        return field_display_name

    def get_task_id(self, task_display_id: str) -> int:
        from ib_tasks.app_interfaces.service_interface import ServiceInterface
        service = ServiceInterface()
        task_ids_dtos = service.get_task_ids_for_given_task_display_ids(
            task_display_ids=[task_display_id])
        task_id = task_ids_dtos[0].task_id
        return task_id

    def get_sub_tasks_count_task_ids(self, task_ids: List[int]) \
            -> List[TaskIdWithSubTasksCountDTO]:
        try:
            sub_tasks_count_dtos = self.interface.get_sub_tasks_count_task_ids(
                task_ids=task_ids
            )
        except InvalidTaskIds:
            raise InvalidTaskIds
        task_id_with_sub_tasks_count_dtos = [
            TaskIdWithSubTasksCountDTO(
                task_id=sub_tasks_count_dto.task_id,
                sub_tasks_count=sub_tasks_count_dto.sub_tasks_count
            )
            for sub_tasks_count_dto in sub_tasks_count_dtos
        ]
        return task_id_with_sub_tasks_count_dtos

    def get_completed_sub_tasks_count_for_task_ids(
            self, task_ids
    ) -> List[TaskIdWithCompletedSubTasksCountDTO]:
        task_with_completed_sub_tasks_count_dtos = \
            self.interface.get_tasks_completed_sub_tasks_count_dtos(task_ids)
        return [
            TaskIdWithCompletedSubTasksCountDTO(
                task_id=dto.task_id,
                completed_sub_tasks_count=dto.completed_sub_tasks_count
            )
            for dto in task_with_completed_sub_tasks_count_dtos
        ]

    def get_task_template_field_dtos(
            self, user_id: str, project_id: str, template_id: str
    ) -> List[FieldIdAndNameDTO]:
        from ib_tasks.app_interfaces.service_interface import ServiceInterface
        service = ServiceInterface()
        field_dtos = service.get_task_template_field_dtos(
            user_id=user_id, project_ids=[project_id], template_id=template_id
        )
        field_id_and_name_dtos = [
            FieldIdAndNameDTO(
                field_id=field_dto.field_id,
                field_display_name=field_dto.field_display_name
            ) for field_dto in field_dtos
        ]
        return field_id_and_name_dtos

    def get_task_complete_details_dto(
            self, task_details_input_dto: TasksDetailsInputDTO
    ) -> TasksCompleteDetailsDTO:
        from ib_tasks.app_interfaces.service_interface import ServiceInterface
        service = ServiceInterface()
        task_complete_details_dto = service.get_tasks_complete_details(
            input_dto=task_details_input_dto
        )
        complete_task_details_dto = self._convert_to_task_complete_details_dto(
            task_complete_details_dto=task_complete_details_dto
        )
        return complete_task_details_dto

    def _convert_to_task_complete_details_dto(
            self, task_complete_details_dto: TasksCompleteDetailsDTO
    ):
        task_base_details_dtos = [
            self._convert_to_task_base_details_dto(
                task_base_details_dto=task_base_details_dto
            ) for task_base_details_dto in
            task_complete_details_dto.task_base_details_dtos
        ]
        task_stage_details_dtos = [
            self._convert_to_task_stage_details_dtos(
                task_stage_details_dto=task_stage_details_dto
            ) for task_stage_details_dto in
            task_complete_details_dto.task_stage_details_dtos
        ]
        task_stage_assignee_dtos = [
            self._convert_to_task_stage_assignees_dtos(
                task_stage_assignee_dto=task_stage_assignee_dto
            ) for task_stage_assignee_dto in
            task_complete_details_dto.task_stage_assignee_dtos
        ]
        return TasksCompleteDetailsDTO(
            task_base_details_dtos=task_base_details_dtos,
            task_stage_details_dtos=task_stage_details_dtos,
            task_stage_assignee_dtos=task_stage_assignee_dtos
        )

    @staticmethod
    def _convert_to_task_base_details_dto(
            task_base_details_dto: TaskBaseDetailsDTO
    ) -> TaskBaseDetailsDTO:
        return TaskBaseDetailsDTO(
            template_id=task_base_details_dto.template_id,
            project_id=task_base_details_dto.project_id,
            task_id=task_base_details_dto.task_id,
            task_display_id=task_base_details_dto.task_display_id,
            title=task_base_details_dto.title,
            description=task_base_details_dto.description,
            start_date=task_base_details_dto.start_date,
            due_date=task_base_details_dto.due_date,
            priority=task_base_details_dto.priority,
        )

    def _convert_to_task_stage_details_dtos(
            self, task_stage_details_dto: GetTaskStageCompleteDetailsDTO
    ) -> GetTaskStageCompleteDetailsDTO:
        field_dtos = [
            self._convert_to_field_details_dto(
                field_details_dto=field_details_dto
            ) for field_details_dto in task_stage_details_dto.field_dtos
        ]
        action_dtos = [
            self._convert_to_stage_action_details_dto(
                stage_action_details_dto=stage_action_details_dto
            )
            for stage_action_details_dto in task_stage_details_dto.action_dtos
        ]
        return GetTaskStageCompleteDetailsDTO(
            task_id=task_stage_details_dto.task_id,
            stage_id=task_stage_details_dto.stage_id,
            stage_color=task_stage_details_dto.stage_color,
            display_name=task_stage_details_dto.display_name,
            db_stage_id=task_stage_details_dto.db_stage_id,
            field_dtos=field_dtos,
            action_dtos=action_dtos,
        )

    def _convert_to_task_stage_assignees_dtos(
            self, task_stage_assignee_dto: TaskStageAssigneeDetailsDTO
    ) -> TaskStageAssigneeDetailsDTO:
        assignee_details = None
        if task_stage_assignee_dto.assignee_details:
            assignee_details = self._convert_to_assignee_details_dto(
                assignee_details_dto=task_stage_assignee_dto.assignee_details
            )
        team_details = None
        if task_stage_assignee_dto.team_details:
            team_details = self._convert_to_team_details_dto(
                team_details_dto=task_stage_assignee_dto.team_details
            )
        return TaskStageAssigneeDetailsDTO(
            task_id=task_stage_assignee_dto.task_id,
            stage_id=task_stage_assignee_dto.stage_id,
            assignee_details=assignee_details,
            team_details=team_details
        )

    @staticmethod
    def _convert_to_field_details_dto(
            field_details_dto: FieldDetailsDTO
    ) -> FieldDetailsDTO:
        return FieldDetailsDTO(
            field_type=field_details_dto.field_type,
            field_id=field_details_dto.field_id,
            key=field_details_dto.key,
            value=field_details_dto.value
        )

    @staticmethod
    def _convert_to_stage_action_details_dto(
            stage_action_details_dto: StageActionDetailsDTO
    ) -> StageActionDetailsDTO:
        return StageActionDetailsDTO(
            action_id=stage_action_details_dto.action_id,
            name=stage_action_details_dto.name,
            stage_id=stage_action_details_dto.stage_id,
            button_text=stage_action_details_dto.button_text,
            button_color=stage_action_details_dto.button_color,
            action_type=stage_action_details_dto.action_type,
            transition_template_id=
            stage_action_details_dto.transition_template_id
        )

    @staticmethod
    def _convert_to_assignee_details_dto(
            assignee_details_dto: AssigneeDetailsDTO
    ) -> Optional[AssigneeDetailsDTO]:
        return AssigneeDetailsDTO(
            assignee_id=assignee_details_dto.assignee_id,
            name=assignee_details_dto.name,
            profile_pic_url=assignee_details_dto.profile_pic_url
        )

    @staticmethod
    def _convert_to_team_details_dto(
            team_details_dto: TeamDetailsDTO
    ) -> Optional[TeamDetailsDTO]:
        return TeamDetailsDTO(
            team_id=team_details_dto.team_id,
            name=team_details_dto.name
        )
