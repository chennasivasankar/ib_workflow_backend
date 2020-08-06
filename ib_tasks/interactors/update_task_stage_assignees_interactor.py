from typing import List

from ib_tasks.exceptions.stage_custom_exceptions import \
    InvalidStageIdsListException, DuplicateStageIds, \
    StageIdsWithInvalidPermissionForAssignee
from ib_tasks.exceptions.task_custom_exceptions import InvalidTaskIdException
from ib_tasks.interactors.presenter_interfaces.update_task_stage_assignees_presenter_interface import \
    UpdateTaskStageAssigneesPresenterInterface
from ib_tasks.interactors.stages_dtos import TaskIdWithStageAssigneesDTO, \
    TaskIdWithStageAssigneeDTO
from ib_tasks.interactors.storage_interfaces.stage_dtos import StageRoleDTO, \
    StageIdWithRoleIdsAndAssigneeIdDTO
from ib_tasks.interactors.storage_interfaces.stages_storage_interface import \
    StageStorageInterface
from ib_tasks.interactors.storage_interfaces.task_storage_interface import \
    TaskStorageInterface
from ib_tasks.interactors.user_role_validation_interactor import \
    UserRoleValidationInteractor


class UpdateTaskStageAssigneesInteractor:
    def __init__(self, stage_storage: StageStorageInterface,
                 task_storage: TaskStorageInterface):
        self.stage_storage = stage_storage
        self.task_storage = task_storage

    def update_task_stage_assignees_wrapper(
            self,
            task_id_with_stage_assignees_dto: TaskIdWithStageAssigneesDTO,
            presenter: UpdateTaskStageAssigneesPresenterInterface):
        try:
            self.update_task_stage_assignees(task_id_with_stage_assignees_dto)
        except InvalidTaskIdException as exception:
            return presenter.raise_invalid_task_id_exception(task_id=exception.task_id)
        except DuplicateStageIds as exception:
            return presenter.raise_duplicate_stage_ids_not_valid(
                duplicate_stage_ids=exception.duplicate_stage_ids)
        except InvalidStageIdsListException as exception:
            return presenter.raise_invalid_stage_ids_exception(
                invalid_stage_ids=exception.invalid_stage_ids)
        except StageIdsWithInvalidPermissionForAssignee as exception:
            return presenter. \
                raise_stage_ids_with_invalid_permission_for_assignee_exception(
                invalid_stage_ids=exception.invalid_stage_ids)

    def update_task_stage_assignees(
            self,
            task_id_with_stage_assignees_dto: TaskIdWithStageAssigneesDTO):
        self._validate_task_id(
            task_id=task_id_with_stage_assignees_dto.task_id)
        stage_ids = self._get_stage_ids_from_given_dto(
            task_id_with_stage_assignees_dto)
        self._check_duplicate_stage_ids(stage_ids)
        valid_stage_ids = self.stage_storage. \
            get_valid_stage_ids_in_given_stage_ids(stage_ids)
        self._validate_stage_ids(stage_ids, valid_stage_ids)
        stage_role_dtos = self.stage_storage. \
            get_stage_role_dtos_given_stage_ids(stage_ids)

        role_ids_and_assignee_id_group_by_stage_id_dtos = \
            self._get_role_ids_and_assignee_id_group_by_stage_id_dtos(
                stage_ids=stage_ids, stage_role_dtos=stage_role_dtos,
                task_id_with_stage_assignees_dto=
                task_id_with_stage_assignees_dto
            )
        self._validate_does_given_assignee_of_stage_ids_have_valid_permission(
            role_ids_and_assignee_id_group_by_stage_id_dtos)
        task_stage_ids_for_updation = self.stage_storage. \
            get_task_stage_ids_in_given_stage_ids(stage_ids)
        task_stage_ids_for_creation = self._get_task_stage_ids_for_creation(
            task_stage_ids_for_updation, stage_ids)
        if task_stage_ids_for_updation:
            task_id_with_stage_assignee_dtos_for_updation = self. \
                _get_task_id_with_stage_assignee_dtos_given_task_stage_ids(
                task_stage_ids_for_updation, task_id_with_stage_assignees_dto)
            self.stage_storage.update_task_stage_assignees(
                task_id_with_stage_assignee_dtos_for_updation)

        if task_stage_ids_for_creation:
            task_id_with_stage_assignee_dtos_for_creation = self. \
                _get_task_id_with_stage_assignee_dtos_given_task_stage_ids(
                task_stage_ids_for_creation, task_id_with_stage_assignees_dto)
            self.stage_storage.create_task_stage_assignees(
                task_id_with_stage_assignee_dtos_for_creation)
        return

    @staticmethod
    def _get_task_id_with_stage_assignee_dtos_given_task_stage_ids(
            task_stage_ids, task_id_with_stage_assignees_dto:
            TaskIdWithStageAssigneesDTO) -> List[TaskIdWithStageAssigneeDTO]:
        task_id = task_id_with_stage_assignees_dto.task_id
        task_id_with_stage_assignee_dtos = []
        for each_task_stage_id in task_stage_ids:
            for each_task_id_with_stage_assignees_dto in \
                    task_id_with_stage_assignees_dto.stage_assignees:
                if each_task_id_with_stage_assignees_dto.stage_id == \
                        each_task_stage_id:
                    task_id_with_stage_assignee_dtos.append(
                        TaskIdWithStageAssigneeDTO(
                            assignee_id=each_task_id_with_stage_assignees_dto.
                                assignee_id,
                            stage_id=each_task_stage_id, task_id=task_id))

        return task_id_with_stage_assignee_dtos

    @staticmethod
    def _validate_does_given_assignee_of_stage_ids_have_valid_permission(
            role_ids_and_assignee_id_group_by_stage_id_dtos):
        stage_ids_with_invalid_permission_for_assignee_id = []
        user_role_validation_interactor = UserRoleValidationInteractor()
        for each_stage_id_with_role_ids_and_assignee_id_dto in \
                role_ids_and_assignee_id_group_by_stage_id_dtos:
            user_has_required_permission = user_role_validation_interactor. \
                does_user_has_required_permission(
                user_id=each_stage_id_with_role_ids_and_assignee_id_dto.
                    assignee_id,
                role_ids=each_stage_id_with_role_ids_and_assignee_id_dto.
                    role_ids)
            user_doesnt_has_required_permission = not \
                user_has_required_permission
            if user_doesnt_has_required_permission:
                stage_ids_with_invalid_permission_for_assignee_id. \
                    append(each_stage_id_with_role_ids_and_assignee_id_dto.
                           stage_id)
        if stage_ids_with_invalid_permission_for_assignee_id:
            raise StageIdsWithInvalidPermissionForAssignee(
                stage_ids_with_invalid_permission_for_assignee_id)
        return

    @staticmethod
    def _get_role_ids_and_assignee_id_group_by_stage_id_dtos(
            stage_ids: List[str],
            task_id_with_stage_assignees_dto: TaskIdWithStageAssigneesDTO,
            stage_role_dtos: List[StageRoleDTO]
    ) -> List[StageIdWithRoleIdsAndAssigneeIdDTO]:
        role_ids_and_assignee_id_group_by_stage_id_dtos = []
        for each_stage_id in stage_ids:

            list_of_role_ids = []
            for each_stage_role_dto in \
                    stage_role_dtos:
                if each_stage_role_dto.stage_id == \
                        each_stage_id:
                    list_of_role_ids.append(each_stage_role_dto.role_id)
            stage_assignee_id = ""
            for each_stage_assignee_dto in task_id_with_stage_assignees_dto. \
                    stage_assignees:
                if each_stage_assignee_dto.stage_id == each_stage_id:
                    stage_assignee_id = each_stage_assignee_dto.assignee_id

            each_stage_id_with_role_ids_and_assignee_id_dto = \
                StageIdWithRoleIdsAndAssigneeIdDTO(
                    stage_id=each_stage_id,
                    role_ids=list_of_role_ids,
                    assignee_id=stage_assignee_id)
            role_ids_and_assignee_id_group_by_stage_id_dtos.append(
                each_stage_id_with_role_ids_and_assignee_id_dto)
        return role_ids_and_assignee_id_group_by_stage_id_dtos

    def _validate_task_id(self, task_id: int):
        is_task_exists = self.task_storage. \
            check_is_task_exists(
            task_id=task_id)

        is_task_does_not_exists = not is_task_exists
        if is_task_does_not_exists:
            raise InvalidTaskIdException(task_id=task_id)

    @staticmethod
    def _get_stage_ids_from_given_dto(
            task_id_with_stage_assignees_dto: TaskIdWithStageAssigneesDTO):
        stage_ids = [
            stage_assignee_dto.stage_id for stage_assignee_dto in
            task_id_with_stage_assignees_dto.stage_assignees
        ]
        return stage_ids

    @staticmethod
    def _validate_stage_ids(stage_ids, valid_stage_ids):
        invalid_stage_ids = [
            stage_id for stage_id in stage_ids
            if stage_id not in valid_stage_ids
        ]
        if invalid_stage_ids:
            from ib_tasks.exceptions.stage_custom_exceptions import \
                InvalidStageIdsListException
            raise InvalidStageIdsListException(invalid_stage_ids)
        return

    @staticmethod
    def _get_task_stage_ids_for_creation(task_stage_ids_for_updation,
                                         stage_ids):
        task_stage_ids_for_creation = [
            stage_id for stage_id in stage_ids
            if stage_id not in task_stage_ids_for_updation
        ]
        return task_stage_ids_for_creation

    @staticmethod
    def _check_duplicate_stage_ids(stage_ids: List[str]):

        length_of_stage_ids = len(stage_ids)
        duplicate_stage_ids = []
        for i in range(length_of_stage_ids):
            k = i + 1
            for j in range(k, length_of_stage_ids):
                if stage_ids[i] == stage_ids[j] and stage_ids[i] \
                        not in duplicate_stage_ids:
                    duplicate_stage_ids.append(stage_ids[i])

        if len(duplicate_stage_ids) != 0:
            raise DuplicateStageIds(duplicate_stage_ids=duplicate_stage_ids)
