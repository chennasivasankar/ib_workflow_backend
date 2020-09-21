from typing import List

from ib_tasks.interactors.dtos.dtos import TasksDetailsInputDTO
from ib_tasks.interactors.mixins.validation_mixin import ValidationMixin
from ib_tasks.interactors.stage_dtos import TaskStageAssigneeDetailsDTO
from ib_tasks.interactors.storage_interfaces.action_storage_interface import ActionStorageInterface
from ib_tasks.interactors.storage_interfaces.fields_storage_interface import FieldsStorageInterface
from ib_tasks.interactors.storage_interfaces.stage_dtos import GetTaskStageCompleteDetailsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface import TaskStageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import TaskStorageInterface
from ib_tasks.interactors.task_dtos import TaskStageIdDTO
from ib_tasks.interactors.task_stage_dtos import TasksCompleteDetailsDTO


class GetTasksCompleteDetailsInteractor(ValidationMixin):

    def __init__(
            self, task_storage: TaskStorageInterface,
            task_stage_storage: TaskStageStorageInterface,
            stage_storage: StageStorageInterface,
            field_storage: FieldsStorageInterface,
            action_storage: ActionStorageInterface
    ):
        self.action_storage = action_storage
        self.field_storage = field_storage
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.task_stage_storage = task_stage_storage

    def get_tasks_complete_details(
            self, input_dto: TasksDetailsInputDTO
    ) -> TasksCompleteDetailsDTO:
        self.validations_for_input_data(input_dto)
        task_stage_dtos = self._get_permitted_task_stage_dtos(input_dto)
        task_stage_details_dtos = self._get_task_stage_fields_and_actions(
            task_stage_dtos=task_stage_dtos,
            input_dto=input_dto
        )
        task_stage_assignee_dtos = self._get_task_assignee_details(
            task_stage_dtos=task_stage_dtos
        )
        task_ids = self._get_task_ids(task_stage_assignee_dtos)
        task_base_details_dtos = self.task_storage.get_base_details_to_task_ids(
            task_ids=task_ids
        )
        return TasksCompleteDetailsDTO(
            task_base_details_dtos=task_base_details_dtos,
            task_stage_assignee_dtos=task_stage_assignee_dtos,
            task_stage_details_dtos=task_stage_details_dtos
        )

    def _get_permitted_task_stage_dtos(
            self, input_dto: TasksDetailsInputDTO
    ) -> List[TaskStageIdDTO]:
        task_ids = input_dto.task_ids
        task_stage_dtos = self.task_stage_storage \
            .get_task_stage_details_dtos(task_ids=task_ids)
        stage_ids = self._get_stage_ids(task_stage_dtos)
        user_roles = self._get_user_roles_in_project(input_dto)
        permitted_stage_ids = self.stage_storage \
            .get_permitted_stage_ids_given_stage_ids(
            user_roles=user_roles, stage_ids=stage_ids
        )
        permitted_task_stage_dtos = [
            task_stage_dto
            for task_stage_dto in task_stage_dtos
            if task_stage_dto.stage_id in permitted_stage_ids
        ]
        return permitted_task_stage_dtos

    def validations_for_input_data(self, input_dto: TasksDetailsInputDTO):
        project_id = input_dto.project_id
        task_ids = input_dto.task_ids
        self.validate_given_project_ids(project_ids=[project_id])
        self._validate_task_ids(task_ids=task_ids)

    def _get_task_stage_fields_and_actions(
            self, task_stage_dtos: List[TaskStageIdDTO],
            input_dto: TasksDetailsInputDTO
    ) -> List[GetTaskStageCompleteDetailsDTO]:
        from ib_tasks.interactors.get_task_fields_and_actions \
            import GetTaskFieldsAndActionsInteractor
        interactor = GetTaskFieldsAndActionsInteractor(
            field_storage=self.field_storage,
            stage_storage=self.stage_storage,
            action_storage=self.action_storage,
            task_storage=self.task_storage
        )
        task_stage_complete_details_dtos = interactor.get_task_fields_and_action(
            task_dtos=task_stage_dtos, user_id=input_dto.user_id,
            view_type=input_dto.view_type
        )
        return task_stage_complete_details_dtos

    @staticmethod
    def _get_task_ids(
            task_stage_assignee_dtos: List[TaskStageAssigneeDetailsDTO]
    ) -> List[int]:
        task_ids = [
            task_stage_assignee_dto.task_id
            for task_stage_assignee_dto in task_stage_assignee_dtos
        ]
        return sorted(list(set(task_ids)))

    def _get_task_assignee_details(
            self, task_stage_dtos: List[TaskStageIdDTO]
    ) -> List[TaskStageAssigneeDetailsDTO]:
        from ib_tasks.interactors.get_stages_assignees_details_interactor \
            import GetStagesAssigneesDetailsInteractor
        interactor = GetStagesAssigneesDetailsInteractor(
            task_stage_storage=self.task_stage_storage
        )
        task_stage_assignee_dtos = \
            interactor.get_stages_assignee_details_by_given_task_ids(
                task_stage_dtos=task_stage_dtos
            )
        return task_stage_assignee_dtos

    @staticmethod
    def _get_user_roles_in_project(
            input_dto: TasksDetailsInputDTO
    ) -> List[str]:
        from ib_tasks.interactors.user_role_validation_interactor \
            import UserRoleValidationInteractor
        validation_interactor = UserRoleValidationInteractor()
        user_roles = validation_interactor.get_user_role_ids_for_project(
            user_id=input_dto.user_id, project_id=input_dto.project_id
        )
        return user_roles

    @staticmethod
    def _get_stage_ids(task_stage_dtos: List[TaskStageIdDTO]):
        return [
            task_stage_dto.stage_id
            for task_stage_dto in task_stage_dtos
        ]

    def _validate_task_ids(self, task_ids: List[int]):
        valid_task_ids = self.task_storage.get_valid_task_ids(task_ids=task_ids)

        invalid_task_ids = [
            task_id
            for task_id in task_ids
            if task_id not in valid_task_ids
        ]
        if invalid_task_ids:
            from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIds
            raise InvalidTaskIds(task_ids=invalid_task_ids)
