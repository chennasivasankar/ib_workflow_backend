from typing import List

from ib_tasks.constants.enum import ViewType
from ib_tasks.interactors.stage_dtos import TaskStageAssigneeDetailsDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_stage_storage_interface import TaskStageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import TaskStorageInterface
from ib_tasks.interactors.task_dtos import TaskStageIdDTO


class GetTasksStageCompleteCompleteDetailsInteractor:

    def __init__(
            self, task_storage: TaskStorageInterface,
            task_stage_storage: TaskStageStorageInterface,
            stage_storage: StageStorageInterface
    ):
        self.stage_storage = stage_storage
        self.task_storage = task_storage
        self.task_stage_storage = task_stage_storage

    def get_task_stage_complete_details(
            self, user_id: str, task_ids: List[int],
            view_type: ViewType, project_id: str
    ):
        self._validate_task_ids(task_ids=task_ids)
        task_stage_dtos = self.task_stage_storage \
            .get_task_stage_details_dtos(task_ids=task_ids)
        stage_ids = self._get_stage_ids(task_stage_dtos)
        user_roles = self._get_user_roles_in_project(user_id, project_id)
        permitted_stage_ids = self.stage_storage \
            .get_permitted_stage_ids_given_stage_ids(
            user_roles=user_roles, stage_ids=stage_ids
        )
        permitted_task_stage_dtos = [
            task_stage_dto
            for task_stage_dto in task_stage_dtos
            if task_stage_dto.stage_id in permitted_stage_ids
        ]
        task_stage_assignee_dtos = self._get_task_assignee_details(
            task_stage_dtos=permitted_task_stage_dtos
        )
        task_ids = self._get_task_ids(task_stage_assignee_dtos)
        task_base_details_dtos = self.task_storage

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
    ):
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
            user_id: str, project_id: str
    ) -> List[str]:
        from ib_tasks.interactors.user_role_validation_interactor \
            import UserRoleValidationInteractor
        validation_interactor = UserRoleValidationInteractor()
        user_roles = validation_interactor.get_user_role_ids_for_project(
            user_id=user_id, project_id=project_id
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
            raise InvalidTaskIds(task_ids=task_ids)
