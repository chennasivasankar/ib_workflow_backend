from dataclasses import dataclass
from typing import List

from ib_tasks.constants.enum import ViewType
from ib_tasks.interactors.presenter_interfaces.dtos import \
    AllTasksOverviewDetailsDTO
from ib_tasks.interactors.stage_dtos import TaskStageAssigneeDetailsDTO
from ib_tasks.interactors.storage_interfaces.action_storage_interface import \
    ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import \
    FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import \
    TaskIdWithStageDetailsDTO, GetTaskStageCompleteDetailsDTO, \
    TaskWithCompleteStageDetailsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface \
    import TaskStageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.task_dtos import GetTaskDetailsDTO
from ib_tasks.interactors.user_role_validation_interactor import \
    UserRoleValidationInteractor


@dataclass
class UserIdPaginationDTO:
    user_id: str
    limit: int
    offset: int


class GetTasksOverviewForUserInteractor:
    def __init__(self, stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface,
                 field_storage: FieldsStorageInterface,
                 action_storage: ActionStorageInterface,
                 task_stage_storage: TaskStageStorageInterface):
        self.task_stage_storage = task_stage_storage
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.field_storage = field_storage
        self.action_storage = action_storage

    def get_filtered_tasks_overview_for_user(
            self, user_id: str, task_ids: List[int], view_type: ViewType,
            project_id: str) -> \
            AllTasksOverviewDetailsDTO:
        stage_ids = self._get_allowed_stage_ids_of_user(
            user_id=user_id,
            project_id=project_id
        )
        task_id_with_stage_details_dtos = \
            self._get_task_with_stage_details_dtos(
                user_id=user_id,
                task_ids=task_ids,
                stage_ids=stage_ids
            )
        task_id_with_stage_id_dtos = self._get_task_id_with_stage_id_dtos(
            task_id_with_stage_details_dtos=task_id_with_stage_details_dtos)
        task_fields_and_action_details_dtos = self._get_task_fields_and_action(
            task_id_with_stage_id_dtos, user_id, view_type=view_type)

        all_tasks_overview_details_dto = \
            self._get_all_tasks_overview_details_dto(
                task_id_with_stage_details_dtos=
                task_id_with_stage_details_dtos,
                task_fields_and_action_details_dtos=
                task_fields_and_action_details_dtos)

        return all_tasks_overview_details_dto

    def _get_all_tasks_overview_details_dto(
            self,
            task_id_with_stage_details_dtos: List[TaskIdWithStageDetailsDTO],
            task_fields_and_action_details_dtos:
            List[GetTaskStageCompleteDetailsDTO]
    ) -> AllTasksOverviewDetailsDTO:
        task_ids_having_no_actions = \
            self._get_task_ids_having_no_stage_actions(
                task_fields_and_action_details_dtos=
                task_fields_and_action_details_dtos)
        task_with_stage_details_having_actions_dtos = \
            self._get_unique_task_with_stage_details_having_actions_dtos(
                task_id_with_stage_details_dtos=
                task_id_with_stage_details_dtos,
                task_ids_having_no_actions=task_ids_having_no_actions)
        task_fields_and_action_details_having_actions_dtos = \
            self._get_fields_and_action_details_of_unique_task_having_actions_dtos(
                task_ids_having_no_actions=task_ids_having_no_actions,
                task_fields_and_action_details_dtos=
                task_fields_and_action_details_dtos)
        task_with_complete_stage_details_dto = \
            self._get_task_with_complete_stage_details_dto(
                task_id_with_stage_details_dtos=
                task_with_stage_details_having_actions_dtos)

        from ib_tasks.interactors.presenter_interfaces.dtos import \
            AllTasksOverviewDetailsDTO
        all_tasks_overview_details_dto = AllTasksOverviewDetailsDTO(
            task_with_complete_stage_details_dtos=task_with_complete_stage_details_dto,
            task_fields_and_action_details_dtos=task_fields_and_action_details_having_actions_dtos,
        )
        return all_tasks_overview_details_dto

    def _get_allowed_stage_ids_of_user(self, user_id: str, project_id: str) -> \
    List[str]:
        user_interactor = UserRoleValidationInteractor()
        stage_ids = user_interactor. \
            get_permitted_stage_ids_given_user_id(
                user_id=user_id, stage_storage=self.stage_storage,
                project_id=project_id
            )
        return stage_ids

    def _get_task_with_stage_details_dtos(
            self, user_id: str, task_ids: List[int], stage_ids: List[str]
    ) -> List[TaskIdWithStageDetailsDTO]:

        from ib_tasks.interactors.get_task_ids_for_user_based_on_stage_ids import \
            GetTaskIdsWithStageDetailsOfUserBasedOnStagesInteractor
        task_ids_with_stage_details_of_user_based_on_stage_ids_interactor = \
            GetTaskIdsWithStageDetailsOfUserBasedOnStagesInteractor(
                stage_storage=self.stage_storage,
                task_storage=self.task_storage,
                task_stage_storage=self.task_stage_storage)
        task_id_with_stage_details_dtos = \
            task_ids_with_stage_details_of_user_based_on_stage_ids_interactor. \
                get_task_ids_with_stage_details_of_user_based_on_stage_ids(
                user_id=user_id, task_ids=task_ids, stage_ids=stage_ids)
        return task_id_with_stage_details_dtos

    def _get_task_with_complete_stage_details_dto(
            self,
            task_id_with_stage_details_dtos: List[TaskIdWithStageDetailsDTO]
    ) -> TaskWithCompleteStageDetailsDTO:
        task_stage_assignee_details_dtos = self._get_assignee_details_dtos(
            task_id_with_stage_details_dtos=task_id_with_stage_details_dtos)
        task_with_complete_stage_details_dto = TaskWithCompleteStageDetailsDTO(
            task_with_stage_details_dto=task_id_with_stage_details_dtos,
            stage_assignee_dtos=task_stage_assignee_details_dtos
        )
        return task_with_complete_stage_details_dto

    def _get_assignee_details_dtos(
            self,
            task_id_with_stage_details_dtos: List[TaskIdWithStageDetailsDTO]
    ) -> List[TaskStageAssigneeDetailsDTO]:
        task_id_with_stage_ids_dtos = self._get_task_id_with_stage_id_dtos(
            task_id_with_stage_details_dtos=task_id_with_stage_details_dtos
        )
        task_stage_assignee_details_dtos = \
            self._get_task_stage_assignee_details_dtos(
                task_id_with_stage_ids_dtos=task_id_with_stage_ids_dtos)
        return task_stage_assignee_details_dtos

    def _get_task_stage_assignee_details_dtos(
            self, task_id_with_stage_ids_dtos: List[GetTaskDetailsDTO]
    ) -> List[TaskStageAssigneeDetailsDTO]:
        from ib_tasks.interactors.get_stages_assignees_details_interactor \
            import GetStagesAssigneesDetailsInteractor
        get_stage_assignee_details_interactor = \
            GetStagesAssigneesDetailsInteractor(
                task_stage_storage=self.task_stage_storage)

        task_stage_assignee_details_dtos = \
            get_stage_assignee_details_interactor. \
                get_stages_assignee_details_by_given_task_ids(
                task_stage_dtos=task_id_with_stage_ids_dtos
            )
        return task_stage_assignee_details_dtos

    def _get_task_fields_and_action(
            self, task_id_with_stage_id_dtos: List[GetTaskDetailsDTO],
            user_id: str, view_type: ViewType
    ) -> List[GetTaskStageCompleteDetailsDTO]:
        from ib_tasks.interactors.get_task_fields_and_actions import \
            GetTaskFieldsAndActionsInteractor
        get_task_fields_and_actions_interactor = \
            GetTaskFieldsAndActionsInteractor(stage_storage=self.stage_storage,
                                              field_storage=self.field_storage,
                                              task_storage=self.task_storage,
                                              action_storage=self.action_storage)
        task_details_dtos = get_task_fields_and_actions_interactor. \
            get_task_fields_and_action(task_dtos=task_id_with_stage_id_dtos,
                                       user_id=user_id, view_type=view_type)
        return task_details_dtos

    @staticmethod
    def _get_task_id_with_stage_id_dtos(
            task_id_with_stage_details_dtos: List[TaskIdWithStageDetailsDTO]
    ) -> List[GetTaskDetailsDTO]:
        task_id_with_stage_id_dtos = [
            GetTaskDetailsDTO(
                task_id=task_id_with_stage_details_dto.task_id,
                stage_id=task_id_with_stage_details_dto.stage_id
            )
            for task_id_with_stage_details_dto in
            task_id_with_stage_details_dtos
        ]
        return task_id_with_stage_id_dtos

    @staticmethod
    def _get_task_ids_having_no_stage_actions(
            task_fields_and_action_details_dtos:
            List[GetTaskStageCompleteDetailsDTO]) -> List[int]:
        task_ids_having_no_actions = []
        for task_fields_and_action_details_dto in task_fields_and_action_details_dtos:
            is_task_stage_having_no_actions = \
                not task_fields_and_action_details_dto.action_dtos

            if is_task_stage_having_no_actions:
                task_id = task_fields_and_action_details_dto.task_id
                task_ids_having_no_actions.append(task_id)
        return task_ids_having_no_actions

    @staticmethod
    def _get_unique_task_with_stage_details_having_actions_dtos(
            task_ids_having_no_actions: List[int],
            task_id_with_stage_details_dtos: List[TaskIdWithStageDetailsDTO]
    ) -> List[TaskIdWithStageDetailsDTO]:
        task_ids = []
        unique_task_with_stage_details_having_actions_dtos = []
        for task_with_stage_details_dto in task_id_with_stage_details_dtos:
            is_unique_task = task_with_stage_details_dto.task_id not in task_ids
            is_task_having_actions = \
                task_with_stage_details_dto.task_id not in task_ids_having_no_actions
            is_unique_task_having_actions = \
                is_unique_task and is_task_having_actions
            if is_unique_task_having_actions:
                unique_task_with_stage_details_having_actions_dtos.append(
                    task_with_stage_details_dto
                )
                task_ids.append(task_with_stage_details_dto.task_id)

        return unique_task_with_stage_details_having_actions_dtos

    @staticmethod
    def _get_fields_and_action_details_of_unique_task_having_actions_dtos(
            task_ids_having_no_actions: List[int],
            task_fields_and_action_details_dtos: List[
                GetTaskStageCompleteDetailsDTO]
    ) -> List[GetTaskStageCompleteDetailsDTO]:
        task_ids = []
        fields_and_action_details_of_unique_task_having_actions_dtos = []
        for task_fields_and_action_details_dto in task_fields_and_action_details_dtos:
            is_unique_task = \
                task_fields_and_action_details_dto.task_id not in task_ids
            is_task_having_actions = \
                task_fields_and_action_details_dto.task_id not in task_ids_having_no_actions
            is_unique_task_having_actions = \
                is_unique_task and is_task_having_actions
            if is_unique_task_having_actions:
                fields_and_action_details_of_unique_task_having_actions_dtos. \
                    append(task_fields_and_action_details_dto)

                task_ids.append(task_fields_and_action_details_dto.task_id)
        return fields_and_action_details_of_unique_task_having_actions_dtos
