from typing import Optional, List

from ib_tasks.adapters.dtos import ColumnStageDTO
from ib_tasks.constants.enum import ViewType
from ib_tasks.interactors.gofs_dtos import FieldDisplayDTO
from ib_tasks.interactors.presenter_interfaces.dtos import \
    TaskCompleteDetailsDTO
from ib_tasks.interactors.stage_dtos import TaskStageAssigneeDetailsDTO
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.actions_dtos import \
    StageActionDetailsDTO, ActionDTO
from ib_tasks.interactors.storage_interfaces.fields_dtos import FieldDetailsDTO
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    GetTaskStageCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface import \
    TaskStageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface


class GetTaskCurrentBoardCompleteDetailsInteractor:

    def __init__(self, user_id: str,
                 field_storage: FieldsStorageInterface,
                 stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface,
                 action_storage: ActionStorageInterface,
                 board_id: str,
                 task_stage_storage: Optional[TaskStageStorageInterface],
                 view_type: ViewType = ViewType.KANBAN.value):
        self.task_stage_storage = task_stage_storage
        self.user_id = user_id
        self.board_id = board_id
        self.field_storage = field_storage
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.action_storage = action_storage
        self.view_type = view_type

    def get_task_current_board_complete_details(self, task_id: int,
                                                stage_ids: List[str]):

        task_display_id = self.task_storage.get_task_display_id_for_task_id(
            task_id=task_id
        )
        if self.board_id is None:
            return self._get_task_complete_details(task_id, task_display_id)
        task_boards_details = self._get_task_boards_details(stage_ids)
        column_stage_dtos = task_boards_details.column_stage_dtos
        board_stage_ids = self._get_present_board_stages(column_stage_dtos)
        actions_dto, fields_dto, task_stage_details = \
            self._get_task_fields_and_actions_dto(board_stage_ids, task_id)
        current_assignees_of_stages = self._get_stage_assignees_details(
            stage_ids=stage_ids, task_id=task_id
        )
        return TaskCompleteDetailsDTO(
            task_id=task_id,
            task_display_id=task_display_id,
            task_boards_details=task_boards_details,
            actions_dto=actions_dto,
            field_dtos=fields_dto,
            task_stage_details=task_stage_details,
            assignees_details=current_assignees_of_stages
        )

    @staticmethod
    def _get_task_complete_details(task_id: int, task_display_id: str):

        return TaskCompleteDetailsDTO(
            task_id=task_id,
            task_display_id=task_display_id,
            task_boards_details=None,
            actions_dto=None,
            field_dtos=None,
            task_stage_details=None,
            assignees_details=None
        )

    def _get_stage_assignees_details(
            self, stage_ids: List[str], task_id
    ) -> List[TaskStageAssigneeDetailsDTO]:
        if self.task_stage_storage is None:
            return []
        from ib_tasks.interactors.get_stages_assignees_details_interactor \
            import GetStagesAssigneesDetailsInteractor
        assignees_interactor = GetStagesAssigneesDetailsInteractor(
            task_stage_storage=self.task_stage_storage
        )
        from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO
        task_stage_dtos = [
            GetTaskDetailsDTO(
                task_id=task_id,
                stage_id=stage_id
            )
            for stage_id in stage_ids
        ]
        return \
            assignees_interactor.get_stages_assignee_details_by_given_task_ids(
                task_stage_dtos=task_stage_dtos
            )

    def _get_task_fields_and_actions_dto(
            self, stage_ids: List[str], task_id: int):

        from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO
        task_stage_dtos = [
            GetTaskDetailsDTO(
                task_id=task_id,
                stage_id=stage_id
            )
            for stage_id in stage_ids
        ]
        from ib_tasks.interactors.get_task_fields_and_actions \
            import GetTaskFieldsAndActionsInteractor
        interactor = GetTaskFieldsAndActionsInteractor(
            field_storage=self.field_storage,
            task_storage=self.task_storage,
            action_storage=self.action_storage,
            stage_storage=self.stage_storage
        )
        task_stage_details_dtos = interactor.get_task_fields_and_action(
            task_dtos=task_stage_dtos, user_id=self.user_id,
            view_type=self.view_type
        )
        actions_dto, fields_dto, task_stage_details = \
            self._get_field_dtos_and_actions_dtos(
                task_stage_details_dtos=task_stage_details_dtos)
        return actions_dto, fields_dto, task_stage_details

    def _get_field_dtos_and_actions_dtos(
            self,
            task_stage_details_dtos: List[GetTaskStageCompleteDetailsDTO]):

        actions_dto = []
        for task_stage_details_dto in task_stage_details_dtos:
            for action_dto in task_stage_details_dto.action_dtos:
                actions_dto.append(action_dto)
        actions_dto = self._get_actions_dto(actions_dto)

        fields_dto = []
        for task_stage_details_dto in task_stage_details_dtos:
            stage_id = task_stage_details_dto.stage_id
            for field_dto in task_stage_details_dto.field_dtos:
                fields_dto.append(self._get_field_dto(field_dto, stage_id))
        from ib_tasks.interactors.stage_dtos import TaskStageDTO
        task_stage_details = [
            TaskStageDTO(
                stage_id=task_stage_details_dto.stage_id,
                db_stage_id=task_stage_details_dto.db_stage_id,
                display_name=task_stage_details_dto.display_name,
                stage_colour=task_stage_details_dto.stage_color
            )
            for task_stage_details_dto in task_stage_details_dtos
        ]

        return actions_dto, fields_dto, task_stage_details

    @staticmethod
    def _get_field_dto(field_dto: FieldDetailsDTO, stage_id: str):

        return FieldDisplayDTO(
            field_id=str(field_dto.field_id),
            field_type=field_dto.field_type,
            stage_id=stage_id,
            key=field_dto.key,
            value=field_dto.value
        )

    @staticmethod
    def _get_actions_dto(actions_dto: List[StageActionDetailsDTO]):

        return [
            ActionDTO(
                action_id=action_dto.action_id,
                name=action_dto.name,
                action_type=action_dto.action_type,
                transition_template_id=action_dto.transition_template_id,
                stage_id=action_dto.stage_id,
                button_text=action_dto.button_text,
                button_color=action_dto.button_color
            )
            for action_dto in actions_dto
        ]

    @staticmethod
    def _get_present_board_stages(column_stage_dtos: List[ColumnStageDTO]):
        return [
            column_stage_dto.stage_id
            for column_stage_dto in column_stage_dtos
        ]

    def _get_task_boards_details(self, stage_ids: List[str]):

        from ib_tasks.adapters.service_adapter import ServiceAdapter
        adapter = ServiceAdapter()
        return adapter.boards_service \
            .get_display_boards_and_column_details(
            user_id=self.user_id, board_id=self.board_id,
            stage_ids=stage_ids
        )